import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from advanced_technical_indicators.technical_indicator_config import get_default_technical_indicator_profile
from advanced_technical_indicators.candle_anatomy_features import build_candle_anatomy_feature_registry
from advanced_technical_indicators.quote_microstructure_features import build_quote_microstructure_feature_registry
from advanced_technical_indicators.mean_reversion_indicators import build_mean_reversion_indicator_expansion_registry


def main():
    profile = get_default_technical_indicator_profile()
    cnd_df, _ = build_candle_anatomy_feature_registry(profile)
    qte_df, _ = build_quote_microstructure_feature_registry(profile)
    mr_df, _ = build_mean_reversion_indicator_expansion_registry(profile)

    print("=" * 70)
    print("PHASE 117: CANDLE, QUOTE & MEAN REVERSION FEATURES")
    print("=" * 70)
    print(f"Candle Anatomy Features    : {len(cnd_df)}")
    print(f"Quote Microstructure Feats : {len(qte_df)}")
    print(f"Mean Reversion Features    : {len(mr_df)}")
    print("=" * 70)


if __name__ == "__main__":
    main()
