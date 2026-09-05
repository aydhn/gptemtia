from typing import Tuple, Dict, Any
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.price_indicator_catalog import build_price_indicator_catalog
from advanced_feature_engine.trend_indicator_catalog import build_trend_indicator_catalog
from advanced_feature_engine.momentum_indicator_catalog import build_momentum_indicator_catalog
from advanced_feature_engine.volatility_indicator_catalog import build_volatility_indicator_catalog
from advanced_feature_engine.mean_reversion_indicator_catalog import build_mean_reversion_indicator_catalog


def build_indicator_catalog_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    price_df, _ = build_price_indicator_catalog(profile)
    trend_df, _ = build_trend_indicator_catalog(profile)
    momentum_df, _ = build_momentum_indicator_catalog(profile)
    volatility_df, _ = build_volatility_indicator_catalog(profile)
    mean_rev_df, _ = build_mean_reversion_indicator_catalog(profile)

    combined_df = pd.concat(
        [price_df, trend_df, momentum_df, volatility_df, mean_rev_df],
        ignore_index=True,
    )
    summary = summarize_indicator_catalog_registry(combined_df)
    return combined_df, summary


def summarize_indicator_catalog_registry(df: pd.DataFrame) -> Dict[str, Any]:
    families = df["indicator_family"].unique().tolist() if not df.empty and "indicator_family" in df.columns else []
    return {
        "total_indicators": len(df),
        "total_families": len(families),
        "families": families,
        "all_non_signal": True,
        "indicators": df["indicator_name"].tolist() if not df.empty and "indicator_name" in df.columns else [],
        "manual_review_required_count": int(df["manual_review_required"].sum()) if not df.empty and "manual_review_required" in df.columns else 0,
        "disclaimer": "Tüm teknik göstergeler yalnızca araştırma ve feature çıkarımı amaçlıdır; AL/SAT veya yatırım tavsiyesi içermez.",
    }
