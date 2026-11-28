<script setup>
import { computed, ref } from 'vue'
import { logic } from '../lesson/calculations.js'

const props = defineProps({ kind: { type: String, required: true }, interactive: Boolean })
const xor = props.kind === 'xor'
const weight = ref(1)
const bias = ref(xor ? -0.5 : -1.2)
const nonlinear = ref(false)
const points = [[0, 0], [0, 1], [1, 0], [1, 1]].map(([x, y]) => ({ x, y, target: Number(xor ? x !== y : x === 1 && y === 1) }))
const display = computed(() => points.map(({ x, y, target }) => ({ x, y, target, prediction: logic(props.kind, x, y, weight.value, bias.value, nonlinear.value) })))
const boundaries = computed(() => xor && nonlinear.value ? [-0.5, 0.5] : [0])
const px = n => 88 + n * 152
const py = n => 209 - n * 152
const defaultBias = () => xor && nonlinear.value ? -1 : xor ? -0.5 : -1.2
function changeMode(enabled) {
  nonlinear.value = enabled
  weight.value = 1
  bias.value = defaultBias()
}
</script>

<template>
  <div class="lecture-interaction gate-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <svg viewBox="0 0 328 264" role="img" :aria-label="`${kind.toUpperCase()} 입력 네 점과 결정 경계`">
      <defs><clipPath :id="`gate-range-${kind}-${interactive ? 'lab' : 'rule'}`"><rect x="36" y="16" width="255" height="235"/></clipPath></defs>
      <rect x="36" y="16" width="255" height="235" rx="10" fill="#edf5f2"/>
      <path d="M36 209H291M88 16V251" fill="none" stroke="#879f99" stroke-width="2"/>
      <g v-if="interactive" :clip-path="`url(#gate-range-${kind}-lab)`">
        <line v-for="offset in boundaries" :key="offset" :x1="px(-1)" :y1="py(offset + weight - bias)" :x2="px(2)" :y2="py(offset - 2 * weight - bias)" stroke="#cf801d" stroke-width="4" stroke-dasharray="8 5"/>
      </g>
      <g v-for="point in display" :key="`${point.x},${point.y}`">
        <circle :cx="px(point.x)" :cy="py(point.y)" r="13" :fill="point.target ? '#137967' : '#fff'" :stroke="interactive && point.target !== point.prediction ? '#ba5f20' : '#137967'" stroke-width="3"/>
        <text :x="px(point.x)" :y="py(point.y) + 4" text-anchor="middle" font-size="12" font-weight="750" :fill="point.target ? '#fff' : '#183c32'">{{ point.target }}</text>
      </g>
      <text x="302" y="213" font-size="16">x₁</text><text x="78" y="15" font-size="16">x₂</text>
    </svg>
    <div>
      <table class="gate-table"><thead><tr><th>입력 (x₁, x₂)</th><th>정답</th><th v-if="interactive">현재 판정</th></tr></thead>
        <tbody><tr v-for="point in display" :key="`${point.x}${point.y}`" :data-gate-correct="interactive ? String(point.target === point.prediction) : undefined"><td>{{ point.x }}, {{ point.y }}</td><td>{{ point.target }}</td><td v-if="interactive">{{ point.prediction }}</td></tr></tbody>
      </table>
      <template v-if="interactive">
        <div class="control-row gate-controls" v-if="xor">
          <button type="button" :aria-pressed="!nonlinear" @click="changeMode(false)">직선 하나</button>
          <button type="button" :aria-pressed="nonlinear" @click="changeMode(true)">ReLU 조합</button>
        </div>
        <div class="control-row gate-controls">
          <label>W {{ weight.toFixed(1) }} <input v-model.number="weight" type="range" min="0.4" max="1.6" step="0.1"></label>
          <label>b {{ bias.toFixed(1) }} <input v-model.number="bias" type="range" min="-1.8" max="-0.3" step="0.1"></label>
          <button type="button" @click="changeMode(false)">초기화</button>
        </div>
      </template>
    </div>
  </div>
</template>
