from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


COMMODITY_MACRO_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "cma_gold_us10y",
        "commodity_symbol": "XAU/USD",
        "macro_indicator": "US_10Y_YIELD",
        "relation_type": "real_rate_inverse_context",
        "macro_context_placeholder": "us10y_yield_context",
        "non_signal": True,
        "notes": "Altın ve ABD 10Y tahvil faizi; korelasyon trade kuralı değildir.",
    },
    {
        "alignment_id": "cma_gold_dxy",
        "commodity_symbol": "XAU/USD",
        "macro_indicator": "DXY_PLACEHOLDER",
        "relation_type": "dollar_index_inverse_context",
        "macro_context_placeholder": "dxy_gold_context",
        "non_signal": True,
        "notes": "Altın ve Dolar endeksi ters yönlü araştırma bağlamı.",
    },
    {
        "alignment_id": "cma_wti_inflation",
        "commodity_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "macro_indicator": "US_CPI_RELEASE",
        "relation_type": "energy_input_cost_context",
        "macro_context_placeholder": "cpi_energy_context",
        "non_signal": True,
        "notes": "Petrol ve manşet enflasyon girdi maliyeti araştırma bağlamı.",
    },
    {
        "alignment_id": "cma_ng_growth",
        "commodity_symbol": "NATURAL_GAS_CONTINUOUS_PLACEHOLDER",
        "macro_indicator": "GLOBAL_GROWTH_SENTIMENT",
        "relation_type": "industrial_energy_demand_context",
        "macro_context_placeholder": "growth_energy_context",
        "non_signal": True,
        "notes": "Doğal gaz ve sanayi büyüme göstergeleri bağlamı.",
    },
]


def build_commodity_macro_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(COMMODITY_MACRO_ITEMS)
    summary = summarize_commodity_macro_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_commodity_macro_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "commodities": list(df["commodity_symbol"].unique()) if "commodity_symbol" in df.columns else [],
        "macro_indicators": list(df["macro_indicator"].unique()) if "macro_indicator" in df.columns else [],
        "all_non_signal": all_non_signal,
        "status": "READY" if all_non_signal else "SAFETY_VIOLATION",
    }
