import os
from pathlib import Path

def generate_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

# advanced_research_engine/__init__.py
generate_file("advanced_research_engine/__init__.py", "")

# advanced_research_engine/research_engine_config.py
generate_file("advanced_research_engine/research_engine_config.py", """
from dataclasses import dataclass
import pandas as pd

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedResearchEngineProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 103
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
    enable_data_interface: bool = True
    enable_feature_interface: bool = True
    enable_regime_interface: bool = True
    enable_ml_interface: bool = True
    enable_backtest_interface: bool = True
    enable_portfolio_interface: bool = True
    enable_report_interface: bool = True
    enable_signal_research_interface: bool = True
    scan_runtime_outputs: bool = True
    scan_continuation_outputs: bool = True
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
    "balanced_research_engine": AdvancedResearchEngineProfile(
        name="balanced_research_engine",
        description="Phase 103 research engine interface layer balanced profile.",
        notes="Phase 103 research engine interface layer için dengeli local/offline profil."
    ),
    "strict_research_engine_safety": AdvancedResearchEngineProfile(
        name="strict_research_engine_safety",
        description="Strict profile.",
        min_readiness_score=0.65,
        min_quality_score=0.65,
        notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen research engine profili."
    ),
    "interface_contract_focus": AdvancedResearchEngineProfile(
        name="interface_contract_focus",
        description="Interface focus.",
        notes="Data/feature/regime/ML/backtest/portfolio/report/signal research interface kontratlarına odaklı profil."
    )
}

def get_advanced_research_engine_profile(name: str) -> AdvancedResearchEngineProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return PROFILES[name]

def list_advanced_research_engine_profiles(enabled_only: bool = True) -> list[AdvancedResearchEngineProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_advanced_research_engine_profiles() -> None:
    for p in PROFILES.values():
        assert p.current_phase == 103
        assert p.target_final_phase == 160
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert p.language != ""
        assert p.max_items > 0
        assert p.max_rows > 0
        assert 0.0 <= p.min_readiness_score <= 1.0
        assert 0.0 <= p.min_quality_score <= 1.0
        assert not p.allow_live_trading
        assert not p.allow_broker_integration

def get_default_advanced_research_engine_profile() -> AdvancedResearchEngineProfile:
    return PROFILES["balanced_research_engine"]
""")

# advanced_research_engine/research_engine_labels.py
generate_file("advanced_research_engine/research_engine_labels.py", """
def list_research_engine_domain_labels():
    return [
        "research_engine_profile_domain", "research_engine_context_domain",
        "research_request_domain", "research_result_domain", "research_interface_domain",
        "data_access_interface_domain", "feature_interface_domain", "regime_interface_domain",
        "ml_interface_domain", "backtest_interface_domain", "portfolio_interface_domain",
        "report_interface_domain", "signal_research_interface_domain", "research_gateway_domain",
        "research_safety_domain", "research_quality_domain", "unknown_research_engine_domain"
    ]

def list_research_engine_status_labels():
    return [
        "research_engine_ready", "research_engine_ready_with_warnings", "research_engine_missing",
        "research_engine_blocked_by_safety", "research_engine_needs_manual_review", "research_engine_unknown"
    ]

def list_research_request_type_labels():
    return [
        "request_data_access", "request_feature_build", "request_regime_analysis",
        "request_ml_research", "request_backtest_research", "request_portfolio_research",
        "request_report_build", "request_signal_research", "request_full_research_dry_run"
    ]

def list_research_result_type_labels():
    return [
        "result_registry", "result_context", "result_dataframe", "result_report",
        "result_score", "result_validation", "result_quality", "result_error", "result_manual_review"
    ]

def list_research_engine_risk_labels():
    return [
        "research_engine_critical_risk", "research_engine_high_risk", "research_engine_medium_risk",
        "research_engine_low_risk", "research_engine_info", "research_engine_unknown_risk"
    ]

def validate_research_engine_domain_label(label: str): return label in list_research_engine_domain_labels()
def validate_research_engine_status(label: str): return label in list_research_engine_status_labels()
def validate_research_request_type(label: str): return label in list_research_request_type_labels()
def validate_research_result_type(label: str): return label in list_research_result_type_labels()
def validate_research_engine_risk_label(label: str): return label in list_research_engine_risk_labels()
""")

# advanced_research_engine/research_engine_models.py
generate_file("advanced_research_engine/research_engine_models.py", """
from dataclasses import dataclass, asdict

@dataclass
class ResearchEngineProfileItem:
    profile_id: str
    profile_name: str
    current_phase: int
    target_final_phase: int
    local_only: bool
    non_production: bool
    research_only: bool
    status_label: str
    warnings: list[str]

@dataclass
class ResearchEngineDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class ResearchContextItem:
    context_id: str
    context_area: str
    context_name: str
    source_ref: str
    research_role: str
    status_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ResearchRequest:
    request_id: str
    request_type: str
    universe: list[str]
    timeframe: str
    horizon: str
    requested_modules: list[str]
    dry_run: bool
    local_only: bool
    metadata: dict

@dataclass
class ResearchResult:
    result_id: str
    request_id: str
    result_type: str
    status_label: str
    output_ref: str
    summary: dict
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ResearchInterfaceContract:
    contract_id: str
    interface_name: str
    input_contract: str
    output_contract: str
    future_phase_range: str
    forbidden_behavior: list[str]
    manual_review_required: bool

@dataclass
class ResearchGatewayItem:
    gateway_id: str
    gateway_area: str
    interface_ref: str
    target_module_ref: str
    future_phase_range: str
    gateway_status: str
    warnings: list[str]

@dataclass
class ResearchEngineFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_research_engine_profile_id(profile_name: str) -> str: return f"prof_{profile_name}"
def build_research_engine_domain_id(domain_label: str) -> str: return f"dom_{domain_label}"
def build_research_context_id(context_area: str, context_name: str) -> str: return f"ctx_{context_area}_{context_name}"
def build_research_request_id(request_type: str, timeframe: str, horizon: str) -> str: return f"req_{request_type}_{timeframe}_{horizon}"
def build_research_result_id(request_id: str, result_type: str) -> str: return f"res_{request_id}_{result_type}"
def build_research_interface_contract_id(interface_name: str) -> str: return f"int_{interface_name}"
def build_research_gateway_id(gateway_area: str, interface_ref: str) -> str: return f"gw_{gateway_area}_{interface_ref}"
def build_research_engine_finding_id(title: str) -> str: return f"find_{hash(title)}"
""")

# Create patch_phase103_2.py for the rest of the generation to avoid giant file
""")
"""
