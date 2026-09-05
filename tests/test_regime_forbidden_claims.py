from advanced_regime_foundation.regime_forbidden_claims import (
    build_regime_forbidden_claim_registry,
    validate_regime_forbidden_claims,
    summarize_regime_forbidden_claims,
)


def test_regime_forbidden_claims():
    df, summary = build_regime_forbidden_claim_registry()
    assert not df.empty
    assert summary["all_blocked"] is True

    # Validate clean string
    clean_text = "This is a descriptive market behavior taxonomy report."
    assert validate_regime_forbidden_claims(clean_text)["is_valid"] is True

    # Validate forbidden strings
    assert validate_regime_forbidden_claims("Bu model kesin al sinyali üretir.")["is_valid"] is False
    assert validate_regime_forbidden_claims("Sistem production ready durumdadır.")["is_valid"] is False
    assert validate_regime_forbidden_claims("Official approval verilmiştir.")["is_valid"] is False
    assert validate_regime_forbidden_claims("Broker ready entegrasyonu tamamlandı.")["is_valid"] is False
    assert validate_regime_forbidden_claims("Burada verilenler yatırım tavsiyesi niteliğindedir.")["is_valid"] is False

    summ = summarize_regime_forbidden_claims(df)
    assert summ["all_blocked"] is True
