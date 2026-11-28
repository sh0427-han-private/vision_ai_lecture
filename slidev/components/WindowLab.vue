<script setup>
import { computed, ref } from 'vue'
import { addPadding, convolutionInput, correlate, crop, edgeKernel, maxPool, paddingInput, poolInput, sumKernel } from '../lesson/calculations.js'

const props = defineProps({ mode: { type: String, default: 'kernel' } })
const isPool = props.mode === 'pool'
const choice = ref(props.mode === 'padding' ? 0 : 1)
const position = ref([0, 0])
const stride = computed(() => isPool ? 2 : props.mode === 'stride' ? choice.value : 1)
const weights = props.mode === 'padding' ? sumKernel : edgeKernel
const input = computed(() => {
  if (isPool) return poolInput
  if (props.mode === 'padding') return addPadding(paddingInput, choice.value)
  return convolutionInput
})
const output = computed(() => isPool ? maxPool(input.value) : correlate(input.value, weights, stride.value))
const origin = computed(() => position.value.map(coordinate => coordinate * stride.value))
const size = isPool ? 2 : 3
const windowData = computed(() => crop(input.value, ...origin.value, size))
const example = computed(() => output.value[position.value[0]][position.value[1]])
const rowSums = computed(() => isPool ? [] : windowData.value.map((row, r) =>
  row.reduce((total, value, c) => total + value * weights[r][c], 0)))

function inWindow(row, column) {
  return row >= origin.value[0] && column >= origin.value[1] && row < origin.value[0] + size && column < origin.value[1] + size
}

function select(row, column) {
  position.value = [row, column]
}

function change(value) {
  choice.value = value
  select(0, 0)
}
</script>

<template>
  <div class="lecture-interaction window-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <div v-if="mode === 'kernel'" class="kernel-context">
      <strong>Conv 계산 확대</strong><ArchitectureFigure compact :highlight="['conv-a', 'conv-b']" />
    </div>
    <div v-if="mode === 'stride' || mode === 'padding'" class="control-row" :aria-label="mode === 'stride' ? '이동 간격' : '패딩'">
      <button v-for="option in mode === 'stride' ? [1, 2] : [0, 1]" :key="option" type="button" :aria-pressed="choice === option" @click="change(option)">
        {{ mode === 'stride' ? '이동 간격' : '패딩' }} {{ option }}
      </button>
    </div>
    <div class="window-layout" :class="{ 'window-with-photo': mode === 'kernel' }">
      <figure v-if="mode === 'kernel'" class="kernel-photo">
        <AppleView mode="mark" />
        <AppleView crop="547 183 85 85" />
        <figcaption>사과 사진의 85×85 픽셀 영역</figcaption>
      </figure>
      <div><h2>입력 · {{ input.length }}×{{ input[0].length }}</h2><MatrixGrid :values="input" :highlight="inWindow" label="입력 행렬"/></div>
      <span class="network-arrow" aria-hidden="true">→</span>
      <div><h2>{{ isPool ? '선택한 2×2 영역' : '커널 · 3×3' }}</h2><MatrixGrid :values="isPool ? windowData : weights" :label="isPool ? '선택한 영역' : '커널 값'"/></div>
      <span class="network-arrow" aria-hidden="true">→</span>
      <div><h2>출력 · {{ output.length }}×{{ output[0].length }}</h2><MatrixGrid :values="output" :highlight="(row, column) => row === position[0] && column === position[1]" :label="isPool ? '풀링 출력' : '특징 맵'" interactive @select="select"/></div>
    </div>
    <div class="equation-panel" aria-live="polite" :data-window-result="example">
      <strong>{{ isPool ? '영역의 최댓값' : '각 행의 곱의 합을 더하면' }}</strong>
      <span v-if="isPool">max({{ windowData.flat().join(', ') }}) = {{ example }}</span>
      <span v-else>{{ rowSums.map(n => `(${n})`).join(' + ') }} = {{ example }}</span>
    </div>
    <div v-if="mode === 'kernel'" class="product-row" aria-label="행별 곱셈">
      <code v-for="(row, r) in windowData" :key="r">{{ row.map((value, c) => `${value}×(${weights[r][c]})`).join(' + ') }} = {{ rowSums[r] }}</code>
    </div>
    <p class="lab-note">출력 칸을 누르면 그 값을 계산한 입력 영역이 강조됩니다.</p>
  </div>
</template>
