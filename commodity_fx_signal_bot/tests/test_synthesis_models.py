import pytest
from local_synthesis.synthesis_models import (
    PhaseFamily, MasterIndexItem, FinalMapNode, FinalBinderSection, SynthesisFinding,
    build_phase_family_id, build_master_index_item_id, build_final_map_node_id,
    build_final_binder_section_id, build_synthesis_finding_id,
    phase_family_to_dict, master_index_item_to_dict, final_map_node_to_dict,
    final_binder_section_to_dict, synthesis_finding_to_dict
)

def test_build_ids():
    assert build_phase_family_id("a") == "fam_a"
    assert build_master_index_item_id("path", "label").startswith("idx_")
    assert build_final_map_node_id("name", "label").startswith("node_")
    assert build_final_binder_section_id("title").startswith("sec_")
    assert build_synthesis_finding_id("title").startswith("fnd_")

def test_dataclass_to_dict():
    p = PhaseFamily("id", "label", "name", "hint", "desc", [], [])
    d = phase_family_to_dict(p)
    assert d["family_id"] == "id"
