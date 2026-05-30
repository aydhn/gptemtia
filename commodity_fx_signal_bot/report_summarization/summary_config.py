from dataclasses import dataclass

@dataclass(frozen=True)
class ReportSummaryProfile:
    name: str
    description: str
    language: str = "tr"
    use_local_only: bool = True
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_reports_output: bool = True
    scan_data_lake: bool = True
    scan_docs: bool = True
    max_reports: int = 5000
    max_chars_per_report: int = 20000
    max_summary_bullets: int = 12
    max_findings: int = 100
    max_warnings: int = 100
    max_follow_up_tasks: int = 50
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_profiles: dict[str, ReportSummaryProfile] = {}

class ConfigError(Exception):
    pass

def _register_profiles() -> None:
    balanced = ReportSummaryProfile(
        name="balanced_local_summaries",
        description="Genel amacli Turkce local/offline rapor ozetleme profili.",
        language="tr",
        use_local_only=True,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        scan_reports_output=True,
        scan_data_lake=True,
        scan_docs=True,
        max_reports=5000,
        max_chars_per_report=20000,
        max_summary_bullets=12,
        notes="Genel amacli Turkce local/offline rapor ozetleme profili."
    )

    executive = ReportSummaryProfile(
        name="executive_brief_summaries",
        description="Kisa executive summary ve ust seviye offline arastirma ozeti icin profil.",
        language="tr",
        use_local_only=True,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        max_summary_bullets=8,
        max_findings=50,
        max_warnings=50,
        notes="Kisa executive summary ve ust seviye offline arastirma ozeti icin profil."
    )

    analyst = ReportSummaryProfile(
        name="analyst_deep_brief_summaries",
        description="Analist icin daha derin finding/warning/follow-up cikarimi yapan profil.",
        language="tr",
        use_local_only=True,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        max_summary_bullets=20,
        max_findings=200,
        max_warnings=200,
        max_follow_up_tasks=100,
        notes="Analist icin daha derin finding/warning/follow-up cikarimi yapan profil."
    )

    weekly = ReportSummaryProfile(
        name="weekly_review_summaries",
        description="Haftalik offline review pack uretimine odakli profil.",
        language="tr",
        use_local_only=True,
        allow_external_llm=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        allow_real_market_download=False,
        max_summary_bullets=15,
        max_findings=150,
        max_warnings=150,
        notes="Haftalik offline review pack uretimine odakli profil."
    )

    _profiles[balanced.name] = balanced
    _profiles[executive.name] = executive
    _profiles[analyst.name] = analyst
    _profiles[weekly.name] = weekly

_register_profiles()

def get_report_summary_profile(name: str) -> ReportSummaryProfile:
    if name not in _profiles:
        raise ConfigError(f"Unknown profile: {name}")
    return _profiles[name]

def list_report_summary_profiles(enabled_only: bool = True) -> list[ReportSummaryProfile]:
    return [p for p in _profiles.values() if not enabled_only or p.enabled]

def validate_report_summary_profiles() -> None:
    for profile in _profiles.values():
        if not profile.language:
            raise ConfigError(f"Profile {profile.name} language cannot be empty.")
        if profile.max_reports <= 0:
            raise ConfigError(f"Profile {profile.name} max_reports must be positive.")
        if profile.max_chars_per_report <= 0:
            raise ConfigError(f"Profile {profile.name} max_chars_per_report must be positive.")
        if profile.max_summary_bullets <= 0:
            raise ConfigError(f"Profile {profile.name} max_summary_bullets must be positive.")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {profile.name} min_quality_score must be between 0 and 1.")
        if not profile.use_local_only:
            raise ConfigError(f"Profile {profile.name} use_local_only must be True.")
        if profile.allow_external_llm:
            raise ConfigError(f"Profile {profile.name} allow_external_llm must be False.")
        if profile.allow_live_commands or profile.allow_broker_commands or profile.allow_deploy_commands or profile.allow_background_daemons or profile.allow_real_market_download:
            raise ConfigError(f"Profile {profile.name} unsafe features must be disabled.")
        if not (profile.scan_reports_output or profile.scan_data_lake or profile.scan_docs):
            raise ConfigError(f"Profile {profile.name} must have at least one scan flag set to True.")

def get_default_report_summary_profile() -> ReportSummaryProfile:
    from config.settings import settings
    return get_report_summary_profile(settings.default_report_summary_profile)
