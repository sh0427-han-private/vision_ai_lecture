<template>
  <div class="opening-flow">
    <figure><AppleView /><figcaption>사과 사진을 입력</figcaption></figure>
    <span aria-hidden="true">→</span>
    <div class="opening-process"><strong>AI 분석</strong><p>표면에서 결함의 단서를 찾습니다.</p></div>
    <span aria-hidden="true">→</span>
    <figure><AppleView mode="mark" crop="240 85 475 475" /><figcaption>결함이 의심되는 위치 표시</figcaption></figure>
  </div>
  <section class="opening-examples">
    <h2>생활 속 Vision AI</h2>
    <ConceptCards :items="[['스마트폰 사진 앱', '사진 속 반려동물 찾기'], ['카메라가 달린 로봇청소기', '바닥의 신발 같은 장애물 알아보기']]" />
  </section>
</template>
