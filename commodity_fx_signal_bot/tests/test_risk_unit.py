from sizing.risk_unit import (
    calculate_theoretical_risk_amount,
    calculate_risk_per_unit_from_atr,
    calculate_theoretical_unit_count,
    calculate_risk_unit_frame
)
import pandas as pd
import numpy as np

def test_calculate_theoretical_risk_amount():
    assert calculate_theoretical_risk_amount(100000.0, 0.01) == 1000.0
    assert calculate_theoretical_risk_amount(-100.0, 0.01) == 0.0

def test_calculate_risk_per_unit_from_atr():
    assert calculate_risk_per_unit_from_atr(2.0, 1.5) == 3.0
    assert calculate_risk_per_unit_from_atr(float('nan')) is None
    assert calculate_risk_per_unit_from_atr(0.0) is None

def test_calculate_theoretical_unit_count():
    assert calculate_theoretical_unit_count(1000.0, 10.0) == 100.0
    assert calculate_theoretical_unit_count(1000.0, None) == 0.0
    assert calculate_theoretical_unit_count(1000.0, float('nan')) == 0.0

def test_calculate_risk_unit_frame():
    df = pd.DataFrame({
        "close": [100.0, 102.0],
        "atr_14": [2.0, 2.5]
    }, index=pd.date_range("2023-01-01", periods=2))

    out_df, warnings = calculate_risk_unit_frame(df, risk_amount=1000.0)
    assert len(out_df) == 2
    assert "theoretical_risk_amount" in out_df.columns
    assert "risk_per_unit_atr_1x" in out_df.columns
    assert out_df["theoretical_unit_count_atr_1x"].iloc[0] == 500.0
