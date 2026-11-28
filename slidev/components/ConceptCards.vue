<script setup>
defineProps({ items: { type: Array, required: true }, flow: Boolean })
</script>

<template>
  <div class="concept-cards" :class="{ 'concept-flow': flow }" :style="{ '--columns': items.length }">
    <section v-for="([title, detail, evidence], index) in items" :key="title" class="concept-card">
      <div v-if="evidence" class="card-evidence">{{ evidence }}</div>
      <h2>{{ title }}</h2>
      <p>{{ detail }}</p>
      <span v-if="flow && index < items.length - 1" class="flow-arrow" aria-hidden="true">→</span>
    </section>
  </div>
</template>
