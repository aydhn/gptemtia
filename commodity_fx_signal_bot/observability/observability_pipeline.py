"""
Master observability runner to orchestrate the generation of reports.
"""

from typing import Dict, Any, Tuple, List, Optional
import pandas as pd

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile, get_default_observability_profile
from observability.health_checks import build_system_health_report, check_config_health, check_paths_health, check_data_lake_health, check_disk_space_health, check_python_environment_health
from observability.component_health import ComponentHealthChecker
from observability.data_freshness import build_data_freshness_report
from observability.artifact_integrity import build_artifact_integrity_report
from observability.runtime_metrics import global_metrics_collector
from observability.self_diagnostics import SelfDiagnosticsRunner


class ObservabilityPipeline:
    """Orchestrates health and observability checks, then logs or saves them."""

    def __init__(
        self,
        data_lake: DataLake,
        settings: Settings,
        profile: Optional[ObservabilityProfile] = None,
    ):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_observability_profile()

    def run_system_healthcheck(self, save: bool = True) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run and return the basic system healthcheck."""
        ch_config = check_config_health(self.settings)
        ch_paths = check_paths_health(self.data_lake.paths)
        ch_lake = check_data_lake_health(self.data_lake)
        ch_disk = check_disk_space_health(self.data_lake.paths.DATA_DIR, self.profile.min_required_disk_free_mb)
        ch_py = check_python_environment_health()

        checks = [ch_config, ch_paths, ch_lake, ch_disk, ch_py]

        df, summary = build_system_health_report(checks)

        if save and self.profile.healthcheck_enabled:
            # Save capabilities will be hooked up later through DataLake changes
            if hasattr(self.data_lake, "save_observability_health_report"):
                self.data_lake.save_observability_health_report("system_healthcheck", df, summary)

        return df, summary

    def run_component_healthcheck(
        self,
        symbols: Optional[List[SymbolSpec]] = None,
        timeframe: str = "1d",
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run and return the component-level healthcheck."""
        if limit and symbols:
            symbols = symbols[:limit]

        ch = ComponentHealthChecker(self.data_lake, self.settings, self.profile)
        df, summary = ch.check_all_components(symbols, timeframe)

        if save and self.profile.healthcheck_enabled:
            if hasattr(self.data_lake, "save_observability_health_report"):
                self.data_lake.save_observability_health_report("component_healthcheck", df, summary)

        return df, summary

    def run_data_freshness_check(
        self,
        symbols: Optional[List[SymbolSpec]] = None,
        timeframe: str = "1d",
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run and return the data freshness check."""
        df, summary = build_data_freshness_report(self.data_lake, symbols, timeframe, self.profile.max_stale_hours_daily)

        if save and self.profile.data_freshness_enabled:
            if hasattr(self.data_lake, "save_data_freshness_report"):
                self.data_lake.save_data_freshness_report(df, summary)

        return df, summary

    def run_artifact_integrity_check(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Run and return the artifact integrity check."""
        df, summary = build_artifact_integrity_report(self.data_lake)

        if save and self.profile.artifact_integrity_enabled:
            if hasattr(self.data_lake, "save_artifact_integrity_report"):
                self.data_lake.save_artifact_integrity_report(df, summary)

        return df, summary

    def run_runtime_metrics_report(
        self,
        save: bool = True,
    ) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Extract current runtime metrics into a report."""
        df = global_metrics_collector.to_dataframe()
        summary = global_metrics_collector.summarize()

        if save and self.profile.runtime_metrics_enabled:
            if hasattr(self.data_lake, "save_runtime_metrics"):
                self.data_lake.save_runtime_metrics("current_session", df, summary)

        return df, summary

    def run_self_diagnostics(
        self,
        symbols: Optional[List[SymbolSpec]] = None,
        timeframe: str = "1d",
        limit: Optional[int] = None,
        save: bool = True,
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Run the overarching self-diagnostics report."""
        sd = SelfDiagnosticsRunner(self.data_lake, self.settings, self.profile)
        details, summary = sd.run_universe_diagnostics(specs=symbols or [], timeframe=timeframe, limit=limit)

        if save and self.profile.healthcheck_enabled:
            if hasattr(self.data_lake, "save_diagnostics_report"):
                self.data_lake.save_diagnostics_report("self_diagnostics", summary)

        return details, summary
