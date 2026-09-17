# -*- coding: utf-8 -*-
"""Unit tests for Phase 160 Phase Completion & 160-Phase Plan Closure."""

from advanced_final_delivery.final_160_phase_completion import (
    build_final_160_phase_completion_report,
    summarize_final_160_phase_completion,
    FINAL_COMPLETION_DOMAIN,
    PHASE_160_COMPLETED,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)
from advanced_final_delivery.final_delivery_models import Final160PhaseCompletionItem


def test_final_160_phase_completion():
    df, summary = build_final_160_phase_completion_report()
    assert not df.empty
    assert summary["current_phase"] == 160
    assert summary["target_final_phase"] == 160
    assert summary["next_phase"] is None
    assert summary["phase_160_completed"] is True
    assert summary["final_plan_closed"] is True
    assert summary["status"] == PHASE_160_COMPLETED
    assert "160 fazlık plan" in summary["declaration"]

    row = df.iloc[0]
    assert row["current_phase"] == 160
    assert row["target_final_phase"] == 160
    assert row["next_phase"] is None
    assert row["plan_status"] == "completed_contract_governance_documentation_acceptance_level"
    assert bool(row["live_trading_ready"]) is False
    assert bool(row["broker_ready"]) is False
    assert bool(row["production_ready"]) is False

    res = summarize_final_160_phase_completion(df)
    assert res["phase_160_completed"] is True
    assert res["final_plan_closed"] is True
