import pandas as pd
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.indicator_output_schema_registry import (
    build_indicator_output_schema_registry,
    validate_indicator_output_schema,
    summarize_indicator_output_schema,
)


def test_indicator_output_schema_registry():
    prof = get_default_technical_indicator_profile()
    df, summary = build_indicator_output_schema_registry(prof)
    assert not df.empty
    assert summary["forbidden_check_active"] is True

    sample_df = pd.DataFrame({"sma_20": [1.0, 2.0], "rsi_14": [50.0, 55.0]})
    res = validate_indicator_output_schema(sample_df, ["sma_20", "rsi_14"])
    assert res["valid"] is True

    # Forbidden column validation
    forbidden_df = pd.DataFrame({"signal": [1, 0]})
    res_bad = validate_indicator_output_schema(forbidden_df, ["signal"])
    assert res_bad["valid"] is False
