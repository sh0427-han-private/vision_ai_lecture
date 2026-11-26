<script setup>
import { onMounted, ref } from 'vue'
import { apple } from '../lesson/assets.js'
import { luma } from '../lesson/calculations.js'

const props = defineProps({ mode: { type: String, default: 'numbers' } })
const channels = ref([])
const numbers = ref([])
const error = ref('')

onMounted(async () => {
  try {
    const image = new Image()
    image.src = apple
    await image.decode()
    const canvas = document.createElement('canvas')
    const isRgb = props.mode === 'channels'
    canvas.width = isRgb ? 192 : 12
    canvas.height = isRgb ? 128 : 8
    const context = canvas.getContext('2d', { willReadFrequently: true })
    context.drawImage(image, 0, 0, canvas.width, canvas.height)
    const buffer = context.getImageData(0, 0, canvas.width, canvas.height).data
    if (!isRgb) {
      numbers.value = Array.from({ length: 8 }, (_, row) => Array.from({ length: 12 }, (_, column) => {
        const i = (row * 12 + column) * 4
        return luma(buffer[i], buffer[i + 1], buffer[i + 2])
      }))
      return
    }
    channels.value = ['R', 'G', 'B'].map((name, channel) => {
      const layer = context.createImageData(canvas.width, canvas.height)
      for (let i = 0; i < buffer.length; i += 4) {
        layer.data[i + channel] = buffer[i + channel]
        layer.data[i + 3] = 255
      }
      context.putImageData(layer, 0, 0)
      return { name, src: canvas.toDataURL('image/png') }
    })
  } catch {
    error.value = '사진을 숫자로 읽을 수 없습니다.'
  }
})
</script>

<template>
  <div v-if="mode === 'numbers'" class="encoding-layout">
    <figure>
      <div class="encoding-photo"><AppleView/><span aria-hidden="true" class="photo-marker"/></div>
      <figcaption>사람이 알아보는 사과</figcaption>
    </figure>
    <span class="network-arrow" aria-hidden="true">→</span>
    <figure v-if="numbers.length" class="encoding-matrix">
      <MatrixGrid :values="numbers" :highlight="(row, column) => row === 2 && column === 7" label="사진을 줄인 8행 12열 밝기 숫자" />
      <figcaption>사진을 8×12로 줄여 읽은 밝기 숫자</figcaption>
    </figure>
    <p v-else role="status">{{ error || '밝기 숫자 계산 중' }}</p>
  </div>
  <div v-else-if="channels.length" class="channel-picture">
    <figure><AppleView/><figcaption>RGB 사진</figcaption></figure>
    <figure v-for="channel in channels" :key="channel.name">
      <img :src="channel.src" :alt="`${channel.name} 채널의 위치별 값`">
      <figcaption>{{ channel.name }} 채널 · H×W</figcaption>
    </figure>
  </div>
  <p v-else role="status">{{ error || '색 채널 계산 중' }}</p>
</template>
