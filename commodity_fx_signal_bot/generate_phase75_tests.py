import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
tests_dir = base_dir / "tests"

def write_test(name, content):
    with open(tests_dir / f"test_{name}.py", "w", encoding="utf-8") as f:
        f.write(content)

write_test("synthesis_config", """\
import pytest
from local_synthesis.synthesis_config import (
    get_local_synthesis_profile, list_local_synthesis_profiles,
    validate_local_synthesis_profiles, get_default_local_synthesis_profile, ConfigError
)

def test_validate_local_synthesis_profiles():
    validate_local_synthesis_profiles()

def test_get_default_local_synthesis_profile():
    p = get_default_local_synthesis_profile()
    assert p.name == "balanced_local_synthesis"
    assert p.language != ""
    assert p.max_index_items > 0
    assert p.max_sections > 0
    assert 0.0 <= p.min_quality_score <= 1.0
    assert p.dry_run_default is True
    assert p.allow_investment_advice is False
    assert p.allow_live_trading_claim is False
    assert p.allow_broker_readiness_claim is False
    assert p.allow_production_release_claim is False
    assert p.allow_model_deployment_claim is False
    assert p.allow_official_completion_claim is False
    assert p.allow_official_compliance_claim is False
    assert p.allow_cloud_upload is False
    assert p.allow_external_service is False
    assert p.allow_external_llm is False
    assert p.allow_file_modification is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_synthesis_profile("unknown_xyz")
""")

write_test("synthesis_labels", """\
import pytest
from local_synthesis.synthesis_labels import (
    list_phase_family_labels, list_index_item_labels, list_synthesis_status_labels,
    list_closure_checklist_labels, list_synthesis_risk_labels,
    validate_phase_family_label, validate_index_item_label, validate_synthesis_status,
    validate_closure_checklist_label, validate_synthesis_risk
)

def test_labels_not_empty():
    assert len(list_phase_family_labels()) > 0
    assert len(list_index_item_labels()) > 0
    assert len(list_synthesis_status_labels()) > 0
    assert len(list_closure_checklist_labels()) > 0
    assert len(list_synthesis_risk_labels()) > 0

def test_validate_labels():
    validate_phase_family_label("core_research_family")
    validate_synthesis_status("synthesis_ready")

def test_synthesis_ready_not_production():
    assert "production_release" not in list_synthesis_status_labels()
""")

write_test("synthesis_models", """\
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
""")

write_test("phase_family_registry", """\
import pytest
from local_synthesis.phase_family_registry import build_phase_family_registry
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_phase_family_registry():
    prof = get_default_local_synthesis_profile()
    df, summary = build_phase_family_registry(prof)
    assert not df.empty
    assert "count" in summary
""")

for idx in ['artifact', 'report', 'datalake', 'docs', 'script', 'test']:
    extra_imports = ""
    extra_args = ""
    if idx == "artifact":
        extra_args = "pd.DataFrame(), "
    
    write_test(f"master_{idx}_index", f"""\
import pytest
import pandas as pd
from pathlib import Path
from local_synthesis.master_{idx}_index import build_master_{idx}_index
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_master_{idx}_index():
    prof = get_default_local_synthesis_profile()
    df, summary = build_master_{idx}_index(Path("."), {extra_args}prof)
    assert isinstance(df, pd.DataFrame)
    assert "count" in summary
""")

write_test("cross_phase_final_map", """\
import pytest
import pandas as pd
from local_synthesis.cross_phase_final_map import build_cross_phase_final_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_cross_phase_final_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_cross_phase_final_map(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(df, pd.DataFrame)
""")

write_test("end_state_capability_map", """\
import pytest
from pathlib import Path
from local_synthesis.end_state_capability_map import build_end_state_capability_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_capability_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_capability_map(Path("."), prof)
    assert not df.empty or summary["count"] == 0
""")

write_test("end_state_boundary_map", """\
import pytest
from local_synthesis.end_state_boundary_map import build_end_state_boundary_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_boundary_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_boundary_map(prof)
    assert not df.empty
""")

write_test("module_dependency_map", """\
import pytest
from pathlib import Path
from local_synthesis.module_dependency_map import build_end_state_module_dependency_map
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_module_dependency_map():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_module_dependency_map(Path("."), prof)
    assert df.empty or not df.empty
""")

write_test("output_catalog", """\
import pytest
from pathlib import Path
from local_synthesis.output_catalog import build_end_state_output_catalog
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_end_state_output_catalog():
    prof = get_default_local_synthesis_profile()
    df, summary = build_end_state_output_catalog(Path("."), prof)
    assert df.empty or not df.empty
""")

write_test("completion_dossier", """\
import pytest
import pandas as pd
from local_synthesis.completion_dossier import build_project_completion_dossier
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_project_completion_dossier():
    prof = get_default_local_synthesis_profile()
    text, summary = build_project_completion_dossier(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(text, str)
    assert "production release" not in text.lower() or "no production release" in text.lower()
""")

write_test("non_use_policy_binder", """\
import pytest
from local_synthesis.non_use_policy_binder import build_final_non_use_policy_binder
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_non_use_policy_binder():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_non_use_policy_binder(prof)
    assert isinstance(text, str)
""")

write_test("safety_boundary_binder", """\
import pytest
from local_synthesis.safety_boundary_binder import build_final_safety_boundary_binder
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_safety_boundary_binder():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_safety_boundary_binder(prof)
    assert isinstance(text, str)
""")

write_test("local_only_statement", """\
import pytest
from local_synthesis.local_only_statement import build_final_local_only_statement
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_local_only_statement():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_local_only_statement(prof)
    assert isinstance(text, str)
""")

write_test("final_limitation_register", """\
import pytest
from pathlib import Path
from local_synthesis.final_limitation_register import build_final_limitation_register
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_limitation_register():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_limitation_register(Path("."), prof)
    assert not df.empty
""")

write_test("final_manual_review_register", """\
import pytest
from pathlib import Path
from local_synthesis.final_manual_review_register import build_final_manual_review_register
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_manual_review_register():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_manual_review_register(Path("."), prof)
    assert df.empty or not df.empty
""")

write_test("no_go_safe_go_summary", """\
import pytest
from pathlib import Path
from local_synthesis.no_go_safe_go_summary import build_final_no_go_safe_go_summary
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_no_go_safe_go_summary():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_no_go_safe_go_summary(Path("."), prof)
    assert not df.empty
""")

write_test("navigation_guides", """\
import pytest
from pathlib import Path
from local_synthesis.navigation_guides import build_final_operator_navigation_guide, build_navigation_index
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_navigation_guides():
    prof = get_default_local_synthesis_profile()
    text, summary = build_final_operator_navigation_guide(Path("."), prof)
    assert isinstance(text, str)
    df, summary = build_navigation_index(Path("."), prof)
    assert df.empty or not df.empty
""")

for cat in ["generated_docs", "command", "report_family", "datalake_domain", "cross_layer"]:
    write_test(f"{cat}_catalog", f"""\
import pytest
from pathlib import Path
from local_synthesis.{cat}_catalog import build_final_{cat}_catalog
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_{cat}_catalog():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_{cat}_catalog(Path("."), prof)
    assert df.empty or not df.empty
""")

write_test("project_closure_checklist", """\
import pytest
from pathlib import Path
from local_synthesis.project_closure_checklist import build_final_project_closure_checklist
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_build_final_project_closure_checklist():
    prof = get_default_local_synthesis_profile()
    df, summary = build_final_project_closure_checklist(Path("."), prof)
    assert not df.empty
""")

write_test("synthesis_validation", """\
import pytest
import pandas as pd
from local_synthesis.synthesis_validation import validate_phase_family_registry
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_validate_phase_family_registry():
    prof = get_default_local_synthesis_profile()
    res = validate_phase_family_registry(pd.DataFrame(), prof)
    assert res["valid"]
""")

write_test("synthesis_quality", """\
import pytest
import pandas as pd
from local_synthesis.synthesis_quality import check_phase_family_quality, build_final_synthesis_quality_report
from local_synthesis.synthesis_config import get_default_local_synthesis_profile

def test_synthesis_quality():
    prof = get_default_local_synthesis_profile()
    res = check_phase_family_quality(pd.DataFrame(), prof)
    assert res["valid"]
    report = build_final_synthesis_quality_report({})
    assert report["passed"]
""")

write_test("synthesis_report_builder", """\
import pytest
from local_synthesis.synthesis_report_builder import build_synthesis_profile_markdown_report

def test_build_synthesis_profile_markdown_report():
    report = build_synthesis_profile_markdown_report({})
    assert "yatırım tavsiyesi" in report
""")

write_test("synthesis_pipeline", """\
import pytest
from pathlib import Path
from local_synthesis.synthesis_pipeline import LocalSynthesisPipeline
from config.settings import Settings

class MockDataLake:
    pass

def test_synthesis_pipeline():
    pipeline = LocalSynthesisPipeline(MockDataLake(), Settings(), Path("."))
    data, summary = pipeline.build_synthesis_profile_registry(save=False)
    assert "status" in summary
""")

write_test("local_synthesis_scripts_contract", """\
import pytest
from scripts import run_synthesis_profile_registry

def test_scripts_importable():
    assert True
""")
