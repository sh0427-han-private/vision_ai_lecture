# 얼룩말 CNN 특징 비유와 전이학습

- 기준 main: c3139cd. Intro13+Course43=56장, 전체 강의 120분.
- C11 기존 얼룩말 CNN Architecture 유지. 바로 뒤 C12 `cnn-why` 추가: 작은 경계/줄무늬 → 부분·형태 조합 → 얼룩말 분류. 사람도 전체 형태와 맥락을 함께 본다는 점과 CNN이 뇌를 동일하게 재현하지 않는다는 한계를 명시했다. 도식은 실제 채널 측정 결과가 아니다.
- C31 `transfer`: C11 원본 Figure와 출처를 재사용하고 특징 추출부 Freeze / 새 과제 Head 교체·학습을 설명. 새 입력은 사과이며 사전학습 특징이 유용한지는 Validation으로 확인한다.
- 원본 외부 호스트가 현재 환경에서 403 차단되어 기존 로컬 구조 fallback을 보존했다. 원본이 표시될 때만 외부 이미지 출처를 표시하고, fallback이면 자체 도식 안내를 표시한다. 원본의 실제 픽셀·렌더 상태는 검증하지 못했다.
- 목차·manifest·운영안·README·가이드·활성 TODO의 장수를 동기화했다. CNN 32분 배분 안에서 새 비유 2분을 배정해 전체 120분을 유지한다.

## 검증

- `verify_curriculum_overhaul.py`, `verify_two_hour_course.py`: 통과. 최신 main의 증강/XOR 고정 연결 설명과 과거 테스트 문자열이 달랐던 두 assertion을 현재 동일 의미 문장에 맞췄다. Gate 동작·계산은 수정하지 않았다.
- `verify_learning_routes.py`: 56장 실제 목차·양방향 이동, AND/XOR W/b 조작, 학습 버튼, Threshold, 복습·키보드·좁은 화면 통과. 전이학습 원본 URL이 C11과 같은지, Freeze/Head 교체 설명이 표시되는지 검증했다. JS 예외 0.
- `audit_visual_slides.py`: 1920×1080 + 1366×768 =112화면. 변경 장 C11/12/31의 겹침/잘림/축소 문제 0. 기존 C8 XOR에서만 1366×768 fit=0.871 축소 경고 1건이 남는다. C8 내용·CSS는 이번 작업에서 수정하지 않았다.
- 숨겨진 실패 외부 이미지도 조사 JSON에 loaded=false로 남기되, 렌더 크기 0인 이미지는 '화면에 깨진 이미지'로 집계하지 않도록 검사기를 개선했다. fallback 실렌더를 확인했으며 외부 이미지 접속 성공이라고 주장하지 않는다.
- 전체 스크린샷과 JSON: `/workspace/.onboarding/vision-ai/zebra-20261019/visual_audit_output/`. C12와 C31 1366×768 원본 스크린샷을 직접 확인했다.
