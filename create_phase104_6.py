import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file('tests/test_profile_composition.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_composition import build_composed_research_profile_registry

def test_composition():
    p = get_default_advanced_config_system_profile()
    df, summary = build_composed_research_profile_registry(p)
    names = df["composed_profile_name"].tolist()
    assert "full_advanced_research_dry_run" in names
    
    for _, row in df.iterrows():
        assert row["manual_review_required"] is True
''')

write_file('tests/test_profile_compatibility.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_compatibility import evaluate_profile_compatibility

def test_compatibility():
    item = evaluate_profile_compatibility("no_scraping", "any")
    assert item.compatibility_status == "profile_ready"
    
    item = evaluate_profile_compatibility("intraday_research_no_live", "live_trading")
    assert item.compatibility_status == "profile_incompatible"
''')

write_file('tests/test_profile_validation.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_validation import validate_no_forbidden_profile_claims

def test_validation():
    res = validate_no_forbidden_profile_claims("kesin al")
    assert res["status"] == "failed"
    
    res = validate_no_forbidden_profile_claims("yatırım tavsiyesi değildir")
    assert res["status"] == "passed"
''')

write_file('tests/test_profile_quality.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_quality import check_for_forbidden_terms_in_profiles

def test_quality():
    res = check_for_forbidden_terms_in_profiles("live trading approved")
    assert len(res["forbidden_terms_found"]) > 0
    
    res = check_for_forbidden_terms_in_profiles("yatırım tavsiyesi değildir")
    assert len(res["forbidden_terms_found"]) == 0
''')

write_file('tests/test_profile_scoring.py', '''
from advanced_config_profiles.advanced_config import get_default_advanced_config_system_profile
from advanced_config_profiles.profile_scoring import calculate_profile_readiness_score

def test_scoring():
    import pandas as pd
    p = get_default_advanced_config_system_profile()
    score = calculate_profile_readiness_score(pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([{"status": "passed"}]), p)
    assert 0 <= score <= 1.0
''')

write_file('tests/test_advanced_config_report_builder.py', '''
from advanced_config_profiles.advanced_config_report_builder import build_advanced_config_disclaimer

def test_report_builder():
    txt = build_advanced_config_disclaimer()
    assert "yatırım tavsiyesi" in txt
    assert "Phase 104" in txt
''')

write_file('tests/test_advanced_config_pipeline.py', '''
from advanced_config_profiles.advanced_config_pipeline import AdvancedConfigProfilePipeline
from config import settings
from data.storage.data_lake import DataLake

def test_pipeline():
    dl = DataLake()
    pipeline = AdvancedConfigProfilePipeline(dl, settings, ".")
    df, summary = pipeline.build_advanced_config_status(save=False)
    assert df is not None
''')

write_file('tests/test_advanced_config_scripts_contract.py', '''
def test_scripts_exist():
    import os
    assert os.path.exists("scripts/run_advanced_config_profile_registry.py")
    assert os.path.exists("scripts/run_research_mode_presets.py")
    assert os.path.exists("scripts/run_profile_composition.py")
    assert os.path.exists("scripts/run_profile_compatibility_matrix.py")
    assert os.path.exists("scripts/run_advanced_config_quality_report.py")
    assert os.path.exists("scripts/run_advanced_config_status.py")
''')
