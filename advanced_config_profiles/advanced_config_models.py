from dataclasses import dataclass

@dataclass
class ConfigProfileItem:
    profile_id: str
    profile_domain: str
    profile_name: str
    description: str
    parameters: dict
    status_label: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ResearchModePreset:
    preset_id: str
    mode_label: str
    preset_name: str
    objective: str
    default_universe_profile: str
    default_timeframe_profile: str
    default_risk_profile: str
    default_report_profile: str
    warnings: list[str]

@dataclass
class ComposedResearchProfile:
    composed_profile_id: str
    composed_profile_name: str
    research_mode: str
    universe_profile: str
    timeframe_profile: str
    asset_class_profile: str
    strategy_family_profile: str
    risk_preference_profile: str
    data_provider_preference_profile: str
    feature_profile: str
    regime_profile: str
    ml_profile: str
    backtest_profile: str
    portfolio_profile: str
    report_profile: str
    safety_profile: str
    compatibility_status: str
    warnings: list[str]
    manual_review_required: bool

@dataclass
class ProfileCompatibilityItem:
    compatibility_id: str
    left_profile: str
    right_profile: str
    compatibility_status: str
    reason: str
    manual_review_required: bool

@dataclass
class ProfileFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool

def build_config_profile_id(profile_domain: str, profile_name: str) -> str:
    return f"{profile_domain}_{profile_name}"

def build_research_mode_preset_id(mode_label: str) -> str:
    return f"preset_{mode_label}"

def build_composed_profile_id(composed_profile_name: str) -> str:
    return f"composed_{composed_profile_name}"

def build_profile_compatibility_id(left_profile: str, right_profile: str) -> str:
    return f"comp_{left_profile}_{right_profile}"

def build_profile_finding_id(title: str) -> str:
    return f"finding_{title.replace(' ', '_').lower()}"

def config_profile_item_to_dict(item: ConfigProfileItem) -> dict:
    return item.__dict__

def research_mode_preset_to_dict(item: ResearchModePreset) -> dict:
    return item.__dict__

def composed_research_profile_to_dict(item: ComposedResearchProfile) -> dict:
    return item.__dict__

def profile_compatibility_item_to_dict(item: ProfileCompatibilityItem) -> dict:
    return item.__dict__

def profile_finding_to_dict(item: ProfileFinding) -> dict:
    return item.__dict__
