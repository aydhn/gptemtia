"""
System-level health checks for core infrastructure.
"""

import importlib.util
import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any, Optional

import pandas as pd

from config.settings import Settings
from config.paths import ProjectPaths
from data.storage.data_lake import DataLake
from observability.observability_models import ComponentHealth


def check_config_health(settings: Settings) -> ComponentHealth:
    """Check the health of the system configuration."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    # Check if essential settings are present
    if settings.base_currency:
        checks_passed += 1
    else:
        checks_failed += 1
        errors.append("base_currency is missing")

    # Ensure secrets are not explicitly printed or exposed directly
    if hasattr(settings, "telegram_bot_token") and settings.telegram_bot_token:
        if settings.telegram_bot_token == "YOUR_TELEGRAM_BOT_TOKEN":
            warnings.append("Telegram bot token is using placeholder value.")
        checks_passed += 1

    status = "healthy"
    health_score = 1.0
    if checks_failed > 0:
        status = "unhealthy"
        health_score = max(0.0, 1.0 - (checks_failed * 0.5))
    elif warnings:
        status = "degraded"
        health_score = 0.9

    return ComponentHealth(
        component="config",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        warnings=warnings,
        errors=errors,
        metadata={"environment": settings.environment}
    )


def check_paths_health(paths_module_or_dict: Optional[Any] = None) -> ComponentHealth:
    """Check if critical directories exist or can be created."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    paths_to_check = []

    if paths_module_or_dict is None:
        from config.paths import ProjectPaths
        paths_to_check = [
            ProjectPaths().DATA_DIR,
            ProjectPaths().LOGS_DIR,
            ProjectPaths().REPORTS_DIR,
            ProjectPaths().LAKE_DIR
        ]
    else:
        # Simplistic approach if we pass a custom obj
        paths_to_check = [
            getattr(paths_module_or_dict, "DATA_DIR", Path("data")),
            getattr(paths_module_or_dict, "LAKE_DIR", Path("data/lake"))
        ]

    for p in paths_to_check:
        if p.exists() and p.is_dir():
            checks_passed += 1
        else:
            try:
                p.mkdir(parents=True, exist_ok=True)
                checks_passed += 1
                warnings.append(f"Directory created during check: {p}")
            except Exception as e:
                checks_failed += 1
                errors.append(f"Failed to access or create directory {p}: {str(e)}")

    status = "healthy"
    health_score = 1.0
    if checks_failed > 0:
        status = "critical"
        health_score = 0.0
    elif warnings:
        status = "degraded"
        health_score = 0.95

    return ComponentHealth(
        component="paths",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        warnings=warnings,
        errors=errors
    )


def check_data_lake_health(data_lake: DataLake) -> ComponentHealth:
    """Check the health of the Data Lake structure."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    if data_lake.root_dir.exists():
        checks_passed += 1
    else:
        checks_failed += 1
        errors.append(f"DataLake root dir missing: {data_lake.root_dir}")

    if hasattr(data_lake, "ohlcv_dir") and data_lake.ohlcv_dir.exists():
        checks_passed += 1
    else:
        warnings.append("DataLake OHLCV dir missing")

    status = "healthy"
    health_score = 1.0
    if checks_failed > 0:
        status = "unhealthy"
        health_score = 0.0
    elif warnings:
        status = "degraded"
        health_score = 0.8

    return ComponentHealth(
        component="data_lake",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        warnings=warnings,
        errors=errors
    )


def check_python_environment_health() -> ComponentHealth:
    """Check Python version and essential installed packages."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    # Check Python version (e.g., requires >= 3.10)
    version_info = sys.version_info
    if version_info.major == 3 and version_info.minor >= 10:
        checks_passed += 1
    else:
        checks_failed += 1
        errors.append(f"Python version {version_info.major}.{version_info.minor} is below recommended 3.10")

    # Check critical libraries
    critical_libs = ['pandas', 'numpy', 'sklearn', 'joblib', 'requests']
    for lib in critical_libs:
        if importlib.util.find_spec(lib) is not None:
            checks_passed += 1
        else:
            checks_failed += 1
            errors.append(f"Critical library missing: {lib}")

    status = "healthy"
    health_score = 1.0
    if checks_failed > 0:
        status = "critical"
        health_score = max(0.0, 1.0 - (checks_failed * 0.2))
    elif warnings:
        status = "degraded"
        health_score = 0.9

    return ComponentHealth(
        component="python_environment",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        warnings=warnings,
        errors=errors,
        metadata={"python_version": f"{version_info.major}.{version_info.minor}.{version_info.micro}"}
    )


def check_disk_space_health(path: Path, min_free_mb: int = 1024) -> ComponentHealth:
    """Check if there is sufficient disk space."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    try:
        # Ensure path exists or use parent
        check_path = path if path.exists() else path.parent
        if not check_path.exists():
            # Fallback to root or current dir
            check_path = Path(os.getcwd())

        total, used, free = shutil.disk_usage(check_path)
        free_mb = free / (1024 * 1024)

        if free_mb >= min_free_mb:
            checks_passed += 1
        else:
            checks_failed += 1
            errors.append(f"Insufficient disk space. Free: {free_mb:.1f}MB, Required: {min_free_mb}MB")

        metadata = {
            "free_mb": round(free_mb, 2),
            "total_mb": round(total / (1024 * 1024), 2),
            "used_mb": round(used / (1024 * 1024), 2)
        }
    except Exception as e:
        checks_failed += 1
        errors.append(f"Failed to check disk space: {str(e)}")
        metadata = {}

    status = "healthy"
    health_score = 1.0
    if checks_failed > 0:
        status = "critical"
        health_score = 0.0

    return ComponentHealth(
        component="disk_space",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=checks_failed,
        warnings=warnings,
        errors=errors,
        metadata=metadata
    )


def check_optional_dependencies_health() -> ComponentHealth:
    """Check optional dependencies."""
    checks_passed = 0
    checks_failed = 0
    warnings = []
    errors = []

    optional_libs = ['matplotlib', 'seaborn', 'optuna', 'xgboost', 'lightgbm']
    for lib in optional_libs:
        if importlib.util.find_spec(lib) is not None:
            checks_passed += 1
        else:
            warnings.append(f"Optional library missing: {lib}. Some features may be disabled.")

    status = "healthy"
    health_score = 1.0
    if warnings:
        status = "degraded"
        health_score = 0.8

    return ComponentHealth(
        component="optional_dependencies",
        status=status,
        health_score=health_score,
        checks_passed=checks_passed,
        checks_failed=0,
        warnings=warnings,
        errors=errors
    )


def build_system_health_report(component_healths: List[ComponentHealth]) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a unified system health report from component checks."""
    if not component_healths:
        return pd.DataFrame(), {}

    # Convert to dataframe
    dicts = []
    for ch in component_healths:
        d = {
            "component": ch.component,
            "status": ch.status,
            "health_score": ch.health_score,
            "checks_passed": ch.checks_passed,
            "checks_failed": ch.checks_failed,
            "warnings_count": len(ch.warnings),
            "errors_count": len(ch.errors),
        }
        dicts.append(d)

    df = pd.DataFrame(dicts)

    # Calculate overall metrics
    total_checks_passed = sum(ch.checks_passed for ch in component_healths)
    total_checks_failed = sum(ch.checks_failed for ch in component_healths)
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
        "total_checks_passed": total_checks_passed,
        "total_checks_failed": total_checks_failed,
        "components_checked": len(component_healths),
        "critical_components": int((df["status"] == "critical").sum()),
        "unhealthy_components": int((df["status"] == "unhealthy").sum()),
        "degraded_components": int((df["status"] == "degraded").sum()),
        "healthy_components": int((df["status"] == "healthy").sum()),
    }

    return df, summary
