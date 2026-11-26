<script setup>
import { computed, ref } from 'vue'
import { evaluate, scoreBins } from '../lesson/calculations.js'

const props = defineProps({ mode: { type: String, default: 'interactive' } })
const threshold = ref(props.mode === 'accuracy' ? 1 : 0.5)
const metrics = computed(() => evaluate(threshold.value))
const percent = value => `${(100 * value).toFixed(1)}%`
const chartX = score => 39 + score * 318
const chartY = count => 138 - count * 2.16
</script>

<template>
  <div class="lecture-interaction score-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <template v-if="mode === 'interactive'">
      <div class="control-row score-controls">
        <label>불량을 알리는 기준
          <select v-model.number="threshold">
            <option v-for="value in [0.3, 0.5, 0.7]" :key="value" :value="value">{{ value.toFixed(2) }}</option>
          </select>
        </label>
        <button type="button" @click="threshold = 0.5">초기화</button>
      </div>
      <p class="example-score">예를 들어 점수 0.60의 사과는 현재 기준에서 <strong>{{ 0.6 >= threshold ? '불량 알림' : '알림 없음' }}</strong>입니다.</p>
      <div class="score-board">
        <figure>
          <h2>같은 100건의 점수 분포</h2>
          <svg viewBox="0 0 378 170" role="img" aria-label="실제 정상과 불량의 점수 분포, 점선은 판정 기준">
            <g v-for="tick in [0, 10, 20, 30, 40, 50]" :key="tick" fill="#536b78" font-size="11" text-anchor="end">
              <line :x1="chartX(0)" :x2="chartX(1)" :y1="chartY(tick)" :y2="chartY(tick)" stroke="#dce8ec" />
              <text x="32" :y="chartY(tick) + 4">{{ tick }}</text>
            </g>
            <g v-for="{ score, defective, normal } in scoreBins" :key="score" fill="#315d69" font-size="12" text-anchor="middle">
              <rect :x="chartX(score) - 12" :y="chartY(normal)" width="24" :height="normal * 2.16" fill="#9aaebc" />
              <rect :x="chartX(score) - 12" :y="chartY(normal + defective)" width="24" :height="defective * 2.16" fill="#218c74" />
              <text :x="chartX(score)" :y="chartY(normal + defective) - 5">{{ normal + defective }}</text>
              <text :x="chartX(score)" y="154">{{ score.toFixed(1) }}</text>
            </g>
            <line :x1="chartX(threshold)" :x2="chartX(threshold)" y1="17" y2="138" stroke="#bd7d37" stroke-width="2" stroke-dasharray="5 3" />
            <text :x="chartX(threshold) + 5" y="17" fill="#935820" font-size="12">기준 {{ threshold.toFixed(2) }}</text>
            <text x="357" y="168" text-anchor="end" fill="#536b78" font-size="11">불량 점수 →</text>
          </svg>
          <figcaption>회색 · 실제 정상　 초록 · 실제 불량</figcaption>
        </figure>
        <section aria-live="polite">
          <h2>정답 × 예측</h2>
          <table class="threshold-table" aria-label="100건의 정답과 예측 비교">
            <thead><tr><td>정답 ↓ / 예측 →</td><th scope="col">불량</th><th scope="col">정상</th></tr></thead>
            <tbody>
              <tr><th scope="row">실제 불량 · 20건</th><td><strong data-score="tp">{{ metrics.tp }}</strong>찾아낸 불량</td><td class="score-missed"><strong data-score="fn">{{ metrics.fn }}</strong>놓친 불량</td></tr>
              <tr><th scope="row">실제 정상 · 80건</th><td class="score-false"><strong data-score="fp">{{ metrics.fp }}</strong>잘못 알린 정상</td><td><strong data-score="tn">{{ metrics.tn }}</strong>정상으로 통과</td></tr>
            </tbody>
          </table>
          <details class="score-details">
            <summary>정밀도와 재현율 미리 보기</summary>
            <p>정밀도 {{ percent(metrics.precision) }} · 재현율 {{ percent(metrics.recall) }}</p>
          </details>
        </section>
      </div>
    </template>
    <div v-else class="score-counts" aria-live="polite">
      <div><span>찾아낸 불량 · TP</span><strong data-score="tp">{{ metrics.tp }}</strong></div>
      <div><span>놓친 불량 · FN</span><strong data-score="fn">{{ metrics.fn }}</strong></div>
      <div><span>잘못 알린 정상 · FP</span><strong data-score="fp">{{ metrics.fp }}</strong></div>
      <div><span>정상으로 통과 · TN</span><strong data-score="tn">{{ metrics.tn }}</strong></div>
    </div>
    <div v-if="mode === 'metrics'" class="score-metrics"><strong>정밀도 {{ percent(metrics.precision) }} = 18 ÷ 22</strong><strong>재현율 {{ percent(metrics.recall) }} = 18 ÷ 20</strong></div>
    <div v-if="mode === 'accuracy'" class="score-metrics"><strong>정확도 {{ percent(metrics.accuracy) }} = 80 ÷ 100</strong><strong>불량 20건 모두 놓침</strong></div>
  </div>
</template>
