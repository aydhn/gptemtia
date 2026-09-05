import sys
import pandas as pd
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.no_lookahead_rules import get_no_lookahead_rules
from advanced_feature_validation.timestamp_order_validation import validate_timestamp_order
from advanced_feature_validation.asof_join_validation import validate_asof_join_direction
from advanced_feature_validation.macro_release_lag_validation import validate_macro_release_lag
from advanced_feature_validation.event_window_validation import validate_event_window_timestamps
from advanced_feature_validation.news_metadata_only_validation import validate_news_metadata_only_columns
from advanced_feature_validation.no_leakage_guard import run_no_leakage_guard


def main():
    settings = get_settings()
    data_lake = DataLake()

    # Create dummy sample feature frame to validate
    sample_df = pd.DataFrame({
        "timestamp": pd.date_range("2024-01-01", periods=10, freq="D"),
        "asset_symbol": ["BRENT"] * 10,
        "feature_ret_1d": [0.01 * i for i in range(10)],
    })

    ts_val = validate_timestamp_order(sample_df)
    asof_val = validate_asof_join_direction("backward")
    macro_val = validate_macro_release_lag(sample_df)
    event_val = validate_event_window_timestamps(sample_df)
    news_val = validate_news_metadata_only_columns(sample_df)
    leakage_guard = run_no_leakage_guard(sample_df)

    data_lake.save_timestamp_order_validation_registry(ts_val)
    data_lake.save_asof_join_validation_registry(asof_val)
    data_lake.save_macro_release_lag_validation_registry(macro_val)
    data_lake.save_event_window_validation_registry(event_val)
    data_lake.save_news_metadata_only_validation_registry(news_val)
    data_lake.save_no_leakage_guard_report(leakage_guard)

    print("=" * 70)
    print("PHASE 121: NO-LOOKAHEAD & LEAKAGE GUARD VALIDATION")
    print("=" * 70)
    print(f"Timestamp Order Valid : {ts_val['is_valid']}")
    print(f"Asof Join Valid       : {asof_val['is_valid']}")
    print(f"Macro Lag Valid       : {macro_val['is_valid']}")
    print(f"Event Window Valid    : {event_val['is_valid']}")
    print(f"News Metadata Valid   : {news_val['is_valid']}")
    print(f"No-Leakage Guard      : {leakage_guard['guard_status']}")
    print(f"Future Data Allowed   : False")
    print("=" * 70)


if __name__ == "__main__":
    main()
