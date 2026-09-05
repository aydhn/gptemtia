import os

def write_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # __init__.py
    write_file('advanced_runtime/__init__.py', '')

    # runtime_config.py
    write_file('advanced_runtime/runtime_config.py', '''from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedRuntimeProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 102
    target_final_phase: int = 160
    dry_run_default: bool = True
    local_only: bool = True
    non_production: bool = True
    research_only: bool = True
    allow_live_trading: bool = False
    allow_broker_integration: bool = False
    allow_real_order: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment: bool = False
    allow_production_deployment: bool = False
    allow_web_server: bool = False
    allow_dashboard: bool = False
    allow_gui_tui: bool = False
    allow_external_llm: bool = False
    allow_vector_db: bool = False
    allow_embedding_api: bool = False
    allow_web_scraping: bool = False
    allow_cloud_publish: bool = False
    allow_docker_push: bool = False
    allow_git_tag: bool = False
    allow_archive_creation: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    scan_settings: bool = True
    scan_paths: bool = True
    scan_datalake: bool = True
    scan_featurestore: bool = True
    scan_reports: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_docs: bool = True
    max_items: int = 1000000
    max_rows: int = 500000
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

PROFILES = {
    "balanced_advanced_runtime": AdvancedRuntimeProfile(
        name="balanced_advanced_runtime",
        description="Balanced offline profile for Phase 102",
        notes="Phase 102 core runtime consolidation için dengeli local/offline runtime profili."
    ),
    "strict_runtime_safety": AdvancedRuntimeProfile(
        name="strict_runtime_safety",
        description="Strict safety profile",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen runtime profili."
    ),
    "runtime_contract_focus": AdvancedRuntimeProfile(
        name="runtime_contract_focus",
        description="Contract focus profile",
        scan_scripts=False,
        scan_tests=False,
        scan_docs=False,
        notes="Settings/paths/DataLake/FeatureStore/report contract üretimine odaklı runtime profili."
    )
}

def get_advanced_runtime_profile(name: str) -> AdvancedRuntimeProfile:
    if name not in PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return PROFILES[name]

def list_advanced_runtime_profiles(enabled_only: bool = True) -> list[AdvancedRuntimeProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def get_default_advanced_runtime_profile() -> AdvancedRuntimeProfile:
    return PROFILES["balanced_advanced_runtime"]

def validate_advanced_runtime_profiles() -> None:
    for p in PROFILES.values():
        if p.current_phase != 102: raise ConfigError("current_phase must be 102")
        if p.target_final_phase != 160: raise ConfigError("target_final_phase must be 160")
        if not p.dry_run_default: raise ConfigError("dry_run_default must be True")
        if not (p.local_only and p.non_production and p.research_only): raise ConfigError("Must be local/non-prod/research")
        if not p.language: raise ConfigError("language must not be empty")
        if p.max_items <= 0 or p.max_rows <= 0: raise ConfigError("max items/rows must be positive")
        if not (0 <= p.min_readiness_score <= 1 and 0 <= p.min_quality_score <= 1): raise ConfigError("Scores must be 0-1")
        if any([p.allow_live_trading, p.allow_broker_integration, p.allow_investment_advice, p.allow_model_deployment, p.allow_web_scraping]):
            raise ConfigError("Risk flags must be False")
''')

    # runtime_labels.py
    write_file('advanced_runtime/runtime_labels.py', '''RUNTIME_DOMAIN_LABELS = [
    "runtime_profile_domain", "runtime_context_domain", "runtime_capability_domain",
    "runtime_module_domain", "runtime_dependency_domain", "runtime_execution_contract_domain",
    "runtime_command_contract_domain", "runtime_output_contract_domain",
    "runtime_datalake_contract_domain", "runtime_featurestore_contract_domain",
    "runtime_report_contract_domain", "runtime_safety_domain", "runtime_health_domain",
    "runtime_quality_domain", "unknown_runtime_domain"
]

RUNTIME_STATUS_LABELS = [
    "runtime_ready", "runtime_ready_with_warnings", "runtime_missing",
    "runtime_blocked_by_safety", "runtime_needs_manual_review", "runtime_unknown"
]

RUNTIME_CAPABILITY_LABELS = [
    "capability_settings", "capability_paths", "capability_datalake",
    "capability_featurestore", "capability_reporting", "capability_scripts",
    "capability_tests", "capability_docs", "capability_advanced_continuation",
    "capability_provider_future", "capability_feature_future", "capability_regime_future",
    "capability_ml_gpu_future", "capability_backtest_future", "capability_portfolio_future",
    "capability_final_integration_future"
]

RUNTIME_RISK_LABELS = [
    "runtime_critical_risk", "runtime_high_risk", "runtime_medium_risk",
    "runtime_low_risk", "runtime_info", "runtime_unknown_risk"
]

def list_runtime_domain_labels(): return RUNTIME_DOMAIN_LABELS
def list_runtime_status_labels(): return RUNTIME_STATUS_LABELS
def list_runtime_capability_labels(): return RUNTIME_CAPABILITY_LABELS
def list_runtime_risk_labels(): return RUNTIME_RISK_LABELS

def validate_runtime_domain_label(label: str): return label in RUNTIME_DOMAIN_LABELS
def validate_runtime_status(label: str): return label in RUNTIME_STATUS_LABELS
def validate_runtime_capability_label(label: str): return label in RUNTIME_CAPABILITY_LABELS
def validate_runtime_risk_label(label: str): return label in RUNTIME_RISK_LABELS
''')

    # runtime_models.py
    write_file('advanced_runtime/runtime_models.py', '''from dataclasses import dataclass, asdict
from typing import List

@dataclass
class RuntimeProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeContextItem:
    context_id: str
    context_area: str
    context_name: str
    source_ref: str
    runtime_role: str
    status_label: str
    manual_review_required: bool
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeCapabilityItem:
    capability_id: str
    capability_label: str
    capability_name: str
    current_status: str
    future_phase_range: str
    required_by: List[str]
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeModuleItem:
    module_id: str
    module_area: str
    module_ref: str
    runtime_role: str
    contract_required: bool
    status_label: str
    warnings: List[str]
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeContractItem:
    contract_id: str
    contract_area: str
    contract_name: str
    input_expectation: str
    output_expectation: str
    forbidden_behavior: List[str]
    manual_review_required: bool
    def to_dict(self): return asdict(self)

@dataclass
class RuntimeHealthFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    def to_dict(self): return asdict(self)

def build_runtime_profile_id(profile_name: str) -> str: return f"profile_{profile_name}"
def build_runtime_context_id(context_area: str, context_name: str) -> str: return f"ctx_{context_area}_{context_name}"
def build_runtime_capability_id(capability_label: str) -> str: return f"cap_{capability_label}"
def build_runtime_module_id(module_area: str, module_ref: str) -> str: return f"mod_{module_area}_{module_ref}"
def build_runtime_contract_id(contract_area: str, contract_name: str) -> str: return f"ctr_{contract_area}_{contract_name}"
def build_runtime_health_finding_id(title: str) -> str: return f"hlt_{title.replace(' ', '_').lower()}"
''')

if __name__ == '__main__':
    main()
