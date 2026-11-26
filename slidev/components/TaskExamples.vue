<script setup>
import { ref } from 'vue'

const options = [
  { name: '분류', question: '이 사진의 사과는 정상인가요, 불량인가요?', output: '이미지 전체 · 불량', mode: 'photo' },
  { name: '검출', question: '사과 표면의 결함은 어디에 있나요?', output: '결함의 이름 + 박스 좌표', mode: 'box' },
  { name: '분할', question: '어느 픽셀까지가 결함인가요?', output: '결함에 속하는 픽셀의 마스크', mode: 'mask' },
]
const active = ref(0)
</script>

<template>
  <div class="lecture-interaction task-layout" @keydown.stop @touchstart.stop @touchend.stop>
    <figure><AppleView :mode="options[active].mode" zoom/><figcaption>같은 교육용 사과 사진과 결함 주석</figcaption></figure>
    <div>
      <div class="control-row" aria-label="Vision AI 과제 선택">
        <button v-for="(option, i) in options" :key="option.name" type="button" :aria-pressed="active === i" @click="active = i">{{ option.name }}</button>
      </div>
      <div class="result-panel" aria-live="polite">
        <strong>{{ options[active].question }}</strong>
        <p>{{ options[active].output }}</p>
      </div>
      <p class="lab-note">오늘 학습 예제는 사과 사진 한 장이 정상인지 불량인지 판정합니다.</p>
    </div>
  </div>
</template>
