"""
Dependency diagnostics for checking pipeline dependencies.
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Tuple

import pandas as pd

from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake


class DependencyDiagnostics:
    """Checks for the presence and basic validity of required pipeline inputs."""

    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def _check_file_dependency(self, path: Path, dependency_name: str, required_for: str) -> Dict[str, Any]:
        """Check a single file dependency."""
        exists = path.exists()

        status = "available" if exists else "missing"
        warnings = []
        if not exists:
            warnings.append(f"Required dependency missing: {path.name}")

        modified_time = None
        row_count = None

        if exists:
            try:
                modified_time = datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                # Basic row count check for parquet
                if path.suffix == '.parquet':
                    # Avoid loading full dataframe just for row count if possible, but fallback to it
                    try:
                        import pyarrow.parquet as pq
                        row_count = pq.read_metadata(path).num_rows
                    except Exception:
                        df = pd.read_parquet(path)
                        row_count = len(df)
                elif path.suffix == '.csv':
                    df = pd.read_csv(path)
                    row_count = len(df)

                if row_count == 0:
                    status = "empty"
                    warnings.append(f"Dependency file is empty: {path.name}")
            except Exception as e:
                status = "error"
                warnings.append(f"Failed to read dependency metadata: {str(e)}")

        return {
            "dependency_name": dependency_name,
            "required_for": required_for,
            "available": exists,
            "status": status,
            "path": str(path),
            "row_count": row_count,
            "modified_time": modified_time,
            "warnings": warnings
        }

    def check_feature_dependencies(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check dependencies required to build features (e.g., OHLCV data)."""
        rows = []

        # Require processed OHLCV data
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)
        ohlcv_path = self.data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / timeframe / f"{safe_symbol}.parquet"

        rows.append(self._check_file_dependency(ohlcv_path, "processed_ohlcv", "feature_pipeline"))

        df = pd.DataFrame(rows)
        summary = {"pipeline": "feature_pipeline", "total_dependencies": len(rows), "missing": sum(not r['available'] for r in rows)}
        return df, summary

    def check_candidate_dependencies(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check dependencies required to build candidates."""
        rows = []

        # We need the feature sets
        feature_sets = ['technical', 'momentum', 'volatility', 'trend', 'volume', 'price_action', 'divergence', 'mtf', 'regime']
        for fs in feature_sets:
            path = self.data_lake.paths.LAKE_FEATURES_DIR / fs / timeframe / f"{DataLake.safe_symbol_name(spec.symbol)}.parquet"
            rows.append(self._check_file_dependency(path, f"{fs}_features", "candidate_pipeline"))

        df = pd.DataFrame(rows)
        summary = {"pipeline": "candidate_pipeline", "total_dependencies": len(rows), "missing": sum(not r['available'] for r in rows)}
        return df, summary

    def check_backtest_dependencies(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check dependencies required to run backtests."""
        rows = []
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)

        # Require processed OHLCV and strategy pool
        ohlcv_path = self.data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(ohlcv_path, "processed_ohlcv", "backtest_pipeline"))

        strategy_path = self.data_lake.paths.LAKE_DIR / "strategy_candidates" / "pool" / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(strategy_path, "strategy_pool", "backtest_pipeline"))

        df = pd.DataFrame(rows)
        summary = {"pipeline": "backtest_pipeline", "total_dependencies": len(rows), "missing": sum(not r['available'] for r in rows)}
        return df, summary

    def check_ml_dependencies(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check dependencies required for ML training/prediction."""
        rows = []
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)

        # Training needs feature sets + processed OHLCV for targets
        ohlcv_path = self.data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(ohlcv_path, "processed_ohlcv", "ml_pipeline"))

        # E.g., a combined feature dataset is usually built first
        dataset_path = self.data_lake.paths.LAKE_DIR / "ml" / "datasets" / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(dataset_path, "ml_dataset", "ml_pipeline"))

        df = pd.DataFrame(rows)
        summary = {"pipeline": "ml_pipeline", "total_dependencies": len(rows), "missing": sum(not r['available'] for r in rows)}
        return df, summary

    def check_paper_dependencies(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check dependencies required for paper trading."""
        rows = []
        safe_symbol = DataLake.safe_symbol_name(spec.symbol)

        # Paper needs latest strategy candidates and current price
        strategy_path = self.data_lake.paths.LAKE_DIR / "strategy_candidates" / "pool" / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(strategy_path, "strategy_pool", "paper_pipeline"))

        ohlcv_path = self.data_lake.paths.LAKE_PROCESSED_OHLCV_DIR / timeframe / f"{safe_symbol}.parquet"
        rows.append(self._check_file_dependency(ohlcv_path, "processed_ohlcv", "paper_pipeline"))

        df = pd.DataFrame(rows)
        summary = {"pipeline": "paper_pipeline", "total_dependencies": len(rows), "missing": sum(not r['available'] for r in rows)}
        return df, summary

    def build_full_dependency_diagnostics(self, spec: SymbolSpec, timeframe: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Build a comprehensive dependency diagnostics report for a symbol."""
        dfs = []

        f_df, _ = self.check_feature_dependencies(spec, timeframe)
        dfs.append(f_df)

        c_df, _ = self.check_candidate_dependencies(spec, timeframe)
        dfs.append(c_df)

        b_df, _ = self.check_backtest_dependencies(spec, timeframe)
        dfs.append(b_df)

        m_df, _ = self.check_ml_dependencies(spec, timeframe)
        dfs.append(m_df)

        p_df, _ = self.check_paper_dependencies(spec, timeframe)
        dfs.append(p_df)

        full_df = pd.concat(dfs, ignore_index=True)
        # Drop exact duplicates if multiple pipelines require the same file
        full_df = full_df.drop_duplicates(subset=["dependency_name", "path"])

        total = len(full_df)
        missing = int(sum(~full_df['available']))

        summary = {
            "symbol": spec.symbol,
            "timeframe": timeframe,
            "total_dependencies": total,
            "missing_dependencies": missing,
            "status": "healthy" if missing == 0 else "degraded"
        }

        return full_df, summary
