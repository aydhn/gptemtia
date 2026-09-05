import pytest
from advanced_economic_calendar.calendar_provider_config import get_default_calendar_provider_profile, list_calendar_provider_profiles
from advanced_economic_calendar.calendar_domain_registry import build_economic_calendar_domain_registry
from advanced_economic_calendar.economic_event_universe import build_economic_event_universe_registry
from advanced_economic_calendar.economic_event_categories import build_economic_event_category_registry
from advanced_economic_calendar.economic_event_importance import build_economic_event_importance_registry
from advanced_economic_calendar.event_indicator_mapping import build_event_region_currency_indicator_mapping_registry
from advanced_economic_calendar.calendar_event_schema import build_calendar_event_schema_contract
from advanced_economic_calendar.release_event_schema import build_release_event_schema_contract
from advanced_economic_calendar.event_surprise_requirements import build_event_surprise_calculation_requirement_registry
from advanced_economic_calendar.event_time_normalization_requirements import build_event_time_normalization_requirement_registry
from advanced_economic_calendar.event_revision_handling_requirements import build_event_revision_handling_requirement_registry
from advanced_economic_calendar.calendar_provider_capabilities import build_calendar_provider_capability_registry
from advanced_economic_calendar.calendar_provider_request import create_calendar_provider_request
from advanced_economic_calendar.calendar_provider_response import create_calendar_provider_response
from advanced_economic_calendar.calendar_provider_errors import create_calendar_provider_error
from advanced_economic_calendar.calendar_provider_interfaces import build_calendar_provider_interface_contract
from advanced_economic_calendar.calendar_adapter_contracts import build_calendar_adapter_contract
from advanced_economic_calendar.calendar_provider_registry import build_calendar_provider_registry
from advanced_economic_calendar.calendar_provider_resolver import build_calendar_provider_resolver_map
from advanced_economic_calendar.calendar_provider_preference_resolver import build_calendar_provider_preference_resolver_report
from advanced_economic_calendar.calendar_provider_capability_matcher import build_calendar_provider_capability_matcher_report
from advanced_economic_calendar.calendar_dry_run_fixture import CalendarDryRunFixtureProvider
from advanced_economic_calendar.calendar_output_validation import build_calendar_output_validation_contract
from advanced_economic_calendar.calendar_safety_boundary import build_calendar_safety_boundary
from advanced_economic_calendar.calendar_health import build_calendar_health_check
from advanced_economic_calendar.calendar_scoring import calculate_calendar_readiness_score
import pandas as pd

def test_unified_advanced_calendar_provider_scripts_contract():
    profile = get_default_calendar_provider_profile()
    
    # Check Profile Attributes
    assert profile.current_phase == 110
    assert profile.target_final_phase == 160
    assert profile.next_phase == 111
    assert profile.local_only is True
    assert profile.non_production is True
    assert profile.research_only is True
    assert profile.dry_run_default is True
    assert profile.allow_web_scraping is False
    assert profile.allow_html_scraping is False
    assert profile.allow_browser_automation_scraping is False
    assert profile.allow_hidden_api_reverse_engineering is False
    assert profile.allow_paywall_bypass is False
    assert profile.allow_rate_limit_abuse is False
    assert profile.allow_event_directional_claim is False
    
    # Check Profiles Registry
    profiles = list_calendar_provider_profiles()
    assert len(profiles) > 0

    # Check Domain Registry
    domains_df, _ = build_economic_calendar_domain_registry(profile)
    assert not domains_df.empty

    # Check Event Universe
    events_df, _ = build_economic_event_universe_registry(profile)
    event_names = events_df['canonical_event'].tolist()
    for e in ["FOMC_RATE_DECISION", "ECB_RATE_DECISION", "CBRT_RATE_DECISION", "US_CPI_RELEASE", "US_NONFARM_PAYROLLS_RELEASE", "US_GDP_RELEASE"]:
        assert e in event_names
    categories = events_df['category_label'].unique()
    assert "event_central_bank_policy" in categories
    assert "event_inflation" in categories
    assert "event_labor" in categories
    assert "event_growth" in categories
    assert "event_pmi_sentiment" in categories
    assert "event_energy_inventory" in categories

    # Check Categories Registry
    cats_df, _ = build_economic_event_category_registry(profile)
    assert not cats_df.empty

    # Check Importance Registry
    imp_df, _ = build_economic_event_importance_registry(profile)
    imp_labels = imp_df['default_importance'].unique()
    assert "event_importance_high" in imp_labels
    
    # Check Indicator Mapping
    map_df, _ = build_event_region_currency_indicator_mapping_registry(profile)
    us_cpi = map_df[map_df['canonical_event'] == 'US_CPI_RELEASE']
    assert not us_cpi.empty
    assert us_cpi.iloc[0]['macro_indicator'] == 'US_CPI_YOY'

    # Check Schemas
    ce_schema, _ = build_calendar_event_schema_contract(profile)
    ce_fields = ce_schema['field_name'].tolist()
    for f in ["scheduled_time", "region", "currency", "category", "importance"]:
        assert f in ce_fields

    re_schema, _ = build_release_event_schema_contract(profile)
    re_fields = re_schema['field_name'].tolist()
    for f in ["actual", "forecast", "previous", "revised_previous", "surprise_value"]:
        assert f in re_fields

    # Check Requirements
    sur_req, _ = build_event_surprise_calculation_requirement_registry(profile)
    assert not sur_req.empty
    assert "surprise = actual - forecast" in sur_req['formula_placeholder'].tolist()
    
    time_req, _ = build_event_time_normalization_requirement_registry(profile)
    time_fields = time_req['time_field'].tolist()
    assert "scheduled_time" in time_fields
    assert "actual_release_time" in time_fields
    
    rev_req, _ = build_event_revision_handling_requirement_registry(profile)
    assert "revised_previous_policy" in rev_req.columns
    assert "revision_status_policy" in rev_req.columns

    # Check Capabilities
    caps, _ = build_calendar_provider_capability_registry(profile)
    assert caps['no_scraping_compliant'].all()

    # Check Request/Response
    req = create_calendar_provider_request("test", "data")
    assert req.dry_run is True
    assert req.local_only is True

    res = create_calendar_provider_response("req", "test", "data", "success")
    assert res.manual_review_required is True

    # Check Interface Contract
    intf, _ = build_calendar_provider_interface_contract(profile)
    assert not intf.empty

    # Check Adapter Contract
    adp, _ = build_calendar_adapter_contract(profile)
    assert not adp.empty
    
    # Check Registry/Resolver
    reg, _ = build_calendar_provider_registry(profile)
    assert not reg.empty
    
    res_map, _ = build_calendar_provider_resolver_map(profile)
    assert not res_map.empty
    
    pref, _ = build_calendar_provider_preference_resolver_report(profile)
    assert not pref.empty
    
    # Check Dry Run Fixture
    dr_fixture = CalendarDryRunFixtureProvider()
    resp = dr_fixture.fetch_calendar(req)
    assert resp.status_label == "success"
    assert resp.manual_review_required is True

    # Check Output Validation
    val, _ = build_calendar_output_validation_contract(profile)
    assert not val.empty
    
    # Check Safety Boundary
    saf, _ = build_calendar_safety_boundary(profile)
    assert not saf.empty

    # Check Health
    health, _ = build_calendar_health_check(None, profile)
    assert not health.empty

    # Check Scoring
    score = calculate_calendar_readiness_score(pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), pd.DataFrame([1]), health, profile)
    assert 0.0 <= score <= 1.0
