from datetime import datetime, timezone, timedelta
from .fetcher import NewsArticle

KST = timezone(timedelta(hours=9))

DEMO_NEWS: dict[str, list[NewsArticle]] = {
    "삼성바이오로직스": [
        NewsArticle(
            title="삼성바이오로직스, 글로벌 빅파마와 4조원 규모 CMO 계약 체결",
            link="https://example.com/news/sbl-1",
            published=datetime(2026, 5, 15, 9, 0, tzinfo=KST),
            source="매일경제",
            company_key="삼성바이오로직스",
            summary="삼성바이오로직스가 유럽계 대형 제약사와 바이오의약품 위탁생산(CMO) 계약을 체결했다.",
        ),
        NewsArticle(
            title="삼성바이오로직스 1Q26 영업이익 8,200억 원 사상 최대",
            link="https://example.com/news/sbl-2",
            published=datetime(2026, 5, 13, 8, 30, tzinfo=KST),
            source="한국경제",
            company_key="삼성바이오로직스",
            summary="1분기 영업이익이 전년 동기 대비 42% 증가한 8,200억 원을 기록했다.",
        ),
        NewsArticle(
            title="Samsung Biologics wins $3B biosimilar manufacturing deal",
            link="https://example.com/news/sbl-3",
            published=datetime(2026, 5, 12, 6, 0, tzinfo=KST),
            source="Korea Herald",
            company_key="삼성바이오로직스",
            summary="Samsung Biologics secured a major biosimilar manufacturing contract.",
        ),
    ],
    "셀트리온": [
        NewsArticle(
            title="셀트리온 '짐펜트라', 미국 시장 점유율 12% 돌파",
            link="https://example.com/news/ct-1",
            published=datetime(2026, 5, 15, 10, 15, tzinfo=KST),
            source="바이오스펙테이터",
            company_key="셀트리온",
            summary="자가면역 바이오시밀러 짐펜트라의 미국 시장 점유율이 12%를 넘어섰다.",
        ),
        NewsArticle(
            title="셀트리온, 피하주사형 허쥬마 유럽 허가 획득",
            link="https://example.com/news/ct-2",
            published=datetime(2026, 5, 14, 9, 0, tzinfo=KST),
            source="헬스조선",
            company_key="셀트리온",
            summary="EMA로부터 트라스투주맙 바이오시밀러 피하주사 제형 승인을 받았다.",
        ),
        NewsArticle(
            title="Celltrion Q1 2026 revenue grows 35% YoY on biosimilar demand",
            link="https://example.com/news/ct-3",
            published=datetime(2026, 5, 11, 7, 0, tzinfo=KST),
            source="Korea Biomedical Review",
            company_key="셀트리온",
            summary="Strong biosimilar sales in the US and Europe drove Q1 growth.",
        ),
    ],
    "롯데바이오로직스": [
        NewsArticle(
            title="롯데바이오로직스, 송도 2공장 GMP 인증 취득",
            link="https://example.com/news/lbl-1",
            published=datetime(2026, 5, 14, 11, 0, tzinfo=KST),
            source="청년의사",
            company_key="롯데바이오로직스",
            summary="인천 송도 제2바이오캠퍼스가 식품의약품안전처 GMP 인증을 획득했다.",
        ),
        NewsArticle(
            title="롯데바이오로직스, ADC 위탁생산 사업 본격화",
            link="https://example.com/news/lbl-2",
            published=datetime(2026, 5, 10, 8, 0, tzinfo=KST),
            source="팜뉴스",
            company_key="롯데바이오로직스",
            summary="항체약물접합체(ADC) CDMO 서비스를 공식 론칭하며 고성장 시장에 진출했다.",
        ),
    ],
    "LG화학": [
        NewsArticle(
            title="LG화학 생명과학 사업부, 비만 치료제 후보물질 임상 2상 착수",
            link="https://example.com/news/lgc-1",
            published=datetime(2026, 5, 15, 8, 0, tzinfo=KST),
            source="약업신문",
            company_key="LG화학",
            summary="GLP-1 계열 비만 치료제 LG계열 신약 후보물질이 임상 2상에 진입했다.",
        ),
        NewsArticle(
            title="LG화학, 글로벌 제약사에 항암제 원료의약품 수출 계약",
            link="https://example.com/news/lgc-2",
            published=datetime(2026, 5, 13, 10, 0, tzinfo=KST),
            source="데일리팜",
            company_key="LG화학",
            summary="북미 빅파마에 항암 계열 API를 5년 장기 공급하는 계약을 체결했다.",
        ),
        NewsArticle(
            title="LG Chem targets $2B in pharma revenue by 2028",
            link="https://example.com/news/lgc-3",
            published=datetime(2026, 5, 9, 6, 30, tzinfo=KST),
            source="Reuters",
            company_key="LG화학",
            summary="LG Chem outlined its mid-term pharma growth strategy at an investor day.",
        ),
    ],
    "셀트리온제약": [
        NewsArticle(
            title="셀트리온제약, 국내 바이오시밀러 유통 실적 역대 최고",
            link="https://example.com/news/ctp-1",
            published=datetime(2026, 5, 15, 7, 0, tzinfo=KST),
            source="의학신문",
            company_key="셀트리온제약",
            summary="셀트리온제약의 국내 바이오시밀러 유통 매출이 전년 대비 28% 증가했다.",
        ),
        NewsArticle(
            title="셀트리온제약, 경구용 항바이러스제 허가 신청",
            link="https://example.com/news/ctp-2",
            published=datetime(2026, 5, 12, 9, 30, tzinfo=KST),
            source="메디파나뉴스",
            company_key="셀트리온제약",
            summary="호흡기 바이러스를 타겟으로 하는 경구 항바이러스 신약 허가를 식약처에 신청했다.",
        ),
    ],
}
