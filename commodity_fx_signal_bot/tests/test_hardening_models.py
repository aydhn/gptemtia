
import pytest
from commodity_fx_signal_bot.local_hardening.hardening_models import build_hardening_domain_id, build_dead_code_candidate_id, build_contract_surface_id, build_freeze_manifest_item_id, HardeningDomain, hardening_domain_to_dict

def test_models():
    assert build_hardening_domain_id("test") == "dom_test"
    assert build_dead_code_candidate_id("a", "b", "c") == "dc_a_b"
    assert build_contract_surface_id("a", "b") == "cs_a_b"
    assert build_freeze_manifest_item_id("a", "b") == "fm_b_a"
    hd = HardeningDomain("id", "lbl", "nm", "desc", [], [])
    assert "domain_id" in hardening_domain_to_dict(hd)
