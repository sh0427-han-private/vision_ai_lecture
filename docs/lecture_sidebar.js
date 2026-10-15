/* One sidebar on Intro and the integrated Vision-AI-first course.
   Accessible toggle, grouped direct links, focus and outside-click dismissal. */
(() => {
  "use strict";
  const data = window.LECTURE_OUTLINE;
  const nav = document.querySelector(".site-header .nav");
  if (!data?.groups?.length || !nav) return;
  const currentPage = location.pathname.split("/").pop() || "intro.html";
  if (!["intro.html","vision_ai_course.html"].includes(currentPage)) return;
  nav.classList.add("lecture-nav");

  const toggle = document.createElement("button");
  toggle.className = "lecture-toc-toggle";
  toggle.type = "button";
  toggle.textContent = "☰ 강의 목차";
  toggle.setAttribute("aria-label", "강의 목차 열기");
  toggle.setAttribute("aria-controls", "lecture-toc-drawer");
  toggle.setAttribute("aria-expanded", "false");
  nav.prepend(toggle);

  const backdrop = document.createElement("div");
  backdrop.className = "lecture-toc-backdrop";
  backdrop.setAttribute("aria-hidden", "true");

  const drawer = document.createElement("aside");
  drawer.className = "lecture-toc-drawer";
  drawer.id = "lecture-toc-drawer";
  drawer.setAttribute("aria-label", "전체 강의 슬라이드 목차");
  drawer.setAttribute("aria-hidden", "true");
  drawer.inert = true;

  const header = document.createElement("div");
  header.className = "lecture-toc-header";
  const labels = document.createElement("div");
  const heading = document.createElement("h2");
  heading.textContent = "전체 강의 목차";
  const count = document.createElement("p");
  const total = data.groups.reduce((n, g) => n + g.items.length, 0);
  count.textContent = total + "장 · 항목을 클릭하면 바로 이동합니다";
  labels.append(heading,count);
  const close = document.createElement("button");
  close.className = "lecture-toc-close";
  close.type = "button";
  close.textContent = "✕ 닫기";
  header.append(labels,close);

  const list = document.createElement("nav");
  list.className = "lecture-toc-sections";
  list.setAttribute("aria-label", "주제별 슬라이드");
  const links = [];
  const detailsByItem = new Map();
  for (const group of data.groups) {
    const details = document.createElement("details");
    details.className = "lecture-toc-unit";
    const summary = document.createElement("summary");
    const name = document.createElement("span");
    name.textContent = group.name;
    const size = document.createElement("small");
    size.className = "lecture-toc-count";
    size.textContent = group.items.length + "장";
    summary.append(name,size);
    const items = document.createElement("div");
    items.className = "lecture-toc-list";
    for (const item of group.items) {
      const link = document.createElement("a");
      link.className = "lecture-toc-link";
      link.href = item.page + "#slide-" + item.slide;
      const n = document.createElement("span");
      n.className = "lecture-toc-n";
      n.textContent = String(item.global).padStart(2,"0");
      const title = document.createElement("span");
      title.className = "lecture-toc-title";
      title.textContent = item.title;
      link.append(n,title);
      link.addEventListener("click", () => setOpen(false));
      items.append(link);
      links.push({link,item,details});
      detailsByItem.set(item.page+"#slide-"+item.slide,details);
    }
    details.append(summary,items);
    list.append(details);
  }
  drawer.append(header,list);
  document.body.append(backdrop,drawer);

  function selectedKey(){
    const match = location.hash.match(/^#slide-(\d+)$/);
    return currentPage + "#slide-" + (match ? Number(match[1]) : 1);
  }
  function highlight(){
    const key = selectedKey();
    let selected;
    for(const entry of links){
      const active = entry.item.page + "#slide-" + entry.item.slide === key;
      if(active){entry.link.setAttribute("aria-current","page");selected=entry;}
      else entry.link.removeAttribute("aria-current");
    }
    if(selected){
      for(const panel of list.querySelectorAll(".lecture-toc-unit")) {
        panel.open = panel === selected.details;
      }
    }
    return selected;
  }
  function setOpen(open) {
    document.body.classList.toggle("lecture-toc-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "✕ 목차 닫기" : "☰ 강의 목차";
    toggle.setAttribute("aria-label", open ? "강의 목차 닫기" : "강의 목차 열기");
    drawer.setAttribute("aria-hidden", String(!open));
    drawer.inert = !open;
    if(open){
      const selected = highlight();
      if(selected)selected.link.scrollIntoView({block:"nearest"});
      close.focus({preventScroll:true});
    }else if(drawer.contains(document.activeElement)){
      toggle.focus({preventScroll:true});
    }
  }
  toggle.addEventListener("click", () =>
    setOpen(!document.body.classList.contains("lecture-toc-open")));
  close.addEventListener("click", () => setOpen(false));
  backdrop.addEventListener("click", () => setOpen(false));
  document.addEventListener("keydown", e => {
    if(e.key==="Escape"&&document.body.classList.contains("lecture-toc-open")){
      e.preventDefault();setOpen(false);
    }
  });
  window.addEventListener("hashchange",highlight);
  highlight();
})();
