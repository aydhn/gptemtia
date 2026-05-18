"""
Self-diagnostics runner to aggregate and recommend actions based on all health checks.
"""

from typing import Dict, Any, Tuple, List, Optional

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.health_checks import check_config_health, check_paths_health, check_data_lake_health, check_disk_space_health, check_python_environment_health
from observability.dependency_diagnostics import DependencyDiagnostics
from observability.data_freshness import build_data_freshness_report
from observability.artifact_integrity import build_artifact_integrity_report
from observability.pipeline_health import PipelineHealthChecker


class SelfDiagnosticsRunner:
    """Runs a suite of diagnostics and aggregates the results."""

    def __init__(self, data_lake: DataLake, settings: Settings, profile: ObservabilityProfile):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile

    def run_basic_diagnostics(self) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Run basic system health checks."""
        ch_config = check_config_health(self.settings)
        ch_paths = check_paths_health(self.data_lake.paths)
        ch_lake = check_data_lake_health(self.data_lake)
        ch_disk = check_disk_space_health(self.data_lake.paths.DATA_DIR, self.profile.min_required_disk_free_mb)
        ch_py = check_python_environment_health()

        checks = [ch_config, ch_paths, ch_lake, ch_disk, ch_py]

        summary = {
            "overall_health_score": sum(c.health_score for c in checks) / len(checks),
            "critical_count": sum(1 for c in checks if c.status == "critical"),
            "error_count": sum(len(c.errors) for c in checks),
            "warning_count": sum(len(c.warnings) for c in checks),
            "degraded_components": [c.component for c in checks if c.status == "degraded"],
            "unhealthy_components": [c.component for c in checks if c.status in ["unhealthy", "critical"]],
        }

        status = "healthy"
        if summary["critical_count"] > 0 or len(summary["unhealthy_components"]) > 0:
            status = "unhealthy"
        elif len(summary["degraded_components"]) > 0:
            status = "degraded"

        summary["overall_health_status"] = status

        return {c.component: c for c in checks}, summary

    def _generate_recommendations(self, basic_sum: Dict[str, Any], df_sum: Dict[str, Any], ai_sum: Dict[str, Any], ph_sum: Dict[str, Any]) -> List[str]:
        """Generate system-level actionable recommendations."""
        actions = []

        if basic_sum.get("overall_health_status") in ["unhealthy", "critical"]:
            actions.append("Fix basic system health issues (check config, disk space, paths).")

        if df_sum.get("missing_count", 0) > 0:
            actions.append("Eksik veriler tespit edildi. Veri indirme pipeline'ını çalıştırın (run_data_update).")

        if df_sum.get("stale_count", 0) > 0:
            actions.append("Güncelliğini yitirmiş (stale) veriler var. Veri güncelleme pipeline'ını çalıştırın.")

        if ai_sum.get("invalid_count", 0) > 0:
            actions.append("Bozuk artifact (dosya) bütünlüğü tespit edildi. Hatalı dosyaları kontrol edip silin veya yeniden üretin.")

        if ph_sum.get("unhealthy_count", 0) > 0:
            actions.append("Bazı pipeline'lar gerekli çıktıları üretememiş. Pipeline orchestration hatalarını kontrol edin.")

        if not actions:
            actions.append("Sistem sağlıklı görünüyor, özel bir aksiyon gerekmiyor.")

        return actions

    def run_universe_diagnostics(self, specs: List[SymbolSpec], timeframe: str = "1d", limit: Optional[int] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Run comprehensive diagnostics across the symbol universe."""

        if limit:
            specs = specs[:limit]

        _, basic_sum = self.run_basic_diagnostics()

        _, df_sum = build_data_freshness_report(self.data_lake, specs, timeframe, self.profile.max_stale_hours_daily)

        _, ai_sum = build_artifact_integrity_report(self.data_lake)

        ph = PipelineHealthChecker(self.data_lake, self.settings, self.profile)
        _, ph_sum = ph.build_pipeline_health_report(specs, timeframe)

        recommendations = self._generate_recommendations(basic_sum, df_sum, ai_sum, ph_sum)

        # Aggregate scores
        scores = [
            basic_sum.get("overall_health_score", 1.0),
            1.0 if df_sum.get("status") == "healthy" else 0.5,
            1.0 if ai_sum.get("status") == "healthy" else 0.0,
            ph_sum.get("overall_score", 1.0)
        ]
        avg_score = sum(scores) / len(scores)

        overall_status = "healthy"
        if avg_score < 0.5 or ai_sum.get("status") == "critical" or basic_sum.get("overall_health_status") == "critical":
            overall_status = "critical"
        elif avg_score < 0.8:
            overall_status = "degraded"

        summary = {
            "overall_health_status": overall_status,
            "overall_health_score": float(avg_score),
            "critical_count": basic_sum.get("critical_count", 0) + (1 if ai_sum.get("status") == "critical" else 0),
            "error_count": basic_sum.get("error_count", 0),
            "warning_count": basic_sum.get("warning_count", 0) + df_sum.get("stale_count", 0),
            "degraded_components": basic_sum.get("degraded_components", []),
            "unhealthy_components": basic_sum.get("unhealthy_components", []),
            "recommended_system_actions": recommendations,
            "reports_generated": ["basic_health", "data_freshness", "artifact_integrity", "pipeline_health"]
        }

        details = {
            "basic_health": basic_sum,
            "data_freshness": df_sum,
            "artifact_integrity": ai_sum,
            "pipeline_health": ph_sum
        }

        return details, summary

    def run_symbol_diagnostics(self, spec: SymbolSpec, timeframe: str = "1d") -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Run diagnostics for a single symbol."""
        return self.run_universe_diagnostics([spec], timeframe, limit=1)
