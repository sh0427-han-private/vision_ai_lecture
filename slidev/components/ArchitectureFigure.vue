<script setup>
import { computed, useId } from 'vue'
import source from '../../docs/assets/lesson/cnn_apple_architecture.svg?raw'
import { apple } from '../lesson/assets.js'

const props = defineProps({ compact: Boolean, highlight: { type: Array, default: () => [] } })
const identifier = useId()
const figure = computed(() => {
  // Use the checked-in drawing, including its local photo and accessible labels.
  let svg = source.replace('../vision_task_apple_reference.jpg', apple)
    .replace(/arch-(title|desc|arrow)\b/g, `$&-${identifier}`)
  if (props.compact) svg = svg.replace('height="430" viewBox="0 0 1280 430"', 'height="85" viewBox="0 0 1280 85"')
  for (const stage of props.highlight) {
    svg = svg.replace(`class="arch-node" data-arch-node="${stage}"`, `class="arch-node arch-hi" data-arch-node="${stage}"`)
  }
  return svg
})
</script>

<template>
  <div class="lecture-architecture" :class="{ 'architecture-strip': compact }" v-html="figure" />
</template>
