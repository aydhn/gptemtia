from sizing.atr_sizing import build_atr_sizing_candidate, build_multi_atr_sizing_candidates

def test_build_atr_sizing_candidate():
    res = build_atr_sizing_candidate(1000.0, 100.0, 2.0, 1.0)
    assert res["valid"] is True
    assert res["risk_per_unit"] == 2.0
    assert res["theoretical_units"] == 500.0
    assert res["theoretical_notional"] == 50000.0

def test_build_atr_sizing_candidate_invalid():
    res1 = build_atr_sizing_candidate(1000.0, None, 2.0, 1.0)
    assert res1["valid"] is False

    res2 = build_atr_sizing_candidate(1000.0, 100.0, None, 1.0)
    assert res2["valid"] is False

def test_build_multi_atr_sizing_candidates():
    res = build_multi_atr_sizing_candidates(1000.0, 100.0, 2.0)
    assert "atr_1.0x" in res
    assert "atr_2.0x" in res
