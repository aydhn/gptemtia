"""Test models."""
from commodity_fx_signal_bot.local_reproducibility_governance.reproducibility_models import (
    build_reproducibility_domain_id, build_reproducibility_dossier_item_id, build_environment_replay_item_id,
    build_deterministic_runbook_item_id, build_build_free_reproduction_item_id,
    ReproducibilityDomain, reproducibility_domain_to_dict, DeterministicRunbookItem
)

def test_models():
    assert build_reproducibility_domain_id("a") == build_reproducibility_domain_id("a")
    assert build_reproducibility_dossier_item_id("a", "b") == build_reproducibility_dossier_item_id("a", "b")
    assert build_environment_replay_item_id("a", "b") == build_environment_replay_item_id("a", "b")
    assert build_deterministic_runbook_item_id("a", "b") == build_deterministic_runbook_item_id("a", "b")
    assert build_build_free_reproduction_item_id("a", "b") == build_build_free_reproduction_item_id("a", "b")
    
    d = ReproducibilityDomain("id", "lbl", "name", "desc", [], [])
    assert reproducibility_domain_to_dict(d)["domain_id"] == "id"
