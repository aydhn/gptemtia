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
