<script setup>
defineProps({ mode: { type: String, default: 'overview' } })

const stages = [
  ['RGB 입력', '64×64×3'],
  ['Conv A + ReLU', '64×64×8'],
  ['Max Pool', '32×32×8'],
  ['Conv B + ReLU', '32×32×16'],
  ['GAP', '특징 16개'],
  ['분류기', '정상·불량 점수'],
]
</script>

<template>
  <div class="network-diagram">
    <div class="network-grouping"><span>사진</span><span>특징 추출기 · Backbone</span><span>판정 · Head</span></div>
    <div class="network-stages">
      <div v-for="([title, shape], index) in stages" :key="title" :class="{ trainable: mode === 'training' && [1, 3, 5].includes(index) }">
        <strong>{{ title }}</strong><span>{{ shape }}</span>
      </div>
    </div>
    <div v-if="mode === 'training'" class="network-training">
      <ConceptCards flow :items="[['예측과 정답', '정답 라벨과 분류기 출력을 비교'], ['손실 · Loss', '예측이 얼마나 어긋났는지 계산'], ['역전파 · Gradient', '각 가중치에 대한 기울기 계산'], ['Optimizer', 'Conv A · Conv B · 분류기 가중치를 갱신']]"/>
      <p class="lab-note">위의 테두리 세 곳이 갱신됩니다. 풀링과 ReLU에도 기울기는 지나가지만 학습 가중치는 없습니다.</p>
    </div>
    <div v-else class="network-example"><AppleView zoom/><p><strong>{{ mode === 'backbone' ? 'Backbone은 공통 특징을 만들고, Head가 과제에 맞는 답을 계산합니다.' : '입력의 숫자가 특징으로 바뀌고, 마지막 층에서 사진 한 장의 점수를 냅니다.' }}</strong><br>이 강의의 가상 사과 CNN은 편향을 포함해 학습 파라미터 1,426개입니다.</p></div>
  </div>
</template>
