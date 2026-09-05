from advanced_regime_foundation.regime_foundation_pipeline import (
    RegimeFoundationPipeline,
)
from advanced_regime_foundation.regime_foundation_validation import (
    build_regime_foundation_validation_report,
    validate_no_forbidden_regime_claims,
)


def test_regime_foundation_validation():
    pipeline = RegimeFoundationPipeline()
    t_prof, _ = pipeline.build_profiles_domains_taxonomy(save=False)
    t_fam, _ = pipeline.build_regime_families(save=False)
    t_man, _ = pipeline.build_manifest_policies(save=False)
    val_inputs = {**t_prof, **t_fam, **t_man}

    df, summary = build_regime_foundation_validation_report(val_inputs)
    assert not df.empty
    assert summary["validation_status"] == "VALIDATION_PASS"
    assert summary["forbidden_claims_clean"] is True
    assert summary["passed_rules"] == summary["total_rules"]

    # Invariant checks: forbidden claims scanner
    assert validate_no_forbidden_regime_claims(text="Clean research descriptive text")["is_valid"] is True
    assert validate_no_forbidden_regime_claims(text="Bu kesin al sinyalidir")["is_valid"] is False
