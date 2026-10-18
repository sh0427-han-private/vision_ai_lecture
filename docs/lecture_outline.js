/* Two-hour principle-focused public lecture. */
window.LECTURE_OUTLINE = {
  "version": "20261018-two-hour",
  "groups": [
    {
      "name": "입력 · 사진과 숫자",
      "items": [
        {
          "page": "intro.html",
          "slide": 1,
          "title": "AI와 시각의 출발점",
          "global": 1
        },
        {
          "page": "intro.html",
          "slide": 2,
          "title": "사람의 시각 · 장면 이해",
          "global": 2
        },
        {
          "page": "intro.html",
          "slide": 3,
          "title": "사람의 의미 인식 vs Pixel 숫자",
          "global": 3
        },
        {
          "page": "intro.html",
          "slide": 4,
          "title": "사진에서 밝기 숫자로",
          "global": 4
        },
        {
          "page": "intro.html",
          "slide": 5,
          "title": "RGB · Pixel당 세 숫자",
          "global": 5
        },
        {
          "page": "intro.html",
          "slide": 6,
          "title": "RGB 이미지와 숫자 배열",
          "global": 6
        },
        {
          "page": "intro.html",
          "slide": 7,
          "title": "해상도에 따른 정보 차이",
          "global": 7
        }
      ]
    },
    {
      "name": "어려움 · 남겨야 할 차이",
      "items": [
        {
          "page": "intro.html",
          "slide": 8,
          "title": "조명·색감에 따른 Pixel 변화",
          "global": 8
        },
        {
          "page": "intro.html",
          "slide": 9,
          "title": "회전·크기·가림·흐림에 따른 변화",
          "global": 9
        },
        {
          "page": "intro.html",
          "slide": 10,
          "title": "다르게 생겨도 같은 종류",
          "global": 10
        },
        {
          "page": "intro.html",
          "slide": 11,
          "title": "큰 변화보다 중요한 차이",
          "global": 11
        }
      ]
    },
    {
      "name": "Task와 학습 원리",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 1,
          "title": "같은 사진, 다른 질문과 정답",
          "global": 12
        },
        {
          "page": "vision_ai_course.html",
          "slide": 2,
          "title": "규칙 기반과 데이터 학습",
          "global": 13
        },
        {
          "page": "vision_ai_course.html",
          "slide": 3,
          "title": "모델 학습 · 오차를 줄이는 반복",
          "global": 14
        },
        {
          "page": "vision_ai_course.html",
          "slide": 4,
          "title": "Loss와 가중치 갱신",
          "global": 15
        },
        {
          "page": "vision_ai_course.html",
          "slide": 5,
          "title": "Training과 Inference의 차이",
          "global": 16
        }
      ]
    },
    {
      "name": "신경망 · 선형성과 비선형성",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 6,
          "title": "퍼셉트론 · Wx + b에서 판정까지",
          "global": 17
        },
        {
          "page": "vision_ai_course.html",
          "slide": 7,
          "title": "여러 층을 거치는 두 입력",
          "global": 18
        },
        {
          "page": "vision_ai_course.html",
          "slide": 8,
          "title": "선형 계산만 쌓으면 단일층과 동등",
          "global": 19
        },
        {
          "page": "vision_ai_course.html",
          "slide": 9,
          "title": "AND와 XOR · 직선으로 구분할 수 있을까?",
          "global": 20
        },
        {
          "page": "vision_ai_course.html",
          "slide": 10,
          "title": "다층 퍼셉트론 · 게이트 조합으로 XOR",
          "global": 21
        },
        {
          "page": "vision_ai_course.html",
          "slide": 11,
          "title": "ReLU · 비선형성의 시작",
          "global": 22
        },
        {
          "page": "vision_ai_course.html",
          "slide": 12,
          "title": "신경망의 핵심 · 계산 사이의 비선형성",
          "global": 23
        }
      ]
    },
    {
      "name": "CNN · 작은 계산에서 전체 구조로",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 13,
          "title": "Kernel · 작은 영역의 가중합",
          "global": 24
        },
        {
          "page": "vision_ai_course.html",
          "slide": 14,
          "title": "Feature Map · 같은 계산을 위치마다",
          "global": 25
        },
        {
          "page": "vision_ai_course.html",
          "slide": 15,
          "title": "CNN · 지역 연결과 가중치 공유",
          "global": 26
        },
        {
          "page": "vision_ai_course.html",
          "slide": 16,
          "title": "RGB 입력과 출력 Channel",
          "global": 27
        },
        {
          "page": "vision_ai_course.html",
          "slide": 17,
          "title": "Stride · 계산 위치의 간격",
          "global": 28
        },
        {
          "page": "vision_ai_course.html",
          "slide": 18,
          "title": "Padding · 입력 바깥에 값 채우기",
          "global": 29
        },
        {
          "page": "vision_ai_course.html",
          "slide": 19,
          "title": "Max Pooling · 영역별 최댓값",
          "global": 30
        },
        {
          "page": "vision_ai_course.html",
          "slide": 20,
          "title": "CNN 전체 구조 · 특징에서 판정까지",
          "global": 31
        },
        {
          "page": "vision_ai_course.html",
          "slide": 21,
          "title": "실제 Feature Map · CNN 내부 반응",
          "global": 32
        },
        {
          "page": "vision_ai_course.html",
          "slide": 22,
          "title": "학습 과정에서 바뀌는 Kernel",
          "global": 33
        },
        {
          "page": "vision_ai_course.html",
          "slide": 23,
          "title": "Backbone과 Task Head",
          "global": 34
        },
        {
          "page": "vision_ai_course.html",
          "slide": 24,
          "title": "전이학습 · 고정과 미세 조정",
          "global": 35
        }
      ]
    },
    {
      "name": "데이터와 평가 · 과제에 적용",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 25,
          "title": "데이터셋 · 판정 기준과 촬영 조건",
          "global": 36
        },
        {
          "page": "vision_ai_course.html",
          "slide": 26,
          "title": "Train · Validation · Test",
          "global": 37
        },
        {
          "page": "vision_ai_course.html",
          "slide": 27,
          "title": "Video Group Split · 데이터 누출 방지",
          "global": 38
        },
        {
          "page": "vision_ai_course.html",
          "slide": 28,
          "title": "Overfitting · 새 데이터 일반화",
          "global": 39
        },
        {
          "page": "vision_ai_course.html",
          "slide": 29,
          "title": "Preprocessing · 입력 규격 맞추기",
          "global": 40
        },
        {
          "page": "vision_ai_course.html",
          "slide": 30,
          "title": "Data Augmentation · 조건 변화 만들기",
          "global": 41
        },
        {
          "page": "vision_ai_course.html",
          "slide": 31,
          "title": "Score Threshold · 판정 기준",
          "global": 42
        },
        {
          "page": "vision_ai_course.html",
          "slide": 32,
          "title": "Confusion Matrix · 100건 평가",
          "global": 43
        },
        {
          "page": "vision_ai_course.html",
          "slide": 33,
          "title": "Precision과 Recall",
          "global": 44
        },
        {
          "page": "vision_ai_course.html",
          "slide": 34,
          "title": "IoU · 박스 겹침 비율",
          "global": 45
        },
        {
          "page": "vision_ai_course.html",
          "slide": 35,
          "title": "과제를 시작할 때 선택할 개념",
          "global": 46
        }
      ]
    }
  ]
};
