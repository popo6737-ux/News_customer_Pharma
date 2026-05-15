import pytest
from datetime import datetime, timezone
from pharma_news.fetcher import NewsArticle
from pharma_news.formatter import format_company_news, format_summary_table


def _make_article(title: str, company: str = "셀트리온") -> NewsArticle:
    return NewsArticle(
        title=title,
        link="https://example.com/news/1",
        published=datetime(2026, 5, 15, 6, 0, 0, tzinfo=timezone.utc),
        source="헬스조선",
        company_key=company,
    )


def test_format_company_news_contains_title():
    articles = [_make_article("셀트리온 FDA 승인")]
    output = format_company_news("셀트리온", articles)
    assert "셀트리온 FDA 승인" in output


def test_format_company_news_empty():
    output = format_company_news("셀트리온", [])
    assert "뉴스를 가져오지 못했습니다" in output


def test_format_summary_table_shows_all_companies():
    companies = ["삼성바이오로직스", "셀트리온", "롯데바이오로직스", "LG화학", "셀트리온제약"]
    results = {c: [_make_article("테스트 기사", c)] for c in companies}
    output = format_summary_table(results)
    for company in companies:
        assert company in output


def test_format_summary_table_shows_count():
    results = {"셀트리온": [_make_article("기사1"), _make_article("기사2")]}
    output = format_summary_table(results)
    assert "2" in output
