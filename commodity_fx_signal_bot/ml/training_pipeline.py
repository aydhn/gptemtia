import pandas as pd
import logging
from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from .training_config import MLTrainingProfile, get_default_ml_training_profile
from .model_trainer import MLModelTrainer, build_model_id, model_training_result_to_dict
from .model_evaluator import build_model_evaluation_report
from .cross_validation import run_cross_validation
from .model_schema import infer_feature_schema, infer_target_schema, feature_schema_to_dict, target_schema_to_dict
from .model_artifacts import save_model_artifact, save_preprocessor_artifact, save_model_metadata, save_schema_snapshot, build_model_artifact_bundle, model_artifact_bundle_to_dict
from .model_registry import ModelRegistryEntry, ModelRegistry, build_registry_status
from .model_quality import build_model_quality_report
import reports.report_builder as report_builder

logger = logging.getLogger(__name__)

class MLTrainingPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: MLTrainingProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_ml_training_profile()

        self.registry = ModelRegistry(data_lake.paths.ml_model_registry)

    def load_training_inputs(
        self,
        spec: SymbolSpec,
        timeframe: str,
        dataset_profile_name: str,
    ) -> tuple[dict, dict]:
        try:
            dataset = self.data_lake.load_ml_supervised_dataset(spec.symbol, timeframe, dataset_profile_name)
            metadata = self.data_lake.load_ml_dataset_metadata(spec.symbol, timeframe, dataset_profile_name)
            split = self.data_lake.load_ml_split_manifest(spec.symbol, timeframe, dataset_profile_name)
            quality = self.data_lake.load_ml_dataset_quality(spec.symbol, timeframe, dataset_profile_name)
            return {"dataset": dataset, "metadata": metadata, "split": split, "quality": quality}, {"warnings": []}
        except Exception as e:
            return {}, {"warnings": [f"Error loading training inputs: {str(e)}"]}

    def train_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: MLTrainingProfile | None = None,
        model_family: str | None = None,
        save: bool = True,
    ) -> tuple[dict, dict]:
        p = profile or self.profile

        if spec.asset_class in ["synthetic", "macro", "benchmark"]:
            return {}, {"warnings": [f"Skipping ML training for {spec.asset_class} symbol {spec.symbol}"]}

        inputs, in_res = self.load_training_inputs(spec, timeframe, p.dataset_profile)
        if in_res["warnings"] or not inputs.get("dataset") is not None or inputs["dataset"].empty:
            return {}, {"warnings": [f"Missing dataset for {spec.symbol} {timeframe}"]}

        dataset = inputs["dataset"]
        split = inputs["split"]

        trainer = MLModelTrainer(p)
        model, preprocessor, train_result, prep_res = trainer.train_from_dataset(
            spec.symbol, timeframe, dataset, split, model_family
        )

        if not model:
            return {"model_id": train_result.model_id, "status": train_result.status}, {"warnings": prep_res["warnings"]}

        eval_metrics, eval_res = build_model_evaluation_report(
            model, preprocessor, dataset, p.target_column, p.task_type, split
        )

        train_result.metrics = eval_metrics

        X, y, _ = trainer.prepare_training_data(dataset, p.target_column)
        cv_df, cv_summary = run_cross_validation(X, y, train_result.model_family, p.task_type, p)

        quality_report = build_model_quality_report(
            model_training_result_to_dict(train_result),
            eval_metrics,
            cv_summary,
            inputs["quality"].get("leakage_audit", {}),
            inputs["quality"]
        )

        registry_status = build_registry_status(
            eval_metrics, quality_report, inputs["quality"].get("leakage_audit", {})
        )

        feature_schema = infer_feature_schema(X)
        target_schema = infer_target_schema(y, p.task_type, p.target_column)

        artifact_paths = {}
        if save:
            model_path = save_model_artifact(model, train_result.model_id, self.data_lake.paths.ml_model_artifacts)
            prep_path = save_preprocessor_artifact(preprocessor, train_result.model_id, self.data_lake.paths.ml_model_artifacts)
            meta_path = save_model_metadata(model_training_result_to_dict(train_result), train_result.model_id, self.data_lake.paths.ml_model_artifacts)
            fs_path = save_schema_snapshot(feature_schema_to_dict(feature_schema), train_result.model_id, self.data_lake.paths.ml_model_artifacts, "feature_schema")
            ts_path = save_schema_snapshot(target_schema_to_dict(target_schema), train_result.model_id, self.data_lake.paths.ml_model_artifacts, "target_schema")

            artifact_paths = {
                "model_path": str(model_path),
                "preprocessor_path": str(prep_path),
                "metadata_path": str(meta_path),
                "feature_schema_path": str(fs_path),
                "target_schema_path": str(ts_path)
            }

            self.data_lake.save_ml_model_evaluation(spec.symbol, timeframe, p.name, train_result.model_id, eval_metrics)
            if not cv_df.empty:
                self.data_lake.save_ml_cv_results(spec.symbol, timeframe, p.name, train_result.model_id, cv_df)
            self.data_lake.save_ml_model_quality(spec.symbol, timeframe, p.name, train_result.model_id, quality_report)

        entry = ModelRegistryEntry(
            model_id=train_result.model_id,
            symbol=spec.symbol,
            timeframe=timeframe,
            training_profile=p.name,
            dataset_profile=p.dataset_profile,
            model_family=train_result.model_family,
            task_type=p.task_type,
            target_column=p.target_column,
            artifact_paths=artifact_paths,
            metrics=eval_metrics,
            cv_summary=cv_summary,
            leakage_audit_passed=inputs["quality"].get("leakage_audit", {}).get("passed", True),
            dataset_quality_passed=inputs["quality"].get("passed", True),
            model_quality_passed=quality_report.get("passed", True),
            registry_status=registry_status,
            created_at_utc=train_result.trained_at_utc,
            warnings=train_result.warnings + prep_res["warnings"] + eval_res["warnings"]
        )

        if save:
            self.registry.register(entry)

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "training_profile": p.name,
            "dataset_profile": p.dataset_profile,
            "model_id": train_result.model_id,
            "model_family": train_result.model_family,
            "task_type": p.task_type,
            "target_column": p.target_column,
            "train_rows": train_result.train_rows,
            "test_rows": train_result.test_rows,
            "feature_count": train_result.feature_count,
            "metrics": eval_metrics,
            "cv_summary": cv_summary,
            "quality_report": quality_report,
            "registry_entry": asdict(entry),
            "warnings": entry.warnings
        }

        return summary, {"warnings": entry.warnings}

    def train_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: MLTrainingProfile | None = None,
        model_family: str | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:
        p = profile or self.profile
        results = []
        processed = 0

        for spec in specs:
            if limit and processed >= limit:
                break

            summary, res = self.train_for_symbol_timeframe(spec, timeframe, p, model_family, save)
            if summary and "model_id" in summary:
                results.append(summary)
                processed += 1

        df = pd.DataFrame([
            {
                "symbol": r["symbol"],
                "model_id": r["model_id"],
                "model_family": r["model_family"],
                "target_column": r["target_column"],
                "train_rows": r["train_rows"],
                "test_rows": r["test_rows"],
                "primary_metric": r.get("metrics", {}).get("balanced_accuracy", r.get("metrics", {}).get("r2", 0.0)),
                "cv_mean_metric": r.get("cv_summary", {}).get("mean_primary_metric", 0.0),
                "quality_passed": r.get("quality_report", {}).get("passed", False),
                "registry_status": r.get("registry_entry", {}).get("registry_status", "unknown")
            }
            for r in results if "model_id" in r
        ])

        return {"processed": processed, "results": results, "ranking_df": df}
