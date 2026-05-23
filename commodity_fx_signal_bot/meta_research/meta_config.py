from dataclasses import dataclass

from config.settings import Settings


class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class MetaResearchProfile:
    name: str
    description: str
    min_sources: int = 3
    min_evidence_quality: float = 0.40
    conflict_threshold: float = 0.35
    high_agreement_threshold: float = 0.70
    uncertainty_penalty_enabled: bool = True
    quality_penalty_enabled: bool = True
    missing_source_penalty_enabled: bool = True
    include_technical: bool = True
    include_strategy: bool = True
    include_risk_level: bool = True
    include_backtest: bool = True
    include_validation: bool = True
    include_ml: bool = True
    include_paper: bool = True
    include_factor: bool = True
    include_synthetic_index: bool = True
    include_portfolio: bool = True
    include_regime: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

_META_RESEARCH_PROFILES = [
    MetaResearchProfile(
        name="balanced_meta_research",
        description="Balanced meta research configuration.",
        min_sources=3,
        min_evidence_quality=0.40,
        conflict_threshold=0.35,
        high_agreement_threshold=0.70,
        notes="Genel amaçlı multi-source meta research ve consensus profili."
    ),
    MetaResearchProfile(
        name="strict_meta_research",
        description="Strict meta research configuration.",
        min_sources=5,
        min_evidence_quality=0.55,
        conflict_threshold=0.25,
        high_agreement_threshold=0.75,
        uncertainty_penalty_enabled=True,
        quality_penalty_enabled=True,
        missing_source_penalty_enabled=True,
        min_quality_score=0.55,
        notes="Daha sıkı kalite, kaynak sayısı ve çelişki toleransı kullanan profil."
    ),
    MetaResearchProfile(
        name="technical_factor_meta_research",
        description="Technical and factor meta research configuration.",
        include_technical=True,
        include_strategy=True,
        include_risk_level=True,
        include_backtest=False,
        include_validation=False,
        include_ml=False,
        include_paper=False,
        include_factor=True,
        include_synthetic_index=True,
        include_portfolio=False,
        include_regime=False,
        notes="Teknik, strateji, sentetik index ve factor araştırmasını birleştirir."
    ),
    MetaResearchProfile(
        name="ml_validation_meta_research",
        description="ML and validation meta research configuration.",
        include_technical=False,
        include_strategy=False,
        include_risk_level=False,
        include_backtest=True,
        include_validation=True,
        include_ml=True,
        include_paper=True,
        include_factor=False,
        include_synthetic_index=False,
        include_portfolio=False,
        include_regime=False,
        notes="Backtest, validation, ML ve paper çıktılarından konsensüs üretir."
    )
]

def list_meta_research_profiles(enabled_only: bool = True) -> list[MetaResearchProfile]:
    if enabled_only:
        return [p for p in _META_RESEARCH_PROFILES if p.enabled]
    return _META_RESEARCH_PROFILES

def get_meta_research_profile(name: str) -> MetaResearchProfile:
    for profile in _META_RESEARCH_PROFILES:
        if profile.name == name:
            return profile
    raise ConfigError(f"Unknown meta research profile: {name}")

def get_default_meta_research_profile() -> MetaResearchProfile:
    settings = Settings()
    return get_meta_research_profile(settings.default_meta_research_profile)

def validate_meta_research_profiles() -> None:
    for profile in _META_RESEARCH_PROFILES:
        if profile.min_sources <= 0:
            raise ConfigError(f"Profile {profile.name} min_sources must be positive")
        if not (0 <= profile.min_evidence_quality <= 1):
            raise ConfigError(f"Profile {profile.name} min_evidence_quality must be between 0 and 1")
        if not (0 <= profile.conflict_threshold <= 1):
            raise ConfigError(f"Profile {profile.name} conflict_threshold must be between 0 and 1")
        if not (0 <= profile.high_agreement_threshold <= 1):
            raise ConfigError(f"Profile {profile.name} high_agreement_threshold must be between 0 and 1")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {profile.name} min_quality_score must be between 0 and 1")

        include_flags = [
            profile.include_technical,
            profile.include_strategy,
            profile.include_risk_level,
            profile.include_backtest,
            profile.include_validation,
            profile.include_ml,
            profile.include_paper,
            profile.include_factor,
            profile.include_synthetic_index,
            profile.include_portfolio,
            profile.include_regime
        ]
        if not any(include_flags):
            raise ConfigError(f"Profile {profile.name} must have at least one include flag set to True")
