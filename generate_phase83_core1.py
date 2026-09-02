import os
from pathlib import Path

def generate_core1():
    base_dir = Path("commodity_fx_signal_bot/local_performance")
    base_dir.mkdir(parents=True, exist_ok=True)
    
    # __init__.py
    (base_dir / "__init__.py").write_text("", encoding="utf-8")
    
    # performance_config.py
    (base_dir / "performance_config.py").write_text("""import os
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
""", encoding="utf-8")
    
    # performance_labels.py
    (base_dir / "performance_labels.py").write_text("""class ConfigError(Exception): pass

DOMAIN_LABELS = [
    "performance_budget_domain", "runtime_profile_domain", "resource_footprint_domain",
    "cpu_estimate_domain", "memory_estimate_domain", "disk_estimate_domain",
    "growth_estimate_domain", "runtime_estimate_domain", "maintenance_cost_domain",
    "machine_suitability_domain", "efficiency_planning_domain", "retention_planning_domain",
    "quality_validation_domain", "unknown_performance_domain"
]

ESTIMATE_LABELS = [
    "cpu_estimate_low", "cpu_estimate_medium", "cpu_estimate_high",
    "memory_estimate_low", "memory_estimate_medium", "memory_estimate_high",
    "disk_estimate_low", "disk_estimate_medium", "disk_estimate_high",
    "runtime_estimate_low", "runtime_estimate_medium", "runtime_estimate_high",
    "estimate_unknown"
]

STATUS_LABELS = [
    "performance_ready_for_rehearsal", "performance_ready_with_warnings",
    "performance_missing", "performance_blocked_by_safety",
    "performance_needs_manual_review", "performance_unknown"
]

EFFICIENCY_CANDIDATE_LABELS = [
    "lightweight_mode_candidate", "output_reduction_candidate", "retention_policy_candidate",
    "report_rotation_candidate", "datalake_retention_candidate", "script_runtime_candidate",
    "test_runtime_candidate", "blocked_by_safety_candidate", "unknown_efficiency_candidate"
]

RISK_LABELS = [
    "performance_critical_risk", "performance_high_risk", "performance_medium_risk",
    "performance_low_risk", "performance_info", "performance_unknown_risk"
]

def list_performance_domain_labels() -> list[str]: return DOMAIN_LABELS
def list_performance_estimate_labels() -> list[str]: return ESTIMATE_LABELS
def list_performance_status_labels() -> list[str]: return STATUS_LABELS
def list_efficiency_candidate_labels() -> list[str]: return EFFICIENCY_CANDIDATE_LABELS
def list_performance_risk_labels() -> list[str]: return RISK_LABELS

def validate_performance_domain_label(label: str) -> None:
    if label not in DOMAIN_LABELS: raise ConfigError("Invalid domain label")
def validate_performance_estimate_label(label: str) -> None:
    if label not in ESTIMATE_LABELS: raise ConfigError("Invalid estimate label")
def validate_performance_status(label: str) -> None:
    if label not in STATUS_LABELS: raise ConfigError("Invalid status label")
def validate_efficiency_candidate_label(label: str) -> None:
    if label not in EFFICIENCY_CANDIDATE_LABELS: raise ConfigError("Invalid candidate label")
def validate_performance_risk(label: str) -> None:
    if label not in RISK_LABELS: raise ConfigError("Invalid risk label")
""", encoding="utf-8")
    
    # performance_models.py
    (base_dir / "performance_models.py").write_text("""import hashlib
from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class PerformanceDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_reports: list[str]
    warnings: list[str]

@dataclass
class ResourceEstimateItem:
    estimate_id: str
    estimate_label: str
    item_name: str
    source_layer: str
    estimate_metric: str
    estimate_value: float | int | str | None
    estimate_basis: str
    warnings: list[str]

@dataclass
class RuntimeEstimateItem:
    runtime_id: str
    target_name: str
    target_type: str
    runtime_estimate_label: str
    estimated_minutes: float | None
    estimate_basis: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class EfficiencyCandidate:
    candidate_id: str
    candidate_label: str
    candidate_name: str
    source_layer: str
    rationale: str
    expected_local_benefit: str
    dry_run_only: bool
    manual_review_required: bool
    warnings: list[str]

@dataclass
class PerformanceFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_performance_domain_id(domain_label: str) -> str:
    return hashlib.md5(f"domain_{domain_label}".encode()).hexdigest()[:12]

def build_resource_estimate_id(item_name: str, estimate_metric: str) -> str:
    return hashlib.md5(f"resource_{item_name}_{estimate_metric}".encode()).hexdigest()[:12]

def build_runtime_estimate_id(target_name: str, target_type: str) -> str:
    return hashlib.md5(f"runtime_{target_type}_{target_name}".encode()).hexdigest()[:12]

def build_efficiency_candidate_id(candidate_label: str, candidate_name: str) -> str:
    return hashlib.md5(f"cand_{candidate_label}_{candidate_name}".encode()).hexdigest()[:12]

def build_performance_finding_id(title: str) -> str:
    return hashlib.md5(f"finding_{title}".encode()).hexdigest()[:12]

def performance_domain_to_dict(item: PerformanceDomain) -> dict: return asdict(item)
def resource_estimate_item_to_dict(item: ResourceEstimateItem) -> dict: return asdict(item)
def runtime_estimate_item_to_dict(item: RuntimeEstimateItem) -> dict: return asdict(item)
def efficiency_candidate_to_dict(item: EfficiencyCandidate) -> dict: return asdict(item)
def performance_finding_to_dict(item: PerformanceFinding) -> dict: return asdict(item)
""", encoding="utf-8")
    
    # performance_domain_registry.py
    (base_dir / "performance_domain_registry.py").write_text("""import pandas as pd
from .performance_config import LocalPerformanceProfile
from .performance_models import PerformanceDomain, build_performance_domain_id, performance_domain_to_dict
from .performance_labels import list_performance_domain_labels

def build_default_performance_domains(profile: LocalPerformanceProfile) -> list[PerformanceDomain]:
    domains = []
    for lbl in list_performance_domain_labels():
        if lbl == "unknown_performance_domain": continue
        domains.append(PerformanceDomain(
            domain_id=build_performance_domain_id(lbl),
            domain_label=lbl,
            domain_name=lbl.replace("_", " ").title(),
            description=f"{lbl} domain for offline planning",
            required_reports=[],
            warnings=["Bu domain official capacity scope degildir."]
        ))
    return domains

def build_performance_domain_registry(profile: LocalPerformanceProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_performance_domains(profile)
    df = pd.DataFrame([performance_domain_to_dict(d) for d in domains])
    summary = summarize_performance_domains(df)
    return df, summary

def summarize_performance_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total": 0, "status": "empty"}
    return {"total": len(domain_df), "domains": domain_df["domain_label"].tolist()}
""", encoding="utf-8")

if __name__ == "__main__":
    generate_core1()
    print("Core 1 generated")
