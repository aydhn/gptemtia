"""Fusion Feature Matrix Builder and Manifest Generator.

Coordinates multi-domain feature fusion and produces validated feature matrices and manifests.
Strictly non-signal, metadata-only, backward-only join, research use only.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Optional, Tuple
import pandas as pd
from advanced_feature_fusion.cross_domain_context_fusion import fuse_cross_domain_context
from advanced_feature_fusion.fusion_feature_models import FusionFeatureMatrixManifest
from advanced_feature_fusion.fusion_feature_matrix_contracts import validate_fusion_feature_matrix_contract
from advanced_feature_fusion.no_lookahead_fusion_guard import validate_no_forbidden_fusion_columns, validate_no_full_article_columns


def build_fusion_feature_matrix(
    base_df: pd.DataFrame,
    macro_df: Optional[pd.DataFrame] = None,
    calendar_df: Optional[pd.DataFrame] = None,
    news_metadata_df: Optional[pd.DataFrame] = None,
    matrix_id: str = "matrix_phase_120_default",
    profile_name: str = "balanced_local_macro_calendar_news_fusion",
    timestamp_col: str = "timestamp",
) -> Tuple[pd.DataFrame, FusionFeatureMatrixManifest]:
    """Build unified multi-domain feature matrix and its validation manifest."""
    # Ensure base input has timestamp sorted
    if base_df.empty:
        df_empty = pd.DataFrame(columns=[timestamp_col])
        manifest = FusionFeatureMatrixManifest(
            matrix_id=matrix_id,
            profile_name=profile_name,
            total_rows=0,
            total_columns=1,
            feature_columns=[],
            domains_included=[],
            start_timestamp="N/A",
            end_timestamp="N/A",
            is_monotonic_increasing=True,
            no_lookahead_guaranteed=True,
            is_strictly_metadata_only=True,
            is_non_signal_guaranteed=True,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        return df_empty, manifest

    # Sort base
    sorted_base = base_df.copy()
    if timestamp_col in sorted_base.columns:
        sorted_base[timestamp_col] = pd.to_datetime(sorted_base[timestamp_col], utc=True)
        sorted_base = sorted_base.sort_values(by=timestamp_col).reset_index(drop=True)

    fused_df = fuse_cross_domain_context(
        base_df=sorted_base,
        macro_df=macro_df,
        calendar_df=calendar_df,
        news_metadata_df=news_metadata_df,
        timestamp_col=timestamp_col,
    )

    # Post-validation
    validate_no_forbidden_fusion_columns(fused_df)
    validate_no_full_article_columns(fused_df)
    violations = validate_fusion_feature_matrix_contract(fused_df, timestamp_col=timestamp_col)
    if violations:
        raise ValueError(f"Fusion feature matrix contract violations: {violations}")

    # Determine domains included
    domains = ["market_base"]
    if macro_df is not None and not macro_df.empty:
        domains.append("macroeconomic")
    if calendar_df is not None and not calendar_df.empty:
        domains.append("calendar_events")
    if news_metadata_df is not None and not news_metadata_df.empty:
        domains.append("news_metadata")

    ts_series = pd.to_datetime(fused_df[timestamp_col], utc=True)
    start_ts = str(ts_series.iloc[0]) if len(ts_series) > 0 else "N/A"
    end_ts = str(ts_series.iloc[-1]) if len(ts_series) > 0 else "N/A"
    feature_cols = [c for c in fused_df.columns if c != timestamp_col]

    manifest = FusionFeatureMatrixManifest(
        matrix_id=matrix_id,
        profile_name=profile_name,
        total_rows=len(fused_df),
        total_columns=len(fused_df.columns),
        feature_columns=feature_cols,
        domains_included=domains,
        start_timestamp=start_ts,
        end_timestamp=end_ts,
        is_monotonic_increasing=bool(ts_series.is_monotonic_increasing),
        no_lookahead_guaranteed=True,
        is_strictly_metadata_only=True,
        is_non_signal_guaranteed=True,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    return fused_df, manifest


def get_fusion_feature_matrix_summary(manifest: FusionFeatureMatrixManifest) -> Dict[str, Any]:
    """Return dictionary summary of matrix manifest."""
    return manifest.to_dict()
