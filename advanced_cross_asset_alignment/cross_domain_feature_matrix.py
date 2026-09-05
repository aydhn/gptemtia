from typing import Tuple, Dict, Any, Optional
import pandas as pd
import numpy as np

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import FeatureMatrixContract
from advanced_cross_asset_alignment.asof_join_policies import safe_asof_join_backward
from advanced_cross_asset_alignment.no_lookahead_alignment_guard import validate_no_forbidden_alignment_columns


def build_cross_domain_feature_matrix_placeholder(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()

    # Synthetic offline fixture for cross-domain matrix representation
    dates = pd.date_range("2026-01-01", periods=10, freq="D", tz="UTC")
    ts_strings = [d.strftime("%Y-%m-%dT%H:%M:%SZ") for d in dates]

    data = {
        "normalized_timestamp": ts_strings,
        "canonical_symbol": ["EUR/USD"] * 10,
        "fx_eur_usd_close": [1.0850 + i * 0.0010 for i in range(10)],
        "fx_eur_usd_sma_w20": [1.0820 + i * 0.0008 for i in range(10)],
        "commodity_xau_usd_close": [2050.0 + i * 5.0 for i in range(10)],
        "commodity_xau_usd_bb_width_w20_std2": [0.025 + i * 0.001 for i in range(10)],
        "macro_us_10y_yield_yield_diff_1d": [0.01 * ((-1) ** i) for i in range(10)],
        "calendar_fomc_event_active_window": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        "news_central_bank_mention_count_1d": [2, 1, 3, 5, 2, 1, 1, 2, 1, 0],
    }
    df = pd.DataFrame(data)

    # Validate non-signal and zero forbidden columns
    val = validate_no_forbidden_alignment_columns(df)
    if not val["is_valid"]:
        raise ValueError(f"Cross-domain feature matrisinde yasaklı sütun tespit edildi: {val['issues']}")

    summary = summarize_cross_domain_feature_matrix(df)
    summary["profile"] = active_profile.name
    return df, summary


def build_aligned_feature_matrix_from_contract(
    base_df: pd.DataFrame,
    context_dfs: Dict[str, pd.DataFrame] | None = None,
    contract: FeatureMatrixContract | None = None,
    contract_name: str | None = None,
    additional_domain_dfs: Dict[str, pd.DataFrame] | None = None,
    **kwargs,
) -> pd.DataFrame:
    """Builds an aligned feature matrix from a base DataFrame and context DataFrames.
    
    Guarantees:
    - Never mutates input DataFrames (works on df.copy()).
    - Uses safe backward-only asof join.
    - Strictly non-signal, no target/label/prediction columns.
    """
    if base_df.empty:
        return base_df.copy()

    aligned = base_df.copy()
    ctx_dfs = context_dfs or additional_domain_dfs or {}

    ts_field = contract.timestamp_field if contract is not None else "normalized_timestamp"

    for domain_name, ctx_df in ctx_dfs.items():
        if ctx_df.empty:
            continue
        c_df = ctx_df.copy()

        # Identify join timestamps
        left_ts = ts_field if ts_field in aligned.columns else ("normalized_timestamp" if "normalized_timestamp" in aligned.columns else "timestamp_utc")
        right_ts = ts_field if ts_field in c_df.columns else ("normalized_timestamp" if "normalized_timestamp" in c_df.columns else "timestamp_utc")

        if left_ts in aligned.columns and right_ts in c_df.columns:
            aligned = safe_asof_join_backward(
                left_df=aligned,
                right_df=c_df,
                left_on=left_ts,
                right_on=right_ts,
            )

    # Validate output columns
    val = validate_no_forbidden_alignment_columns(aligned)
    if not val["is_valid"]:
        raise ValueError(f"Hizalanmış matriste yasaklı kolonlar bulundu: {val['issues']}")

    return aligned



def summarize_cross_domain_feature_matrix(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_rows": 0, "total_features": 0, "status": "EMPTY"}

    feature_cols = [c for c in df.columns if c not in ["normalized_timestamp", "canonical_symbol"]]
    val = validate_no_forbidden_alignment_columns(df)

    return {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "total_features": len(feature_cols),
        "contract_name": "cross_domain_research",
        "feature_columns": feature_cols,
        "is_non_signal": True,
        "non_signal": True,
        "forbidden_columns_found": val["forbidden_columns_found"],
        "status": "READY" if val["is_valid"] else "SAFETY_VIOLATION",
    }

