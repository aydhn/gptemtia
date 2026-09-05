from advanced_regime_rule_free.regime_rule_free_domain_registry import (
    build_regime_rule_free_domain_registry,
)


def test_build_regime_rule_free_domain_registry():
    df, summary = build_regime_rule_free_domain_registry()
    assert not df.empty
    assert summary["total_domains"] >= 15
    assert summary["current_phase"] == 128
    assert summary["all_non_signal"] is True
    assert summary["all_non_executable"] is True

    domain_ids = df["domain_id"].tolist()
    assert "rule_free_labeling_contracts" in domain_ids
    assert "candidate_state_schema" in domain_ids
    assert "pseudo_state_schema" in domain_ids
    assert "unsupervised_prep_contracts" in domain_ids
    assert "clustering_input_contracts" in domain_ids
    assert "phase_129_handoff" in domain_ids
