"""Temporary CI geometry investigation: isolated sidebar styles on Intro."""
from playwright.sync_api import sync_playwright

def capture(page, label):
    v=page.evaluate("""() => {
      const s=document.querySelector('.slide.active');
      const b=s.querySelector('.slide-inner');
      const css=getComputedStyle(s);
      return {fit:s.dataset.fitScale, inner:[b.scrollWidth,b.scrollHeight],
              slide:[s.clientWidth,s.clientHeight],
              padding:[css.paddingLeft,css.paddingRight,css.paddingTop,css.paddingBottom],
              doc:[document.documentElement.scrollWidth,innerWidth],
              header:document.querySelector('header').getBoundingClientRect().height};
    }""")
    print("SIDEBAR_GEOMETRY",label,v,flush=True)

with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
    page=browser.new_page(viewport={"width":1366,"height":768})
    page.goto("http://127.0.0.1:8765/intro.html#slide-7",wait_until="load")
    page.wait_for_timeout(600)
    capture(page,"baseline")
    page.locator('link[href*="lecture_sidebar.css"]').evaluate("(el)=>el.disabled=true")
    page.evaluate("window.dispatchEvent(new Event('resize'))")
    page.wait_for_timeout(350)
    capture(page,"stylesheet_disabled")
    page.evaluate("""() => {
      for (const el of document.querySelectorAll(
        '.lecture-toc-drawer,.lecture-toc-backdrop,.lecture-toc-toggle')) el.remove();
      window.dispatchEvent(new Event('resize'));
    }""")
    page.wait_for_timeout(350)
    capture(page,"sidebar_dom_removed")
    browser.close()
