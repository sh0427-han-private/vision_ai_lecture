<script setup>
defineProps({ number: String, concept: String, title: String, lead: String, foot: String })
</script>

<template>
  <article class="lecture-slide" :data-concept="concept" :data-lecture-number="number">
    <header class="lecture-header">
      <p v-if="concept === 'start'" class="presenter-line">안녕하세요. 저는 Vision AI를 하는 사람입니다.</p>
      <h1>{{ title }}</h1>
      <p v-if="lead" class="lecture-lead">{{ lead }}</p>
    </header>
    <div class="lecture-body"><slot /></div>
    <footer class="lecture-footer"><span>{{ foot }}</span><span>{{ number }}</span></footer>
  </article>
</template>
