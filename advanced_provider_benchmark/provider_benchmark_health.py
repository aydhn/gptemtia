from pathlib import Path
from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_provider_benchmark.provider_benchmark_config import ProviderBenchmarkProfile


def build_provider_benchmark_health_check(
    project_root: Path,
    profile: ProviderBenchmarkProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    checks: List[Dict[str, Any]] = []

    # 1. Upstream modules availability (Phase 106 - 114)
    upstream_pkgs = [
        ("advanced_data_providers", 106),
        ("advanced_fx_providers", 107),
        ("advanced_commodity_providers", 108),
        ("advanced_macro_providers", 109),
        ("advanced_economic_calendar", 110),
        ("advanced_news_metadata", 111),
        ("advanced_data_quality", 112),
        ("advanced_data_normalization", 113),
        ("advanced_data_lineage", 114),
    ]
    for pkg_name, phase_num in upstream_pkgs:
        pkg_dir = project_root / pkg_name
        is_avail = pkg_dir.exists() and (pkg_dir / "__init__.py").exists()
        checks.append({
            "check_category": "upstream_layer",
            "component": pkg_name,
            "phase": phase_num,
            "status": "PASS" if is_avail else "FAIL",
            "detail": f"Phase {phase_num} upstream layer package is present" if is_avail else "Missing package directory",
        })

    # 2. Phase 115 core modules
    core_modules = [
        "provider_benchmark_config",
        "provider_benchmark_labels",
        "provider_benchmark_models",
        "provider_benchmark_profile_registry",
        "provider_benchmark_domain_registry",
        "provider_benchmark_metric_registry",
        "provider_benchmark_weight_registry",
        "provider_coverage_benchmark",
        "provider_capability_benchmark",
        "provider_quality_benchmark",
        "provider_normalization_benchmark",
        "provider_traceability_benchmark",
        "provider_license_provenance_benchmark",
        "provider_no_scraping_compliance",
        "provider_metadata_only_compliance",
        "provider_manual_review_benchmark",
        "fx_provider_benchmark",
        "commodity_provider_benchmark",
        "macro_provider_benchmark",
        "calendar_provider_benchmark",
        "news_metadata_provider_benchmark",
        "cross_domain_provider_benchmark",
        "provider_benchmark_scoring",
        "provider_ranking_research",
        "provider_benchmark_findings",
        "provider_benchmark_manual_review_queue",
        "provider_benchmark_report_builder",
        "provider_benchmark_pipeline",
        "provider_benchmark_health",
        "provider_benchmark_validation",
        "provider_benchmark_safety_boundary",
        "phase_116_handoff",
    ]
    benchmark_dir = project_root / "advanced_provider_benchmark"
    for mod in core_modules:
        mod_file = benchmark_dir / f"{mod}.py"
        is_avail = mod_file.exists()
        checks.append({
            "check_category": "phase_115_core_module",
            "component": mod,
            "phase": 115,
            "status": "PASS" if is_avail else "FAIL",
            "detail": f"Module {mod}.py exists" if is_avail else "Module missing",
        })

    # 3. Output directories
    req_dirs = [
        project_root / "data" / "lake" / "advanced_provider_benchmark",
        project_root / "reports" / "output" / "advanced_provider_benchmark",
        project_root / "docs" / "generated" / "advanced_provider_benchmark",
    ]
    for d in req_dirs:
        is_avail = d.exists()
        checks.append({
            "check_category": "directory_structure",
            "component": str(d.name),
            "phase": 115,
            "status": "PASS" if is_avail else "FAIL",
            "detail": f"Directory {d.relative_to(project_root)} exists" if is_avail else "Directory missing",
        })

    df = pd.DataFrame.from_records(checks)
    summary = summarize_provider_benchmark_health(df)
    return df, summary


def summarize_provider_benchmark_health(df: pd.DataFrame) -> Dict[str, Any]:
    total = len(df)
    passed = int((df["status"] == "PASS").sum()) if not df.empty and "status" in df.columns else 0
    failed = total - passed
    return {
        "overall_status": "PASS" if failed == 0 else "FAIL",
        "total_checks": total,
        "passed_checks": passed,
        "failed_checks": failed,
        "current_phase": 115,
        "target_final_phase": 160,
    }
