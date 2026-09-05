import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.price_action_indicators import build_price_action_indicator_registry
from advanced_technical_indicators.return_indicators import build_return_indicator_registry
from advanced_technical_indicators.moving_average_indicators import build_moving_average_indicator_registry
from advanced_technical_indicators.trend_indicators import build_trend_indicator_expansion_registry


def main():
    profile = get_default_technical_indicator_profile()
    pa_df, pa_sum = build_price_action_indicator_registry(profile)
    ret_df, ret_sum = build_return_indicator_registry(profile)
    ma_df, ma_sum = build_moving_average_indicator_registry(profile)
    tr_df, tr_sum = build_trend_indicator_expansion_registry(profile)

    print("=" * 70)
    print("PHASE 117: PRICE, RETURN, MOVING AVERAGE & TREND EXPANSION")
    print("=" * 70)
    print(f"Price Action Indicators : {len(pa_df)}")
    print(f"Return Indicators       : {len(ret_df)}")
    print(f"Moving Average Inds     : {len(ma_df)}")
    print(f"Trend Indicators        : {len(tr_df)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
