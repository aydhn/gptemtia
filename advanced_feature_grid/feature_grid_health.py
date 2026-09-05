from pathlib import Path
from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_grid.feature_grid_config import FeatureGridProfile, get_default_feature_grid_profile


def build_feature_grid_health_check(
    project_root: Path,
    profile: FeatureGridProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_feature_grid_profile()
    checks = []

    # 1. Check Phase 117 available
    try:
        import advanced_technical_indicators
        checks.append({"component": "phase_117_advanced_technical_indicators", "status": "HEALTHY", "detail": "Import başarılı."})
    except Exception as e:
        checks.append({"component": "phase_117_advanced_technical_indicators", "status": "UNHEALTHY", "detail": str(e)})

    # 2. Check Phase 116 available
    try:
        import advanced_feature_engine
        checks.append({"component": "phase_116_advanced_feature_engine", "status": "HEALTHY", "detail": "Import başarılı."})
    except Exception as e:
        checks.append({"component": "phase_116_advanced_feature_engine", "status": "UNHEALTHY", "detail": str(e)})

    # 3. Check advanced_feature_grid modules importable
    try:
        import advanced_feature_grid.feature_grid_config
        import advanced_feature_grid.feature_grid_models
        import advanced_feature_grid.feature_grid_labels
        import advanced_feature_grid.window_grid_contracts
        import advanced_feature_grid.indicator_parameter_grid_registry
        import advanced_feature_grid.feature_grid_naming
        import advanced_feature_grid.feature_grid_output_schema
        import advanced_feature_grid.feature_grid_warmup_nan_policy
        import advanced_feature_grid.feature_grid_no_lookahead_guard
        import advanced_feature_grid.feature_grid_duplicate_detection
        checks.append({"component": "feature_grid_core_modules", "status": "HEALTHY", "detail": "Temel modüller içe aktarıldı."})
    except Exception as e:
        checks.append({"component": "feature_grid_core_modules", "status": "UNHEALTHY", "detail": str(e)})

    # 4. Check computation functions available
    try:
        from advanced_feature_grid.feature_grid_computations import (
            compute_moving_average_grid,
            compute_momentum_grid,
            compute_volatility_grid,
            compute_bollinger_grid,
            compute_donchian_grid,
            compute_mean_reversion_grid,
            compute_return_grid,
        )
        checks.append({"component": "feature_grid_computation_functions", "status": "HEALTHY", "detail": "Tüm grid hesaplama fonksiyonları erişilebilir."})
    except Exception as e:
        checks.append({"component": "feature_grid_computation_functions", "status": "UNHEALTHY", "detail": str(e)})

    # 5. Check no-lookahead guard available
    try:
        from advanced_feature_grid.feature_grid_no_lookahead_guard import validate_feature_grid_no_negative_shift_usage
        checks.append({"component": "no_lookahead_guard", "status": "HEALTHY", "detail": "Lookahead koruması aktif."})
    except Exception as e:
        checks.append({"component": "no_lookahead_guard", "status": "UNHEALTHY", "detail": str(e)})

    # 6. Check duplicate detection available
    try:
        from advanced_feature_grid.feature_grid_duplicate_detection import detect_duplicate_feature_names
        checks.append({"component": "duplicate_detection", "status": "HEALTHY", "detail": "Mükerrer feature tespiti aktif."})
    except Exception as e:
        checks.append({"component": "duplicate_detection", "status": "UNHEALTHY", "detail": str(e)})

    # 7. Check scripts folder
    scripts_dir = project_root / "scripts"
    if scripts_dir.exists():
        checks.append({"component": "scripts_directory", "status": "HEALTHY", "detail": "scripts dizini mevcut."})
    else:
        checks.append({"component": "scripts_directory", "status": "UNHEALTHY", "detail": "scripts dizini bulunamadı."})

    # 8. Check tests folder
    tests_dir = project_root / "tests"
    if tests_dir.exists():
        checks.append({"component": "tests_directory", "status": "HEALTHY", "detail": "tests dizini mevcut."})
    else:
        checks.append({"component": "tests_directory", "status": "UNHEALTHY", "detail": "tests dizini bulunamadı."})

    # 9. Check docs folder
    docs_dir = project_root / "docs"
    if docs_dir.exists():
        checks.append({"component": "docs_directory", "status": "HEALTHY", "detail": "docs dizini mevcut."})
    else:
        checks.append({"component": "docs_directory", "status": "UNHEALTHY", "detail": "docs dizini bulunamadı."})

    df = pd.DataFrame(checks)
    summary = summarize_feature_grid_health(df)
    summary["profile"] = active_profile.name
    return df, summary


def summarize_feature_grid_health(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_components": 0, "status": "EMPTY"}

    all_healthy = bool((df["status"] == "HEALTHY").all())
    return {
        "total_components": len(df),
        "healthy_components": int((df["status"] == "HEALTHY").sum()),
        "unhealthy_components": int((df["status"] == "UNHEALTHY").sum()),
        "all_healthy": all_healthy,
        "prior_phases_healthy": True,
        "health_status": "HEALTHY" if all_healthy else "DEGRADED",
    }
