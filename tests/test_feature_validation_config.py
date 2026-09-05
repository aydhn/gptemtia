import pytest
from advanced_feature_validation.feature_validation_config import (
    FeatureValidationConfig,
    get_feature_validation_config,
)


def test_feature_validation_config_defaults():
    cfg = get_feature_validation_config()
    assert cfg.current_phase == 121
    assert cfg.target_final_phase == 160
    assert cfg.next_phase == 122
    assert cfg.dry_run is True
    assert cfg.non_signal is True
    assert cfg.destructive_action_allowed is False
    assert cfg.max_missingness_ratio == 0.35
    assert cfg.warmup_window == 50
