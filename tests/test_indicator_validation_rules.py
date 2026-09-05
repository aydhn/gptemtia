import pandas as pd
from advanced_technical_indicators.indicator_validation_rules import (
    validate_indicator_dataframe,
    validate_indicator_output_no_forbidden_columns,
    validate_indicator_output_numeric_sanity,
    build_indicator_validation_rule_registry,
    summarize_indicator_validation_rules,
)
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile


def test_indicator_validation_rules():
    df = pd.DataFrame({"sma_20": [1.0, 2.0, 3.0]})
    assert validate_indicator_dataframe(df)["valid"] is True
    assert validate_indicator_output_no_forbidden_columns(df)["valid"] is True
    assert validate_indicator_output_numeric_sanity(df, ["sma_20"])["valid"] is True

    bad_df = pd.DataFrame({"signal_buy": [1, 0]})
    assert validate_indicator_output_no_forbidden_columns(bad_df)["valid"] is False

    prof = get_default_technical_indicator_profile()
    reg_df, summary = build_indicator_validation_rule_registry(prof)
    assert not reg_df.empty
    assert summary["status"] == "READY"
