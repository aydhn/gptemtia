import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file('tests/test_advanced_config.py', '''
import pytest
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile, validate_advanced_config_system_profiles

def test_default_profile():
    p = get_default_advanced_config_system_profile()
    assert p.current_phase == 104
    assert p.target_final_phase == 160
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False

def test_validation():
    validate_advanced_config_system_profiles()
''')

write_file('tests/test_advanced_config_labels.py', '''
from advanced_config_profiles.advanced_config_labels import list_profile_domain_labels

def test_labels():
    labels = list_profile_domain_labels()
    assert "config_profile_domain" in labels
''')

write_file('tests/test_advanced_config_models.py', '''
from advanced_config_profiles.advanced_config_models import ConfigProfileItem

def test_model():
    c = ConfigProfileItem("id", "domain", "name", "desc", {}, "ready", [], False)
    assert c.profile_id == "id"
''')

write_file('tests/test_config_profile_registry.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.config_profile_registry import build_advanced_config_profile_registry

def test_registry():
    p = get_default_advanced_config_system_profile()
    df, summary = build_advanced_config_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_research_mode_presets.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.research_mode_presets import build_research_mode_preset_registry

def test_research_mode_presets():
    p = get_default_advanced_config_system_profile()
    df, summary = build_research_mode_preset_registry(p)
    assert len(df) > 0
    # verify presets
    presets = df["mode_label"].tolist()
    assert "short_term_fx_research" in presets
''')

write_file('tests/test_universe_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.universe_profiles import build_universe_profile_registry

def test_universe():
    p = get_default_advanced_config_system_profile()
    df, summary = build_universe_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "major_fx_pairs" in names
    assert "precious_metals" in names
''')

write_file('tests/test_timeframe_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.timeframe_profiles import build_timeframe_profile_registry

def test_timeframe():
    p = get_default_advanced_config_system_profile()
    df, summary = build_timeframe_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "daily_research" in names
    assert "multi_timeframe_research" in names
''')

write_file('tests/test_asset_class_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.asset_class_profiles import build_asset_class_profile_registry

def test_asset_class():
    p = get_default_advanced_config_system_profile()
    df, summary = build_asset_class_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_strategy_family_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.strategy_family_profiles import build_strategy_family_profile_registry

def test_strategy_family():
    p = get_default_advanced_config_system_profile()
    df, summary = build_strategy_family_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "trend_following_research" in names
    assert "mean_reversion_research" in names
''')

write_file('tests/test_risk_preference_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.risk_preference_profiles import build_risk_preference_profile_registry

def test_risk_preference():
    p = get_default_advanced_config_system_profile()
    df, summary = build_risk_preference_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "conservative_research" in names
    assert "balanced_research" in names
    assert "aggressive_research_only" in names
''')

write_file('tests/test_data_provider_preference_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.data_provider_preference_profiles import build_data_provider_preference_profile_registry

def test_data_provider_preference():
    p = get_default_advanced_config_system_profile()
    df, summary = build_data_provider_preference_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "no_scraping_public_api_preferred" in names
''')

write_file('tests/test_feature_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.feature_profiles import build_feature_profile_registry

def test_feature():
    p = get_default_advanced_config_system_profile()
    df, summary = build_feature_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "standard_technical_features" in names
    assert "macro_factor_features" in names
    assert "cross_asset_features" in names
''')

write_file('tests/test_regime_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.regime_profiles import build_regime_profile_registry

def test_regime():
    p = get_default_advanced_config_system_profile()
    df, summary = build_regime_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_ml_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.ml_profiles import build_ml_profile_registry

def test_ml():
    p = get_default_advanced_config_system_profile()
    df, summary = build_ml_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "no_ml_baseline" in names
    assert "gpu_optional_ml_research" in names
''')

write_file('tests/test_backtest_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.backtest_profiles import build_backtest_profile_registry

def test_backtest():
    p = get_default_advanced_config_system_profile()
    df, summary = build_backtest_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_portfolio_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.portfolio_profiles import build_portfolio_profile_registry

def test_portfolio():
    p = get_default_advanced_config_system_profile()
    df, summary = build_portfolio_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_report_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.report_profiles import build_report_profile_registry

def test_report():
    p = get_default_advanced_config_system_profile()
    df, summary = build_report_profile_registry(p)
    assert len(df) > 0
''')

write_file('tests/test_safety_profiles.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.safety_profiles import build_safety_profile_registry

def test_safety():
    p = get_default_advanced_config_system_profile()
    df, summary = build_safety_profile_registry(p)
    names = df["profile_name"].tolist()
    assert "strict_no_advice_safety" in names
    assert "strict_no_live_broker_safety" in names
''')
