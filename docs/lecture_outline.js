/* Public lecture: 19 Intro plus 52 Vision AI and YOLO slides (71 total). */
window.LECTURE_OUTLINE = {
  "version": "20261016-sourced-cnn-yolo-figures-52",
  "groups": [
    {
      "name": "Intro · 시각의 중요성에서 숫자까지",
      "items": [
        {
          "page": "intro.html",
          "slide": 1,
          "title": "AI는 세상을 어떻게 볼까?",
          "global": 1
        },
        {
          "page": "intro.html",
          "slide": 2,
          "title": "사람은 눈으로 주변 세상의 많은 정보를 파악합니다",
          "global": 2
        },
        {
          "page": "intro.html",
          "slide": 3,
          "title": "그래서 Vision은 일상과 기술 모두에서 중요합니다",
          "global": 3
        },
        {
          "page": "intro.html",
          "slide": 4,
          "title": "이 이미지는 무엇으로 보이나요?",
          "global": 4
        },
        {
          "page": "intro.html",
          "slide": 5,
          "title": "사람에게는 사과, 컴퓨터와 AI에게는 숫자 배열",
          "global": 5
        },
        {
          "page": "intro.html",
          "slide": 6,
          "title": "같은 사과도 밝기와 색감이 바뀌면 Pixel 값이 달라집니다",
          "global": 6
        },
        {
          "page": "intro.html",
          "slide": 7,
          "title": "화각·회전·가림·초점도 같은 사과의 Pixel을 바꿉니다",
          "global": 7
        },
        {
          "page": "intro.html",
          "slide": 8,
          "title": "사진의 위치를 바꾸면 Pixel 숫자도 바뀝니다",
          "global": 8
        },
        {
          "page": "intro.html",
          "slide": 9,
          "title": "RGB 이미지에서는 Pixel 한 칸에 숫자 3개가 있습니다",
          "global": 9
        },
        {
          "page": "intro.html",
          "slide": 10,
          "title": "컴퓨터는 컬러 이미지 한 장을 수많은 숫자로 입력받습니다",
          "global": 10
        },
        {
          "page": "intro.html",
          "slide": 11,
          "title": "해상도가 높을수록 더 많은 Pixel로 장면을 표현합니다",
          "global": 11
        },
        {
          "page": "intro.html",
          "slide": 12,
          "title": "같은 장면도 해상도에 따라 담을 수 있는 정보가 달라집니다",
          "global": 12
        },
        {
          "page": "intro.html",
          "slide": 13,
          "title": "‘본다’는 것은 무엇(What)과 어디(Where)를 이해하는 일",
          "global": 13
        },
        {
          "page": "intro.html",
          "slide": 14,
          "title": "2D 이미지에서 3D 공간을 알아내기는 어렵습니다",
          "global": 14
        },
        {
          "page": "intro.html",
          "slide": 15,
          "title": "밝기값을 3D로 그려도 실제 거리가 생기지는 않습니다",
          "global": 15
        },
        {
          "page": "intro.html",
          "slide": 16,
          "title": "AI는 Pixel을 외우는 대신, 여러 조건에서 반복되는 Pattern을 배워야 합니다",
          "global": 16
        },
        {
          "page": "intro.html",
          "slide": 17,
          "title": "Vision AI는 숫자 배열에서 필요한 Pattern을 찾아 결과로 바꿉니다",
          "global": 17
        },
        {
          "page": "intro.html",
          "slide": 18,
          "title": "같은 장면도 Sensor가 다르면 컴퓨터가 받는 데이터가 달라집니다",
          "global": 18
        },
        {
          "page": "intro.html",
          "slide": 19,
          "title": "우리는 이미 매일 Vision Sensor를 사용하고 있습니다",
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
          "title": "필요한 결과부터 정하면 Vision Task가 정해집니다",
          "original": "V2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 2,
          "global": 21,
          "title": "이미지 전체의 상태나 종류를 예측합니다",
          "original": "V3"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 3,
          "global": 22,
          "title": "객체나 결함의 위치를 사각형으로 찾습니다",
          "original": "V4"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 4,
          "global": 23,
          "title": "어느 Pixel이 관심 영역인지 구분합니다",
          "original": "V5"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 5,
          "global": 24,
          "title": "같은 사진이라도 Task가 바뀌면 정답 형태가 바뀝니다",
          "original": "V6"
        }
      ]
    },
    {
      "name": "AI · 사람이 만든 규칙과 학습의 차이",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 6,
          "global": 25,
          "title": "AI·머신러닝·딥러닝은 어떻게 다를까요?",
          "original": "A2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 7,
          "global": 26,
          "title": "판단 기준을 사람이 쓰거나, 데이터에서 배웁니다",
          "original": "A3"
        }
      ]
    },
    {
      "name": "Spatial Filtering · Pixel에서 특징 단서까지",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 8,
          "global": 27,
          "title": "한 Pixel을 바꿀 수도, 주변 Pixel을 함께 볼 수도 있습니다",
          "original": "V9"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 9,
          "global": 28,
          "title": "3×3 Kernel은 움직이며 출력 Pixel을 하나씩 만듭니다",
          "original": "V10"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 10,
          "global": 29,
          "title": "동일 입력에서도 Mean·Gaussian·Median 결과는 다릅니다",
          "original": "V14"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 11,
          "global": 30,
          "title": "밝기가 급격히 바뀌는 위치에서 경계 단서를 얻습니다",
          "original": "V16"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 12,
          "global": 31,
          "title": "Spatial Filtering의 Kernel 개념은 CNN으로 연결됩니다",
          "original": "V17"
        }
      ]
    },
    {
      "name": "신경망 · CNN 최소 개념",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 13,
          "global": 32,
          "title": "입력마다 가중치를 곱하고, 더해서 하나의 판정을 만듭니다",
          "original": "A8"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 14,
          "global": 33,
          "title": "여러 계산을 Layer로 연결하면 신경망이 됩니다",
          "original": "A11"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 15,
          "global": 34,
          "title": "Layer를 쌓을 때 비선형 계산도 필요합니다",
          "original": "A13"
        }
      ]
    },
    {
      "name": "CNN · 이미지에서 특징을 찾는 원리",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 16,
          "global": 35,
          "title": "CNN의 기본 구조는 특징 추출 → 출력 → 학습입니다",
          "original": "N1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 17,
          "global": 36,
          "title": "CNN 블록을 이루는 세 계산: Conv·BN·ReLU",
          "original": "N2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 18,
          "global": 37,
          "title": "CNN은 작은 영역을 보고 같은 가중치를 재사용합니다",
          "original": "V18"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 19,
          "global": 38,
          "title": "같은 필터도 이미지 영역에 따라 반응이 달라집니다",
          "original": "V19"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 20,
          "global": 39,
          "title": "반응값을 위치대로 모으면 특징 지도가 됩니다",
          "original": "V21"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 21,
          "global": 40,
          "title": "RGB 전체를 보는 필터 하나가 출력 Channel 하나를 만듭니다",
          "original": "V22"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 22,
          "global": 41,
          "title": "필터를 몇 칸씩 이동할지 정합니다",
          "original": "V23"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 23,
          "global": 42,
          "title": "가장자리 주변에 값을 채워 계산 범위를 조절합니다",
          "original": "V24"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 24,
          "global": 43,
          "title": "공간 해상도를 줄여 더 작은 특징 지도를 만듭니다",
          "original": "V25"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 25,
          "global": 44,
          "title": "Layer는 앞의 특징을 조합해 더 복잡한 표현을 만듭니다",
          "original": "V28"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 26,
          "global": 45,
          "title": "특징을 만드는 부분과, 결과를 만드는 부분을 나눠 봅니다",
          "original": "V31"
        }
      ]
    },
    {
      "name": "YOLO · 학습한 필터로 이미지 이해",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 27,
          "global": 46,
          "title": "고정 필터는 사람이 정하고, YOLO의 필터는 학습합니다",
          "original": "Y1"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 28,
          "global": 47,
          "title": "YOLO는 Backbone → Neck → Head로 검출합니다",
          "original": "Y2"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 29,
          "global": 48,
          "title": "YOLO Detection의 출력은 Class·Box·Score입니다",
          "original": "Y3"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 30,
          "global": 49,
          "title": "YOLO에서도 목적에 따라 Classify·Detect·Segment 모델을 선택합니다",
          "original": "Y4"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 31,
          "global": 50,
          "title": "YOLO를 활용해도 데이터·Label·검증은 직접 준비해야 합니다",
          "original": "Y5"
        }
      ]
    },
    {
      "name": "학습 · YOLO가 필터를 배우는 과정",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 32,
          "global": 51,
          "title": "학습은 예측 오차가 줄도록 계산 기준을 바꾸는 과정입니다",
          "original": "A15"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 33,
          "global": 52,
          "title": "Loss는 예측과 정답의 차이를 학습용 숫자로 바꿉니다",
          "original": "A16"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 34,
          "global": 53,
          "title": "예측 → 오차 → Gradient → 수정을 반복합니다",
          "original": "A21"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 35,
          "global": 54,
          "title": "배울 때는 Weight를 바꾸고, 사용할 때는 고정합니다",
          "original": "A22"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 36,
          "global": 55,
          "title": "데이터를 작은 묶음으로 나누어 반복해서 봅니다",
          "original": "A28"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 37,
          "global": 56,
          "title": "CNN의 필터도 오차를 줄이는 방향으로 학습합니다",
          "original": "V33"
        }
      ]
    },
    {
      "name": "데이터 · YOLO 모델 준비",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 38,
          "global": 57,
          "title": "데이터는 실제 사용할 조건을 대표해야 합니다",
          "original": "A29"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 39,
          "global": 58,
          "title": "학습·모델 선택·최종 평가의 데이터를 나눕니다",
          "original": "A30"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 40,
          "global": 59,
          "title": "같은 영상의 비슷한 Frame은 통째로 분리합니다",
          "original": "A31"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 41,
          "global": 60,
          "title": "모델이 기대하는 크기·값 범위·채널 순서를 맞춥니다",
          "original": "A33"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 42,
          "global": 61,
          "title": "의미를 유지하는 변화를 학습 중에 보여줍니다",
          "original": "A34"
        }
      ]
    },
    {
      "name": "전이학습 · 새 현장에 적용",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 43,
          "global": 62,
          "title": "이미 배운 가중치에서 내 Task의 학습을 시작합니다",
          "original": "V34"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 44,
          "global": 63,
          "title": "고정할 부분과 추가 학습할 부분을 구분합니다",
          "original": "V35"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 45,
          "global": 64,
          "title": "Train에서 잘하는 것과 새 데이터에서 잘하는 것은 다릅니다",
          "original": "A35"
        }
      ]
    },
    {
      "name": "평가 · 현장 적용",
      "items": [
        {
          "page": "vision_ai_course.html",
          "slide": 46,
          "global": 65,
          "title": "점수에 기준을 적용하면 실제 판정이 됩니다",
          "original": "A38"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 47,
          "global": 66,
          "title": "정답과 판정을 비교해 네 가지 결과를 셉니다",
          "original": "A39"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 48,
          "global": 67,
          "title": "알람의 정확성과 불량을 찾는 비율을 구분합니다",
          "original": "A40"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 49,
          "global": 68,
          "title": "위치와 영역은 정답과 얼마나 겹치는지 평가합니다",
          "original": "V7"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 50,
          "global": 69,
          "title": "높은 점수만으로 판단 근거가 맞다고 보장할 수 없습니다",
          "original": "V36"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 51,
          "global": 70,
          "title": "문제 정의부터 운영 관찰까지 연결해 개선합니다",
          "original": "V37"
        },
        {
          "page": "vision_ai_course.html",
          "slide": 52,
          "global": 71,
          "title": "운영의 실패 사례를 다음 데이터와 학습에 연결합니다",
          "original": "A44"
        }
      ]
    }
  ]
};
