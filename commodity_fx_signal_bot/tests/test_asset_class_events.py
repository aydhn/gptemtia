import pytest
import pandas as pd
from asset_profiles.asset_class_events import (
    detect_asset_behavior_events,
    detect_group_regime_events,
    detect_relative_strength_events,
    build_asset_class_event_frame,
)


def test_detect_asset_behavior_events():
    idx = pd.date_range("2023-01-01", periods=2)
    df = pd.DataFrame(
        {
            "asset_behavior_regime_label": [
                "asset_low_volume_confidence",
                "asset_high_gap_risk",
            ],
            "asset_profile_confidence": [0.9, 0.2],
        },
        index=idx,
    )

    events = detect_asset_behavior_events(df)
    assert events["event_asset_low_volume_confidence_warning"].iloc[0] == 1
    assert events["event_asset_high_gap_risk_warning"].iloc[1] == 1
    assert events["event_asset_profile_low_confidence_warning"].iloc[1] == 1


def test_build_asset_class_event_frame():
    idx = pd.date_range("2023-01-01", periods=1)
    df = pd.DataFrame(
        {
            "asset_behavior_regime_label": ["asset_unknown"],
            "asset_profile_confidence": [0.5],
            "asset_group_regime_label": ["group_uptrend"],
            "asset_relative_strength_regime_label": ["asset_group_leader"],
            "asset_correlation_regime_label": ["asset_group_decoupling"],
            "group_metals_dispersion_high": [1],
        },
        index=idx,
    )

    events, summary = build_asset_class_event_frame(df)
    assert not events.empty

    # Check that events are candidates/warnings, not buy/sell signals
    cols = list(events.columns)
    assert not any("buy" in c.lower() or "sell" in c.lower() for c in cols)

    assert events["event_asset_group_uptrend_context"].iloc[0] == 1
    assert events["event_asset_group_leader_candidate"].iloc[0] == 1
    assert events["event_asset_group_decoupling"].iloc[0] == 1
    assert events["event_asset_high_dispersion_context"].iloc[0] == 1
