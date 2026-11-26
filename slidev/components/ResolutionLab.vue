<script setup>
import { onMounted, ref } from 'vue'
import { apple } from '../lesson/assets.js'

const sizes = [160, 320, 640]
const selected = ref(0)
const rendered = ref([])
const failed = ref(false)
onMounted(async () => {
  try {
    const image = new Image()
    image.src = apple
    await image.decode()
    const cropWidth = Math.min(image.naturalWidth, image.naturalHeight * 16 / 9)
    const cropHeight = cropWidth * 9 / 16
    rendered.value = sizes.map(width => {
      const height = width * 9 / 16
      const full = document.createElement('canvas')
      full.width = width
      full.height = height
      const context = full.getContext('2d')
      context.imageSmoothingQuality = 'high'
      context.drawImage(image, (image.naturalWidth - cropWidth) / 2, (image.naturalHeight - cropHeight) / 2,
        cropWidth, cropHeight, 0, 0, width, height)
      const zoom = document.createElement('canvas')
      zoom.width = 300
      zoom.height = 190
      const zoomContext = zoom.getContext('2d')
      zoomContext.imageSmoothingEnabled = false
      zoomContext.drawImage(full, 0.54 * width, 0.27 * height, 0.15 * width, 0.095 * width, 0, 0, zoom.width, zoom.height)
      return { full: full.toDataURL(), zoom: zoom.toDataURL(), width, height }
    })
  } catch {
    failed.value = true
  }
})
</script>

<template>
  <div class="lecture-interaction resolution-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <div class="control-row">
      <button v-for="(width, i) in sizes" :key="width" type="button" :aria-pressed="selected === i" @click="selected = i">{{ width }}×{{ width * 9 / 16 }}</button>
    </div>
    <div v-if="rendered.length" class="resolution-images" :data-raster-width="rendered[selected].width">
      <figure><img :src="rendered[selected].full" alt="선택한 해상도로 축소한 사과 사진"><figcaption>{{ rendered[selected].width }}×{{ rendered[selected].height }}로 축소</figcaption></figure>
      <figure><img :src="rendered[selected].zoom" alt="축소 이미지에서 같은 결함 위치를 확대한 그림"><figcaption>같은 위치를 화면에서 같은 크기로 확대</figcaption></figure>
    </div>
    <p v-else role="status">{{ failed ? '비교할 사진을 불러오지 못했습니다.' : '해상도를 계산하는 중입니다.' }}</p>
  </div>
</template>
