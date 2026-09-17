import pytest
import pandas as pd
from advanced_backtest_acceptance.backtest_acceptance_go_no_go_boundaries import (
    build_backtest_acceptance_go_no_go_boundary_registry,
    validate_backtest_acceptance_go_no_go_request,
    GO_CONDITIONS,
    NO_GO_CONDITIONS,
)
from advanced_backtest_acceptance.backtest_acceptance_labels import (
    GO_CONTRACT_ONLY,
    NO_GO_LIVE_TRADING,
    NO_GO_BROKER_EXECUTION,
)

def test_backtest_acceptance_go_no_go_boundaries():
    df, summary = build_backtest_acceptance_go_no_go_boundary_registry()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(summary, dict)
    assert len(df) == len(GO_CONDITIONS) + len(NO_GO_CONDITIONS)
    assert summary["go_count"] == len(GO_CONDITIONS)
    assert summary["no_go_count"] == len(NO_GO_CONDITIONS)
    assert summary["status"] == "ACCEPTED"
    assert summary["non_signal"] is True

    # Invariants
    assert (df["non_signal"] == True).all()
    assert (df["non_production"] == True).all()
    assert (df["local_only"] == True).all()

    # Test validator with known GO
    go_res = validate_backtest_acceptance_go_no_go_request("proceed_to_phase_153_portfolio_construction_contracts")
    assert go_res["decision"] == "GO"
    assert go_res["allowed"] is True
    assert go_res["boundary_label"] == GO_CONTRACT_ONLY

    # Test validator with known NO-GO
    nogo_res = validate_backtest_acceptance_go_no_go_request("live_trading")
    assert nogo_res["decision"] == "NO_GO"
    assert nogo_res["allowed"] is False
    assert nogo_res["boundary_label"] == NO_GO_LIVE_TRADING

    # Test validator with dict input
    dict_nogo = validate_backtest_acceptance_go_no_go_request({"action": "broker_execution"})
    assert dict_nogo["decision"] == "NO_GO"
    assert dict_nogo["allowed"] is False
    assert dict_nogo["boundary_label"] == NO_GO_BROKER_EXECUTION

    # Test unrecognized action defaults to NO_GO
    unrec = validate_backtest_acceptance_go_no_go_request("completely_unknown_action_xyz")
    assert unrec["decision"] == "NO_GO"
    assert unrec["allowed"] is False
    assert unrec["boundary_label"] == "no_go_unknown"
