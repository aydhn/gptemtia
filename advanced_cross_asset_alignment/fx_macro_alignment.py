from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)


FX_MACRO_ITEMS: List[Dict[str, Any]] = [
    {
        "alignment_id": "fxm_eur_usd_rates",
        "fx_pair": "EUR/USD",
        "macro_indicator": "FED_POLICY_RATE",
        "indicator_category": "central_bank_rate",
        "macro_context_placeholder": "rate_differential_context",
        "non_signal": True,
        "notes": "Fed politika faizi; trade sinyali veya kesin yön tahmini değildir.",
    },
    {
        "alignment_id": "fxm_eur_usd_ecb",
        "fx_pair": "EUR/USD",
        "macro_indicator": "ECB_POLICY_RATE",
        "indicator_category": "central_bank_rate",
        "macro_context_placeholder": "ecb_rate_context",
        "non_signal": True,
        "notes": "ECB politika faizi bağlamı; sinyal içermez.",
    },
    {
        "alignment_id": "fxm_eur_usd_dxy",
        "fx_pair": "EUR/USD",
        "macro_indicator": "DXY_PLACEHOLDER",
        "indicator_category": "dollar_index",
        "macro_context_placeholder": "dxy_inverse_context",
        "non_signal": True,
        "notes": "Dolar endeksi bağlamı; sinyal üretimi kesin yasaktır.",
    },
    {
        "alignment_id": "fxm_usd_try_cbrt",
        "fx_pair": "USD/TRY",
        "macro_indicator": "CBRT_POLICY_RATE",
        "indicator_category": "central_bank_rate",
        "macro_context_placeholder": "cbrt_one_week_repo_context",
        "non_signal": True,
        "notes": "TCMB bir hafta vadeli repo faizi bağlamı; araştırma amaçlıdır.",
    },
    {
        "alignment_id": "fxm_usd_try_cpi",
        "fx_pair": "USD/TRY",
        "macro_indicator": "TR_CPI_PLACEHOLDER",
        "indicator_category": "inflation",
        "macro_context_placeholder": "tr_cpi_context",
        "non_signal": True,
        "notes": "Yurt içi TÜFE yıllık/aylık değişim bağlamı.",
    },
]


def build_fx_macro_alignment_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    df = pd.DataFrame(FX_MACRO_ITEMS)
    summary = summarize_fx_macro_alignment(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_fx_macro_alignment(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_alignments": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    return {
        "total_alignments": len(df),
        "fx_pairs": list(df["fx_pair"].unique()) if "fx_pair" in df.columns else [],
        "macro_indicators": list(df["macro_indicator"].unique()) if "macro_indicator" in df.columns else [],
        "all_non_signal": all_non_signal,
        "status": "READY" if all_non_signal else "SAFETY_VIOLATION",
    }
