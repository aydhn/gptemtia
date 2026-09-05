from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FX_COMMODITY_PAIRS: List[Dict[str, Any]] = [
    {
        "alignment_id": "fxc_eur_usd_xau_usd",
        "fx_pair": "EUR/USD",
        "commodity_symbol": "XAU/USD",
        "relation_type": "dollar_denomination_context",
        "quote_currency": "USD",
        "correlation_context_placeholder": "rolling_corr_placeholder",
        "non_signal": True,
        "notes": "Ortak karşıt para birimi (USD) bağlamı; sinyal içermez.",
    },
    {
        "alignment_id": "fxc_usd_try_xau_usd",
        "fx_pair": "USD/TRY",
        "commodity_symbol": "XAU/USD",
        "relation_type": "local_currency_gold_context",
        "quote_currency": "TRY",
        "correlation_context_placeholder": "gram_gold_synthetic_context",
        "non_signal": True,
        "notes": "Yerel para birimi altın bağlamı (USD/TRY ve XAU/USD); sinyal üretmez.",
    },
    {
        "alignment_id": "fxc_usd_cad_wti",
        "fx_pair": "USD/CAD",
        "commodity_symbol": "WTI_CRUDE_CONTINUOUS_PLACEHOLDER",
        "relation_type": "petrocurrency_context",
        "quote_currency": "USD",
        "correlation_context_placeholder": "energy_fx_context",
        "non_signal": True,
        "notes": "Kanada Doları ve ham petrol ilişkisi araştırma bağlamı.",
    },
]


def build_fx_commodity_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(FX_COMMODITY_PAIRS)
    summary = summarize_fx_commodity_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_fx_commodity_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "fx_pairs": list(df["fx_pair"].unique()) if "fx_pair" in df.columns else [],
        "commodities": list(df["commodity_symbol"].unique()) if "commodity_symbol" in df.columns else [],
        "all_non_signal": all_non_signal,
        "status": "READY" if all_non_signal else "SAFETY_VIOLATION",
    }
