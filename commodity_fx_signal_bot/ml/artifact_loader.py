import os
import joblib
import pandas as pd
from typing import Tuple, Dict, Any, Optional
from pathlib import Path

from data.storage.data_lake import DataLake
from ml.prediction_config import MLPredictionProfile

class ModelArtifactLoader:
    def __init__(self, data_lake: DataLake):
        self.lake = data_lake
        self.models_dir = self.lake.paths.ml_models
        self.artifacts_dir = self.lake.paths.ml_model_artifacts
        self.registry_dir = self.lake.paths.ml_model_registry

    def load_registry_entries(
        self,
        symbol: Optional[str] = None,
        timeframe: Optional[str] = None,
        training_profile: Optional[str] = None,
        target_column: Optional[str] = None,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Load entries from the model registry that match the filters."""
        registry_files = list(self.registry_dir.glob("*.csv"))
        if not registry_files:
            return pd.DataFrame(), {"status": "no_registry_files"}

        all_dfs = []
        for file in registry_files:
            df = pd.read_csv(file)
            all_dfs.append(df)

        if not all_dfs:
            return pd.DataFrame(), {"status": "empty_registry"}

        full_df = pd.concat(all_dfs, ignore_index=True)

        # Apply filters
        if symbol:
            full_df = full_df[full_df["symbol"] == symbol]
        if timeframe:
            full_df = full_df[full_df["timeframe"] == timeframe]
        if training_profile:
            full_df = full_df[full_df["training_profile"] == training_profile]
        if target_column:
            full_df = full_df[full_df["target_column"] == target_column]

        return full_df, {"status": "loaded", "rows": len(full_df)}

    def select_candidate_models(
        self,
        registry_df: pd.DataFrame,
        profile: MLPredictionProfile,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Select candidates based on MLPredictionProfile rules."""
        if registry_df.empty:
            return registry_df, {"selected": 0}

        df = registry_df.copy()

        # Apply strict filters based on quality columns if they exist
        if "model_quality_score" in df.columns:
            df = df[df["model_quality_score"] >= profile.min_model_quality_score]
        if "dataset_quality_score" in df.columns:
            df = df[df["dataset_quality_score"] >= profile.min_dataset_quality_score]
        if "leakage_risk_score" in df.columns:
            df = df[df["leakage_risk_score"] <= profile.max_leakage_risk_score]

        # Filter families
        if "model_family" in df.columns:
            df = df[df["model_family"].isin(profile.allowed_model_families)]

        # Reject warning models if not allowed
        if not profile.allow_warning_models and "model_status" in df.columns:
            df = df[~df["model_status"].isin(["warning", "rejected", "failed"])]

        return df, {"selected": len(df), "original": len(registry_df)}

    def load_model_bundle(self, model_id: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Safely load model, preprocessor, and schema."""
        model_path = self.models_dir / f"{model_id}_model.joblib"
        preprocessor_path = self.artifacts_dir / f"{model_id}_preprocessor.joblib"
        schema_path = self.artifacts_dir / f"{model_id}_schema.joblib"

        bundle = {}
        status = {}

        if not model_path.exists():
            status["error"] = f"Model artifact not found for {model_id}"
            return bundle, status

        try:
            bundle["model"] = joblib.load(model_path)
            if preprocessor_path.exists():
                bundle["preprocessor"] = joblib.load(preprocessor_path)
            if schema_path.exists():
                bundle["schema"] = joblib.load(schema_path)
            status["success"] = True
        except Exception as e:
            status["error"] = f"Failed to load bundle: {str(e)}"

        return bundle, status

    def validate_model_bundle(self, bundle: Dict[str, Any], dataset_metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """Check if bundle contains required items."""
        if not bundle.get("model"):
            return {"valid": False, "reason": "No model in bundle"}
        return {"valid": True}
