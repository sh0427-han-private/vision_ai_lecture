<script setup>
import { apple } from '../lesson/assets.js'
import { appleBoxes, overlap } from '../lesson/calculations.js'

const { target, prediction } = appleBoxes
const match = overlap(target, prediction)
</script>

<template>
  <div class="iou-example">
    <figure>
      <svg viewBox="440 100 300 300" role="img" aria-label="사과 결함의 정답 박스와 교육용 예측 박스, 두 박스가 겹치는 영역">
        <image :href="apple" width="960" height="640"/>
        <rect :x="match.x" :y="match.y" :width="match.width" :height="match.height" fill="#3ed4ac" fill-opacity=".52"/>
        <rect v-bind="target" fill="none" stroke="#b7ffea" stroke-width="4"/>
        <rect v-bind="prediction" fill="none" stroke="#ffe297" stroke-width="4" stroke-dasharray="8 4"/>
      </svg>
      <figcaption>실선은 정답, 점선은 예측 예시</figcaption>
    </figure>
    <div class="iou-calculation">
      <ConceptCards :items="[['교집합', '두 박스가 겹치는 영역', `${match.intersection}`], ['합집합', '두 박스를 합쳐 덮는 전체 영역', `${match.union}`]]"/>
      <div class="equation-panel" :data-iou="match.iou"><strong>IoU</strong><span>{{ match.intersection }} ÷ {{ match.union }} ≈ {{ match.iou.toFixed(3) }}</span></div>
    </div>
  </div>
</template>
