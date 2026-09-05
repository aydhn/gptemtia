import pytest
from advanced_data_lineage.data_lineage_config import (
    get_data_lineage_profile,
    list_data_lineage_profiles,
    validate_data_lineage_profiles,
    get_default_data_lineage_profile,
    ConfigError,
)


def test_default_profile():
    p = get_default_data_lineage_profile()
    assert p.name == "balanced_local_lineage_provenance"
    assert p.current_phase == 114
    assert p.target_final_phase == 160
    assert p.next_phase == 115
    assert p.dry_run_default is True
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False
    assert p.allow_broker_integration is False
    assert p.allow_real_order is False
    assert p.allow_investment_advice is False
    assert p.allow_lineage_score_as_signal is False
    assert p.allow_official_approval_claim is False
    assert p.allow_source_overwrite is False
    assert p.allow_auto_destructive_cleaning is False
    assert p.allow_web_scraping is False
    assert p.allow_full_article_download is False
    assert p.allow_copyrighted_article_copy is False
    assert p.min_traceability_score == 0.45


def test_list_and_validate_profiles():
    profiles = list_data_lineage_profiles()
    assert len(profiles) >= 3
    validate_data_lineage_profiles()


def test_strict_safety_profile():
    p = get_data_lineage_profile("strict_lineage_provenance_safety")
    assert p.min_traceability_score == 0.65
    assert p.allow_live_trading is False
    assert p.allow_web_scraping is False


def test_dry_run_profile():
    p = get_data_lineage_profile("dry_run_lineage_contract_focus")
    assert p.dry_run_default is True
    assert p.allow_broker_integration is False


def test_unknown_profile_raises():
    with pytest.raises(ConfigError):
        get_data_lineage_profile("non_existent_profile_xyz")
