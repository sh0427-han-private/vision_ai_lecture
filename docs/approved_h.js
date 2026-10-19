/* Actual raster downsampling of one unchanged source ROI for P54. */
(() => {
  const canvases=[...document.querySelectorAll('[data-h-review-resolution]')];
  if(!canvases.length)return;
  const source=new Image();
  source.onload=()=>{
    for(const canvas of canvases){
      const size=Number(canvas.dataset.hReviewResolution);
      canvas.width=size;canvas.height=size;
      const ctx=canvas.getContext('2d');ctx.imageSmoothingEnabled=true;ctx.imageSmoothingQuality='high';
      ctx.drawImage(source,300,85,450,450,0,0,size,size);
      canvas.dataset.ready='true';
    }
  };
  source.onerror=()=>{for(const canvas of canvases){canvas.dataset.ready='error';canvas.replaceWith(Object.assign(document.createElement('p'),{textContent:'사진을 불러오지 못했습니다.'}));}};
  source.src='assets/vision_task_apple_reference.jpg';
})();
