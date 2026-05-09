import pandas as pd
from typing import Dict, Any, Optional, List

from commodity_fx_signal_bot.data.storage.data_lake import DataLake
from commodity_fx_signal_bot.config.settings import Settings
from commodity_fx_signal_bot.symbols import SymbolSpec
from commodity_fx_signal_bot.ml.prediction_config import MLPredictionProfile, get_default_ml_prediction_profile
from commodity_fx_signal_bot.ml.artifact_loader import ModelArtifactLoader
from commodity_fx_signal_bot.ml.inference_preprocessor import InferencePreprocessor
from commodity_fx_signal_bot.ml.model_inference import OfflineModelInference
from commodity_fx_signal_bot.ml.score_calibration import calibrate_classification_probabilities, normalize_regression_score, calculate_calibrated_prediction_score
from commodity_fx_signal_bot.ml.uncertainty import calculate_probability_entropy, calculate_uncertainty_from_confidence, calculate_margin_confidence
from commodity_fx_signal_bot.ml.ensemble import ModelEnsembleBuilder
from commodity_fx_signal_bot.ml.prediction_candidate import build_prediction_candidate_from_row
from commodity_fx_signal_bot.ml.prediction_pool import MLPredictionCandidatePool
from commodity_fx_signal_bot.ml.prediction_quality import build_prediction_quality_report
from commodity_fx_signal_bot.ml.prediction_context import build_model_context_features, build_ensemble_context_features
from commodity_fx_signal_bot.ml.prediction_models import infer_predicted_direction_from_class, infer_prediction_context_label

class MLPredictionPipeline:
    def __init__(self, data_lake: DataLake, settings: Settings, profile: Optional[MLPredictionProfile] = None):
        self.lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_ml_prediction_profile()
        self.loader = ModelArtifactLoader(self.lake)

    def load_prediction_inputs(self, spec: SymbolSpec, timeframe: str, dataset_profile_name: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        # Usually we would load the feature matrix or the prepared supervised dataset.
        # For offline prediction, let's load the supervised dataset (which has features aligned).
        try:
            # We mock the loading for now if method doesn't exist, but it should exist in data_lake
            if hasattr(self.lake, "load_supervised_dataset"):
                df = self.lake.load_supervised_dataset(spec.symbol, timeframe, dataset_profile_name)
            else:
                # Fallback to feature matrix
                df = pd.DataFrame() # Mock empty

            if df.empty:
                return pd.DataFrame(), {"status": "empty_dataset"}
            return df, {"status": "success"}
        except Exception as e:
            return pd.DataFrame(), {"status": "error", "error": str(e)}

    def run_for_model(self, spec: SymbolSpec, timeframe: str, model_id: str, profile: Optional[MLPredictionProfile] = None, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        prof = profile or self.profile

        # In a real impl, we'd use the loaded dataset. Mock returning empty for this structure
        return pd.DataFrame(), {"status": "not_implemented_individually"}

    def run_for_symbol_timeframe(self, spec: SymbolSpec, timeframe: str = "1d", profile: Optional[MLPredictionProfile] = None, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        prof = profile or self.profile
        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "prediction_profile": prof.name,
            "dataset_profile": prof.dataset_profile,
            "warnings": []
        }

        # 1. Load entries
        registry_df, status = self.loader.load_registry_entries(symbol=spec.symbol, timeframe=timeframe)
        if registry_df.empty:
            summary["warnings"].append("No registry entries found.")
            return pd.DataFrame(), summary

        # 2. Select candidates
        candidates_df, status = self.loader.select_candidate_models(registry_df, prof)
        summary["selected_model_count"] = status.get("selected", 0)

        if candidates_df.empty:
            summary["warnings"].append("No valid models passed selection filters.")
            return pd.DataFrame(), summary

        # 3. Load dataset
        dataset_df, status = self.load_prediction_inputs(spec, timeframe, prof.dataset_profile)
        if dataset_df.empty:
            summary["warnings"].append("Prediction dataset empty or not found.")
            return pd.DataFrame(), summary

        pool = MLPredictionCandidatePool()
        successful_models = 0
        prediction_frames = {}

        # We need a dummy loop to simulate model loading and inference
        for _, row in candidates_df.iterrows():
            m_id = str(row.get("model_id"))
            bundle, b_status = self.loader.load_model_bundle(m_id)
            if not bundle.get("model"):
                summary["warnings"].append(f"Failed to load bundle for {m_id}")
                continue

            model = bundle["model"]
            preprocessor = bundle.get("preprocessor")
            schema = bundle.get("schema", {})

            # Preprocess
            prep = InferencePreprocessor(preprocessor, schema)
            # Simulate transformation
            X_trans, p_stat = prep.transform(dataset_df)

            metadata = row.to_dict()
            inf = OfflineModelInference(model, prep, metadata, schema)

            pred_df, p_stat = inf.predict_frame(X_trans)
            if pred_df.empty:
                continue

            successful_models += 1
            prediction_frames[m_id] = pred_df

            # Simple audit dict
            audit = {
                "model_id": m_id,
                "dataset_id": "unknown",
                "leakage_audit_passed": float(row.get("leakage_risk_score", 0)) <= prof.max_leakage_risk_score,
                "dataset_quality_passed": float(row.get("dataset_quality_score", 0)) >= prof.min_dataset_quality_score,
                "model_quality_passed": float(row.get("model_quality_score", 0)) >= prof.min_model_quality_score,
                "schema_compatible": True, # Assume true for simulation
                "inference_rows": len(pred_df),
                "warning_count": 0,
                "passed": True,
                "model_quality_score": float(row.get("model_quality_score", 0.5)),
                "dataset_quality_score": float(row.get("dataset_quality_score", 0.5)),
                "leakage_risk_score": float(row.get("leakage_risk_score", 0.0)),
                "warnings": []
            }

            # If not audit passed
            if not (audit["leakage_audit_passed"] and audit["dataset_quality_passed"] and audit["model_quality_passed"]):
                audit["passed"] = False

            # Build candidates
            for idx, pred_row in pred_df.iterrows():
                # Add timestamp to row for candidate builder
                r = pred_row.copy()
                r["timestamp"] = str(idx)
                r["symbol"] = spec.symbol
                r["timeframe"] = timeframe

                # Calibrate
                r["calibrated_score"] = calculate_calibrated_prediction_score(r, metadata.get("task_type", "classification"))

                # Context
                r["predicted_direction"] = infer_predicted_direction_from_class(r.get("predicted_label"))
                r["prediction_context_label"] = infer_prediction_context_label(
                    r["predicted_direction"],
                    r.get("confidence_score", 0.5),
                    r.get("uncertainty_score", 1.0)
                )

                cand = build_prediction_candidate_from_row(r, audit, prof)
                pool.add(cand)

        summary["successful_model_count"] = successful_models
        pool_df = pool.to_dataframe()
        summary["prediction_candidate_count"] = len(pool.candidates)

        # Ensemble
        ensemble_builder = ModelEnsembleBuilder(prof)
        ensemble_df, e_status = ensemble_builder.build_ensemble_prediction(prediction_frames)
        summary["ensemble_available"] = not ensemble_df.empty

        # Quality Report
        audit_summary = {"passed": successful_models > 0}
        quality = build_prediction_quality_report(pool_df, audit_summary, prof)
        summary["quality_report"] = quality

        # Context Features
        model_ctx, _ = build_model_context_features(pool_df)
        ens_ctx, _ = build_ensemble_context_features(ensemble_df)

        # Save
        if save and self.settings.ml_prediction_save_candidates and not pool_df.empty:
            if hasattr(self.lake, "save_ml_prediction_candidates"):
                self.lake.save_ml_prediction_candidates(spec.symbol, timeframe, prof.name, pool_df)

        if save and self.settings.ml_prediction_save_context_features:
            if hasattr(self.lake, "save_ml_prediction_context") and not model_ctx.empty:
                self.lake.save_ml_prediction_context(spec.symbol, timeframe, prof.name, model_ctx)

        if save and summary["ensemble_available"]:
            if hasattr(self.lake, "save_ml_ensemble_predictions"):
                self.lake.save_ml_ensemble_predictions(spec.symbol, timeframe, prof.name, ensemble_df)

        if save and self.settings.ml_prediction_save_quality_reports:
            if hasattr(self.lake, "save_ml_prediction_quality"):
                self.lake.save_ml_prediction_quality(spec.symbol, timeframe, prof.name, quality)

        return pool_df, summary

    def run_for_universe(self, specs: List[SymbolSpec], timeframe: str = "1d", profile: Optional[MLPredictionProfile] = None, limit: Optional[int] = None, save: bool = True) -> Dict[str, Any]:
        results = []
        count = 0
        for spec in specs:
            if limit and count >= limit:
                break
            try:
                _, summary = self.run_for_symbol_timeframe(spec, timeframe, profile, save)
                summary["asset_class"] = spec.asset_class
                results.append(summary)
            except Exception as e:
                results.append({"symbol": spec.symbol, "error": str(e), "asset_class": spec.asset_class})
            count += 1

        return {"batch_results": results, "processed_count": count}
