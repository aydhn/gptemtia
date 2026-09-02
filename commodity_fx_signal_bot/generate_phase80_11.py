import os

def write_file(path: str, content: str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

test_config = """
import pytest
from local_closure.closure_config import get_local_closure_profile, get_default_local_closure_profile, validate_local_closure_profiles
from core.exceptions import ConfigError

def test_validate_local_closure_profiles():
    validate_local_closure_profiles()

def test_get_default_local_closure_profile():
    p = get_default_local_closure_profile()
    assert p.name == "balanced_local_closure"
    assert p.language == "tr"
    assert p.max_items > 0
    assert 0 <= p.min_readiness_score <= 1
    assert p.dry_run_default is True
    assert not p.allow_real_v1_release
    assert not p.allow_live_trading_claim

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_closure_profile("unknown_profile")
"""
write_file("tests/test_closure_config.py", test_config)

test_labels = """
from local_closure.closure_labels import list_closure_domain_labels, list_closure_item_labels, list_closure_status_labels, list_roadmap_status_labels, list_closure_risk_labels, validate_closure_domain_label, validate_closure_status

def test_label_lists():
    assert len(list_closure_domain_labels()) > 0
    assert len(list_closure_item_labels()) > 0
    assert len(list_closure_status_labels()) > 0
    assert len(list_roadmap_status_labels()) > 0
    assert len(list_closure_risk_labels()) > 0

def test_validate_labels():
    validate_closure_domain_label("meta_review_domain")
    validate_closure_status("closure_ready_for_rehearsal")

def test_closure_ready_for_rehearsal():
    assert "closure_ready_for_rehearsal" in list_closure_status_labels()
"""
write_file("tests/test_closure_labels.py", test_labels)

test_models = """
from local_closure.closure_models import ClosureDomain, build_closure_domain_id, closure_domain_to_dict

def test_models():
    id1 = build_closure_domain_id("test")
    id2 = build_closure_domain_id("test")
    assert id1 == id2
    
    domain = ClosureDomain(id1, "test_label", "Test", "Desc", ["req"], [])
    d = closure_domain_to_dict(domain)
    assert d["domain_id"] == id1
    assert d["domain_label"] == "test_label"
"""
write_file("tests/test_closure_models.py", test_models)

test_registry = """
from local_closure.closure_domain_registry import build_closure_domain_registry, build_default_closure_domains
from local_closure.closure_config import get_default_local_closure_profile

def test_closure_domain_registry():
    p = get_default_local_closure_profile()
    df, summary = build_closure_domain_registry(p)
    assert not df.empty
    assert summary["total_domains"] > 0
    
    domains = build_default_closure_domains(p)
    assert len(domains) > 0
    for d in domains:
        for r in d.required_outputs:
            assert "secret" not in r.lower()
"""
write_file("tests/test_closure_domain_registry.py", test_registry)

test_meta = """
from pathlib import Path
from local_closure.meta_review import build_final_project_meta_review_report, build_meta_review_sections
from local_closure.closure_config import get_default_local_closure_profile

def test_meta_review():
    p = get_default_local_closure_profile()
    text, summary = build_final_project_meta_review_report(Path.cwd(), p)
    assert isinstance(text, str)
    assert len(text) > 0
    assert "UYARI" in text
    
    sections = build_meta_review_sections(Path.cwd(), p)
    assert len(sections) > 0
"""
write_file("tests/test_meta_review.py", test_meta)

test_lessons = """
from pathlib import Path
from local_closure.lessons_learned import build_lessons_learned_compendium, build_default_lessons_learned, export_lessons_learned_markdown
from local_closure.closure_config import get_default_local_closure_profile

def test_lessons():
    p = get_default_local_closure_profile()
    df, summary = build_lessons_learned_compendium(Path.cwd(), p)
    assert not df.empty
    assert summary["total_lessons"] > 0
    
    md = export_lessons_learned_markdown(df, summary)
    assert "UYARI" in md
"""
write_file("tests/test_lessons_learned.py", test_lessons)

test_roadmap = """
from pathlib import Path
from local_closure.roadmap_backlog import build_future_roadmap_backlog, build_default_roadmap_items
from local_closure.closure_config import get_default_local_closure_profile

def test_roadmap():
    p = get_default_local_closure_profile()
    df, summary = build_future_roadmap_backlog(Path.cwd(), p)
    assert not df.empty
    assert summary["total_items"] > 0
    
    # live_trading is blocked
    live_item = df[df["title"] == "Live Trading Connection"]
    assert not live_item.empty
    assert live_item.iloc[0]["status"] == "roadmap_blocked_by_safety"
"""
write_file("tests/test_roadmap_backlog.py", test_roadmap)

test_candidates = """
import pandas as pd
from local_closure.future_phase_candidates import build_future_phase_candidate_registry
from local_closure.closure_config import get_default_local_closure_profile

def test_candidates():
    p = get_default_local_closure_profile()
    roadmap_df = pd.DataFrame([{"title": "Test", "status": "roadmap_candidate", "rationale": "R"}])
    df, summary = build_future_phase_candidate_registry(roadmap_df, p)
    assert not df.empty
    assert summary["total_candidates"] == 1
"""
write_file("tests/test_future_phase_candidates.py", test_candidates)

test_gov = """
from pathlib import Path
from local_closure.governance_rehearsal import build_post_project_governance_rehearsal_guide, build_governance_rehearsal_sections
from local_closure.closure_config import get_default_local_closure_profile

def test_governance():
    p = get_default_local_closure_profile()
    text, summary = build_post_project_governance_rehearsal_guide(Path.cwd(), p)
    assert isinstance(text, str)
    assert "UYARI" in text
    assert len(build_governance_rehearsal_sections(p)) > 0
"""
write_file("tests/test_governance_rehearsal.py", test_gov)
