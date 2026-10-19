/* Actual activation image: disclose failure instead of fabricating measured maps. */
(() => {
  'use strict';
  for (const root of document.querySelectorAll('[data-d55-real-maps]')) {
    const probe = new Image();
    probe.onload = () => {
      root.dataset.loadState = 'ready';
      window.dispatchEvent(new Event('resize'));
    };
    probe.onerror = () => {
      root.dataset.loadState = 'error';
      window.dispatchEvent(new Event('resize'));
    };
    probe.src = new URL('assets/lesson/cnn_squeezenet_actual_feature_maps.png', document.baseURI).href;
  }
})();
