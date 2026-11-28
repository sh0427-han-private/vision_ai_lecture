<script setup>
defineProps({
  values: { type: Array, required: true },
  label: { type: String, required: true },
  highlight: { type: Function, default: () => false },
  tones: Boolean,
  interactive: Boolean,
})
defineEmits(['select'])
</script>

<template>
  <div class="matrix" role="group" :aria-label="label">
    <div v-for="(row, rid) in values" :key="rid" class="matrix-row">
      <component
        :is="interactive ? 'button' : 'span'" v-for="(value, cid) in row" :key="cid"
        class="matrix-cell" :class="{ selected: highlight(rid, cid) }"
        :type="interactive ? 'button' : undefined"
        :aria-label="interactive ? `${rid + 1}행 ${cid + 1}열, ${value}` : undefined"
        :aria-pressed="interactive ? highlight(rid, cid) : undefined"
        :style="tones ? { backgroundColor: `rgb(${value},${value},${value})`, color: value >= 145 ? '#17243b' : '#fff' } : undefined"
        @click="interactive && $emit('select', rid, cid)"
      >{{ value }}</component>
    </div>
  </div>
</template>
