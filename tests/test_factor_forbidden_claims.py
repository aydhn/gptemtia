import pytest
from advanced_factor_metadata.factor_forbidden_claims import (
    build_factor_forbidden_claim_registry,
    summarize_factor_forbidden_claims,
    validate_factor_forbidden_claims,
)


def test_build_factor_forbidden_claim_registry():
    df, summary = build_factor_forbidden_claim_registry()
    assert not df.empty
    assert summary["total_forbidden_claims"] >= 14
    assert summary["non_signal"] is True

    stats = summarize_factor_forbidden_claims(df)
    assert stats["total_forbidden_patterns"] == len(df)
    assert stats["non_signal"] is True


def test_validate_factor_forbidden_claims():
    clean_text = "Faktör metrikleri sadece yerel araştırma için kullanılır."
    clean_res = validate_factor_forbidden_claims(clean_text)
    assert clean_res["is_clean"] is True
    assert clean_res["violations_count"] == 0

    dirty_texts = [
        "Bu model kesin al tavsiyesi verir.",
        "Trend faktörü yüksek ise long aç.",
        "Sistem production ready durumdadır.",
        "Resmi official approval onaylanmıştır.",
        "Burada yatırım tavsiyesi verilmektedir.",
    ]
    for dt in dirty_texts:
        res = validate_factor_forbidden_claims(dt)
        assert res["is_clean"] is False
        assert res["violations_count"] > 0
