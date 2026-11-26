<script setup>
defineProps({ cases: { type: Array, required: true }, frame: Boolean })
</script>

<template>
  <div class="apple-comparisons" :style="{ '--columns': cases.length }">
    <figure v-for="([title, description, options], index) in cases" :key="title">
      <div class="comparison-photo" :class="options?.effect">
        <AppleView :normal="options?.normal" :mode="options?.mode || 'photo'" :filter="options?.filter" :x="frame ? index * 26 - 39 : 0" :zoom="options?.zoom"/>
      </div>
      <h2>{{ title }}</h2>
      <figcaption>{{ description }}</figcaption>
    </figure>
  </div>
</template>
