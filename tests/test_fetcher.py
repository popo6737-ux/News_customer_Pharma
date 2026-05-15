import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timezone
from pharma_news.fetcher import NewsArticle, fetch_news_for_company

SAMPLE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Google News</title>
    <item>
      <title>셀트리온, 바이오시밀러 FDA 승인 획득</title>
      <link>https://example.com/news/1</link>
      <pubDate>Thu, 15 May 2026 03:00:00 GMT</pubDate>
      <source>헬스조선</source>
      <description>셀트리온이 미국 FDA로부터 바이오시밀러 승인을 받았습니다.</description>
    </item>
    <item>
      <title>Celltrion reports record Q1 revenue</title>
      <link>https://example.com/news/2</link>
      <pubDate>Wed, 14 May 2026 08:00:00 GMT</pubDate>
      <source>Korea Herald</source>
      <description>Celltrion announced record revenue for Q1 2026.</description>
    </item>
  </channel>
</rss>""".encode("utf-8")


def _make_mock_response(data: bytes):
    mock_resp = MagicMock()
    mock_resp.read.return_value = data
    mock_resp.__enter__ = lambda s: s
    mock_resp.__exit__ = MagicMock(return_value=False)
    return mock_resp


@patch("urllib.request.urlopen")
def test_fetch_deduplication(mock_urlopen):
    mock_urlopen.return_value = _make_mock_response(SAMPLE_RSS)
    company = {
        "name_ko": "셀트리온",
        "name_en": "Celltrion",
        "search_keywords": ["셀트리온", "Celltrion"],
        "ticker": "068270",
    }
    articles = fetch_news_for_company(company, max_results=10)
    titles = [a.title for a in articles]
    assert len(titles) == len(set(titles)), "중복 기사가 존재합니다"


@patch("urllib.request.urlopen")
def test_fetch_sorted_by_date(mock_urlopen):
    mock_urlopen.return_value = _make_mock_response(SAMPLE_RSS)
    company = {
        "name_ko": "셀트리온",
        "name_en": "Celltrion",
        "search_keywords": ["셀트리온"],
        "ticker": "068270",
    }
    articles = fetch_news_for_company(company, max_results=10)
    dates = [a.published for a in articles]
    assert dates == sorted(dates, reverse=True), "날짜 내림차순 정렬이 되어야 합니다"


@patch("urllib.request.urlopen")
def test_fetch_company_key_set(mock_urlopen):
    mock_urlopen.return_value = _make_mock_response(SAMPLE_RSS)
    company = {
        "name_ko": "셀트리온",
        "name_en": "Celltrion",
        "search_keywords": ["셀트리온"],
        "ticker": "068270",
    }
    articles = fetch_news_for_company(company, max_results=10)
    for art in articles:
        assert art.company_key == "셀트리온"


def test_article_published_kst():
    art = NewsArticle(
        title="테스트",
        link="https://example.com",
        published=datetime(2026, 5, 15, 3, 0, 0, tzinfo=timezone.utc),
        source="테스트매체",
        company_key="셀트리온",
    )
    kst_str = art.published_kst()
    assert "2026-05-15" in kst_str
