import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from dataclasses import dataclass, field


@dataclass
class NewsArticle:
    title: str
    link: str
    published: datetime
    source: str
    company_key: str
    summary: str = ""

    def published_kst(self) -> str:
        return self.published.strftime("%Y-%m-%d %H:%M")


def _fetch_google_news_rss(keyword: str, max_results: int = 10) -> list[NewsArticle]:
    encoded = urllib.parse.quote(keyword)
    url = (
        f"https://news.google.com/rss/search"
        f"?q={encoded}&hl=ko&gl=KR&ceid=KR:ko"
    )
    headers = {"User-Agent": "Mozilla/5.0 (compatible; PharmaNewsBot/1.0)"}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
    except Exception as exc:
        raise RuntimeError(f"RSS fetch failed for '{keyword}': {exc}") from exc

    root = ET.fromstring(data)
    channel = root.find("channel")
    if channel is None:
        return []

    articles: list[NewsArticle] = []
    for item in channel.findall("item")[:max_results]:
        title_el = item.find("title")
        link_el = item.find("link")
        pub_el = item.find("pubDate")
        source_el = item.find("source")
        desc_el = item.find("description")

        title = title_el.text.strip() if title_el is not None else ""
        link = link_el.text.strip() if link_el is not None else ""
        source = source_el.text.strip() if source_el is not None else "Unknown"
        summary = desc_el.text.strip() if desc_el is not None else ""

        try:
            published = parsedate_to_datetime(pub_el.text) if pub_el is not None else datetime.now(tz=timezone.utc)
        except Exception:
            published = datetime.now(tz=timezone.utc)

        articles.append(
            NewsArticle(
                title=title,
                link=link,
                published=published,
                source=source,
                company_key="",
                summary=summary,
            )
        )

    return articles


def fetch_news_for_company(company: dict, max_results: int = 10) -> list[NewsArticle]:
    seen_titles: set[str] = set()
    results: list[NewsArticle] = []

    for keyword in company["search_keywords"]:
        articles = _fetch_google_news_rss(keyword, max_results)
        for art in articles:
            if art.title not in seen_titles:
                seen_titles.add(art.title)
                art.company_key = company["name_ko"]
                results.append(art)

    results.sort(key=lambda a: a.published, reverse=True)
    return results[:max_results]
