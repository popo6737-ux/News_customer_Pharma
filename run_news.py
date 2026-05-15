#!/usr/bin/env python3
"""
한국 제약사 뉴스 스킬
대상: 삼성바이오로직스, 셀트리온, 롯데바이오로직스, LG화학, 셀트리온제약
"""

import argparse
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from pharma_news import (
    COMPANIES,
    fetch_news_for_company,
    format_company_news,
    format_summary_table,
)

COMPANY_CHOICES = list(COMPANIES.keys()) + ["all"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="한국 제약사 최신 뉴스를 가져옵니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python run_news.py                          # 전체 5개사 뉴스
  python run_news.py -c celltrion             # 셀트리온 뉴스만
  python run_news.py -c samsung_biologics lg_chem   # 복수 선택
  python run_news.py -n 5                     # 회사당 5건
  python run_news.py --summary                # 요약 테이블만 출력
        """,
    )
    parser.add_argument(
        "-c", "--companies",
        nargs="+",
        choices=COMPANY_CHOICES,
        default=["all"],
        metavar="COMPANY",
        help=f"대상 회사 (기본: all). 선택 가능: {', '.join(COMPANIES.keys())}",
    )
    parser.add_argument(
        "-n", "--max-results",
        type=int,
        default=10,
        metavar="N",
        help="회사당 최대 뉴스 건수 (기본: 10)",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="요약 테이블만 출력",
    )
    return parser.parse_args()


def resolve_companies(choices: list[str]) -> list[dict]:
    if "all" in choices:
        return list(COMPANIES.values())
    return [COMPANIES[c] for c in choices if c in COMPANIES]


def fetch_all(companies: list[dict], max_results: int) -> dict[str, list]:
    results: dict[str, list] = {}
    with ThreadPoolExecutor(max_workers=len(companies)) as pool:
        future_map = {
            pool.submit(fetch_news_for_company, c, max_results): c["name_ko"]
            for c in companies
        }
        for future in as_completed(future_map):
            company_name = future_map[future]
            try:
                results[company_name] = future.result()
            except Exception as exc:
                print(f"[오류] {company_name}: {exc}", file=sys.stderr)
                results[company_name] = []
    return results


def main() -> None:
    args = parse_args()
    companies = resolve_companies(args.companies)

    if not companies:
        print("선택된 회사가 없습니다.", file=sys.stderr)
        sys.exit(1)

    print(f"\n뉴스를 가져오는 중... ({len(companies)}개사, 회사당 최대 {args.max_results}건)")
    results = fetch_all(companies, args.max_results)

    if args.summary:
        print(format_summary_table(results))
        return

    print(format_summary_table(results))
    for company_name, articles in results.items():
        print(format_company_news(company_name, articles))


if __name__ == "__main__":
    main()
