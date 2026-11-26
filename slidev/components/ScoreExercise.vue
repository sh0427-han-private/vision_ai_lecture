<script setup>
import { computed, ref } from 'vue'
import { evaluate, scoreBins } from '../lesson/calculations.js'

const props = defineProps({ mode: { type: String, default: 'interactive' } })
const threshold = ref(props.mode === 'accuracy' ? 1 : 0.5)
const metrics = computed(() => evaluate(threshold.value))
const percent = value => `${(100 * value).toFixed(1)}%`
</script>

<template>
  <div class="lecture-interaction score-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <template v-if="mode === 'interactive'">
      <div class="control-row">
        <label>불량을 알리는 기준
          <select v-model.number="threshold">
            <option v-for="value in [0.3, 0.5, 0.7]" :key="value" :value="value">{{ value.toFixed(2) }}</option>
          </select>
        </label>
        <button type="button" @click="threshold = 0.5">초기화</button>
      </div>
      <p class="example-score">예를 들어 점수 0.60의 사과는 현재 기준에서 <strong>{{ 0.6 >= threshold ? '불량 알림' : '알림 없음' }}</strong>입니다.</p>
      <div class="score-histogram" aria-label="불량 점수 분포">
        <div v-for="bin in scoreBins" :key="bin.score" class="score-bin" :class="{ 'score-alert': bin.score >= threshold }">
          <b>{{ bin.defective + bin.normal }}건</b>
          <div class="score-stack" :style="{ '--normal': `${bin.normal * 1.1}px`, '--defective': `${bin.defective * 1.1}px` }" :aria-label="`실제 정상 ${bin.normal}건, 실제 불량 ${bin.defective}건`"><i/><i/></div>
          <span>점수 {{ bin.score.toFixed(1) }}</span>
        </div>
      </div>
      <p class="score-legend">회색 · 실제 정상　　초록 · 실제 불량</p>
    </template>
    <div class="score-counts" aria-live="polite">
      <div><span>{{ mode === 'interactive' ? '찾아낸 불량' : '찾아낸 불량 · TP' }}</span><strong data-score="tp">{{ metrics.tp }}</strong></div>
      <div><span>{{ mode === 'interactive' ? '놓친 불량' : '놓친 불량 · FN' }}</span><strong data-score="fn">{{ metrics.fn }}</strong></div>
      <div><span>{{ mode === 'interactive' ? '잘못 알린 정상' : '잘못 알린 정상 · FP' }}</span><strong data-score="fp">{{ metrics.fp }}</strong></div>
      <div><span>{{ mode === 'interactive' ? '정상으로 통과' : '정상으로 통과 · TN' }}</span><strong data-score="tn">{{ metrics.tn }}</strong></div>
    </div>
    <details v-if="mode === 'interactive'" class="score-details">
      <summary>정밀도와 재현율 미리 보기</summary>
      <p>정밀도 {{ percent(metrics.precision) }} · 재현율 {{ percent(metrics.recall) }}</p>
    </details>
    <div v-if="mode === 'metrics'" class="score-metrics"><strong>정밀도 {{ percent(metrics.precision) }} = 18 ÷ 22</strong><strong>재현율 {{ percent(metrics.recall) }} = 18 ÷ 20</strong></div>
    <div v-if="mode === 'accuracy'" class="score-metrics"><strong>정확도 {{ percent(metrics.accuracy) }} = 80 ÷ 100</strong><strong>불량 20건 모두 놓침</strong></div>
  </div>
</template>
