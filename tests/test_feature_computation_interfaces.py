from advanced_feature_engine.feature_engine_config import get_default_feature_engine_profile
from advanced_feature_engine.feature_computation_interfaces import (
    BaseFeatureComputer,
    build_feature_computation_interface_contract,
)


def test_feature_computation_interfaces():
    profile = get_default_feature_engine_profile()
    df, summary = build_feature_computation_interface_contract(profile)

    assert not df.empty
    assert summary["all_enforced"] is True
    assert summary["non_signal"] is True
