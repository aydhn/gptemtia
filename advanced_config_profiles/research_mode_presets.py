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
