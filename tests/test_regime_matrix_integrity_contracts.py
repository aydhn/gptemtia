from advanced_regime_matrix.regime_matrix_config import get_default_regime_matrix_profile
from advanced_regime_matrix.regime_matrix_integrity_contracts import (
    build_regime_matrix_integrity_contracts,
    validate_matrix_integrity_rule_coverage,
)


def test_build_regime_matrix_integrity_contracts():
    prof = get_default_regime_matrix_profile()
    df, s = build_regime_matrix_integrity_contracts(prof)
    assert len(df) == 8
    assert s["total_rules"] == 8
    assert s["all_non_signal"] is True
    assert s["all_source_preserved"] is True
    assert validate_matrix_integrity_rule_coverage() is True
