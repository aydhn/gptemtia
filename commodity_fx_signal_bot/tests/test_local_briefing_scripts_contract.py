import pytest

def test_local_briefing_scripts_contract():
    try:
        import scripts.run_briefing_profile_registry
        import scripts.run_executive_summary_pack
        import scripts.run_briefing_deck_source
        import scripts.run_decision_context_binder
        import scripts.run_stakeholder_communication_kit
        import scripts.run_briefing_quality_report
        import scripts.run_briefing_status
    except Exception as e:
        pytest.fail(f"Script import failed: {e}")
