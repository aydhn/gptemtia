import os
import re

with open("commodity_fx_signal_bot/config/settings.py", "r") as f:
    settings_content = f.read()

settings_injection = """
    # Evidence Governance Settings
    evidence_governance_enabled: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ENABLED", "true")).lower() == "true")
    default_evidence_governance_profile: str = field(default_factory=lambda: os.getenv("DEFAULT_EVIDENCE_GOVERNANCE_PROFILE", "balanced_local_evidence"))
    evidence_governance_default_language: str = field(default_factory=lambda: os.getenv("EVIDENCE_GOVERNANCE_DEFAULT_LANGUAGE", "tr"))
    evidence_governance_dry_run_default: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_DRY_RUN_DEFAULT", "true")).lower() == "true")
    evidence_governance_allow_official_compliance_claims: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_OFFICIAL_COMPLIANCE_CLAIMS", "false")).lower() == "true")
    evidence_governance_allow_legal_opinion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LEGAL_OPINION", "false")).lower() == "true")
    evidence_governance_allow_cloud_export: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_CLOUD_EXPORT", "false")).lower() == "true")
    evidence_governance_allow_external_auditor_upload: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_AUDITOR_UPLOAD", "false")).lower() == "true")
    evidence_governance_allow_file_modification: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_MODIFICATION", "false")).lower() == "true")
    evidence_governance_allow_file_deletion: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_FILE_DELETION", "false")).lower() == "true")
    evidence_governance_allow_live_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_LIVE_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_broker_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BROKER_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_deploy_commands: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_DEPLOY_COMMANDS", "false")).lower() == "true")
    evidence_governance_allow_background_daemons: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_BACKGROUND_DAEMONS", "false")).lower() == "true")
    evidence_governance_allow_real_market_download: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_REAL_MARKET_DOWNLOAD", "false")).lower() == "true")
    evidence_governance_allow_external_llm: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_ALLOW_EXTERNAL_LLM", "false")).lower() == "true")
    evidence_governance_scan_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_REPORTS", "true")).lower() == "true")
    evidence_governance_scan_data_lake: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DATA_LAKE", "true")).lower() == "true")
    evidence_governance_scan_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_DOCS", "true")).lower() == "true")
    evidence_governance_scan_generated_docs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_GENERATED_DOCS", "true")).lower() == "true")
    evidence_governance_scan_quality_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_QUALITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_scan_security_outputs: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SCAN_SECURITY_OUTPUTS", "true")).lower() == "true")
    evidence_governance_max_artifacts: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACTS", "200000")))
    evidence_governance_max_artifact_mb: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_MAX_ARTIFACT_MB", "50")))
    evidence_governance_freshness_days_warning: int = field(default_factory=lambda: int(os.getenv("EVIDENCE_GOVERNANCE_FRESHNESS_DAYS_WARNING", "30")))
    evidence_governance_save_reports: bool = field(default_factory=lambda: str(os.getenv("EVIDENCE_GOVERNANCE_SAVE_REPORTS", "true")).lower() == "true")
    evidence_governance_min_quality_score: float = field(default_factory=lambda: float(os.getenv("EVIDENCE_GOVERNANCE_MIN_QUALITY_SCORE", "0.40")))

    def __post_init__(self):
"""

if "evidence_governance_enabled" not in settings_content:
    settings_content = re.sub(r'    def __post_init__\(self\):', settings_injection, settings_content)
    with open("commodity_fx_signal_bot/config/settings.py", "w") as f:
        f.write(settings_content)
