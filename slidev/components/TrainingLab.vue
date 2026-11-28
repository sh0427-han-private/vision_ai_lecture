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
    <div class="training-context"><AppleView zoom/><span>사과 사진과 정답으로 배우는 원리를 작은 숫자 예제로 확인합니다.</span></div>
    <div class="training-layout">
      <section class="training-calculation">
        <h2>정답 4를 맞히도록 학습시키면?</h2>
        <div class="training-input"><span>입력 {{ training.input }}</span><span aria-hidden="true">→</span><span>예측 = W × 입력</span><span aria-hidden="true">→</span><span>정답 {{ training.target }}</span></div>
        <div class="training-equation" aria-live="polite">ŷ = {{ format(weight) }} × 2 = <strong data-learning="prediction">{{ format(result.predicted) }}</strong></div>
        <div class="control-row">
          <button class="training-step" type="button" :disabled="steps >= 8" @click="train">학습 1단계</button>
          <button type="button" @click="reset">초기화</button>
          <span>{{ steps }}회 갱신</span>
        </div>
        <p>가중치 W = <b data-learning="weight">{{ format(weight) }}</b></p>
        <p>손실 = ({{ format(result.predicted) }} − 4)² = <b data-learning="loss">{{ format(result.loss) }}</b></p>
      </section>
      <section class="training-chart">
        <h2>예측이 정답에 가까워지는 과정</h2>
        <div class="training-bars" aria-hidden="true">
          <div><strong>{{ training.target }}</strong><i style="height: var(--chart-y)"/></div>
          <div><strong>{{ format(result.predicted) }}</strong><i :style="{ height: `calc(var(--chart-y) * ${result.predicted / training.target})` }"/></div>
        </div>
        <div class="training-chart-labels"><span>정답(고정)</span><span>현재 예측</span></div>
      </section>
    </div>
  </div>
</template>
