<script setup>
import { evaluate } from '../lesson/calculations.js'

const { tp, fn, fp, tn } = evaluate(0.5)
</script>

<template>
  <table class="confusion-table">
    <caption>교육용 검증 예시 100건 · 임계값 0.50</caption>
    <thead><tr><td/><th scope="col">예측 · 불량</th><th scope="col">예측 · 정상</th></tr></thead>
    <tbody>
      <tr><th scope="row">실제 · 불량</th><td><strong>{{ tp }}</strong> 찾아낸 불량 · TP</td><td class="false-result"><strong>{{ fn }}</strong> 놓친 불량 · FN</td></tr>
      <tr><th scope="row">실제 · 정상</th><td class="false-result"><strong>{{ fp }}</strong> 잘못 알린 정상 · FP</td><td><strong>{{ tn }}</strong> 정상으로 통과 · TN</td></tr>
    </tbody>
  </table>
</template>
