import os
from pathlib import Path
import re

def update_settings():
    settings_path = Path("commodity_fx_signal_bot/config/settings.py")
    if not settings_path.exists():
        print("commodity_fx_signal_bot/config/settings.py not found")
        return
    content = settings_path.read_text(encoding="utf-8")
    
    if "local_performance_enabled: bool" not in content:
        new_settings = """
    local_performance_enabled: bool = True
    default_local_performance_profile: str = "balanced_local_performance"
    local_performance_default_language: str = "tr"
    local_performance_dry_run_default: bool = True
    local_performance_allow_real_benchmark: bool = False
    local_performance_allow_load_test: bool = False
    local_performance_allow_stress_test: bool = False
    local_performance_allow_production_profiling: bool = False
    local_performance_allow_background_monitoring: bool = False
    local_performance_allow_cloud_cost_estimate: bool = False
    local_performance_allow_cloud_upload: bool = False
    local_performance_allow_package_publish: bool = False
    local_performance_allow_external_service: bool = False
    local_performance_allow_external_llm: bool = False
    local_performance_allow_file_modification: bool = False
    local_performance_allow_file_deletion: bool = False
    local_performance_allow_file_move: bool = False
    local_performance_allow_overwrite: bool = False
    local_performance_allow_production_capacity_claim: bool = False
    local_performance_allow_performance_certification_claim: bool = False
    local_performance_allow_live_trading_claim: bool = False
    local_performance_allow_broker_readiness_claim: bool = False
    local_performance_allow_investment_advice: bool = False
    local_performance_allow_investment_performance_claim: bool = False
    local_performance_allow_model_deployment_claim: bool = False
    local_performance_scan_source: bool = True
    local_performance_scan_docs: bool = True
    local_performance_scan_reports: bool = True
    local_performance_scan_data_lake: bool = True
    local_performance_scan_scripts: bool = True
    local_performance_scan_tests: bool = True
    local_performance_scan_generated_docs: bool = True
    local_performance_scan_simplification_outputs: bool = True
    local_performance_scan_safety_outputs: bool = True
    local_performance_default_cpu_budget_label: str = "average_local_cpu"
    local_performance_default_memory_budget_mb: int = 8192
    local_performance_default_disk_budget_mb: int = 51200
    local_performance_default_runtime_budget_minutes: int = 30
    local_performance_max_items: int = 500000
    local_performance_max_estimate_rows: int = 100000
    local_performance_min_readiness_score: float = 0.40
    local_performance_min_quality_score: float = 0.40
    local_performance_save_reports: bool = True
"""
        # Find where to insert
        pattern = r"(class Settings\(BaseSettings\):.*?)(    model_config = )"
        replacement = r"\1" + new_settings + r"\n\2"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        settings_path.write_text(content, encoding="utf-8")
        print("Updated settings.py")

def update_env():
    env_path = Path("commodity_fx_signal_bot/.env.example")
    if not env_path.exists():
        print("commodity_fx_signal_bot/.env.example not found")
        return
    content = env_path.read_text(encoding="utf-8")
    if "LOCAL_PERFORMANCE_ENABLED" not in content:
        content += """
LOCAL_PERFORMANCE_ENABLED=true
DEFAULT_LOCAL_PERFORMANCE_PROFILE=balanced_local_performance
LOCAL_PERFORMANCE_DEFAULT_LANGUAGE=tr
LOCAL_PERFORMANCE_DRY_RUN_DEFAULT=true
LOCAL_PERFORMANCE_ALLOW_REAL_BENCHMARK=false
LOCAL_PERFORMANCE_ALLOW_LOAD_TEST=false
LOCAL_PERFORMANCE_ALLOW_STRESS_TEST=false
LOCAL_PERFORMANCE_ALLOW_PRODUCTION_PROFILING=false
LOCAL_PERFORMANCE_ALLOW_BACKGROUND_MONITORING=false
LOCAL_PERFORMANCE_ALLOW_CLOUD_COST_ESTIMATE=false
LOCAL_PERFORMANCE_ALLOW_CLOUD_UPLOAD=false
LOCAL_PERFORMANCE_ALLOW_PACKAGE_PUBLISH=false
LOCAL_PERFORMANCE_ALLOW_EXTERNAL_SERVICE=false
LOCAL_PERFORMANCE_ALLOW_EXTERNAL_LLM=false
LOCAL_PERFORMANCE_ALLOW_FILE_MODIFICATION=false
LOCAL_PERFORMANCE_ALLOW_FILE_DELETION=false
LOCAL_PERFORMANCE_ALLOW_FILE_MOVE=false
LOCAL_PERFORMANCE_ALLOW_OVERWRITE=false
LOCAL_PERFORMANCE_ALLOW_PRODUCTION_CAPACITY_CLAIM=false
LOCAL_PERFORMANCE_ALLOW_PERFORMANCE_CERTIFICATION_CLAIM=false
LOCAL_PERFORMANCE_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_PERFORMANCE_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_PERFORMANCE_ALLOW_INVESTMENT_ADVICE=false
LOCAL_PERFORMANCE_ALLOW_INVESTMENT_PERFORMANCE_CLAIM=false
LOCAL_PERFORMANCE_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_PERFORMANCE_SCAN_SOURCE=true
LOCAL_PERFORMANCE_SCAN_DOCS=true
LOCAL_PERFORMANCE_SCAN_REPORTS=true
LOCAL_PERFORMANCE_SCAN_DATA_LAKE=true
LOCAL_PERFORMANCE_SCAN_SCRIPTS=true
LOCAL_PERFORMANCE_SCAN_TESTS=true
LOCAL_PERFORMANCE_SCAN_GENERATED_DOCS=true
LOCAL_PERFORMANCE_SCAN_SIMPLIFICATION_OUTPUTS=true
LOCAL_PERFORMANCE_SCAN_SAFETY_OUTPUTS=true
LOCAL_PERFORMANCE_DEFAULT_CPU_BUDGET_LABEL=average_local_cpu
LOCAL_PERFORMANCE_DEFAULT_MEMORY_BUDGET_MB=8192
LOCAL_PERFORMANCE_DEFAULT_DISK_BUDGET_MB=51200
LOCAL_PERFORMANCE_DEFAULT_RUNTIME_BUDGET_MINUTES=30
LOCAL_PERFORMANCE_MAX_ITEMS=500000
LOCAL_PERFORMANCE_MAX_ESTIMATE_ROWS=100000
LOCAL_PERFORMANCE_MIN_READINESS_SCORE=0.40
LOCAL_PERFORMANCE_MIN_QUALITY_SCORE=0.40
LOCAL_PERFORMANCE_SAVE_REPORTS=true
"""
        env_path.write_text(content, encoding="utf-8")
        print("Updated commodity_fx_signal_bot/.env.example")

def update_paths():
    paths_path = Path("commodity_fx_signal_bot/config/paths.py")
    if not paths_path.exists():
        print("commodity_fx_signal_bot/config/paths.py not found")
        return
    content = paths_path.read_text(encoding="utf-8")
    if "LAKE_LOCAL_PERFORMANCE" not in content:
        paths_to_add = """
    LAKE_LOCAL_PERFORMANCE = DATA_LAKE_DIR / "local_performance"
    LAKE_LOCAL_PERFORMANCE_PROFILES = LAKE_LOCAL_PERFORMANCE / "profiles"
    LAKE_LOCAL_PERFORMANCE_DOMAINS = LAKE_LOCAL_PERFORMANCE / "domains"
    LAKE_LOCAL_PERFORMANCE_BUDGET = LAKE_LOCAL_PERFORMANCE / "budget"
    LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE = LAKE_LOCAL_PERFORMANCE / "runtime_profile"
    LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT = LAKE_LOCAL_PERFORMANCE / "resource_footprint"
    LAKE_LOCAL_PERFORMANCE_CPU = LAKE_LOCAL_PERFORMANCE / "cpu"
    LAKE_LOCAL_PERFORMANCE_MEMORY = LAKE_LOCAL_PERFORMANCE / "memory"
    LAKE_LOCAL_PERFORMANCE_DISK = LAKE_LOCAL_PERFORMANCE / "disk"
    LAKE_LOCAL_PERFORMANCE_GROWTH = LAKE_LOCAL_PERFORMANCE / "growth"
    LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME = LAKE_LOCAL_PERFORMANCE / "script_runtime"
    LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME = LAKE_LOCAL_PERFORMANCE / "test_runtime"
    LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME = LAKE_LOCAL_PERFORMANCE / "pipeline_runtime"
    LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST = LAKE_LOCAL_PERFORMANCE / "maintenance_cost"
    LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT = LAKE_LOCAL_PERFORMANCE / "maintenance_effort"
    LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME = LAKE_LOCAL_PERFORMANCE / "operator_time"
    LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY = LAKE_LOCAL_PERFORMANCE / "machine_suitability"
    LAKE_LOCAL_PERFORMANCE_EFFICIENCY = LAKE_LOCAL_PERFORMANCE / "efficiency"
    LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE = LAKE_LOCAL_PERFORMANCE / "lightweight_mode"
    LAKE_LOCAL_PERFORMANCE_WARNINGS = LAKE_LOCAL_PERFORMANCE / "warnings"
    LAKE_LOCAL_PERFORMANCE_RETENTION = LAKE_LOCAL_PERFORMANCE / "retention"
    LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO = LAKE_LOCAL_PERFORMANCE / "no_go_safe_go"
    LAKE_LOCAL_PERFORMANCE_EXCEPTIONS = LAKE_LOCAL_PERFORMANCE / "exceptions"
    LAKE_LOCAL_PERFORMANCE_GAPS = LAKE_LOCAL_PERFORMANCE / "gaps"
    LAKE_LOCAL_PERFORMANCE_RISKS = LAKE_LOCAL_PERFORMANCE / "risks"
    LAKE_LOCAL_PERFORMANCE_SCORING = LAKE_LOCAL_PERFORMANCE / "scoring"
    LAKE_LOCAL_PERFORMANCE_VALIDATION = LAKE_LOCAL_PERFORMANCE / "validation"
    LAKE_LOCAL_PERFORMANCE_QUALITY = LAKE_LOCAL_PERFORMANCE / "quality"
    
    OUTPUT_LOCAL_PERFORMANCE = REPORTS_OUTPUT_DIR / "local_performance"
    OUTPUT_LOCAL_PERFORMANCE_CSV = OUTPUT_LOCAL_PERFORMANCE / "csv"
    OUTPUT_LOCAL_PERFORMANCE_MARKDOWN = OUTPUT_LOCAL_PERFORMANCE / "markdown"
    OUTPUT_LOCAL_PERFORMANCE_TXT = OUTPUT_LOCAL_PERFORMANCE / "txt"
    OUTPUT_LOCAL_PERFORMANCE_JSON = OUTPUT_LOCAL_PERFORMANCE / "json"
    
    DOCS_GENERATED_LOCAL_PERFORMANCE = DOCS_DIR / "generated" / "local_performance"
"""
        
        # Add inside ProjectPaths class
        pattern = r"(class ProjectPaths:.*?)(    @classmethod)"
        replacement = r"\1" + paths_to_add + r"\n\2"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Also need to add to ensure_project_directories
        ensure_pattern = r"(def ensure_project_directories\(\):.*?)(    \])"
        ensure_replacement = r"\1        ProjectPaths.LAKE_LOCAL_PERFORMANCE,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_PROFILES,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_DOMAINS,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_BUDGET,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_RUNTIME_PROFILE,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_RESOURCE_FOOTPRINT,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_CPU,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_MEMORY,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_DISK,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_GROWTH,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_SCRIPT_RUNTIME,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_TEST_RUNTIME,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_PIPELINE_RUNTIME,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_COST,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_MAINTENANCE_EFFORT,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_OPERATOR_TIME,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_MACHINE_SUITABILITY,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_EFFICIENCY,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_LIGHTWEIGHT_MODE,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_WARNINGS,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_RETENTION,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_NO_GO_SAFE_GO,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_EXCEPTIONS,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_GAPS,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_RISKS,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_SCORING,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_VALIDATION,\n        ProjectPaths.LAKE_LOCAL_PERFORMANCE_QUALITY,\n        ProjectPaths.OUTPUT_LOCAL_PERFORMANCE,\n        ProjectPaths.OUTPUT_LOCAL_PERFORMANCE_CSV,\n        ProjectPaths.OUTPUT_LOCAL_PERFORMANCE_MARKDOWN,\n        ProjectPaths.OUTPUT_LOCAL_PERFORMANCE_TXT,\n        ProjectPaths.OUTPUT_LOCAL_PERFORMANCE_JSON,\n        ProjectPaths.DOCS_GENERATED_LOCAL_PERFORMANCE,\n\2"
        content = re.sub(ensure_pattern, ensure_replacement, content, flags=re.DOTALL)
        
        paths_path.write_text(content, encoding="utf-8")
        print("Updated paths.py")

if __name__ == "__main__":
    update_settings()
    update_env()
    update_paths()
    print("Done")
