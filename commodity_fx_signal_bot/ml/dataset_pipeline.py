import logging
import pandas as pd
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from config.settings import Settings
from .dataset_config import MLDatasetProfile, get_default_ml_dataset_profile
from .feature_matrix_builder import FeatureMatrixBuilder
from .target_engineering import build_target_frame
from .dataset_builder import SupervisedDatasetBuilder
from .leakage_checks import build_leakage_audit_report
from .dataset_quality import build_dataset_quality_report
from .splitters import chronological_train_validation_test_split, apply_purging_for_target_horizon, build_split_manifest, split_manifest_to_dict
from .dataset_registry import build_dataset_metadata, dataset_metadata_to_dict

logger = logging.getLogger(__name__)

class MLDatasetPipeline:
    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: MLDatasetProfile | None = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_ml_dataset_profile()
        self.feature_builder = FeatureMatrixBuilder(self.data_lake)
        self.dataset_builder = SupervisedDatasetBuilder(self.profile)

    def build_for_symbol_timeframe(
        self,
        spec: SymbolSpec,
        timeframe: str = "1d",
        profile: MLDatasetProfile | None = None,
        save: bool = True,
    ) -> tuple[pd.DataFrame, dict]:

        prof = profile or self.profile

        # 1. Processed OHLCV
        df = self.data_lake.load_processed_ohlcv(spec.symbol, timeframe)
        if df is None or df.empty:
            return pd.DataFrame(), {"warnings": [f"No OHLCV data for {spec.symbol} {timeframe}"]}

        # 2. X
        X, f_summary = self.feature_builder.build_feature_matrix(spec, timeframe, prof.feature_sets)

        # 3. y
        # We need candidate and backtest data for outcome targets if requested
        candidate_df = None
        backtest_df = None
        if "candidate_outcome" in prof.target_types:
            candidate_df = self.data_lake.load_signal_candidates(spec.symbol, timeframe)
            # backtest_df = self.data_lake.load_backtest_trades(...) # Simplification for now

        y, t_summary = build_target_frame(df, candidate_df, backtest_df, prof)

        # 4. Supervised Dataset
        dataset, d_summary = self.dataset_builder.build_supervised_dataset(X, y)

        if dataset.empty:
             return dataset, {"warnings": ["Resulting dataset is empty"]}

        # 5. Leakage Audit
        audit = build_leakage_audit_report(X, y)

        # 6. Quality Report
        quality = build_dataset_quality_report(X, y, dataset, prof)

        # 7. Split Manifest
        # For simplicity, using a generic target for splitting logic (or just splitting the whole set)
        target_col = prof.target_types[0] if prof.target_types else "none"
        train, val, test, _ = chronological_train_validation_test_split(dataset, prof.validation_size_ratio, prof.test_size_ratio)

        if prof.use_purged_split and prof.embargo_bars > 0:
             train, _ = apply_purging_for_target_horizon(train, test, prof.embargo_bars)

        split_manifest = build_split_manifest(
             spec.symbol, timeframe, prof.name, target_col, train, val, test,
             prof.embargo_bars, prof.use_purged_split, []
        )

        # 8. Metadata
        metadata = build_dataset_metadata(
             spec.symbol, timeframe, prof.name, dataset, list(X.columns), list(y.columns),
             list(prof.feature_sets), audit, quality
        )

        # 9. Save
        if save:
             if self.settings.ml_save_feature_matrix:
                  self.data_lake.save_ml_feature_matrix(spec.symbol, timeframe, prof.name, X)
             if self.settings.ml_save_target_frame:
                  self.data_lake.save_ml_target_frame(spec.symbol, timeframe, prof.name, y)
             if self.settings.ml_save_supervised_dataset:
                  self.data_lake.save_ml_supervised_dataset(spec.symbol, timeframe, prof.name, dataset)

             self.data_lake.save_ml_split_manifest(spec.symbol, timeframe, prof.name, split_manifest_to_dict(split_manifest))
             self.data_lake.save_ml_dataset_metadata(spec.symbol, timeframe, prof.name, dataset_metadata_to_dict(metadata))
             self.data_lake.save_ml_dataset_quality(spec.symbol, timeframe, prof.name, quality)

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "profile": prof.name,
            "dataset_id": metadata.dataset_id,
            "row_count": len(dataset),
            "feature_count": len(X.columns),
            "target_count": len(y.columns),
            "missing_feature_sets": f_summary.get("missing_feature_sets", []),
            "leakage_audit": audit,
            "quality_report": quality,
            "split_manifest": split_manifest_to_dict(split_manifest),
            "metadata": dataset_metadata_to_dict(metadata),
            "warnings": f_summary.get("warnings", []) + t_summary.get("warnings", []) + d_summary.get("warnings", [])
        }

        return dataset, summary

    def build_for_universe(
        self,
        specs: list[SymbolSpec],
        timeframe: str = "1d",
        profile: MLDatasetProfile | None = None,
        limit: int | None = None,
        save: bool = True,
    ) -> dict:

        prof = profile or self.profile
        results = []
        count = 0

        for spec in specs:
            if limit and count >= limit:
                break

            if spec.asset_class == 'synthetic' or spec.asset_class == 'macro' or spec.benchmark_enabled:
                continue

            logger.info(f"Building ML dataset for {spec.symbol} {timeframe}")
            try:
                _, summary = self.build_for_symbol_timeframe(spec, timeframe, prof, save)

                # Status logic
                status = "dataset_ready_candidate"
                if not summary.get("quality_report", {}).get("passed", False):
                     status = "dataset_warning_candidate"
                if not summary.get("leakage_audit", {}).get("passed", False):
                     status = "leakage_risk_high"

                results.append({
                    "symbol": spec.symbol,
                    "asset_class": spec.asset_class,
                    "row_count": summary.get("row_count", 0),
                    "feature_count": summary.get("feature_count", 0),
                    "target_count": summary.get("target_count", 0),
                    "leakage_audit_passed": summary.get("leakage_audit", {}).get("passed", False),
                    "quality_passed": summary.get("quality_report", {}).get("passed", False),
                    "missing_feature_sets_count": len(summary.get("missing_feature_sets", [])),
                    "dataset_status": status
                })
                count += 1
            except Exception as e:
                logger.error(f"Failed to build dataset for {spec.symbol}: {e}")

        return {
            "processed": count,
            "results": results
        }
