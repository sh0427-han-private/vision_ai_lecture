<template>
  <div class="recap-questions lecture-interaction" @keydown.stop @touchstart.stop @touchend.stop>
    <details v-for="[question, answer] in [
      ['사진은 컴퓨터에 어떻게 들어가나요?', '픽셀 위치마다 밝기 또는 RGB 숫자가 배열에 들어갑니다.'],
      ['CNN은 작은 특징을 어떻게 찾나요?', '같은 커널로 여러 영역의 값을 계산해 특징 맵을 만듭니다.'],
      ['학습할 때 무엇이 바뀌나요?', '예측과 정답으로 손실을 계산하고 커널과 분류기의 가중치를 갱신합니다.'],
      ['새로운 사과에서도 잘 되는지 어떻게 확인하나요?', '검증에서 기준을 정한 뒤 처음 보는 사과 그룹의 오류를 확인합니다.'],
    ]" :key="question">
      <summary>{{ question }}</summary><p>{{ answer }}</p>
    </details>
  </div>
</template>
