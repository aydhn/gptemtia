from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class ResearchReportProfile:
    name: str
    description: str
    language: str = "tr"
    max_symbols: int = 50
    max_rows_per_table: int = 20
    include_technical_summary: bool = True
    include_risk_level_summary: bool = True
    include_backtest_summary: bool = True
    include_performance_summary: bool = True
    include_validation_summary: bool = True
    include_ml_summary: bool = True
    include_paper_summary: bool = True
    include_quality_summary: bool = True
    output_markdown: bool = True
    output_csv: bool = True
    output_txt: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_research_report": ResearchReportProfile(
        name="balanced_research_report",
        description="Genel amaçlı sembol ve evren araştırma raporu profili.",
        notes="Genel amaçlı sembol ve evren araştırma raporu profili.",
    ),
    "technical_focused_research_report": ResearchReportProfile(
        name="technical_focused_research_report",
        description="Teknik görünüm ve aday seviyeleri odaklı rapor.",
        include_backtest_summary=False,
        include_performance_summary=False,
        include_validation_summary=False,
        include_ml_summary=False,
        include_paper_summary=False,
        notes="Teknik görünüm ve aday seviyeleri odaklı rapor."
    ),
    "backtest_validation_research_report": ResearchReportProfile(
        name="backtest_validation_research_report",
        description="Backtest, benchmark, walk-forward ve overfitting araştırma özeti.",
        include_technical_summary=False,
        include_ml_summary=False,
        include_paper_summary=False,
        notes="Backtest, benchmark, walk-forward ve overfitting araştırma özeti."
    ),
    "ml_research_report": ResearchReportProfile(
        name="ml_research_report",
        description="ML dataset/model/prediction/integration araştırma özeti.",
        include_technical_summary=False,
        include_risk_level_summary=False,
        include_backtest_summary=False,
        include_performance_summary=False,
        include_paper_summary=False,
        notes="ML dataset/model/prediction/integration araştırma özeti."
    ),
    "paper_digest_research_report": ResearchReportProfile(
        name="paper_digest_research_report",
        description="Paper simulation ve ML context günlük digest profili.",
        include_technical_summary=False,
        include_backtest_summary=False,
        include_performance_summary=False,
        include_validation_summary=False,
        notes="Paper simulation ve ML context günlük digest profili."
    ),
}

def get_research_report_profile(name: str) -> ResearchReportProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown research report profile: {name}")
    return _PROFILES[name]

def list_research_report_profiles(enabled_only: bool = True) -> list[ResearchReportProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_research_report_profiles() -> None:
    for profile in _PROFILES.values():
        if profile.max_symbols <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid max_symbols: {profile.max_symbols}")
        if profile.max_rows_per_table <= 0:
            raise ConfigError(f"Profile {profile.name} has invalid max_rows_per_table: {profile.max_rows_per_table}")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {profile.name} has invalid min_quality_score: {profile.min_quality_score}")
        if profile.language not in ("tr", "en"):
            raise ConfigError(f"Profile {profile.name} has unsupported language: {profile.language}")

def get_default_research_report_profile() -> ResearchReportProfile:
    from config.settings import settings
    return get_research_report_profile(settings.default_research_report_profile)
