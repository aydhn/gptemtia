import os
from pathlib import Path
import re

def main():
    base_dir = Path("commodity_fx_signal_bot")
    ls_dir = base_dir / "local_simplification"
    ls_dir.mkdir(parents=True, exist_ok=True)
    
    (ls_dir / "__init__.py").write_text("")
    
    with open(ls_dir / "simplification_config.py", "w", encoding="utf-8") as f:
        f.write("""from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalSimplificationProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_auto_refactor: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cleanup_execution: bool = False
    allow_package_publish: bool = False
    allow_cloud_upload: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_production_cleanup_claim: bool = False
    allow_architecture_approval_claim: bool = False
    allow_compliance_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_source: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_reuse_outputs: bool = True
    scan_closure_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_candidate_items: int = 100000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_simplification": LocalSimplificationProfile(
        name="balanced_local_simplification",
        description="Genel amacli local/offline modular simplification, complexity map ve maintainability rehearsal profili.",
        notes="Genel amaçlı local/offline modular simplification, complexity map ve maintainability rehearsal profili."
    ),
    "complexity_map_focus": LocalSimplificationProfile(
        name="complexity_map_focus",
        description="Module/folder/file/function/script/test/report/DataLake/docs complexity ve sprawl haritalaması odaklı profil.",
        notes="Module/folder/file/function/script/test/report/DataLake/docs complexity ve sprawl haritalaması odaklı profil.",
    ),
    "slimming_plan_focus": LocalSimplificationProfile(
        name="slimming_plan_focus",
        description="Optional slimming plan, consolidation candidates ve maintainability seed odaklı profil.",
        notes="Optional slimming plan, consolidation candidates ve maintainability seed odaklı profil.",
        max_candidate_items=50000
    ),
    "strict_simplification_safety": LocalSimplificationProfile(
        name="strict_simplification_safety",
        description="Auto-refactor, file action, production cleanup, architecture approval, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        notes="Auto-refactor, file action, production cleanup, architecture approval, live/broker/advice overclaim denetimini sıkılaştıran profil.",
        max_items=300000,
        max_candidate_items=50000,
        min_readiness_score=0.60,
        min_quality_score=0.60
    )
}

def get_local_simplification_profile(name: str) -> LocalSimplificationProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown simplification profile: {name}")
    return _PROFILES[name]

def list_local_simplification_profiles(enabled_only: bool = True) -> list[LocalSimplificationProfile]:
    return [p for p in _PROFILES.values() if not enabled_only or p.enabled]

def validate_local_simplification_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} missing language")
        if p.max_items <= 0 or p.max_candidate_items <= 0:
            raise ConfigError(f"Profile {name} max_items must be positive")
        if not (0 <= p.min_readiness_score <= 1) or not (0 <= p.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} min_scores must be in 0-1")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True")
        if p.allow_auto_refactor or p.allow_file_modification or p.allow_file_deletion:
            raise ConfigError(f"Profile {name} must not allow destructive actions")

def get_default_local_simplification_profile() -> LocalSimplificationProfile:
    return _PROFILES["balanced_local_simplification"]
""")

    with open(ls_dir / "simplification_labels.py", "w", encoding="utf-8") as f:
        f.write("""def list_simplification_domain_labels() -> list[str]:
    return [
        "complexity_map_domain", "module_family_complexity_domain", "sprawl_analysis_domain",
        "optional_slimming_domain", "consolidation_candidate_domain", "naming_simplification_domain",
        "config_simplification_domain", "datalake_simplification_domain", "script_cli_simplification_domain",
        "test_suite_simplification_domain", "docs_navigation_domain", "repo_ergonomics_domain",
        "maintainability_seed_domain", "quality_validation_domain", "unknown_simplification_domain"
    ]

def list_simplification_candidate_labels() -> list[str]:
    return [
        "safe_consolidation_candidate", "duplicate_pattern_candidate", "naming_simplification_candidate",
        "config_simplification_candidate", "datalake_method_simplification_candidate",
        "script_cli_simplification_candidate", "test_suite_simplification_candidate",
        "docs_navigation_simplification_candidate", "maintainability_seed_candidate",
        "blocked_by_safety_candidate", "unknown_simplification_candidate"
    ]

def list_simplification_status_labels() -> list[str]:
    return [
        "simplification_ready_for_rehearsal", "simplification_ready_with_warnings",
        "simplification_missing", "simplification_blocked_by_safety",
        "simplification_needs_manual_review", "simplification_unknown"
    ]

def list_complexity_level_labels() -> list[str]:
    return [
        "complexity_low", "complexity_medium", "complexity_high",
        "complexity_very_high", "complexity_unknown"
    ]

def list_simplification_risk_labels() -> list[str]:
    return [
        "simplification_critical_risk", "simplification_high_risk",
        "simplification_medium_risk", "simplification_low_risk",
        "simplification_info", "simplification_unknown_risk"
    ]

def validate_simplification_domain_label(label: str) -> None:
    if label not in list_simplification_domain_labels():
        raise ValueError(f"Invalid domain label: {label}")

def validate_simplification_candidate_label(label: str) -> None:
    if label not in list_simplification_candidate_labels():
        raise ValueError(f"Invalid candidate label: {label}")

def validate_simplification_status(label: str) -> None:
    if label not in list_simplification_status_labels():
        raise ValueError(f"Invalid status label: {label}")

def validate_complexity_level(label: str) -> None:
    if label not in list_complexity_level_labels():
        raise ValueError(f"Invalid complexity level: {label}")

def validate_simplification_risk(label: str) -> None:
    if label not in list_simplification_risk_labels():
        raise ValueError(f"Invalid risk label: {label}")
""")

    with open(ls_dir / "simplification_models.py", "w", encoding="utf-8") as f:
        f.write("""from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class SimplificationDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_reports: list[str]
    warnings: list[str]

@dataclass
class ComplexityItem:
    item_id: str
    item_name: str
    item_path: Optional[str]
    source_layer: str
    metric_name: str
    metric_value: Union[float, int, str, None]
    complexity_level: str
    warnings: list[str]

@dataclass
class SimplificationCandidate:
    candidate_id: str
    candidate_label: str
    candidate_name: str
    source_layer: str
    rationale: str
    expected_benefit: str
    manual_review_required: bool
    safety_boundaries: list[str]
    warnings: list[str]

@dataclass
class SlimmingPlanItem:
    plan_item_id: str
    title: str
    category: str
    priority_hint: str
    action_type: str
    dry_run_only: bool
    prerequisites: list[str]
    warnings: list[str]

@dataclass
class SimplificationFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_simplification_domain_id(domain_label: str) -> str:
    return f"domain_{domain_label}"

def build_complexity_item_id(item_name: str, metric_name: str) -> str:
    return f"comp_{item_name}_{metric_name}".replace(" ", "_")

def build_simplification_candidate_id(candidate_label: str, candidate_name: str) -> str:
    return f"cand_{candidate_label}_{candidate_name}".replace(" ", "_")

def build_slimming_plan_item_id(title: str, category: str) -> str:
    return f"plan_{category}_{title}".replace(" ", "_")

def build_simplification_finding_id(title: str) -> str:
    return f"finding_{title}".replace(" ", "_")

def simplification_domain_to_dict(item: SimplificationDomain) -> dict:
    return {
        "domain_id": item.domain_id, "domain_label": item.domain_label,
        "domain_name": item.domain_name, "description": item.description,
        "required_reports": ",".join(item.required_reports), "warnings": ",".join(item.warnings)
    }

def complexity_item_to_dict(item: ComplexityItem) -> dict:
    return {
        "item_id": item.item_id, "item_name": item.item_name, "item_path": item.item_path,
        "source_layer": item.source_layer, "metric_name": item.metric_name,
        "metric_value": item.metric_value, "complexity_level": item.complexity_level,
        "warnings": ",".join(item.warnings)
    }

def simplification_candidate_to_dict(item: SimplificationCandidate) -> dict:
    return {
        "candidate_id": item.candidate_id, "candidate_label": item.candidate_label,
        "candidate_name": item.candidate_name, "source_layer": item.source_layer,
        "rationale": item.rationale, "expected_benefit": item.expected_benefit,
        "manual_review_required": item.manual_review_required,
        "safety_boundaries": ",".join(item.safety_boundaries), "warnings": ",".join(item.warnings)
    }

def slimming_plan_item_to_dict(item: SlimmingPlanItem) -> dict:
    return {
        "plan_item_id": item.plan_item_id, "title": item.title, "category": item.category,
        "priority_hint": item.priority_hint, "action_type": item.action_type,
        "dry_run_only": item.dry_run_only, "prerequisites": ",".join(item.prerequisites),
        "warnings": ",".join(item.warnings)
    }

def simplification_finding_to_dict(item: SimplificationFinding) -> dict:
    return {
        "finding_id": item.finding_id, "risk_label": item.risk_label, "title": item.title,
        "description": item.description, "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required, "warnings": ",".join(item.warnings)
    }
""")

    print("Created phase 82 core 1")

if __name__ == "__main__":
    main()
