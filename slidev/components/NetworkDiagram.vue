<script setup>
defineProps({ mode: { type: String, default: 'overview' } })
</script>

<template>
  <div class="network-diagram">
    <ArchitectureFigure :compact="mode === 'training'" :highlight="mode === 'training' ? ['conv-a', 'conv-b', 'head'] : []" />
    <div v-if="mode === 'training'" class="network-training">
      <ConceptCards flow :items="[['예측과 정답', '정답 라벨과 분류기 출력을 비교'], ['손실 · Loss', '예측이 얼마나 어긋났는지 계산'], ['역전파 · Gradient', '각 가중치에 대한 기울기 계산'], ['Optimizer', 'Conv A · Conv B · 분류기 가중치를 갱신']]"/>
      <p class="lab-note">강조한 Conv A·Conv B·Dense 2가 갱신됩니다. 풀링과 ReLU에도 기울기는 지나가지만 학습 가중치는 없습니다.</p>
    </div>
    <p v-else class="network-note">{{ mode === 'backbone' ? 'Backbone은 공통 특징을 만들고, Head가 과제에 맞는 답을 계산합니다.' : 'Conv와 Dense의 가중치는 학습됩니다. ReLU·풀링·채널별 평균은 정해진 연산을 적용합니다.' }}</p>
  </div>
</template>
