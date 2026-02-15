# personal-colour-labspace

[![DOI](https://zenodo.org/badge/1158264019.svg)](https://doi.org/10.5281/zenodo.18646259)

**Languages:** [English](README.md) | [日本語](README_ja.md) | 한국어 (이 페이지) | [Deutsch](README_de.md)

이 저장소는 논문
**“Personal Colour between Perceptual Space and Social Practice”** (게재 확정; 교정 중)
을(를) 보완하는 익명화 데이터셋과 최소 재현 가능 코드를 제공합니다.

본 저장소는 색 좌표로부터 퍼스널 컬러 라벨을 분류하는 분석의 재현성을 지원합니다.

## 저장소 구조
- `data/lab_samples.csv` — 샘플 단위 익명화 데이터셋 (RGB 및 CIE L\*a\*b\*)
- `data/README_data.md` — 데이터 사전 / 코드북
- `run_pipeline.py` — 데이터셋 로드 및 검증을 위한 최소 실행 스크립트
- `requirements.txt` — Python 의존성
- `config.example.yml` — 설정 템플릿 (경로 및 난수 시드)
- `.gitignore` — 생성된 출력물과 로컬 설정 파일 제외

## 데이터 요약
각 행은 하나의 색 샘플에 해당합니다. 데이터셋에는 다음이 포함됩니다:
- sRGB 값 (`rgb_hex`, `r`, `g`, `b`)
- CIE L\*a\*b\* 좌표 (`L_star`, `a_star`, `b_star`)
- 두 종류의 퍼스널 컬러 라벨:
  - `tone2_label` (이진 톤)
  - `season_label` (계절 라벨; `spring_autumn` 과 같은 모호한 범주 포함)

자세한 내용은 `data/README_data.md` 를 참고하세요.

## 빠른 시작
1. Python 환경을 만들고 의존성을 설치합니다:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. 로컬 설정 파일을 생성합니다:
   ```bash
   cp config.example.yml config.yml
   ```
3. 실행합니다:
   ```bash
   python run_pipeline.py
   ```

## 재현성 관련 참고 사항
- 본 저장소는 기기/환경에 종속적인 절대 경로(예: 개인 Google Drive 디렉터리)를 피하도록 설계되었습니다.
- 난수 시드는 `config.yml` 로 제어됩니다 (기본값: `seed: 42`).
- 데이터셋은 RGB와 CIE L\*a\*b\* 값을 모두 제공하여, 구현 방식에 따른 변환 세부사항에 의존하지 않는 후속 분석을 가능하게 합니다.

## 라이선스 및 인용
- 코드 라이선스: MIT License (`LICENSE` 참고)
- 데이터 라이선스: CC BY 4.0 (`data/LICENSE` 참고)
- 인용: Zenodo Concept DOI(전체 버전)를 인용해 주세요: https://doi.org/10.5281/zenodo.18646259

