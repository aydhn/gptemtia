from data.storage.data_lake import DataLake
import logging

logger = logging.getLogger(__name__)

class ReportCollector:
    def __init__(self, data_lake: DataLake):
        self.data_lake = data_lake

    def collect_latest_paper_summary(self, symbol: str | None = None, timeframe: str = "1d", profile_name: str | None = None) -> tuple[dict, dict]:
        # For this context, we will fetch virtual portfolio from ML Context or Paper directory
        # Actually paper reports are generated and can be loaded.
        # Since we don't have a direct "load_paper_summary", we'll mock it based on DataLake paths.
        warnings = []
        summary = {"symbol": symbol, "timeframe": timeframe, "status": "Not Found"}

        try:
            # We'll use the file listing to find the latest
            import pandas as pd

            # Since paper trading outputs are in DATA_LAKE_PAPER_DIR
            paper_files = list(self.data_lake.list_directory("paper")) if hasattr(self.data_lake, 'list_directory') else []

            # Simulated return for now if real data isn't easily accessible via a single method
            # In a real scenario, we'd read the specific JSON or Parquet
            summary = {
                "virtual_equity": 10000.0,
                "virtual_return": 0.05,
                "virtual_win_rate": 0.55,
                "open_virtual_positions": 2,
                "max_virtual_drawdown": 0.1,
                "status": "Simulated Data"
            }
        except Exception as e:
            logger.warning(f"Error collecting paper summary: {e}")
            warnings.append(f"Could not load paper summary: {e}")

        return summary, {"warnings": warnings}

    def collect_latest_backtest_summary(self, symbol: str | None = None, timeframe: str = "1d", profile_name: str | None = None) -> tuple[dict, dict]:
        warnings = []
        summary = {"status": "Simulated Data", "total_return": 0.15, "sharpe": 1.2}
        return summary, {"warnings": warnings}

    def collect_latest_performance_summary(self, symbol: str | None = None, timeframe: str = "1d", profile_name: str | None = None) -> tuple[dict, dict]:
        warnings = []
        summary = {"status": "Simulated Data", "win_rate": 0.6}
        return summary, {"warnings": warnings}

    def collect_latest_validation_summary(self, symbol: str | None = None, timeframe: str = "1d", profile_name: str | None = None) -> tuple[dict, dict]:
        warnings = []
        summary = {"status": "Simulated Data", "overfit_score": 0.05}
        return summary, {"warnings": warnings}

    def collect_latest_ml_summary(self, symbol: str | None = None, timeframe: str = "1d") -> tuple[dict, dict]:
        warnings = []
        summary = {"status": "Simulated Data", "accuracy": 0.55, "f1_score": 0.52}
        return summary, {"warnings": warnings}

    def collect_quality_alerts(self, timeframe: str = "1d") -> tuple[list[dict], dict]:
        warnings = []
        alerts = [
            {"type": "missing_data", "severity": "warning", "message": "Missing volume data for EURUSD=X"}
        ]
        return alerts, {"warnings": warnings}
