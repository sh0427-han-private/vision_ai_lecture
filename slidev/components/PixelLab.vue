<script setup>
import { computed, onMounted, ref, shallowRef } from 'vue'
import { apple } from '../lesson/assets.js'
import { adjustBrightness, luma } from '../lesson/calculations.js'

const props = defineProps({ mode: { type: String, default: 'gray' } })
const gray = props.mode === 'gray'
const size = gray ? 6 : 1
const image = ref(null)
const pixels = shallowRef(null)
const failed = ref('')
const width = ref(gray ? 48 : 960)
const height = ref(gray ? 32 : 640)
const x = ref(0)
const y = ref(0)
const brightness = ref(1)
function reset() {
  x.value = gray ? 18 : Math.floor(width.value * 0.62)
  y.value = gray ? 10 : Math.floor(height.value * 0.35)
  brightness.value = 1
}
reset()

function readImage() {
  if (pixels.value || !image.value?.naturalWidth) return
  try {
    if (!gray) {
      width.value = image.value.naturalWidth
      height.value = image.value.naturalHeight
    }
    const canvas = document.createElement('canvas')
    canvas.width = width.value
    canvas.height = height.value
    const context = canvas.getContext('2d', { willReadFrequently: true })
    context.drawImage(image.value, 0, 0, canvas.width, canvas.height)
    pixels.value = context.getImageData(0, 0, canvas.width, canvas.height).data
    reset()
  } catch {
    failed.value = '사진의 픽셀을 읽을 수 없습니다.'
  }
}
onMounted(readImage)

function move(col, row) {
  x.value = Math.min(width.value - size, Math.max(0, col))
  y.value = Math.min(height.value - size, Math.max(0, row))
}

function choose(event) {
  if (!pixels.value || !event.detail) return
  const rect = image.value.getBoundingClientRect()
  const offset = gray ? 3 : 0
  move(Math.floor((event.clientX - rect.left) * width.value / rect.width) - offset,
    Math.floor((event.clientY - rect.top) * height.value / rect.height) - offset)
}

const directions = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] }
function navigateImage(event) {
  const delta = directions[event.key]
  if (!delta) return
  event.preventDefault()
  move(x.value + delta[0], y.value + delta[1])
}

function rgbAt(col, row) {
  const offset = (row * width.value + col) * 4
  return pixels.value.slice(offset, offset + 3)
}

const colors = computed(() => pixels.value ? Array.from(rgbAt(x.value, y.value)) : [])
const grayValues = computed(() => pixels.value && gray ? Array.from({ length: 6 }, (_, row) =>
  Array.from({ length: 6 }, (_, col) => adjustBrightness(luma(...rgbAt(x.value + col, y.value + row)), brightness.value))) : [])
const marker = computed(() => ({
  left: `${(x.value + (gray ? 0 : 0.5)) / width.value * 100}%`,
  top: `${(y.value + (gray ? 0 : 0.5)) / height.value * 100}%`,
  width: gray ? `${size / width.value * 100}%` : undefined,
  height: gray ? `${size / height.value * 100}%` : undefined,
}))
</script>

<template>
  <div class="lecture-interaction pixel-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <figure>
      <button class="photo-picker" type="button" :aria-label="gray ? '사진에서 6×6 영역 선택' : '사진에서 RGB 픽셀 선택'" @click="choose" @keydown="navigateImage">
        <img ref="image" :src="apple" alt="픽셀을 읽을 사과 사진" :style="gray ? { filter: `grayscale(1) brightness(${brightness})` } : undefined" @load="readImage" @error="failed = '사과 사진을 불러오지 못했습니다.'">
        <span v-if="pixels" aria-hidden="true" class="photo-marker" :class="{ point: !gray }" :style="marker"/>
      </button>
      <figcaption>사진을 누르거나 방향키로 선택 영역을 이동합니다.</figcaption>
    </figure>
    <div v-if="pixels" class="pixel-details">
      <output class="pixel-coordinate" :data-x="x" :data-y="y">{{ gray ? `x ${x}–${x + 5}, y ${y}–${y + 5}` : `x ${x}, y ${y}` }}</output>
      <div v-if="gray" class="gray-pair">
        <div><h2>밝기값</h2><MatrixGrid :values="grayValues" label="6×6 밝기값" /></div>
        <div><h2>같은 값의 명암</h2><MatrixGrid :values="grayValues" label="6×6 명암" tones /></div>
      </div>
      <div v-else class="rgb-result">
        <div class="rgb-swatch" :style="{ background: `rgb(${colors.join(',')})` }" aria-hidden="true"/>
        <div v-for="(name, i) in ['R', 'G', 'B']" :key="name" class="rgb-readout"><span>{{ name }}</span><b>{{ colors[i] }}</b></div>
      </div>
      <div class="control-row pixel-controls">
        <label v-if="gray">밝기 {{ brightness.toFixed(1) }}× <input v-model.number="brightness" type="range" min="0.5" max="1.5" step="0.1"></label>
        <button type="button" @click="reset">초기화</button>
      </div>
      <p class="lab-note">{{ gray ? '48×32 축소 사진에서 8비트 밝기값을 계산합니다.' : `원본 사진 ${height}×${width}에서 읽은 RGB입니다.` }}</p>
    </div>
    <p v-else role="status">{{ failed || '픽셀을 읽는 중입니다.' }}</p>
  </div>
</template>
