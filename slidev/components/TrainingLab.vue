<script setup>
import { computed, ref } from 'vue'
import { nextWeight, regression, training } from '../lesson/calculations.js'

const weight = ref(training.initialWeight)
const steps = ref(0)
const result = computed(() => regression(weight.value))
const format = value => String(Number(value.toFixed(3)))

function train() {
  if (steps.value === 8) return
  weight.value = nextWeight(weight.value)
  steps.value += 1
}

function reset() {
  weight.value = training.initialWeight
  steps.value = 0
}
</script>

<template>
  <div class="lecture-interaction training-lab" @keydown.stop @touchstart.stop @touchend.stop>
    <div class="training-strip" aria-live="polite">
      <div><small>입력</small><strong>{{ training.input }}</strong></div>
      <div><small>정답</small><strong>{{ training.target }}</strong></div>
      <div><small>예측</small><strong data-learning="prediction">{{ format(result.predicted) }}</strong></div>
      <div><small>손실 · Loss</small><strong data-learning="loss">{{ format(result.loss) }}</strong></div>
      <div><small>가중치 · W</small><strong data-learning="weight">{{ format(weight) }}</strong></div>
    </div>
    <div class="training-chart" aria-label="예측과 정답의 차이">
      <div><span>예측</span><progress :value="result.predicted" max="4" aria-label="예측값"/></div>
      <div><span>정답</span><progress value="4" max="4" aria-label="정답값"/></div>
    </div>
    <div class="equation-panel"><strong>오차에 주는 벌점</strong><span>({{ format(result.predicted) }} − 4)² = {{ format(result.loss) }}</span></div>
    <div class="control-row">
      <button type="button" :disabled="steps >= 8" @click="train">학습 1단계</button>
      <button type="button" @click="reset">초기화</button>
      <span>{{ steps }}회 갱신</span>
    </div>
  </div>
</template>
