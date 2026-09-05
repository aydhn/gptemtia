from advanced_config_profiles.advanced_config_report_builder import build_advanced_config_disclaimer

def test_report_builder():
    txt = build_advanced_config_disclaimer()
    assert "yatırım tavsiyesi" in txt
    assert "Phase 104" in txt
