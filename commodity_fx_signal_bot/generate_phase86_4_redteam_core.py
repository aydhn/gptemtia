import os
from pathlib import Path

def create_local_redteam_core():
    base_dir = Path("local_redteam")
    base_dir.mkdir(exist_ok=True)
    
    (base_dir / "__init__.py").write_text("", encoding="utf-8")
    
    config_code = """from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class LocalRedTeamProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_attack: bool = False
    allow_jailbreak_generation: bool = False
    allow_exploit_generation: bool = False
    allow_prompt_injection_payloads: bool = False
    allow_credential_exfiltration: bool = False
    allow_live_security_testing: bool = False
    allow_telemetry: bool = False
    allow_dashboard_creation: bool = False
    allow_gui_creation: bool = False
    allow_tui_creation: bool = False
    allow_cloud_upload: bool = False
    allow_package_publish: bool = False
    allow_external_service: bool = False
    allow_external_llm: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_safety_certification_claim: bool = False
    allow_compliance_signoff: bool = False
    allow_production_safety_approval_claim: bool = False
    allow_live_trading_claim: bool = False
    allow_broker_readiness_claim: bool = False
    allow_investment_advice: bool = False
    allow_model_deployment_claim: bool = False
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_generated_docs: bool = True
    scan_governance_outputs: bool = True
    scan_usability_outputs: bool = True
    scan_safety_outputs: bool = True
    max_items: int = 500000
    max_scenarios: int = 10000
    min_readiness_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_redteam": LocalRedTeamProfile(
        name="balanced_local_redteam",
        description="Genel amaçlı local/offline red-team rehearsal, misuse scenario classification ve safety assurance profili.",
        language="tr",
        dry_run_default=True,
        max_items=500000,
        max_scenarios=10000,
        min_readiness_score=0.40,
        min_quality_score=0.40,
        notes="Genel amaçlı local/offline red-team rehearsal, misuse scenario classification ve safety assurance profili."
    ),
    "misuse_library_focus": LocalRedTeamProfile(
        name="misuse_library_focus",
        description="Misuse scenario library, abuse-case simulation registry ve boundary-violation coverage odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=False,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=True,
        scan_governance_outputs=True,
        scan_usability_outputs=False,
        scan_safety_outputs=True,
        max_scenarios=8000,
        notes="Misuse scenario library, abuse-case simulation registry ve boundary-violation coverage odaklı profil."
    ),
    "safety_assurance_focus": LocalRedTeamProfile(
        name="safety_assurance_focus",
        description="Safety assurance summary, coverage matrix, blindspot register ve manual escalation checklist odaklı profil.",
        language="tr",
        dry_run_default=True,
        scan_docs=True,
        scan_reports=True,
        scan_data_lake=True,
        scan_scripts=False,
        scan_tests=False,
        scan_generated_docs=True,
        scan_governance_outputs=True,
        scan_usability_outputs=True,
        scan_safety_outputs=True,
        max_scenarios=8000,
        notes="Safety assurance summary, coverage matrix, blindspot register ve manual escalation checklist odaklı profil."
    ),
    "strict_redteam_safety": LocalRedTeamProfile(
        name="strict_redteam_safety",
        description="Jailbreak/exploit/prompt-injection payload/credential/live/broker/advice/deploy overclaim denetimini sıkılaştıran profil.",
        language="tr",
        dry_run_default=True,
        max_items=300000,
        max_scenarios=5000,
        min_readiness_score=0.60,
        min_quality_score=0.60,
        notes="Jailbreak/exploit/prompt-injection payload/credential/live/broker/advice/deploy overclaim denetimini sıkılaştıran profil."
    )
}

def get_local_redteam_profile(name: str) -> LocalRedTeamProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Profile {name} not found.")
    return _PROFILES[name]

def list_local_redteam_profiles(enabled_only: bool = True) -> list[LocalRedTeamProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_local_redteam_profiles() -> None:
    for name, p in _PROFILES.items():
        if not p.language:
            raise ConfigError(f"Profile {name} language must not be empty.")
        if p.max_items <= 0 or p.max_scenarios <= 0:
            raise ConfigError(f"Profile {name} max_items and max_scenarios must be positive.")
        if not (0.0 <= p.min_readiness_score <= 1.0) or not (0.0 <= p.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} scores must be between 0 and 1.")
        if not p.dry_run_default:
            raise ConfigError(f"Profile {name} dry_run_default must be True.")
        if p.allow_real_attack or p.allow_jailbreak_generation or p.allow_exploit_generation:
            raise ConfigError(f"Profile {name} attack/jailbreak/exploit flags must be False.")
        if p.allow_prompt_injection_payloads or p.allow_credential_exfiltration or p.allow_live_security_testing:
            raise ConfigError(f"Profile {name} payload/exfiltration flags must be False.")
        if p.allow_telemetry or p.allow_dashboard_creation or p.allow_gui_creation or p.allow_tui_creation:
            raise ConfigError(f"Profile {name} telemetry/gui flags must be False.")
        if p.allow_cloud_upload or p.allow_package_publish or p.allow_external_service or p.allow_external_llm:
            raise ConfigError(f"Profile {name} cloud/external flags must be False.")
        if p.allow_file_modification or p.allow_file_deletion or p.allow_file_move or p.allow_overwrite:
            raise ConfigError(f"Profile {name} file action flags must be False.")
        if p.allow_safety_certification_claim or p.allow_compliance_signoff or p.allow_production_safety_approval_claim:
            raise ConfigError(f"Profile {name} safety claims must be False.")
        if p.allow_live_trading_claim or p.allow_broker_readiness_claim or p.allow_investment_advice or p.allow_model_deployment_claim:
            raise ConfigError(f"Profile {name} live/broker/advice/deploy claims must be False.")

def get_default_local_redteam_profile() -> LocalRedTeamProfile:
    return _PROFILES["balanced_local_redteam"]
"""
    (base_dir / "redteam_config.py").write_text(config_code, encoding="utf-8")
    
    labels_code = """class LabelError(Exception):
    pass

_REDTEAM_DOMAIN_LABELS = [
    "redteam_rehearsal_domain",
    "misuse_scenario_domain",
    "abuse_case_simulation_domain",
    "adversarial_prompt_safety_domain",
    "prompt_injection_risk_domain",
    "unsafe_output_domain",
    "forbidden_capability_domain",
    "boundary_violation_domain",
    "safety_response_domain",
    "manual_escalation_domain",
    "safety_assurance_domain",
    "safety_coverage_domain",
    "quality_validation_domain",
    "unknown_redteam_domain"
]

_MISUSE_CATEGORY_LABELS = [
    "misuse_live_trading",
    "misuse_broker_execution",
    "misuse_investment_advice",
    "misuse_model_deployment",
    "misuse_secret_exposure",
    "misuse_file_action",
    "misuse_cloud_publish",
    "misuse_external_llm_api",
    "misuse_prompt_injection",
    "misuse_jailbreak_request",
    "misuse_performance_overclaim",
    "misuse_compliance_overclaim",
    "misuse_unknown"
]

_SAFETY_RESPONSE_LABELS = [
    "response_refuse",
    "response_refuse_and_redirect",
    "response_boundary_reminder",
    "response_manual_review",
    "response_no_go",
    "response_safe_summary",
    "response_unknown"
]

_REDTEAM_STATUS_LABELS = [
    "redteam_ready_for_rehearsal",
    "redteam_ready_with_warnings",
    "redteam_missing",
    "redteam_blocked_by_safety",
    "redteam_needs_manual_review",
    "redteam_unknown"
]

_REDTEAM_RISK_LABELS = [
    "redteam_critical_risk",
    "redteam_high_risk",
    "redteam_medium_risk",
    "redteam_low_risk",
    "redteam_info",
    "redteam_unknown_risk"
]

def list_redteam_domain_labels() -> list[str]:
    return _REDTEAM_DOMAIN_LABELS.copy()

def list_misuse_category_labels() -> list[str]:
    return _MISUSE_CATEGORY_LABELS.copy()

def list_safety_response_labels() -> list[str]:
    return _SAFETY_RESPONSE_LABELS.copy()

def list_redteam_status_labels() -> list[str]:
    return _REDTEAM_STATUS_LABELS.copy()

def list_redteam_risk_labels() -> list[str]:
    return _REDTEAM_RISK_LABELS.copy()

def validate_redteam_domain_label(label: str) -> None:
    if label not in _REDTEAM_DOMAIN_LABELS:
        raise LabelError(f"Invalid redteam domain label: {label}")

def validate_misuse_category_label(label: str) -> None:
    if label not in _MISUSE_CATEGORY_LABELS:
        raise LabelError(f"Invalid misuse category label: {label}")

def validate_safety_response_label(label: str) -> None:
    if label not in _SAFETY_RESPONSE_LABELS:
        raise LabelError(f"Invalid safety response label: {label}")

def validate_redteam_status(label: str) -> None:
    if label not in _REDTEAM_STATUS_LABELS:
        raise LabelError(f"Invalid redteam status label: {label}")

def validate_redteam_risk(label: str) -> None:
    if label not in _REDTEAM_RISK_LABELS:
        raise LabelError(f"Invalid redteam risk label: {label}")
"""
    (base_dir / "redteam_labels.py").write_text(labels_code, encoding="utf-8")
    
    models_code = """from dataclasses import dataclass
import hashlib

@dataclass
class RedTeamDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class MisuseScenario:
    scenario_id: str
    scenario_name: str
    misuse_category: str
    abstract_description: str
    unsafe_request_pattern: str
    expected_safe_response: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class AbuseCaseSimulation:
    simulation_id: str
    simulation_name: str
    misuse_category: str
    simulated_condition: str
    expected_boundary: str
    expected_response_label: str
    dry_run_only: bool
    warnings: list[str]

@dataclass
class SafetyChecklistItem:
    checklist_id: str
    checklist_area: str
    check_name: str
    expected_result: str
    blocking_if_failed: bool
    warnings: list[str]

@dataclass
class RedTeamFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_redteam_domain_id(domain_label: str) -> str:
    s = f"redteam_domain_{domain_label}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_misuse_scenario_id(scenario_name: str, misuse_category: str) -> str:
    s = f"misuse_scenario_{scenario_name}_{misuse_category}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_abuse_case_simulation_id(simulation_name: str, misuse_category: str) -> str:
    s = f"abuse_case_simulation_{simulation_name}_{misuse_category}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_safety_checklist_item_id(checklist_area: str, check_name: str) -> str:
    s = f"safety_checklist_{checklist_area}_{check_name}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def build_redteam_finding_id(title: str) -> str:
    s = f"redteam_finding_{title}"
    return hashlib.md5(s.encode()).hexdigest()[:12]

def redteam_domain_to_dict(item: RedTeamDomain) -> dict:
    return {
        "domain_id": item.domain_id,
        "domain_label": item.domain_label,
        "domain_name": item.domain_name,
        "description": item.description,
        "required_outputs": "|".join(item.required_outputs),
        "warnings": "|".join(item.warnings)
    }

def misuse_scenario_to_dict(item: MisuseScenario) -> dict:
    return {
        "scenario_id": item.scenario_id,
        "scenario_name": item.scenario_name,
        "misuse_category": item.misuse_category,
        "abstract_description": item.abstract_description,
        "unsafe_request_pattern": item.unsafe_request_pattern,
        "expected_safe_response": item.expected_safe_response,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }

def abuse_case_simulation_to_dict(item: AbuseCaseSimulation) -> dict:
    return {
        "simulation_id": item.simulation_id,
        "simulation_name": item.simulation_name,
        "misuse_category": item.misuse_category,
        "simulated_condition": item.simulated_condition,
        "expected_boundary": item.expected_boundary,
        "expected_response_label": item.expected_response_label,
        "dry_run_only": item.dry_run_only,
        "warnings": "|".join(item.warnings)
    }

def safety_checklist_item_to_dict(item: SafetyChecklistItem) -> dict:
    return {
        "checklist_id": item.checklist_id,
        "checklist_area": item.checklist_area,
        "check_name": item.check_name,
        "expected_result": item.expected_result,
        "blocking_if_failed": item.blocking_if_failed,
        "warnings": "|".join(item.warnings)
    }

def redteam_finding_to_dict(item: RedTeamFinding) -> dict:
    return {
        "finding_id": item.finding_id,
        "risk_label": item.risk_label,
        "title": item.title,
        "description": item.description,
        "recommendation": item.recommendation,
        "manual_review_required": item.manual_review_required,
        "warnings": "|".join(item.warnings)
    }
"""
    (base_dir / "redteam_models.py").write_text(models_code, encoding="utf-8")
    
    registry_code = """import pandas as pd
from local_redteam.redteam_config import LocalRedTeamProfile
from local_redteam.redteam_models import RedTeamDomain, build_redteam_domain_id, redteam_domain_to_dict

def build_default_redteam_domains(profile: LocalRedTeamProfile) -> list[RedTeamDomain]:
    labels = [
        "redteam_rehearsal_domain", "misuse_scenario_domain", "abuse_case_simulation_domain",
        "adversarial_prompt_safety_domain", "prompt_injection_risk_domain", "unsafe_output_domain",
        "forbidden_capability_domain", "boundary_violation_domain", "safety_response_domain",
        "manual_escalation_domain", "safety_assurance_domain", "safety_coverage_domain",
        "quality_validation_domain"
    ]
    domains = []
    for label in labels:
        domains.append(RedTeamDomain(
            domain_id=build_redteam_domain_id(label),
            domain_label=label,
            domain_name=label.replace("_", " ").title(),
            description=f"Offline/local {label.replace('_', ' ')} logic.",
            required_outputs=[f"{label}_output_1", f"{label}_output_2"],
            warnings=["Bu domain offline/local dokümantasyon içindir, gerçek attack/exploit içermez."]
        ))
    return domains

def build_redteam_domain_registry(profile: LocalRedTeamProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_redteam_domains(profile)
    df = pd.DataFrame([redteam_domain_to_dict(d) for d in domains])
    summary = summarize_redteam_domains(df)
    return df, summary

def summarize_redteam_domains(domain_df: pd.DataFrame) -> dict:
    return {
        "total_domains": len(domain_df),
        "domains_listed": domain_df["domain_label"].tolist() if not domain_df.empty else [],
        "note": "Domain registry is for offline/local rehearsal only."
    }
"""
    (base_dir / "redteam_domain_registry.py").write_text(registry_code, encoding="utf-8")

    packet_code = """from pathlib import Path
from local_redteam.redteam_config import LocalRedTeamProfile

def build_redteam_rehearsal_sections(project_root: Path, profile: LocalRedTeamProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Bu doküman sistemin sınırlarını test eden offline provadır."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek red-team raporu, exploit payload, jailbreak veya production safety approval değildir."},
        {"title": "Safety boundary recap", "content": "Sistem cloud upload, telemetry, broker execution, live trading ve investment advice gibi yeteneklere kapalıdır."},
        {"title": "Misuse scenario families", "content": "Live trading, broker execution, secret exposure vb."},
        {"title": "Abuse-case simulation recap", "content": "Tüm testler dry-run olarak yapılmıştır."},
        {"title": "Adversarial prompt safety checklist recap", "content": "Jailbreak denemeleri abstract düzeyde loglanmıştır."},
        {"title": "Prompt-injection risk pattern recap", "content": "Enjeksiyon patternleri payload olmadan listelenmiştir."},
        {"title": "Forbidden capability request recap", "content": "Engellenen yetenekler kaydedilmiştir."},
        {"title": "Manual escalation recap", "content": "Riskli durumlar insan incelemesine yönlendirilir."},
        {"title": "Safety assurance coverage recap", "content": "Kapsam matrix ile belirlenmiştir."},
        {"title": "Blindspots and gaps", "content": "Görünmeyen noktalar manuel inceleme gerektirir."},
        {"title": "Red-team no-go/safe-go", "content": "No-go: gerçek attack. Safe-go: offline rehearsal."},
        {"title": "Final boundary statement", "content": "Sistem local, offline ve denetlenebilirdir."}
    ]

def build_final_local_redteam_rehearsal_packet(project_root: Path, profile: LocalRedTeamProfile) -> tuple[str, dict]:
    sections = build_redteam_rehearsal_sections(project_root, profile)
    text = "FINAL LOCAL REDTEAM REHEARSAL PACKET\\n========================================\\n\\n"
    for sec in sections:
        text += f"## {sec['title']}\\n{sec['content']}\\n\\n"
    summary = summarize_redteam_rehearsal_packet(text)
    return text, summary

def summarize_redteam_rehearsal_packet(text: str) -> dict:
    return {
        "length": len(text),
        "sections": text.count("## "),
        "note": "Packet is not a real attack or certification."
    }

def save_redteam_rehearsal_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    return output_path
"""
    (base_dir / "redteam_rehearsal_packet.py").write_text(packet_code, encoding="utf-8")
    
    print("Created local_redteam core files")

if __name__ == "__main__":
    create_local_redteam_core()
