---
name: pharma-news
description: 한국 제약사 최신 뉴스 조회. 삼성바이오로직스, 셀트리온, 롯데바이오로직스, LG화학, 셀트리온제약 중 하나 이상을 선택해 Google News RSS에서 뉴스를 수집하고 요약한다.
---

# 한국 제약사 뉴스 스킬

대상 5개사: 삼성바이오로직스, 셀트리온, 롯데바이오로직스, LG화학, 셀트리온제약

## 호출 방법

```
/pharma-news                          # 전체 5개사 뉴스
/pharma-news 셀트리온                  # 특정 회사
/pharma-news 삼성바이오로직스 LG화학     # 복수 선택
/pharma-news --summary                # 요약 테이블만
```

## 실행 워크플로우

### 1. 인자 파싱

사용자가 회사명을 지정했으면 해당 회사만, 아니면 전체 5개사 대상으로 진행한다.

회사명 → 내부 키 매핑:
- 삼성바이오로직스 / Samsung Biologics → `samsung_biologics`
- 셀트리온 / Celltrion → `celltrion`
- 롯데바이오로직스 / Lotte Biologics → `lotte_biologics`
- LG화학 / LG Chem → `lg_chem`
- 셀트리온제약 / Celltrion Pharm → `celltrion_pharm`

### 2. 뉴스 수집

프로젝트 루트에서 `run_news.py`를 실행한다.

```bash
# 전체
python run_news.py -n 10

# 특정 회사 (내부 키 사용)
python run_news.py -c celltrion samsung_biologics -n 10

# 요약만
python run_news.py --summary

# 네트워크 없는 환경 (데모)
python run_news.py --demo
```

네트워크 오류(403, timeout 등)가 발생하면 `--demo` 플래그를 추가해 샘플 데이터로 실행한다.

### 3. 결과 출력

수집된 뉴스를 다음 형식으로 대화창에 정리해서 전달한다:

```
## 한국 제약사 최신 뉴스 — YYYY-MM-DD

### 회사명
1. **기사 제목** — 출처 (날짜)
   링크
2. ...
```

뉴스가 0건이면 "해당 회사 뉴스를 가져오지 못했습니다."라고 명시한다.

### 4. 오류 처리

| 상황 | 대응 |
|------|------|
| 네트워크 차단(403) | `--demo` 모드로 재실행, 샘플 데이터임을 안내 |
| 특정 회사만 0건 | 해당 회사만 오류 안내, 나머지 정상 출력 |
| 잘못된 회사명 | 유효한 회사 목록 안내 후 재질문 |

## 완료 기준

모든 선택된 회사의 뉴스가 출력되면 스킬을 종료한다. 마지막에 조회한 회사 수와 총 기사 건수를 한 줄로 요약한다.
