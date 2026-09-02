import os
from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalPerformanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_benchmark: bool = False
    allow_load_test: bool = False
    allow_stress_test: bool = False
    allow_production_profiling: bool = False
    allow_background_monitoring: bool = False
    allow_cloud_cost_estimate: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_production_capacity_claim: bool = False
    allow_performance_certification_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_investment_performance_claim: bool = False
    allow_model_deployment_claim: bool = False
    scan_source: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_simplification_outputs: bool = True
    scan_safety_outputs: bool = True
    default_cpu_budget_label: str = "average_local_cpu"
    default_memory_budget_mb: int = 8192
    default_disk_budget_mb: int = 51200
    default_runtime_budget_minutes: int = 30
    max_items: int = 500000
    max_estimate_rows: int = 100000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_local_performance": LocalPerformanceProfile(
        name="balanced_local_performance",
        description="Genel amacli local/offline performance budgeting profil",
        notes="Genel amaçlı local/offline performance budgeting, runtime profile ve resource-footprint rehearsal profili."
    ),
    "lightweight_runtime_focus": LocalPerformanceProfile(
        name="lightweight_runtime_focus",
        description="Lightweight mode focus",
        default_memory_budget_mb=4096,
        default_disk_budget_mb=25600,
        default_runtime_budget_minutes=15,
        max_estimate_rows=50000,
        notes="Hafif runtime profile, lightweight mode recommendation ve heavy output warning odaklı profil."
    ),
    "maintenance_cost_focus": LocalPerformanceProfile(
        name="maintenance_cost_focus",
        description="Maintenance cost focus",
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=True,
        scan_tests=True,
        scan_generated_docs=True,
        notes="Maintenance cost estimate, operator time budget ve maintenance effort matrix odaklı profil."
    ),
    "strict_performance_safety": LocalPerformanceProfile(
        name="strict_performance_safety",
        description="Strict safety focus",
        default_memory_budget_mb=4096,
        default_disk_budget_mb=25600,
        default_runtime_budget_minutes=10,
        max_items=300000,
        max_estimate_rows=50000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Benchmark/load/stress/profiling/cloud/live/broker/advice overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_performance_profile(name: str) -> LocalPerformanceProfile:
    if name not in PROFILES:
        raise ConfigError(f"Bilinmeyen profil: {name}")
    return PROFILES[name]

def list_local_performance_profiles(enabled_only: bool = True) -> list[LocalPerformanceProfile]:
    if enabled_only:
        return [p for p in PROFILES.values() if p.enabled]
    return list(PROFILES.values())

def validate_local_performance_profiles() -> None:
    for p in PROFILES.values():
        if not p.language:
            raise ConfigError(f"Profil {p.name}: language bos olamaz.")
        if p.default_memory_budget_mb <= 0 or p.default_disk_budget_mb <= 0 or p.default_runtime_budget_minutes <= 0 or p.max_items <= 0 or p.max_estimate_rows <= 0:
            raise ConfigError(f"Profil {p.name}: limitler pozitif olmali.")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profil {p.name}: scorelar 0-1 araliginda olmali.")
        if not p.dry_run_default:
            raise ConfigError(f"Profil {p.name}: dry_run_default True olmali.")
        if any([p.allow_real_benchmark, p.allow_load_test, p.allow_stress_test, p.allow_production_profiling, p.allow_background_monitoring, p.allow_cloud_cost_estimate, p.allow_cloud_upload, p.allow_package_publish, p.allow_external_service, p.allow_external_llm, p.allow_file_modification, p.allow_file_deletion, p.allow_file_move, p.allow_overwrite, p.allow_production_capacity_claim, p.allow_performance_certification_claim, p.allow_live_trading_claim, p.allow_broker_readiness_claim, p.allow_investment_advice, p.allow_investment_performance_claim, p.allow_model_deployment_claim]):
            raise ConfigError(f"Profil {p.name}: external/live islemlere izin verilemez.")

def get_default_local_performance_profile() -> LocalPerformanceProfile:
    return PROFILES["balanced_local_performance"]
