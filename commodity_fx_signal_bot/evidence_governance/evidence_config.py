from dataclasses import dataclass

@dataclass(frozen=True)
class EvidenceGovernanceProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_official_compliance_claims: bool = False
    allow_legal_opinion: bool = False
    allow_cloud_export: bool = False
    allow_external_auditor_upload: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    allow_external_llm: bool = False
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_docs: bool = True
    scan_generated_docs: bool = True
    scan_quality_outputs: bool = True
    scan_security_outputs: bool = True
    max_artifacts: int = 200000
    max_artifact_mb: int = 50
    freshness_days_warning: int = 30
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def get_evidence_governance_profile(name: str) -> EvidenceGovernanceProfile:
    profiles = {p.name: p for p in list_evidence_governance_profiles()}
    if name not in profiles:
        raise ValueError(f"Unknown evidence governance profile: {name}")
    return profiles[name]

def list_evidence_governance_profiles(enabled_only: bool = True) -> list[EvidenceGovernanceProfile]:
    profiles = [
        EvidenceGovernanceProfile(
            name="balanced_local_evidence",
            description="Default balanced profile",
            notes="Genel amaçlı local/offline evidence binder ve control mapping profili."
        ),
        EvidenceGovernanceProfile(
            name="strict_evidence_boundary",
            description="Strict boundary profile",
            max_artifact_mb=20,
            freshness_days_warning=14,
            min_quality_score=0.60,
            notes="Daha sıkı evidence freshness, secret boundary ve official-claim kontrolü profili."
        ),
        EvidenceGovernanceProfile(
            name="security_evidence_focus",
            description="Security focus profile",
            freshness_days_warning=21,
            notes="Secrets hygiene, backup safety, packaging safety, master safety ve final safety evidence odaklı profil."
        ),
        EvidenceGovernanceProfile(
            name="operator_evidence_pack",
            description="Operator profile",
            max_artifacts=100000,
            notes="Operatörün local evidence binder, digest ve traceability raporlarını hızlı üretmesi için profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_evidence_governance_profiles() -> None:
    profiles = list_evidence_governance_profiles(enabled_only=False)
    for p in profiles:
        if not p.language:
            raise ValueError(f"Profile {p.name} must have a language")
        if p.max_artifacts <= 0:
            raise ValueError(f"Profile {p.name} max_artifacts must be positive")
        if p.max_artifact_mb <= 0:
            raise ValueError(f"Profile {p.name} max_artifact_mb must be positive")
        if p.freshness_days_warning <= 0:
            raise ValueError(f"Profile {p.name} freshness_days_warning must be positive")
        if p.min_quality_score < 0.0 or p.min_quality_score > 1.0:
            raise ValueError(f"Profile {p.name} min_quality_score must be between 0 and 1")
        if not p.dry_run_default:
            raise ValueError(f"Profile {p.name} dry_run_default must be True")
        if p.allow_official_compliance_claims or p.allow_legal_opinion or p.allow_cloud_export or p.allow_external_auditor_upload or p.allow_file_modification or p.allow_file_deletion:
            raise ValueError(f"Profile {p.name} allow flags must be False")

def get_default_evidence_governance_profile() -> EvidenceGovernanceProfile:
    from config.settings import Settings
    s = Settings()
    return get_evidence_governance_profile(s.default_evidence_governance_profile)
