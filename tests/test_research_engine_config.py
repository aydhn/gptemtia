def test_config_phase():
    from advanced_research_engine.research_engine_config import get_default_advanced_research_engine_profile
    p = get_default_advanced_research_engine_profile()
    assert p.current_phase == 103
    assert p.target_final_phase == 160
    assert p.dry_run_default is True
    assert p.local_only is True
    assert p.non_production is True
    assert p.research_only is True
    assert p.allow_live_trading is False
