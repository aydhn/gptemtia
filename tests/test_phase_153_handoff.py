import pytest
import pandas as pd
from advanced_backtest_acceptance.phase_153_handoff import (
    build_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report,
    summarize_phase_153_handoff,
    HANDOFF_ITEMS,
)

def test_phase_153_handoff():
    df, summary = build_phase_153_portfolio_construction_position_sizing_risk_budgeting_handoff_report()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(HANDOFF_ITEMS)
    assert summary["total_prerequisites"] == len(HANDOFF_ITEMS)
    assert summary["all_satisfied"] is True
    assert summary["handoff_ready"] is True
    assert summary["current_phase"] == 152
    assert summary["next_phase"] == 153
    assert summary["target_final_phase"] == 160
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Check invariants
    assert (df["satisfied"] == True).all()
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()

    # Summarize function
    summ = summarize_phase_153_handoff(df)
    assert summ["prerequisite_count"] == len(HANDOFF_ITEMS)
    assert summ["all_satisfied"] is True
    assert summ["handoff_ready"] is True
    assert summ["non_signal"] is True
