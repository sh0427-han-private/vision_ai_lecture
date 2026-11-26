<script setup>
import input from '../figures/apple-feature-input.png?url'
import maps from '../figures/apple-feature-maps.png?url'
import metadata from '../figures/apple-feature-maps.json'
</script>

<template>
  <div class="feature-evidence">
    <figure><img :src="input" alt="공식 전처리를 거친 224×224 사과 사진"><figcaption>실제 모델 입력 · 224×224 RGB</figcaption></figure>
    <div class="feature-layer-labels">
      <div v-for="stage in metadata.stages" :key="stage.layer">
        <strong>features[{{ stage.layer }}]</strong><span>{{ stage.shape.join('×') }}</span><span>채널 {{ stage.channels.join(', ') }}</span>
      </div>
    </div>
    <figure><img :src="maps" alt="SqueezeNet 세 단계에서 계산한 학습 특징 맵, 각 단계에서 네 채널 표시"><figcaption>각 단계에서 위치별 차이가 큰 채널 4개를 표시</figcaption></figure>
  </div>
</template>
