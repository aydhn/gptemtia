import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file('advanced_config_profiles/__init__.py', '')

write_file('advanced_config_profiles/advanced_config.py', '''
from dataclasses import dataclass

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AdvancedConfigSystemProfile:
    name: str
    description: str
    language: str = "tr"
    current_phase: int = 104
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
    enable_profile_composition: bool = True
    enable_profile_compatibility_matrix: bool = True
    enable_profile_validation: bool = True
    enable_profile_quality_report: bool = True
    max_profiles: int = 1000
    max_composed_profiles: int = 5000
    min_readiness_score: float = 0.45
    min_quality_score: float = 0.45
    enabled: bool = True
    notes: str = ""

def get_default_advanced_config_system_profile() -> AdvancedConfigSystemProfile:
    return AdvancedConfigSystemProfile(
        name="balanced_advanced_config",
        description="Phase 104 Advanced Config Profile System için dengeli local/offline config profili.",
        notes="Phase 104 Advanced Config Profile System için dengeli local/offline config profili."
    )

def list_advanced_config_system_profiles(enabled_only: bool = True) -> list[AdvancedConfigSystemProfile]:
    profiles = [
        get_default_advanced_config_system_profile(),
        AdvancedConfigSystemProfile(
            name="strict_config_safety",
            description="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen config profili.",
            min_readiness_score=0.65,
            min_quality_score=0.65,
            notes="Canlı trading, broker, deployment, scraping, external API ve yatırım tavsiyesi sınırlarını sıkı denetleyen config profili."
        ),
        AdvancedConfigSystemProfile(
            name="profile_composition_focus",
            description="Araştırma modu, evren, zaman dilimi, strateji ve risk profillerini kompoze etmeye odaklı profil.",
            enable_profile_composition=True,
            enable_profile_compatibility_matrix=True,
            notes="Araştırma modu, evren, zaman dilimi, strateji ve risk profillerini kompoze etmeye odaklı profil."
        )
    ]
    if enabled_only:
        return [p for p in profiles if p.enabled]
    return profiles

def get_advanced_config_system_profile(name: str) -> AdvancedConfigSystemProfile:
    for p in list_advanced_config_system_profiles(enabled_only=False):
        if p.name == name:
            return p
    raise ConfigError(f"Unknown profile: {name}")

def validate_advanced_config_system_profiles() -> None:
    for p in list_advanced_config_system_profiles(enabled_only=False):
        assert p.current_phase == 104
        assert p.target_final_phase == 160
        assert p.dry_run_default is True
        assert p.local_only is True
        assert p.non_production is True
        assert p.research_only is True
        assert not p.allow_live_trading
        assert not p.allow_broker_integration
        assert not p.allow_real_order
        assert not p.allow_investment_advice
        assert not p.allow_model_deployment
        assert not p.allow_production_deployment
        assert not p.allow_web_server
        assert not p.allow_dashboard
        assert not p.allow_gui_tui
        assert not p.allow_external_llm
        assert not p.allow_vector_db
        assert not p.allow_embedding_api
        assert not p.allow_web_scraping
        assert not p.allow_cloud_publish
        assert not p.allow_docker_push
        assert not p.allow_git_tag
        assert not p.allow_archive_creation
        assert not p.allow_file_deletion
        assert not p.allow_file_move
        assert not p.allow_overwrite
        assert 0 <= p.min_readiness_score <= 1
        assert 0 <= p.min_quality_score <= 1
''')

write_file('advanced_config_profiles/advanced_config_labels.py', '''
class AdvancedConfigLabels:
    pass

def list_profile_domain_labels():
    return [
        "config_profile_domain",
        "research_mode_domain",
        "universe_profile_domain",
        "timeframe_profile_domain",
        "asset_class_profile_domain",
        "strategy_family_profile_domain",
        "risk_preference_profile_domain",
        "data_provider_preference_domain",
        "feature_profile_domain",
        "regime_profile_domain",
        "ml_profile_domain",
        "backtest_profile_domain",
        "portfolio_profile_domain",
        "report_profile_domain",
        "safety_profile_domain",
        "composed_profile_domain",
        "compatibility_domain",
        "validation_domain",
        "quality_domain",
        "unknown_profile_domain"
    ]

def list_research_mode_labels():
    return [
        "mode_short_term_research",
        "mode_medium_term_research",
        "mode_long_term_research",
        "mode_intraday_research_no_live",
        "mode_swing_research",
        "mode_macro_sensitive_research",
        "mode_regime_sensitive_research",
        "mode_volatility_research",
        "mode_cross_asset_research",
        "mode_portfolio_research"
    ]

def list_risk_preference_labels():
    return [
        "risk_conservative",
        "risk_balanced",
        "risk_aggressive_research",
        "risk_low_drawdown_focus",
        "risk_volatility_adjusted",
        "risk_experimental_research_only"
    ]

def list_profile_status_labels():
    return [
        "profile_ready",
        "profile_ready_with_warnings",
        "profile_missing",
        "profile_incompatible",
        "profile_blocked_by_safety",
        "profile_needs_manual_review",
        "profile_unknown"
    ]

def validate_profile_domain_label(label: str):
    if label not in list_profile_domain_labels():
        raise ValueError(f"Invalid profile domain label: {label}")

def validate_research_mode_label(label: str):
    if label not in list_research_mode_labels():
        raise ValueError(f"Invalid research mode label: {label}")

def validate_risk_preference_label(label: str):
    if label not in list_risk_preference_labels():
        raise ValueError(f"Invalid risk preference label: {label}")

def validate_profile_status(label: str):
    if label not in list_profile_status_labels():
        raise ValueError(f"Invalid profile status label: {label}")
''')

write_file('advanced_config_profiles/advanced_config_models.py', '''
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
''')

write_file('advanced_config_profiles/config_profile_registry.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_config_profile_items(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    domains = [
        "research modes", "universe profiles", "timeframe profiles", "asset class profiles",
        "strategy family profiles", "risk preference profiles", "data provider preference profiles",
        "feature profiles", "regime profiles", "ML profiles", "backtest profiles",
        "portfolio profiles", "report profiles", "safety profiles"
    ]
    items = []
    for d in domains:
        items.append(ConfigProfileItem(
            profile_id=build_config_profile_id(d.replace(" ", "_"), "default"),
            profile_domain=d,
            profile_name="default",
            description=f"Default profile for {d}",
            parameters={"is_default": True},
            status_label="profile_ready",
            warnings=[],
            manual_review_required=False
        ))
    return items

def build_advanced_config_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_config_profile_items(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    summary = summarize_config_profile_registry(df)
    return df, summary

def summarize_config_profile_registry(df: pd.DataFrame) -> dict:
    return {
        "total_profiles": len(df) if df is not None else 0,
        "domains": df['profile_domain'].unique().tolist() if df is not None and not df.empty else []
    }
''')

write_file('advanced_config_profiles/research_mode_presets.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ResearchModePreset, research_mode_preset_to_dict, build_research_mode_preset_id

def build_default_research_mode_presets(profile: AdvancedConfigSystemProfile) -> list[ResearchModePreset]:
    presets = [
        "short_term_fx_research", "medium_term_fx_research", "long_term_macro_fx_research",
        "gold_macro_research", "oil_macro_research", "broad_commodities_research",
        "cross_asset_macro_research", "volatility_regime_research", "trend_following_research",
        "mean_reversion_research", "portfolio_simulation_research", "intraday_research_no_live"
    ]
    items = []
    for p in presets:
        items.append(ResearchModePreset(
            preset_id=build_research_mode_preset_id(p),
            mode_label=p,
            preset_name=p.replace("_", " ").title(),
            objective=f"Research preset for {p}",
            default_universe_profile="default",
            default_timeframe_profile="default",
            default_risk_profile="default",
            default_report_profile="default",
            warnings=["Canlı işlem iddiası yok", "Yatırım tavsiyesi değildir", "dry-run/local-only"]
        ))
    return items

def build_research_mode_preset_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_research_mode_presets(profile)
    df = pd.DataFrame([research_mode_preset_to_dict(item) for item in items])
    summary = summarize_research_mode_presets(df)
    return df, summary

def summarize_research_mode_presets(df: pd.DataFrame) -> dict:
    return {
        "total_presets": len(df) if df is not None else 0
    }
''')

write_file('advanced_config_profiles/universe_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_universe_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["major_fx_pairs", "extended_fx_pairs", "precious_metals", "energy_commodities", 
             "industrial_metals", "agriculture_commodities", "macro_cross_asset", "custom_research_universe_placeholder"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("universe_profile_domain", n),
        profile_domain="universe_profile_domain",
        profile_name=n,
        description=f"Universe profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_universe_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_universe_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_universe_profiles(df)

def summarize_universe_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/timeframe_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_timeframe_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["1h_research_no_live", "4h_research", "daily_research", "weekly_research", 
             "multi_timeframe_research", "macro_event_window_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("timeframe_profile_domain", n),
        profile_domain="timeframe_profile_domain",
        profile_name=n,
        description=f"Timeframe profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_timeframe_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_timeframe_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_timeframe_profiles(df)

def summarize_timeframe_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/asset_class_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_asset_class_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["fx", "precious_metals", "energy", "industrial_metals", "agriculture", "macro_indicators", "cross_asset"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("asset_class_profile_domain", n),
        profile_domain="asset_class_profile_domain",
        profile_name=n,
        description=f"Asset class profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_asset_class_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_asset_class_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_asset_class_profiles(df)

def summarize_asset_class_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/strategy_family_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_strategy_family_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["trend_following_research", "mean_reversion_research", "volatility_breakout_research", 
             "macro_event_research", "regime_adaptive_research", "cross_asset_confirmation_research", 
             "ensemble_research", "portfolio_signal_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("strategy_family_profile_domain", n),
        profile_domain="strategy_family_profile_domain",
        profile_name=n,
        description=f"Strategy family profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_strategy_family_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_strategy_family_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_strategy_family_profiles(df)

def summarize_strategy_family_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/risk_preference_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_risk_preference_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["conservative_research", "balanced_research", "aggressive_research_only", 
             "low_drawdown_research", "volatility_adjusted_research", "experimental_research_only"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("risk_preference_profile_domain", n),
        profile_domain="risk_preference_profile_domain",
        profile_name=n,
        description=f"Risk preference profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["Risk profiles sadece simülasyon ve araştırma bağlamıdır", "Gerçek portföy yönetimi değildir"],
        manual_review_required=False
    ) for n in names]

def build_risk_preference_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_risk_preference_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_risk_preference_profiles(df)

def summarize_risk_preference_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/data_provider_preference_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_data_provider_preference_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_scraping_public_api_preferred", "local_cache_preferred", "manual_file_import_preferred", 
             "official_provider_preferred", "macro_calendar_provider_placeholder", "news_metadata_provider_placeholder"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("data_provider_preference_domain", n),
        profile_domain="data_provider_preference_domain",
        profile_name=n,
        description=f"Data provider preference for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["Scraping yok", "Gerçek veri indirme değildir"],
        manual_review_required=False
    ) for n in names]

def build_data_provider_preference_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_data_provider_preference_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_data_provider_preference_profiles(df)

def summarize_data_provider_preference_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/feature_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_feature_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["minimal_technical_features", "standard_technical_features", "advanced_technical_features", 
             "volatility_features", "trend_momentum_features", "mean_reversion_features", 
             "macro_factor_features", "cross_asset_features", "full_feature_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("feature_profile_domain", n),
        profile_domain="feature_profile_domain",
        profile_name=n,
        description=f"Feature profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_feature_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_feature_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_feature_profiles(df)

def summarize_feature_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/regime_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_regime_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_regime_baseline", "volatility_regime", "trend_range_regime", 
             "macro_regime", "cross_asset_regime", "full_regime_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("regime_profile_domain", n),
        profile_domain="regime_profile_domain",
        profile_name=n,
        description=f"Regime profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_regime_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_regime_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_regime_profiles(df)

def summarize_regime_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/ml_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_ml_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["no_ml_baseline", "classical_ml_research", "time_series_ml_research", 
             "ensemble_ml_research", "gpu_optional_ml_research", "explainable_ml_research", "drift_aware_ml_research"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("ml_profile_domain", n),
        profile_domain="ml_profile_domain",
        profile_name=n,
        description=f"ML profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=["ML profile model deployment değildir", "GPU optional olmalı; CPU fallback notu bulunmalı"],
        manual_review_required=False
    ) for n in names]

def build_ml_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_ml_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_ml_profiles(df)

def summarize_ml_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')

write_file('advanced_config_profiles/backtest_profiles.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile
from .advanced_config_models import ConfigProfileItem, config_profile_item_to_dict, build_config_profile_id

def build_default_backtest_profiles(profile: AdvancedConfigSystemProfile) -> list[ConfigProfileItem]:
    names = ["simple_baseline_backtest", "cost_aware_backtest", "slippage_aware_backtest", 
             "walk_forward_backtest", "stress_test_backtest", "monte_carlo_robustness_backtest", "full_reliability_backtest"]
    return [ConfigProfileItem(
        profile_id=build_config_profile_id("backtest_profile_domain", n),
        profile_domain="backtest_profile_domain",
        profile_name=n,
        description=f"Backtest profile for {n}",
        parameters={},
        status_label="profile_ready",
        warnings=[],
        manual_review_required=False
    ) for n in names]

def build_backtest_profile_registry(profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_backtest_profiles(profile)
    df = pd.DataFrame([config_profile_item_to_dict(item) for item in items])
    return df, summarize_backtest_profiles(df)

def summarize_backtest_profiles(df: pd.DataFrame) -> dict:
    return {"total": len(df) if df is not None else 0}
''')
