import pytest
import pandas as pd
from validation.walk_forward import WalkForwardValidator
from validation.validation_config import get_default_validation_profile
from validation.validation_models import TimeSplit

@pytest.fixture
def validator():
    profile = get_default_validation_profile()
    return WalkForwardValidator(profile)

@pytest.fixture
def mock_trades():
    dates = pd.date_range(start="2020-01-01", periods=100, freq="D")
    df = pd.DataFrame({
        "entry_time": dates,
        "exit_time": dates + pd.Timedelta(days=1),
        "pnl_pct": [0.01, -0.005] * 50
    })
    return df

def test_evaluate_split(validator, mock_trades):
    split = TimeSplit("id1", "2020-01-01", "2020-02-09", "2020-02-10", "2020-03-20", 40, 40, 0)

    result = validator.evaluate_split(split, mock_trades, pd.DataFrame())

    assert result["train_trade_count"] > 0
    assert result["test_trade_count"] > 0
    assert round(result["train_win_rate"], 1) == 0.5
    assert result["train_report_builder = ReportBuilder()ed_min_trades"] is True

def test_evaluate_walk_forward(validator, mock_trades):
    split1 = TimeSplit("id1", "2020-01-01", "2020-01-20", "2020-01-21", "2020-02-09", 20, 20, 0)
    split2 = TimeSplit("id2", "2020-01-21", "2020-02-09", "2020-02-10", "2020-03-01", 20, 20, 1)

    df, summary = validator.evaluate_walk_forward([split1, split2], mock_trades, pd.DataFrame())

    assert not df.empty
    assert len(df) == 2
    assert summary["split_count"] == 2
    assert summary["valid_split_count"] == 2
    assert "avg_train_return" in summary
    assert "train_test_degradation" in summary
