/* Public course: Intro 19, Vision AI integrated 49; total 68 slides. */
window.LECTURE_OUTLINE = {
  "version": "20261017-gate-story-49",
  "groups": [
    {
      "name": "Intro · 시각의 중요성에서 숫자까지",
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
          "title": "일상 속 Vision 기술",
          "global": 3
        },
        {
          "page": "intro.html",
          "slide": 4,
          "title": "사진 속 객체 인식",
          "global": 4
        },
        {
          "page": "intro.html",
          "slide": 5,
          "title": "사람의 의미 인식 vs Pixel 숫자",
          "global": 5
        },
        {
          "page": "intro.html",
          "slide": 6,
          "title": "조명·색감에 따른 Pixel 변화",
          "global": 6
        },
        {
          "page": "intro.html",
          "slide": 7,
          "title": "시점·회전·가림·초점 변화",
          "global": 7
        },
        {
          "page": "intro.html",
          "slide": 8,
          "title": "위치 변화와 Pixel 배열",
          "global": 8
        },
        {
          "page": "intro.html",
          "slide": 9,
          "title": "RGB · Pixel당 세 숫자",
          "global": 9
        },
        {
          "page": "intro.html",
          "slide": 10,
          "title": "RGB 이미지와 숫자 배열",
          "global": 10
        },
        {
          "page": "intro.html",
          "slide": 11,
          "title": "해상도와 Pixel 수",
          "global": 11
        },
        {
          "page": "intro.html",
          "slide": 12,
          "title": "해상도에 따른 정보 차이",
          "global": 12
        },
        {
          "page": "intro.html",
          "slide": 13,
          "title": "시각 이해 · What과 Where",
          "global": 13
        },
        {
          "page": "intro.html",
          "slide": 14,
          "title": "2D 이미지와 3D 공간의 모호함",
          "global": 14
        },
        {
          "page": "intro.html",
          "slide": 15,
          "title": "밝기값 3D 표시 vs 실제 거리",
          "global": 15
        },
        {
          "page": "intro.html",
          "slide": 16,
          "title": "외우는 Pixel, 학습하는 Pattern",
          "global": 16
        },
        {
          "page": "intro.html",
          "slide": 17,
          "title": "Vision AI · Pixel에서 결과까지",
          "global": 17
        },
        {
          "page": "intro.html",
          "slide": 18,
          "title": "센서별 입력 데이터 비교",
          "global": 18
        },
        {
          "page": "intro.html",
          "slide": 19,
          "title": "우리 주변의 Vision Sensor",
          "global": 19
        }
      ]
    },
    {
      "name": "Vision Task · 무엇을 찾을까?",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 1,
          "global": 20,
          "title": "Vision AI Task 선택",
          "original": "V2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 2,
          "global": 21,
          "title": "Classification · 이미지 전체 분류",
          "original": "V3"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 3,
          "global": 22,
          "title": "Detection · 위치와 종류 찾기",
          "original": "V4"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 4,
          "global": 23,
          "title": "Segmentation · Pixel 단위 분할",
          "original": "V5"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 5,
          "global": 24,
          "title": "같은 사진, 다른 정답 형태",
          "original": "V6"
        }
      ]
    },
    {
      "name": "AI · 규칙과 학습",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 6,
          "global": 25,
          "title": "AI · 머신러닝 · 딥러닝의 관계",
          "original": "A2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 7,
          "global": 26,
          "title": "규칙 기반과 데이터 학습",
          "original": "A3"
        }
      ]
    },
    {
      "name": "CNN · 왜 쓰고 무엇을 배우나",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 8,
          "global": 27,
          "title": "왜 CNN을 사용할까? · 이미지의 국소 패턴과 가중치 공유",
          "original": "N1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 9,
          "global": 28,
          "title": "CNN 전체 구조와 특징 추출",
          "original": "C1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 10,
          "global": 29,
          "title": "실제 Feature Map · CNN 내부 반응",
          "original": "M1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 11,
          "global": 30,
          "title": "Feature Visualization · 학습된 특징",
          "original": "V28"
        }
      ]
    },
    {
      "name": "Kernel · 특징과 가중치",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 12,
          "global": 31,
          "title": "CNN의 지역 연결과 가중치 공유",
          "original": "V18"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 13,
          "global": 32,
          "title": "Kernel · 작은 영역을 반복 탐색",
          "original": "V10"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 14,
          "global": 33,
          "title": "Kernel 반응 · 패턴에 따른 차이",
          "original": "V19"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 15,
          "global": 34,
          "title": "고정된 필터와 학습하는 Kernel의 차이",
          "original": "F1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 16,
          "global": 35,
          "title": "퍼셉트론 · Wx + b에서 판정까지",
          "original": "A8"
        }
      ]
    },
    {
      "name": "AI 원리 · 선형성·AND·XOR",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 17,
          "global": 36,
          "title": "활성화 함수가 없으면 깊어도 단층",
          "original": "N2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 18,
          "global": 37,
          "title": "AND와 XOR · 직선으로 구분할 수 있을까?",
          "original": "N3"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 19,
          "global": 38,
          "title": "ReLU · 비선형성의 시작",
          "original": "A13"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 20,
          "global": 39,
          "title": "다층 퍼셉트론 · 게이트 조합으로 XOR",
          "original": "N4"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 21,
          "global": 40,
          "title": "신경망 · 선형 변환 사이의 비선형성",
          "original": "A11"
        }
      ]
    },
    {
      "name": "CNN · 특징 계산과 크기 변화",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 22,
          "global": 41,
          "title": "학습 과정에서 바뀌는 Kernel",
          "original": "V33"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 23,
          "global": 42,
          "title": "CNN 블록 · Conv와 활성화",
          "original": "C2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 24,
          "global": 43,
          "title": "Feature Map · 위치별 반응값",
          "original": "V21"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 25,
          "global": 44,
          "title": "RGB Channel과 학습 필터",
          "original": "V22"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 26,
          "global": 45,
          "title": "Stride를 늘리면 Feature Map의 칸 수가 줄어듭니다",
          "original": "V23"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 27,
          "global": 46,
          "title": "Padding으로 가장자리도 계산하고 크기를 유지합니다",
          "original": "V24"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 28,
          "global": 47,
          "title": "Max Pooling은 영역의 가장 큰 반응만 남깁니다",
          "original": "V25"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 29,
          "global": 48,
          "title": "Backbone과 Task Head",
          "original": "V31"
        }
      ]
    },
    {
      "name": "모델 학습 · 예측부터 Weight 갱신",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 30,
          "global": 49,
          "title": "모델 학습 · 오차를 줄이는 반복",
          "original": "A15"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 31,
          "global": 50,
          "title": "Loss · 예측과 정답의 차이",
          "original": "A16"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 32,
          "global": 51,
          "title": "Forward · Gradient · Weight 갱신",
          "original": "A21"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 33,
          "global": 52,
          "title": "Training과 Inference의 차이",
          "original": "A22"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 34,
          "global": 53,
          "title": "Batch · Iteration · Epoch",
          "original": "A28"
        }
      ]
    },
    {
      "name": "데이터 · 현장 환경과 준비",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 35,
          "global": 54,
          "title": "데이터셋 · 촬영 조건과 Label",
          "original": "A29"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 36,
          "global": 55,
          "title": "Train · Validation · Test",
          "original": "A30"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 37,
          "global": 56,
          "title": "Video Group Split · 데이터 누출 방지",
          "original": "A31"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 38,
          "global": 57,
          "title": "Preprocessing · 입력 규격 맞추기",
          "original": "A33"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 39,
          "global": 58,
          "title": "Data Augmentation · 조건 변화 만들기",
          "original": "A34"
        }
      ]
    },
    {
      "name": "전이학습 · 새 환경 적용",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 40,
          "global": 59,
          "title": "Transfer Learning · 사전학습 활용",
          "original": "V34"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 41,
          "global": 60,
          "title": "Freeze와 Fine-tuning",
          "original": "V35"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 42,
          "global": 61,
          "title": "Overfitting · 새 데이터 일반화",
          "original": "A35"
        }
      ]
    },
    {
      "name": "평가 · 현장 적용",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 43,
          "global": 62,
          "title": "Score Threshold · 판정 기준",
          "original": "A38"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 44,
          "global": 63,
          "title": "Confusion Matrix · 100건 평가",
          "original": "A39"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 45,
          "global": 64,
          "title": "Precision과 Recall",
          "original": "A40"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 46,
          "global": 65,
          "title": "IoU · 박스 겹침 비율",
          "original": "V7"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 47,
          "global": 66,
          "title": "Grad-CAM · 클래스별 판단 근거",
          "original": "V36"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 48,
          "global": 67,
          "title": "Vision AI 프로젝트 전체 흐름",
          "original": "V37"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 49,
          "global": 68,
          "title": "운영 데이터와 재학습",
          "original": "A44"
        }
      ]
    }
  ]
};
