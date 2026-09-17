# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Construction Master Manifest."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_construction_manifest import (
    build_portfolio_construction_manifest,
)


def test_portfolio_construction_manifest():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_construction_manifest(profile)
    assert len(df) == 1
    row = df.iloc[0]

    assert row["manifest_id"] == "MNF-153-001"
    assert row["current_phase"] == 153
    assert row["target_final_phase"] == 160
    assert row["next_phase"] == 154

    # Strict prohibitions
    assert row["portfolio_constructed"] == False
    assert row["position_sizing_generated"] == False
    assert row["capital_allocation_generated"] == False
    assert row["portfolio_weights_generated"] == False
    assert row["orders_generated"] == False
    assert row["broker_order_sent"] == False
    assert row["live_order_sent"] == False
    assert row["optimizer_executed"] == False
    assert row["metric_calculated"] == False
    assert row["model_training_executed"] == False
    assert row["prediction_generated"] == False

    # Positive safety guarantees
    assert row["non_signal"] == True
    assert row["local_only"] == True
    assert row["dry_run"] == True
    assert row["non_production"] == True
    assert row["source_preserved"] == True
    assert row["manual_review_required"] == True
    assert row["phase_154_handoff_ready"] == True
    assert row["status"] == "portfolio_contract_ready"
