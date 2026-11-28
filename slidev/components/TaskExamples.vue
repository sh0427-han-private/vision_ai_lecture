<script setup>
import { ref } from 'vue'

const options = [
  { name: '분류', english: 'Classification', question: '이 사진은 정상인가요, 불량인가요?', output: '이미지 전체 · 불량', mode: 'photo' },
  { name: '검출', english: 'Detection', question: '표면의 결함은 어디에 있나요?', output: '결함의 이름과 박스 좌표', mode: 'box' },
  { name: '분할', english: 'Segmentation', question: '어느 픽셀까지가 결함인가요?', output: '결함에 속하는 픽셀의 마스크', mode: 'mask' },
]
const active = ref(0)
</script>

<template>
  <div class="lecture-interaction task-layout" @keydown.stop @touchstart.stop @touchend.stop>
    <div class="task-panels" aria-label="Vision AI 과제 선택">
      <button v-for="(option, i) in options" :key="option.name" class="task-panel" type="button" :aria-label="option.name" :aria-pressed="active === i" @click="active = i">
        <strong>{{ option.english }} · {{ option.name }}</strong>
        <AppleView :mode="option.mode" crop="425 130 330 210"/>
        <span class="task-question">{{ option.question }}</span>
        <span class="task-answer">정답 · {{ option.output }}</span>
      </button>
    </div>
    <div class="result-panel" aria-live="polite">
      <strong>{{ options[active].name }}</strong> · {{ options[active].output }}
      <p>그림의 박스와 마스크는 같은 사진에 사람이 표시한 정답 예시입니다.</p>
    </div>
  </div>
</template>
