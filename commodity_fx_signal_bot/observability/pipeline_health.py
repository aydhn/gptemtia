"""
Pipeline health diagnostics for ensuring pipelines produce required outputs.
"""

from typing import Dict, Any, Tuple, List
from pathlib import Path

import pandas as pd

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile


class PipelineHealthChecker:
    """Checks the health of various processing pipelines."""

    def __init__(self, data_lake: DataLake, settings: Settings, profile: ObservabilityProfile):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile

    def _check_path_exists(self, path: Path) -> bool:
        """Check if a path exists and is not empty."""
        return path.exists() and path.stat().st_size > 0

    def check_pipeline_outputs(
        self,
        pipeline_name: str,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Dict[str, Any]:
        """Check if a specific pipeline produced its expected outputs for a symbol."""
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)

        expected_paths = []
        if pipeline_name == "data":
            expected_paths.append(self.data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "features":
            expected_paths.append(self.data_lake.paths.LAKE_FEATURES_TECHNICAL_DIR / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "signals":
            expected_paths.append(self.data_lake.paths.LAKE_DIR / "signal_candidates" / "pool" / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "decisions":
            expected_paths.append(self.data_lake.paths.LAKE_DIR / "decision_candidates" / "pool" / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "strategies":
            expected_paths.append(self.data_lake.paths.LAKE_DIR / "strategy_candidates" / "pool" / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "backtest":
            expected_paths.append(self.data_lake.paths.LAKE_DIR / "backtest" / "ledgers" / timeframe / f"{safe_symbol}.parquet")
        elif pipeline_name == "paper":
            expected_paths.append(self.data_lake.paths.LAKE_DIR / "paper" / "portfolios" / f"{safe_symbol}_{timeframe}.json")

        if not expected_paths:
            return {
                "required_outputs_available": False,
                "latest_modified_time": None,
                "warnings": [f"No expected paths configured for pipeline {pipeline_name}"]
            }

        all_exist = all(self._check_path_exists(p) for p in expected_paths)

        latest_mod = None
        if all_exist:
            latest_mod = max(p.stat().st_mtime for p in expected_paths)

        return {
            "required_outputs_available": all_exist,
            "latest_modified_time": latest_mod,
            "warnings": [f"Missing expected output for {pipeline_name}"] if not all_exist else []
        }

    def check_pipeline_quality_reports(
        self,
        pipeline_name: str,
        spec: SymbolSpec,
        timeframe: str,
    ) -> Dict[str, Any]:
        """Check if quality reports exist and passed for a pipeline."""
        # This is a stub for specific quality report checks (e.g., data quality, feature quality)
        return {
            "quality_passed": True,
            "warnings": []
        }

    def build_pipeline_health_report(
        self,
        specs: List[SymbolSpec],
        timeframe: str = "1d",
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build a comprehensive pipeline health report."""
        pipelines = [
            "data", "features", "signals", "decisions", "strategies",
            "backtest", "paper"
        ]

        rows = []
        for spec in specs:
            for pl in pipelines:
                out_check = self.check_pipeline_outputs(pl, spec, timeframe)
                qual_check = self.check_pipeline_quality_reports(pl, spec, timeframe)

                avail = out_check["required_outputs_available"]
                qual = qual_check["quality_passed"]

                status = "healthy"
                score = 1.0
                if not avail:
                    status = "unhealthy"
                    score = 0.0
                elif not qual:
                    status = "degraded"
                    score = 0.5

                warnings = out_check["warnings"] + qual_check["warnings"]

                rows.append({
                    "symbol": spec.symbol,
                    "timeframe": timeframe,
                    "pipeline_name": pl,
                    "required_outputs_available": avail,
                    "quality_passed": qual,
                    "latest_modified_time": out_check["latest_modified_time"],
                    "health_status": status,
                    "health_score": score,
                    "warnings": warnings
                })

        df = pd.DataFrame(rows)

        if df.empty:
            return df, {
                "total_pipelines_checked": 0,
                "healthy_count": 0,
                "degraded_count": 0,
                "unhealthy_count": 0,
                "overall_status": "unknown"
            }

        unhealthy = int((df["health_status"] == "unhealthy").sum())
        degraded = int((df["health_status"] == "degraded").sum())
        healthy = int((df["health_status"] == "healthy").sum())

        overall = "healthy"
        if unhealthy > 0:
            overall = "unhealthy"
        elif degraded > 0:
            overall = "degraded"

        summary = {
            "total_pipelines_checked": len(df),
            "healthy_count": healthy,
            "degraded_count": degraded,
            "unhealthy_count": unhealthy,
            "overall_status": overall,
            "overall_score": float(df["health_score"].mean())
        }

        return df, summary
