import pytest
from scenarios.scenario_config import get_default_scenario_profile
from scenarios.workflow_packs import (
    build_symbol_research_workflow_pack, build_governance_review_workflow_pack,
    build_experiment_review_workflow_pack, build_default_workflow_packs
)

def test_workflow_packs():
    profile = get_default_scenario_profile()

    p1 = build_symbol_research_workflow_pack("GC=F", profile)
    assert "workflow_id" in p1
    assert "safe_commands" in p1

    p2 = build_governance_review_workflow_pack(profile)
    assert p2["workflow_name"] == "governance_review"

    df, summary = build_default_workflow_packs(profile)
    assert not df.empty
    assert summary["total_packs"] > 0
