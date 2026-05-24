from dataclasses import dataclass

@dataclass(frozen=True)
class ResearchPlanningProfile:
    name: str
    description: str
    research_planning_default_timeframe: str = "1d"
    max_backlog_items: int = 500
    max_next_best_experiments: int = 25
    min_priority_score: float = 0.35
    high_priority_threshold: float = 0.70
    include_governance_signals: bool = True
    include_experiment_signals: bool = True
    include_meta_signals: bool = True
    include_factor_signals: bool = True
    include_portfolio_signals: bool = True
    include_regime_signals: bool = True
    include_validation_signals: bool = True
    include_ml_signals: bool = True
    include_paper_signals: bool = True
    include_observability_signals: bool = True
    dry_run: bool = True
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

class ConfigError(Exception):
    pass

PROFILES = {
    "balanced_research_planning": ResearchPlanningProfile(
        name="balanced_research_planning",
        description="Balanced research planning profile.",
        max_backlog_items=500,
        max_next_best_experiments=25,
        min_priority_score=0.35,
        high_priority_threshold=0.70,
        dry_run=True,
        notes="Genel amaçlı offline research planning ve backlog profili."
    ),
    "strict_research_planning": ResearchPlanningProfile(
        name="strict_research_planning",
        description="Strict research planning profile.",
        max_backlog_items=1000,
        max_next_best_experiments=40,
        min_priority_score=0.45,
        high_priority_threshold=0.75,
        min_quality_score=0.55,
        dry_run=True,
        notes="Daha sıkı kalite ve öncelik eşiği kullanan planlama profili."
    ),
    "experiment_focused_planning": ResearchPlanningProfile(
        name="experiment_focused_planning",
        description="Experiment focused research planning profile.",
        include_factor_signals=False,
        include_portfolio_signals=False,
        include_regime_signals=False,
        max_next_best_experiments=50,
        dry_run=True,
        notes="Experiment tracking, validation, ML ve paper çıktılarından backlog üretmeye odaklı profil."
    ),
    "governance_debt_planning": ResearchPlanningProfile(
        name="governance_debt_planning",
        description="Governance debt planning profile.",
        include_meta_signals=False,
        include_factor_signals=False,
        include_portfolio_signals=False,
        include_regime_signals=False,
        dry_run=True,
        notes="Governance, lineage, audit, freshness ve integrity borçlarını önceliklendiren profil."
    )
}

def get_research_planning_profile(name: str) -> ResearchPlanningProfile:
    if name not in PROFILES:
        raise ConfigError(f"Unknown research planning profile: {name}")
    return PROFILES[name]

def list_research_planning_profiles(enabled_only: bool = True) -> list[ResearchPlanningProfile]:
    profiles = list(PROFILES.values())
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def validate_research_planning_profiles() -> None:
    for name, profile in PROFILES.items():
        if profile.max_backlog_items <= 0:
            raise ConfigError(f"Profile {name} has invalid max_backlog_items")
        if profile.max_next_best_experiments <= 0:
            raise ConfigError(f"Profile {name} has invalid max_next_best_experiments")
        if not (0 <= profile.min_priority_score <= 1):
            raise ConfigError(f"Profile {name} has invalid min_priority_score")
        if not (0 <= profile.high_priority_threshold <= 1):
            raise ConfigError(f"Profile {name} has invalid high_priority_threshold")
        if profile.high_priority_threshold < profile.min_priority_score:
            raise ConfigError(f"Profile {name} high_priority_threshold < min_priority_score")
        if not (0 <= profile.min_quality_score <= 1):
            raise ConfigError(f"Profile {name} has invalid min_quality_score")
        if not profile.dry_run:
            raise ConfigError(f"Profile {name} dry_run must be True")

        any_include = (
            profile.include_governance_signals or
            profile.include_experiment_signals or
            profile.include_meta_signals or
            profile.include_factor_signals or
            profile.include_portfolio_signals or
            profile.include_regime_signals or
            profile.include_validation_signals or
            profile.include_ml_signals or
            profile.include_paper_signals or
            profile.include_observability_signals
        )
        if not any_include:
            raise ConfigError(f"Profile {name} must have at least one include flag True")

def get_default_research_planning_profile() -> ResearchPlanningProfile:
    return PROFILES["balanced_research_planning"]
