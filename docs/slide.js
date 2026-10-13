(() => {
  const slides = Array.from(document.querySelectorAll(".slide"));
  if (!slides.length) return;

  const prevButton = document.querySelector("[data-slide-prev]");
  const nextButton = document.querySelector("[data-slide-next]");
  const currentLabel = document.querySelector("[data-slide-current]");
  const totalLabel = document.querySelector("[data-slide-total]");
  const progressBar = document.querySelector("[data-slide-progress]");
  const nextPage = document.body.dataset.nextPage || "";
  const prevPage = document.body.dataset.prevPage || "";
  const modeToggle = document.querySelector("[data-lesson-mode-toggle]");
  const modeLabel = document.querySelector("[data-lesson-mode-summary]");
  // "전체" remains the default to preserve all existing deep links.
  // Core mode skips only slides explicitly marked data-level="detail".
  let coreMode = new URLSearchParams(location.search).get("mode") === "core";

  let currentIndex = 0;
  let wheelLocked = false;
  let touchStartX = 0;
  let touchStartY = 0;
  let fitFrame = 0;

  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function included(index) {
    return !coreMode || slides[index]?.dataset.level !== "detail";
  }

  function nearbyIncluded(index, preferNext = true) {
    const start = clamp(index, 0, slides.length - 1);
    if (included(start)) return start;
    if (preferNext) {
      for (let i = start + 1; i < slides.length; i++) {
        if (included(i)) return i;
      }
    }
    for (let i = start - 1; i >= 0; i--) {
      if (included(i)) return i;
    }
    return 0;
  }

  function pathTo(page) {
    const target = new URL(page, location.href);
    if (coreMode) target.searchParams.set("mode", "core");
    else target.searchParams.delete("mode");
    target.hash = "#slide-1";
    return target.href;
  }

  function indexFromHash() {
    const match = location.hash.match(/^#slide-(\d+)$/);
    if (!match) return 0;
    return nearbyIncluded(Number(match[1]) - 1);
  }

  function fitActiveSlide() {
    const slide = slides[currentIndex];
    const inner = slide?.querySelector(".slide-inner");
    if (!slide || !inner || !slide.classList.contains("active")) return;

    inner.style.zoom = "1";
    inner.style.transform = "";
    slide.removeAttribute("data-fit-scale");

    const style = getComputedStyle(slide);
    const availableWidth =
      slide.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
    const availableHeight =
      slide.clientHeight - parseFloat(style.paddingTop) - parseFloat(style.paddingBottom);

    const naturalWidth = Math.max(inner.scrollWidth, inner.getBoundingClientRect().width);
    const naturalHeight = Math.max(inner.scrollHeight, inner.getBoundingClientRect().height);

    if (!naturalWidth || !naturalHeight || availableWidth <= 0 || availableHeight <= 0) return;

    const scale = Math.min(
      1,
      availableWidth / naturalWidth,
      availableHeight / naturalHeight
    );

    if (scale < 0.998) {
      if (CSS.supports("zoom", "0.9")) {
        inner.style.zoom = String(scale);
      } else {
        inner.style.transform = `scale(${scale})`;
      }
      slide.dataset.fitScale = scale.toFixed(3);
    } else {
      slide.dataset.fitScale = "1.000";
    }
  }

  function scheduleFit() {
    cancelAnimationFrame(fitFrame);
    fitFrame = requestAnimationFrame(() => {
      fitActiveSlide();
      requestAnimationFrame(fitActiveSlide);
    });
  }

  function render() {
    slides.forEach((slide, index) => {
      const active = index === currentIndex;
      slide.classList.toggle("active", active);
      slide.setAttribute("aria-hidden", String(!active));
      if (!active) {
        const inner = slide.querySelector(".slide-inner");
        if (inner) {
          inner.style.zoom = "1";
          inner.style.transform = "";
        }
        slide.removeAttribute("data-fit-scale");
      }
    });

    const pathIndices = slides
      .map((_, i) => i)
      .filter(included);
    const pathPosition = Math.max(0, pathIndices.indexOf(currentIndex)) + 1;
    if (currentLabel) currentLabel.textContent = String(pathPosition);
    if (totalLabel) totalLabel.textContent = String(pathIndices.length);
    if (progressBar) {
      progressBar.style.width = ((pathPosition / pathIndices.length) * 100) + "%";
    }
    if (modeToggle) {
      modeToggle.textContent = coreMode ? "심화 포함 전체 보기" : "핵심만 보기";
      modeToggle.setAttribute("aria-pressed", String(coreMode));
    }
    if (modeLabel) {
      const detailCount = slides.length - slides.filter(s => s.dataset.level === "detail").length;
      modeLabel.textContent = coreMode
        ? "핵심 과정 · 심화 " + (slides.length - detailCount) + "장 제외"
        : "전체 과정 · 심화 포함";
    }

    if (prevButton) prevButton.disabled = currentIndex === 0 && !prevPage;
    if (nextButton) {
      nextButton.disabled = currentIndex === slides.length - 1 && !nextPage;
    }

    history.replaceState(null, "", "#slide-" + (currentIndex + 1));
    scheduleFit();
  }

  function goTo(index) {
    currentIndex = nearbyIncluded(index);
    render();
  }

  function next() {
    for (let i = currentIndex + 1; i < slides.length; i++) {
      if (included(i)) return goTo(i);
    }
    if (nextPage) location.href = pathTo(nextPage);
  }

  function previous() {
    for (let i = currentIndex - 1; i >= 0; i--) {
      if (included(i)) return goTo(i);
    }
    if (prevPage) location.href = pathTo(prevPage);
  }

  prevButton?.addEventListener("click", previous);
  nextButton?.addEventListener("click", next);

  modeToggle?.addEventListener("click", () => {
    coreMode = !coreMode;
    const url = new URL(location.href);
    if (coreMode) url.searchParams.set("mode", "core");
    else url.searchParams.delete("mode");
    history.replaceState(null, "", url.pathname + url.search + url.hash);
    currentIndex = nearbyIncluded(currentIndex);
    render();
  });

  addEventListener("keydown", (event) => {
    const target = event.target;
    if (
      target instanceof HTMLInputElement ||
      target instanceof HTMLTextAreaElement ||
      target instanceof HTMLSelectElement
    ) return;

    if (
      event.key === "ArrowRight" ||
      event.key === "PageDown" ||
      event.key === " "
    ) {
      event.preventDefault();
      next();
    } else if (
      event.key === "ArrowLeft" ||
      event.key === "PageUp"
    ) {
      event.preventDefault();
      previous();
    } else if (event.key === "Home") {
      event.preventDefault();
      goTo(0);
    } else if (event.key === "End") {
      event.preventDefault();
      goTo(slides.length - 1);
    }
  });

  addEventListener("wheel", (event) => {
    if (wheelLocked || Math.abs(event.deltaY) < 25) return;
    event.preventDefault();
    wheelLocked = true;
    if (event.deltaY > 0) next();
    else previous();
    setTimeout(() => {
      wheelLocked = false;
    }, 500);
  }, { passive: false });

  addEventListener("touchstart", (event) => {
    const touch = event.changedTouches[0];
    touchStartX = touch.clientX;
    touchStartY = touch.clientY;
  }, { passive: true });

  addEventListener("touchend", (event) => {
    const touch = event.changedTouches[0];
    const deltaX = touch.clientX - touchStartX;
    const deltaY = touch.clientY - touchStartY;
    if (Math.abs(deltaX) < 50 || Math.abs(deltaX) < Math.abs(deltaY)) return;
    if (deltaX < 0) next();
    else previous();
  }, { passive: true });

  slides.forEach((slide) => {
    slide.querySelectorAll("img").forEach((img) => {
      if (!img.complete) img.addEventListener("load", scheduleFit, { once: true });
    });
  });

  addEventListener("resize", scheduleFit);
  addEventListener("load", scheduleFit, { once: true });
  if (document.fonts?.ready) {
    document.fonts.ready.then(scheduleFit).catch(() => {});
  }

  addEventListener("hashchange", () => {
    currentIndex = indexFromHash();
    render();
  });

  currentIndex = indexFromHash();
  render();
})();