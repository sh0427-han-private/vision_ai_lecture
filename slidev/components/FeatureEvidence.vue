<script setup>
import input from '../figures/apple-feature-input.png?url'
import maps from '../figures/apple-feature-maps.png?url'
import metadata from '../figures/apple-feature-maps.json'

const stageNames = ['얕은 층', '중간 층', '깊은 층']
const panelSize = 96
const panelStep = 102
</script>

<template>
  <div class="feature-evidence">
    <figure class="feature-stage feature-input">
      <h2>입력 사진</h2><p>224×224×3</p>
      <img :src="input" alt="공식 전처리를 거친 224×224 사과 사진">
      <figcaption>모델에 넣은 교육용 사과</figcaption>
    </figure>
    <figure v-for="(stage, row) in metadata.stages" :key="stage.layer" class="feature-stage" :class="`feature-stage-${row}`">
      <h2>{{ stageNames[row] }}</h2><p>{{ stage.shape.join('×') }}</p>
      <div class="feature-tiles">
        <svg v-for="(channel, column) in stage.channels" :key="channel" :viewBox="`${column * panelStep} ${row * panelStep} ${panelSize} ${panelSize}`" role="img" :aria-label="`${stageNames[row]}의 채널 ${channel} 특징 맵`">
          <image :href="maps" width="402" height="300"/>
        </svg>
      </div>
      <figcaption>features[{{ stage.layer }}] · 4 / {{ stage.shape[2] }}채널<br>{{ stage.channels.join(', ') }}</figcaption>
    </figure>
  </div>
</template>
