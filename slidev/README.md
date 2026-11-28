# Vision AI 기초 · Slidev 덱

제목 표지 1장과 본문 55장입니다. 비전공자 대상 120분 구성으로, 현재 HTML 강의의 제목·순서·Concept를 유지합니다. Slidev의 화면 번호에는 표지가 포함되므로 본문 P01은 `#/2`, P55는 `#/56`입니다.

## 열기

Node.js 22.12 이상이 필요합니다. 이 폴더에서 실행합니다.

```powershell
npm ci
npm run dev -- --bind 127.0.0.1
```

미리보기에는 [발표 화면](http://localhost:3030/), Slidev의 목차, 발표자 노트가 있습니다. `npm test`는 슬라이드 순서와 계산값을 확인하고, `npm run build`는 기존 Pages와 같은 하위 경로에서 사용할 `dist/`를 생성합니다. 정적 빌드를 서빙할 때는 `/vision_ai_lecture/slidev/` 아래에 둡니다.

## 내용 관리

- `slides.md`가 표지와 `units/A.md`~`units/H.md`를 불러옵니다. 각 장의 발표자 노트에는 설명 순서와 참고 자료가 있습니다. [장별 출처](SOURCES.md)
- 계산 기준은 기존 강의 커밋 `77d04e1074f1d7c1b20e7f458a137456f1fba02b`입니다. 픽셀값은 같은 로컬 사진에서 읽습니다. 그 외 교육용 계산은 `lesson/calculations.js`에 두고 관련 장에서 함께 씁니다. 각 위젯은 독립적인 상태로 시작하며 초기화할 수 있습니다.
- P35는 공식 SqueezeNet1.1 가중치와 기존 강의의 생성 사과 사진을 사용합니다. 이후 다시 계산할 경우 CPU용 PyTorch 2.9.1, torchvision 0.24.1, Pillow, NumPy 환경에서 `python scripts/render_feature_maps.py`를 실행합니다. [입력 해시와 층별 기록](figures/apple-feature-maps.json)

## 배포와 검수

Pages 워크플로에서 새 정적 덱을 기존 `docs` 산출물의 `slidev/`에 넣습니다. 공개 전에는 기존 표지와 대표 Intro·Course 링크, Slidev 표지, 장별 주소 새로고침, 이미지와 글꼴을 동일한 하위 경로에서 확인합니다. 배포 후 문제를 발견하면 작업 담당자가 마지막 정상 Pages 배포를 다시 실행하거나 이 PR을 되돌려 기존 공개 주소의 동작을 확인합니다.

수업에서는 P05·P29·P41·P48을 수강생에게 한 번 조작하게 하고, P32~34는 강사가 대표 설정만 시연합니다. 실제 120분 리허설이나 수강생 이해도는 별도로 기록합니다. 리허설에서 시간이 부족하면 P32~34의 추가 경우와 P45의 미세조정 설명을 발표자 노트에서만 다룹니다.
