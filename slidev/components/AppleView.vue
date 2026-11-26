<script setup>
import { apple, normalApple } from '../lesson/assets.js'

defineProps({ mode: { type: String, default: 'photo' }, filter: String, x: { type: Number, default: 0 }, normal: Boolean, zoom: Boolean })
</script>

<template>
  <svg :viewBox="zoom ? '430 100 295 295' : '0 0 960 640'" class="apple-view" role="img" :aria-label="normal ? '교육용 정상 사과 사진' : '표면에 작은 반점이 있는 교육용 사과 사진'">
    <rect width="960" height="640" fill="#e9eeed"/>
    <image :href="normal ? normalApple : apple" :x="x" width="960" height="640" :style="{ filter }"/>
    <ellipse v-if="mode === 'mark'" cx="589" cy="224" rx="26" ry="26" fill="none" stroke="#ffde88" stroke-width="8"/>
    <rect v-if="mode === 'box'" x="565" y="197" width="53" height="57" rx="2" fill="none" stroke="#4ff0d0" stroke-width="6"/>
    <path v-if="mode === 'mask'" d="M581 201 Q601 193 612 214 Q619 228 605 243 Q589 255 575 236 Q566 222 572 209 Z" fill="#40e7c6" fill-opacity=".68" stroke="#e1fff7" stroke-width="3"/>
  </svg>
</template>
