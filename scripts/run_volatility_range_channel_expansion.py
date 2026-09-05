import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.volatility_indicators import build_volatility_indicator_expansion_registry
from advanced_technical_indicators.range_indicators import build_range_indicator_registry
from advanced_technical_indicators.channel_indicators import build_channel_indicator_registry


def main():
    profile = get_default_technical_indicator_profile()
    vol_df, _ = build_volatility_indicator_expansion_registry(profile)
    rng_df, _ = build_range_indicator_registry(profile)
    chn_df, _ = build_channel_indicator_registry(profile)

    print("=" * 70)
    print("PHASE 117: VOLATILITY, RANGE & CHANNEL EXPANSION")
    print("=" * 70)
    print(f"Volatility Indicators : {len(vol_df)}")
    print(f"Range Indicators      : {len(rng_df)}")
    print(f"Channel Indicators    : {len(chn_df)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
