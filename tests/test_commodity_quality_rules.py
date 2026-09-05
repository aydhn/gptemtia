import pytest
import pandas as pd
from advanced_data_quality.data_quality_config import get_default_data_quality_profile
from advanced_data_quality.commodity_quality_rules import (
    build_commodity_quality_rule_set,
    check_commodity_spot_quality,
    check_commodity_ohlcv_quality,
    check_futures_metadata_quality,
)


def test_commodity_quality_rules():
    profile = get_default_data_quality_profile()
    df_rules, _ = build_commodity_quality_rule_set(profile)
    assert len(df_rules) >= 2

    # Missing field in spot
    spot_df = pd.DataFrame([{"symbol": "GOLD", "spot_price": 2500.0}])
    f_spot = check_commodity_spot_quality(spot_df, "comm_test_prov")
    assert any(f.finding_type == "finding_missing_required_field" for f in f_spot)

    # Missing OHLCV fields
    ohlc_df = pd.DataFrame([{"symbol": "CL", "timestamp": "2026-09-01"}])
    f_ohlc = check_commodity_ohlcv_quality(ohlc_df, "comm_test_prov")
    assert any(f.field_name == "open" for f in f_ohlc)

    # Futures metadata
    meta_df = pd.DataFrame([{"symbol": "CL"}])
    f_meta = check_futures_metadata_quality(meta_df, "comm_test_prov")
    assert any(f.field_name == "expiry_date" for f in f_meta)
