"""
Component-level health checking.
"""

from typing import Dict, Any, Tuple, List, Optional

import pandas as pd

from config.settings import Settings
from config.symbols import SymbolSpec
from data.storage.data_lake import DataLake
from observability.observability_config import ObservabilityProfile
from observability.observability_models import ComponentHealth


class ComponentHealthChecker:
    """Checks the health of specific system components."""

    def __init__(self, data_lake: DataLake, settings: Settings, profile: ObservabilityProfile):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile

    def _check_ml_component(self) -> ComponentHealth:
        """Check ML component basic health."""
        checks_passed = 0
        checks_failed = 0
        warnings = []
        errors = []

        # Check if directories exist
        ml_dir = self.data_lake.paths.LAKE_DIR / "ml"
        if not ml_dir.exists():
            warnings.append("ML directory is missing")
            checks_failed += 1
        else:
            checks_passed += 1

            # Check for models or registry
            models_dir = ml_dir / "models"
            if models_dir.exists() and any(models_dir.iterdir()):
                checks_passed += 1
            else:
                warnings.append("No ML models found")

        status = "healthy"
        health_score = 1.0
        if checks_failed > 0:
            status = "degraded"
            health_score = 0.7

        return ComponentHealth(
            component="ml_pipeline",
            status=status,
            health_score=health_score,
            checks_passed=checks_passed,
            checks_failed=checks_failed,
            warnings=warnings,
            errors=errors
        )

    def _check_paper_component(self) -> ComponentHealth:
        """Check Paper trading component basic health."""
        checks_passed = 0
        checks_failed = 0
        warnings = []
        errors = []

        paper_dir = self.data_lake.paths.LAKE_DIR / "paper"
        if not paper_dir.exists():
            warnings.append("Paper directory is missing")
            checks_failed += 1
        else:
            checks_passed += 1

            portfolios_dir = paper_dir / "portfolios"
            if portfolios_dir.exists() and any(portfolios_dir.iterdir()):
                checks_passed += 1
            else:
                warnings.append("No paper portfolios found")

        status = "healthy"
        health_score = 1.0
        if checks_failed > 0:
            status = "degraded"
            health_score = 0.7

        return ComponentHealth(
            component="paper_pipeline",
            status=status,
            health_score=health_score,
            checks_passed=checks_passed,
            checks_failed=checks_failed,
            warnings=warnings,
            errors=errors
        )

    def _check_notification_component(self) -> ComponentHealth:
        """Check Notification component basic health."""
        checks_passed = 0
        checks_failed = 0
        warnings = []
        errors = []

        if not self.settings.telegram_bot_token:
            warnings.append("Telegram token not configured")
            checks_failed += 1
        else:
            checks_passed += 1

        # Check delivery logs
        delivery_logs = self.data_lake.paths.LAKE_DIR / "notifications" / "delivery_logs"
        if delivery_logs.exists() and any(delivery_logs.iterdir()):
            checks_passed += 1
        else:
            # Not strictly a failure, maybe just hasn't run yet
            warnings.append("No notification delivery logs found")

        status = "healthy"
        health_score = 1.0
        if checks_failed > 0:
            status = "degraded"
            health_score = 0.5

        return ComponentHealth(
            component="notification_pipeline",
            status=status,
            health_score=health_score,
            checks_passed=checks_passed,
            checks_failed=checks_failed,
            warnings=warnings,
            errors=errors
        )

    def check_component(self, component: str, symbol: Optional[str] = None, timeframe: str = "1d") -> ComponentHealth:
        """Check the health of a specific component by name."""
        # This is a simplified dispatcher for components
        if component == "ml_pipeline":
            return self._check_ml_component()
        elif component == "paper_pipeline":
            return self._check_paper_component()
        elif component == "notification_pipeline":
            return self._check_notification_component()

        # Fallback generic check
        return ComponentHealth(
            component=component,
            status="unknown",
            health_score=0.5,
            checks_passed=0,
            checks_failed=0,
            warnings=[f"Specific health check not implemented for {component}"],
            errors=[]
        )

    def check_all_components(self, symbols: Optional[List[SymbolSpec]] = None, timeframe: str = "1d") -> Tuple[pd.DataFrame, Dict[str, Any]]:
        """Check all registered components and return a summary report."""
        components = ["ml_pipeline", "paper_pipeline", "notification_pipeline", "orchestration_pipeline"]

        healths = [self.check_component(c, None, timeframe) for c in components]

        dicts = []
        for ch in healths:
            dicts.append({
                "component": ch.component,
                "status": ch.status,
                "health_score": ch.health_score,
                "checks_passed": ch.checks_passed,
                "checks_failed": ch.checks_failed,
                "warnings_count": len(ch.warnings),
                "errors_count": len(ch.errors),
            })

        df = pd.DataFrame(dicts)

        avg_score = df["health_score"].mean() if not df.empty else 0.0
        overall_status = "healthy"
        if "critical" in df["status"].values:
            overall_status = "critical"
        elif "unhealthy" in df["status"].values:
            overall_status = "unhealthy"
        elif "degraded" in df["status"].values:
            overall_status = "degraded"

        summary = {
            "overall_status": overall_status,
            "overall_score": float(avg_score),
            "components_checked": len(components),
            "critical_components": int((df["status"] == "critical").sum()),
            "unhealthy_components": int((df["status"] == "unhealthy").sum()),
            "degraded_components": int((df["status"] == "degraded").sum()),
            "healthy_components": int((df["status"] == "healthy").sum()),
        }

        return df, summary
