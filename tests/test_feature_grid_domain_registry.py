from advanced_feature_grid.feature_grid_domain_registry import build_feature_grid_domain_registry
from advanced_feature_grid.feature_grid_config import get_default_feature_grid_profile


def test_feature_grid_domain_registry():
    profile = get_default_feature_grid_profile()
    df, summary = build_feature_grid_domain_registry(profile)

    assert not df.empty
    assert summary["total_domains"] >= 20
    assert summary["current_phase"] == 118
    assert summary["non_signal"] is True

    domain_labels = list(df["domain_label"])
    assert "window_grid_contract_domain" in domain_labels
    assert "no_lookahead_guard_domain" in domain_labels
    assert "moving_average_grid_domain" in domain_labels
    assert "phase_119_handoff_domain" in domain_labels
