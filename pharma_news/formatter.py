from .fetcher import NewsArticle

SEPARATOR = "─" * 60


def format_company_news(company_name: str, articles: list[NewsArticle]) -> str:
    lines = [
        f"\n{'=' * 60}",
        f"  {company_name}",
        f"{'=' * 60}",
    ]

    if not articles:
        lines.append("  뉴스를 가져오지 못했습니다.")
        return "\n".join(lines)

    for i, art in enumerate(articles, 1):
        lines.append(f"\n[{i}] {art.title}")
        lines.append(f"    날짜   : {art.published_kst()}")
        lines.append(f"    출처   : {art.source}")
        lines.append(f"    링크   : {art.link}")

    return "\n".join(lines)


def format_summary_table(results: dict[str, list[NewsArticle]]) -> str:
    lines = ["\n" + "=" * 60, "  한국 제약사 최신 뉴스 요약", "=" * 60]
    for company_name, articles in results.items():
        count = len(articles)
        latest = articles[0].published_kst() if articles else "-"
        lines.append(f"  {company_name:<20} {count:>3}건  (최신: {latest})")
    lines.append("=" * 60)
    return "\n".join(lines)
