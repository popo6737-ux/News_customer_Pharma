import pytest
from pharma_news import COMPANIES


EXPECTED_KEYS = {
    "samsung_biologics",
    "celltrion",
    "lotte_biologics",
    "lg_chem",
    "celltrion_pharm",
}


def test_all_companies_present():
    assert set(COMPANIES.keys()) == EXPECTED_KEYS


def test_company_schema():
    required_fields = {"name_ko", "name_en", "search_keywords", "ticker"}
    for key, company in COMPANIES.items():
        assert required_fields.issubset(company.keys()), f"{key} missing fields"
        assert isinstance(company["search_keywords"], list)
        assert len(company["search_keywords"]) >= 1


def test_korean_names():
    ko_names = {c["name_ko"] for c in COMPANIES.values()}
    assert "삼성바이오로직스" in ko_names
    assert "셀트리온" in ko_names
    assert "롯데바이오로직스" in ko_names
    assert "LG화학" in ko_names
    assert "셀트리온제약" in ko_names
