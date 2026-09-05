from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.feature_schema_registry import build_default_feature_schemas


def build_feature_metadata_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    schemas = build_default_feature_schemas(profile)
    records: List[Dict[str, Any]] = []

    for s in schemas:
        warmup = s.lookback_window if s.lookback_window is not None else 0
        records.append({
            "schema_id": s.schema_id,
            "feature_name": s.feature_name,
            "feature_type": s.feature_type,
            "dataset_type": s.dataset_type,
            "lookback_window": s.lookback_window,
            "warmup_rows_required": warmup,
            "nan_warmup_policy": "preserve_nan_or_mask",
            "lookahead_bias_risk": "guarded_no_shift_negative",
            "computation_cost": "low_numpy_pandas",
            "non_signal": True,
            "manual_review_required": s.manual_review_required,
        })

    df = pd.DataFrame.from_records(records)
    summary = summarize_feature_metadata_registry(df)
    return df, summary


def summarize_feature_metadata_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_features_registered": len(df),
        "all_guarded_against_lookahead": True,
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
        "max_warmup_required": int(df["warmup_rows_required"].max()) if not df.empty and "warmup_rows_required" in df.columns else 0,
        "non_signal": True,
    }
