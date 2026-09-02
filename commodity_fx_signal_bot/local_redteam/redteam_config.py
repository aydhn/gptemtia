from dataclasses import dataclass

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
