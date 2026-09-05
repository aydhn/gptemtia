from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile
from advanced_feature_engine.factor_schema_registry import build_default_factor_schemas


def build_factor_metadata_registry(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    schemas = build_default_factor_schemas(profile)
    records: List[Dict[str, Any]] = []

    for f in schemas:
        records.append({
            "factor_id": f.factor_id,
            "factor_name": f.factor_name,
            "factor_type": f.factor_type,
            "future_phase_owner": f.future_phase_owner,
            "required_feature_count": len(f.required_features),
            "required_features": ",".join(f.required_features),
            "normalization_strategy": "zscore_cross_sectional_placeholder",
            "aggregation_method": "equal_weighted_composite_placeholder",
            "non_signal": True,
            "manual_review_required": f.manual_review_required,
        })

    df = pd.DataFrame.from_records(records)
    summary = summarize_factor_metadata_registry(df)
    return df, summary


def summarize_factor_metadata_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_factors_registered": len(df),
        "all_non_signal": bool(df["non_signal"].all()) if not df.empty and "non_signal" in df.columns else True,
        "target_phase_owner": "Phase 122",
        "non_signal": True,
    }
