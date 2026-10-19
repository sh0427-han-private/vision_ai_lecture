/* Intro13 + Course45 = 58 slides, no Preprocessing-only slide, 120 minutes. */
window.LECTURE_OUTLINE = {
  "version": "20261019-no-preprocessing-58",
  "groups": [
    {
      "name": "필요성 · 사진과 숫자",
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
          "title": "Vision AI가 필요한 이유",
          "global": 3
        },
        {
          "page": "intro.html",
          "slide": 4,
          "title": "사람의 의미 인식 vs Pixel 숫자",
          "global": 4
        },
        {
          "page": "intro.html",
          "slide": 5,
          "title": "사진에서 밝기 숫자로",
          "global": 5
        },
        {
          "page": "intro.html",
          "slide": 6,
          "title": "RGB · Pixel당 세 숫자",
          "global": 6
        },
        {
          "page": "intro.html",
          "slide": 7,
          "title": "RGB 이미지와 숫자 배열",
          "global": 7
        },
        {
          "page": "intro.html",
          "slide": 8,
          "title": "해상도에 따른 정보 차이",
          "global": 8
        }
      ]
    },
    {
      "name": "어려움 · 변화와 중요한 차이",
      "items": [
        {
          "page": "intro.html",
          "slide": 9,
          "title": "조명·색감에 따른 Pixel 변화",
          "global": 9
        },
        {
          "page": "intro.html",
          "slide": 10,
          "title": "회전·크기·가림·흐림에 따른 변화",
          "global": 10
        },
        {
          "page": "intro.html",
          "slide": 11,
          "title": "다르게 생겨도 같은 종류",
          "global": 11
        },
        {
          "page": "intro.html",
          "slide": 12,
          "title": "큰 변화보다 중요한 차이",
          "global": 12
        },
        {
          "page": "intro.html",
          "slide": 13,
          "title": "Vision AI는 왜 어려울까?",
          "global": 13
        }
      ]
    },
    {
      "name": "Vision Task · 모델·Label",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 1,
          "title": "같은 사진, 다른 질문과 정답",
          "global": 14
        },
        {
          "page": "vision_ai_course.html",
          "slide": 2,
          "title": "규칙 기반과 데이터 학습",
          "global": 15
        },
        {
          "page": "vision_ai_course.html",
          "slide": 3,
          "title": "지금 Vision AI는 어디까지 왔나?",
          "global": 16
        },
        {
          "page": "vision_ai_course.html",
          "slide": 4,
          "title": "첫 선택 · 어떤 모델을 쓸까?",
          "global": 17
        },
        {
          "page": "vision_ai_course.html",
          "slide": 5,
          "title": "내 과제에 맞는 모델과 Label",
          "global": 18
        }
      ]
    },
    {
      "name": "퍼셉트론 → AND/XOR의 규칙과 비선형성",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 6,
          "title": "퍼셉트론 · 하나의 W와 b로 판정",
          "global": 19
        },
        {
          "page": "vision_ai_course.html",
          "slide": 7,
          "title": "AND Gate · 두 입력이 모두 1일 때",
          "global": 20
        },
        {
          "page": "vision_ai_course.html",
          "slide": 8,
          "title": "AND Gate · Weight와 Bias로 직선 이동",
          "global": 21
        },
        {
          "page": "vision_ai_course.html",
          "slide": 9,
          "title": "XOR Gate · 입력이 다를 때만 1",
          "global": 22
        },
        {
          "page": "vision_ai_course.html",
          "slide": 10,
          "title": "XOR · 선형층을 쌓아도 직선 하나",
          "global": 23
        },
        {
          "page": "vision_ai_course.html",
          "slide": 11,
          "title": "ReLU · 비선형성의 시작",
          "global": 24
        },
        {
          "page": "vision_ai_course.html",
          "slide": 12,
          "title": "비선형성 · 깊어져도 직선이면?",
          "global": 25
        }
      ]
    },
    {
      "name": "CNN · Kernel과 특징 추출",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 13,
          "title": "CNN Architecture · 사진에서 분류까지",
          "global": 26
        },
        {
          "page": "vision_ai_course.html",
          "slide": 14,
          "title": "왜 CNN인가? · 특징을 모아 얼룩말을 알아보기",
          "global": 27
        },
        {
          "page": "vision_ai_course.html",
          "slide": 15,
          "title": "Kernel · 작은 영역의 가중합",
          "global": 28
        },
        {
          "page": "vision_ai_course.html",
          "slide": 16,
          "title": "Feature Map · 같은 계산을 위치마다",
          "global": 29
        },
        {
          "page": "vision_ai_course.html",
          "slide": 17,
          "title": "CNN · 지역 연결과 가중치 공유",
          "global": 30
        },
        {
          "page": "vision_ai_course.html",
          "slide": 18,
          "title": "RGB에서 Feature Channel까지",
          "global": 31
        },
        {
          "page": "vision_ai_course.html",
          "slide": 19,
          "title": "Stride · 계산 위치의 간격",
          "global": 32
        },
        {
          "page": "vision_ai_course.html",
          "slide": 20,
          "title": "Padding · 같은 입력, 다른 출력 크기",
          "global": 33
        },
        {
          "page": "vision_ai_course.html",
          "slide": 21,
          "title": "Max Pooling · 영역별 최댓값",
          "global": 34
        },
        {
          "page": "vision_ai_course.html",
          "slide": 22,
          "title": "실제 Feature Map · CNN 내부 반응",
          "global": 35
        },
        {
          "page": "vision_ai_course.html",
          "slide": 23,
          "title": "Backbone과 Task Head",
          "global": 36
        }
      ]
    },
    {
      "name": "데이터 · 독립 분할과 증강",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 24,
          "title": "데이터셋 · 어떤 사진으로 배우나",
          "global": 37
        },
        {
          "page": "vision_ai_course.html",
          "slide": 25,
          "title": "Train · Validation · Test",
          "global": 38
        },
        {
          "page": "vision_ai_course.html",
          "slide": 26,
          "title": "Video Group Split · 데이터 누출 방지",
          "global": 39
        },
        {
          "page": "vision_ai_course.html",
          "slide": 27,
          "title": "Data Augmentation · 같은 정답, 다른 조건",
          "global": 40
        }
      ]
    },
    {
      "name": "학습 · CNN Feature 재사용과 지도/비지도",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 28,
          "title": "모델 학습 · 오차를 줄이는 반복",
          "global": 41
        },
        {
          "page": "vision_ai_course.html",
          "slide": 29,
          "title": "Loss · 틀린 정도를 줄이는 방향",
          "global": 42
        },
        {
          "page": "vision_ai_course.html",
          "slide": 30,
          "title": "CNN 학습 · 예측에서 Weight 갱신까지",
          "global": 43
        },
        {
          "page": "vision_ai_course.html",
          "slide": 31,
          "title": "Training과 Inference의 차이",
          "global": 44
        },
        {
          "page": "vision_ai_course.html",
          "slide": 32,
          "title": "전이학습 · 특징은 고정하고 분류기만 학습",
          "global": 45
        },
        {
          "page": "vision_ai_course.html",
          "slide": 33,
          "title": "같은 CNN 특징 · 지도와 비지도 활용",
          "global": 46
        },
        {
          "page": "vision_ai_course.html",
          "slide": 34,
          "title": "Batch · Step · Epoch",
          "global": 47
        },
        {
          "page": "vision_ai_course.html",
          "slide": 35,
          "title": "Overfitting · 새 데이터 일반화",
          "global": 48
        }
      ]
    },
    {
      "name": "평가 · 결함을 놓치지 않는가",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 36,
          "title": "Score Threshold · 판정 기준",
          "global": 49
        },
        {
          "page": "vision_ai_course.html",
          "slide": 37,
          "title": "Confusion Matrix · 100건 평가",
          "global": 50
        },
        {
          "page": "vision_ai_course.html",
          "slide": 38,
          "title": "Accuracy의 함정 · 모두 정상이라면?",
          "global": 51
        },
        {
          "page": "vision_ai_course.html",
          "slide": 39,
          "title": "Precision과 Recall",
          "global": 52
        },
        {
          "page": "vision_ai_course.html",
          "slide": 40,
          "title": "IoU · 박스 겹침 비율",
          "global": 53
        }
      ]
    },
    {
      "name": "원리 복습 · 사과 검사",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 41,
          "title": "Vision AI 원리 · 한 장으로 연결",
          "global": 54
        },
        {
          "page": "vision_ai_course.html",
          "slide": 42,
          "title": "첫 과제를 위한 네 가지 질문",
          "global": 55
        },
        {
          "page": "vision_ai_course.html",
          "slide": 43,
          "title": "실행 결과 확인 · 임계값과 오류 수",
          "global": 56
        },
        {
          "page": "vision_ai_course.html",
          "slide": 44,
          "title": "실패 사진이 알려 주는 것",
          "global": 57
        },
        {
          "page": "vision_ai_course.html",
          "slide": 45,
          "title": "Vision AI 원리 · 무엇을 설명할 수 있나?",
          "global": 58
        }
      ]
    }
  ]
};
