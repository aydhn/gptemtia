import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")
TESTS_DIR = BASE_DIR / "tests"

# tests/test_acceptance_config.py
with open(TESTS_DIR / "test_acceptance_config.py", "w", encoding="utf-8") as f:
    f.write('''import pytest
from local_acceptance.acceptance_config import (
    validate_local_acceptance_profiles,
    get_default_local_acceptance_profile,
    get_local_acceptance_profile,
    ConfigError
)

def test_validate_local_acceptance_profiles():
    validate_local_acceptance_profiles()

def test_get_default_local_acceptance_profile():
    p = get_default_local_acceptance_profile()
    assert p.name == "balanced_local_acceptance"
    assert p.dry_run_default is True

def test_get_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_acceptance_profile("unknown_profile")
''')

# tests/test_acceptance_labels.py
with open(TESTS_DIR / "test_acceptance_labels.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_labels import (
    list_acceptance_domain_labels,
    list_acceptance_status_labels,
    validate_acceptance_domain_label,
    validate_acceptance_status
)

def test_list_labels():
    assert len(list_acceptance_domain_labels()) > 0
    assert len(list_acceptance_status_labels()) > 0

def test_validate_labels():
    validate_acceptance_domain_label("final_acceptance_domain")
    validate_acceptance_status("acceptance_ready_for_rehearsal")
''')

# tests/test_acceptance_models.py
with open(TESTS_DIR / "test_acceptance_models.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_models import (
    build_acceptance_domain_id,
    build_acceptance_checklist_item_id,
    build_reviewer_question_id,
    build_evidence_trace_id,
    AcceptanceDomain,
    acceptance_domain_to_dict
)

def test_build_ids():
    assert len(build_acceptance_domain_id("test")) == 8
    assert len(build_acceptance_checklist_item_id("dom", "item")) == 8
    assert len(build_reviewer_question_id("q")) == 8
    assert len(build_evidence_trace_id("file", "name")) == 8

def test_to_dict():
    d = AcceptanceDomain("id", "label", "name", "desc", [], [])
    res = acceptance_domain_to_dict(d)
    assert res["domain_id"] == "id"
''')

# tests/test_acceptance_domain_registry.py
with open(TESTS_DIR / "test_acceptance_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_domain_registry import build_acceptance_domain_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_domain_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_domain_registry(p)
    assert not df.empty
    assert s["total_domains"] > 0
''')

# tests/test_acceptance_simulation.py
with open(TESTS_DIR / "test_acceptance_simulation.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_acceptance.acceptance_simulation import build_final_acceptance_simulation_checklist
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_acceptance_simulation_checklist():
    p = get_default_local_acceptance_profile()
    df, s = build_final_acceptance_simulation_checklist(Path("."), p)
    assert not df.empty
    assert s["total_items"] > 0
''')

# tests/test_reviewer_pack.py
with open(TESTS_DIR / "test_reviewer_pack.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.reviewer_pack import build_independent_reviewer_pack
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_independent_reviewer_pack():
    p = get_default_local_acceptance_profile()
    text, s = build_independent_reviewer_pack(None, None, None, p)
    assert "Independent Reviewer Pack" in text
''')

# tests/test_reviewer_questions.py
with open(TESTS_DIR / "test_reviewer_questions.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.reviewer_questions import build_reviewer_question_bank
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_reviewer_question_bank():
    p = get_default_local_acceptance_profile()
    df, s = build_reviewer_question_bank(p)
    assert not df.empty
''')

# tests/test_reviewer_evidence_matrix.py
with open(TESTS_DIR / "test_reviewer_evidence_matrix.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.reviewer_evidence_matrix import build_reviewer_evidence_request_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_reviewer_evidence_request_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"question": "test"}])
    res_df, s = build_reviewer_evidence_request_matrix(df, Path("."), p)
    assert "mapped_evidence" in res_df.columns
''')

# tests/test_evidence_trail.py
with open(TESTS_DIR / "test_evidence_trail.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_acceptance.evidence_trail import build_audit_style_local_evidence_trail
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_audit_style_local_evidence_trail():
    p = get_default_local_acceptance_profile()
    df, s = build_audit_style_local_evidence_trail(Path("."), p)
    assert not df.empty
''')

# tests/test_evidence_output_trace.py
with open(TESTS_DIR / "test_evidence_output_trace.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.evidence_output_trace import build_evidence_output_trace_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_evidence_output_trace_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"test": "val"}])
    res, s = build_evidence_output_trace_matrix(df, Path("."), p)
    assert "linked_output" in res.columns
''')

# tests/test_evidence_test_trace.py
with open(TESTS_DIR / "test_evidence_test_trace.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.evidence_test_trace import build_evidence_test_trace_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_evidence_test_trace_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"test": "val"}])
    res, s = build_evidence_test_trace_matrix(df, Path("."), p)
    assert "linked_test" in res.columns
''')

# tests/test_evidence_doc_trace.py
with open(TESTS_DIR / "test_evidence_doc_trace.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.evidence_doc_trace import build_evidence_doc_trace_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_evidence_doc_trace_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"test": "val"}])
    res, s = build_evidence_doc_trace_matrix(df, Path("."), p)
    assert "linked_doc" in res.columns
''')

# tests/test_evidence_safety_trace.py
with open(TESTS_DIR / "test_evidence_safety_trace.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from pathlib import Path
from local_acceptance.evidence_safety_trace import build_evidence_safety_boundary_trace_matrix
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_evidence_safety_boundary_trace_matrix():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame([{"test": "val"}])
    res, s = build_evidence_safety_boundary_trace_matrix(df, Path("."), p)
    assert "linked_safety" in res.columns
''')

# tests/test_signoff_rehearsal.py
with open(TESTS_DIR / "test_signoff_rehearsal.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.signoff_rehearsal import build_signoff_rehearsal_checklist, build_signoff_rehearsal_binder
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_signoff_rehearsal():
    p = get_default_local_acceptance_profile()
    df, s = build_signoff_rehearsal_checklist(p)
    assert not df.empty
    text, ts = build_signoff_rehearsal_binder(df, pd.DataFrame(), pd.DataFrame(), p)
    assert "Sign-off Rehearsal Binder" in text
''')

# tests/test_verification_rehearsal.py
with open(TESTS_DIR / "test_verification_rehearsal.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_acceptance.verification_rehearsal import build_final_verification_rehearsal_plan
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_rehearsal_plan():
    p = get_default_local_acceptance_profile()
    df, s = build_final_verification_rehearsal_plan(Path("."), p)
    assert not df.empty
''')

# tests/test_verification_scenarios.py
with open(TESTS_DIR / "test_verification_scenarios.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.verification_scenarios import build_final_verification_scenario_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_scenario_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_final_verification_scenario_registry(p)
    assert not df.empty
''')

# tests/test_acceptance_criteria.py
with open(TESTS_DIR / "test_acceptance_criteria.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_criteria import build_acceptance_criteria_registry
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_criteria_registry():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_criteria_registry(p)
    assert not df.empty
''')

# tests/test_acceptance_exceptions.py
with open(TESTS_DIR / "test_acceptance_exceptions.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_exceptions import build_acceptance_exception_register
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_exception_register():
    p = get_default_local_acceptance_profile()
    df, s = build_acceptance_exception_register(pd.DataFrame(), pd.DataFrame(), p)
    assert df.empty
''')

# tests/test_acceptance_no_go_safe_go.py
with open(TESTS_DIR / "test_acceptance_no_go_safe_go.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
import pandas as pd
from local_acceptance.acceptance_no_go_safe_go import (
    build_acceptance_no_go_register,
    build_acceptance_safe_go_register,
    build_acceptance_no_go_safe_go_summary
)
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_no_go_safe_go():
    p = get_default_local_acceptance_profile()
    n_df, _ = build_acceptance_no_go_register(Path("."), p)
    s_df, _ = build_acceptance_safe_go_register(Path("."), p)
    assert not n_df.empty
    assert not s_df.empty
    sm_df, _ = build_acceptance_no_go_safe_go_summary(n_df, s_df, p)
    assert not sm_df.empty
''')

# tests/test_review_templates.py
with open(TESTS_DIR / "test_review_templates.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.review_templates import build_independent_review_notes_template, build_acceptance_response_template
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_review_templates():
    p = get_default_local_acceptance_profile()
    nt, _ = build_independent_review_notes_template(p)
    rt, _ = build_acceptance_response_template(p)
    assert "Independent Review Notes" in nt
    assert "Acceptance Response" in rt
''')

# tests/test_verification_evidence_binder.py
with open(TESTS_DIR / "test_verification_evidence_binder.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.verification_evidence_binder import build_final_verification_evidence_binder
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_final_verification_evidence_binder():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    text, _ = build_final_verification_evidence_binder(df, df, df, df, df, p)
    assert "Verification Evidence" in text
''')

# tests/test_acceptance_gaps.py
with open(TESTS_DIR / "test_acceptance_gaps.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_gaps import build_acceptance_gap_register
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_gap_register():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, _ = build_acceptance_gap_register(df, df, df, df, p)
    assert res.empty
''')

# tests/test_acceptance_risks.py
with open(TESTS_DIR / "test_acceptance_risks.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_risks import build_acceptance_risk_summary
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_risk_summary():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, _ = build_acceptance_risk_summary(df, df, df, p)
    assert res.empty
''')

# tests/test_acceptance_scoring.py
with open(TESTS_DIR / "test_acceptance_scoring.py", "w", encoding="utf-8") as f:
    f.write('''import pandas as pd
from local_acceptance.acceptance_scoring import build_acceptance_readiness_score_report
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_readiness_score_report():
    p = get_default_local_acceptance_profile()
    df = pd.DataFrame()
    res, s = build_acceptance_readiness_score_report(df, df, df, p)
    assert not res.empty
    assert s["score"] > 0
''')

# tests/test_acceptance_validation.py
with open(TESTS_DIR / "test_acceptance_validation.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_validation import build_acceptance_validation_report
from local_acceptance.acceptance_config import get_default_local_acceptance_profile

def test_build_acceptance_validation_report():
    p = get_default_local_acceptance_profile()
    res, s = build_acceptance_validation_report({}, p)
    assert not res.empty
''')

# tests/test_acceptance_quality.py
with open(TESTS_DIR / "test_acceptance_quality.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_quality import build_acceptance_quality_report

def test_build_acceptance_quality_report():
    res = build_acceptance_quality_report({})
    assert res["passed"] is True
''')

# tests/test_acceptance_report_builder.py
with open(TESTS_DIR / "test_acceptance_report_builder.py", "w", encoding="utf-8") as f:
    f.write('''from local_acceptance.acceptance_report_builder import build_acceptance_domain_registry_markdown_report

def test_build_acceptance_domain_registry_markdown_report():
    md = build_acceptance_domain_registry_markdown_report({})
    assert "Acceptance Domain Registry" in md
''')

# tests/test_acceptance_pipeline.py
with open(TESTS_DIR / "test_acceptance_pipeline.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from config.settings import Settings
from local_acceptance.acceptance_pipeline import LocalAcceptancePipeline
from data.storage.data_lake import DataLake

def test_local_acceptance_pipeline():
    s = Settings()
    dl = DataLake(s)
    pipeline = LocalAcceptancePipeline(dl, s, Path("."))
    dfs, sm = pipeline.build_acceptance_domain_registry(save=False)
    assert not dfs["domain"].empty
''')

# tests/test_local_acceptance_scripts_contract.py
with open(TESTS_DIR / "test_local_acceptance_scripts_contract.py", "w", encoding="utf-8") as f:
    f.write('''def test_scripts_import():
    try:
        import scripts.run_acceptance_domain_registry
        import scripts.run_final_acceptance_simulation
        import scripts.run_independent_reviewer_pack
        import scripts.run_acceptance_evidence_trail
        import scripts.run_signoff_rehearsal
        import scripts.run_acceptance_quality_report
        import scripts.run_acceptance_status
    except Exception as e:
        assert False, f"Import failed: {e}"
''')
