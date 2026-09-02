import os

os.makedirs("tests", exist_ok=True)

with open("tests/test_training_config.py", "w", encoding="utf-8") as f:
    f.write('''import pytest
from local_training.training_config import validate_local_training_profiles, get_default_local_training_profile, get_local_training_profile, ConfigError

def test_validate_local_training_profiles():
    validate_local_training_profiles()

def test_get_default_local_training_profile():
    p = get_default_local_training_profile()
    assert p.language == "tr"
    assert p.max_lessons > 0
    assert p.max_walkthrough_steps > 0
    assert 0 <= p.min_training_quality_score <= 1
    assert p.dry_run_default is True
    assert p.allow_cloud_upload is False
    assert p.allow_external_training_service is False
    assert p.allow_external_llm is False
    assert p.allow_file_modification is False
    assert p.allow_file_deletion is False
    assert p.allow_file_move is False
    assert p.allow_overwrite is False
    assert p.allow_live_commands is False
    assert p.allow_broker_commands is False
    assert p.allow_deploy_commands is False
    assert p.allow_background_daemons is False
    assert p.allow_real_market_download is False
    assert p.allow_certification_claim is False
    assert p.allow_investment_advice_training is False

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_training_profile("unknown_profile")
''')

with open("tests/test_training_labels.py", "w", encoding="utf-8") as f:
    f.write('''import pytest
from local_training.training_labels import list_training_domain_labels, list_training_lesson_status_labels, list_onboarding_role_labels, list_assessment_status_labels, list_training_risk_labels, validate_training_domain_label, validate_onboarding_role

def test_labels_not_empty():
    assert len(list_training_domain_labels()) > 0
    assert len(list_training_lesson_status_labels()) > 0
    assert len(list_onboarding_role_labels()) > 0
    assert len(list_assessment_status_labels()) > 0
    assert len(list_training_risk_labels()) > 0

def test_validate_valid_labels():
    validate_training_domain_label("operator_training")
    validate_onboarding_role("operator_role")

def test_operator_role_is_not_live_authorization():
    assert "operator_role" in list_onboarding_role_labels()
''')

with open("tests/test_training_models.py", "w", encoding="utf-8") as f:
    f.write('''from local_training.training_models import build_training_domain_id, build_onboarding_path_id, build_training_lesson_id, build_training_faq_id, TrainingLesson, training_lesson_to_dict

def test_ids_deterministic():
    assert build_training_domain_id("test") == build_training_domain_id("test")
    assert build_onboarding_path_id("test", "test") == build_onboarding_path_id("test", "test")
    assert build_training_lesson_id("test", "test") == build_training_lesson_id("test", "test")
    assert build_training_faq_id("test") == build_training_faq_id("test")

def test_dataclass_to_dict():
    tl = TrainingLesson("id", "name", "dom", "role", "obj", ["step"], ["safe"], ["out"], "stat", ["warn"])
    d = training_lesson_to_dict(tl)
    assert "lesson_id" in d
    assert "safe_commands" in d
    assert "safe" in d["safe_commands"]
''')

with open("tests/test_training_domain_registry.py", "w", encoding="utf-8") as f:
    f.write('''from local_training.training_config import get_default_local_training_profile
from local_training.training_domain_registry import build_training_domain_registry, build_default_training_domains

def test_domain_registry():
    prof = get_default_local_training_profile()
    df, summary = build_training_domain_registry(prof)
    assert not df.empty
    doms = build_default_training_domains(prof)
    assert len(doms) > 0
    for d in doms:
        assert "cloud" not in d.domain_name
        assert "external" not in d.domain_name
''')

with open("tests/test_onboarding_paths.py", "w", encoding="utf-8") as f:
    f.write('''from local_training.training_config import get_default_local_training_profile
from local_training.onboarding_paths import build_role_based_onboarding_paths, build_operator_onboarding_path, build_analyst_onboarding_path, build_developer_onboarding_path

def test_onboarding_paths():
    prof = get_default_local_training_profile()
    df, sum = build_role_based_onboarding_paths(prof)
    assert not df.empty
    op = build_operator_onboarding_path(prof)
    assert op.role_label == "operator_role"
    an = build_analyst_onboarding_path(prof)
    assert an.role_label == "analyst_role"
    dev = build_developer_onboarding_path(prof)
    assert dev.role_label == "developer_role"
''')

with open("tests/test_operator_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.operator_training_pack import build_operator_training_pack, build_operator_training_sections

def test_operator_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_operator_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    secs = build_operator_training_sections(Path("."), prof)
    assert isinstance(secs, list)
    assert "yatırım tavsiyesi" in txt or "Yatırım tavsiyesi" in txt
''')

with open("tests/test_analyst_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.analyst_training_pack import build_analyst_training_pack

def test_analyst_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_analyst_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert "yatırım danışmanlığı değildir" in txt.lower() or "yatırım danışmanlığı" in txt.lower()
    assert "kesin al/sat" in txt.lower()
''')

with open("tests/test_developer_training_pack.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.developer_training_pack import build_developer_training_pack

def test_developer_pack():
    prof = get_default_local_training_profile()
    txt, sum = build_developer_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert "deployment instruction değildir" in txt.lower() or "deployment" in txt.lower()
''')

with open("tests/test_safe_usage_training.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.safe_usage_training import build_safe_usage_training_pack, build_safe_usage_rules, build_forbidden_action_training

def test_safe_usage():
    prof = get_default_local_training_profile()
    txt, sum = build_safe_usage_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert not build_safe_usage_rules(prof).empty
    assert not build_forbidden_action_training(prof).empty
''')

with open("tests/test_non_use_policy_training.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.non_use_policy_training import build_non_use_policy_training_pack, build_non_use_policy_examples, build_safe_vs_unsafe_prompt_examples

def test_non_use():
    prof = get_default_local_training_profile()
    txt, sum = build_non_use_policy_training_pack(Path("."), prof)
    assert isinstance(txt, str)
    assert not build_non_use_policy_examples(prof).empty
    assert not build_safe_vs_unsafe_prompt_examples(prof).empty
''')

with open("tests/test_walkthrough_registry.py", "w", encoding="utf-8") as f:
    f.write('''from local_training.training_config import get_default_local_training_profile
from local_training.walkthrough_registry import build_guided_walkthrough_registry, build_default_walkthroughs

def test_walkthrough_registry():
    prof = get_default_local_training_profile()
    df, sum = build_guided_walkthrough_registry(prof)
    assert not df.empty
    assert not build_default_walkthroughs(prof).empty
''')

with open("tests/test_local_walkthroughs.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.local_walkthroughs import build_local_walkthrough_lessons, build_walkthrough_steps, validate_walkthrough_steps_safety

def test_local_walkthroughs():
    prof = get_default_local_training_profile()
    df, sum = build_local_walkthrough_lessons(Path("."), prof)
    assert not df.empty
    steps = build_walkthrough_steps("repo", prof)
    assert isinstance(steps, list)
    val = validate_walkthrough_steps_safety(steps, prof)
    assert val["is_safe"]
''')

with open("tests/test_command_lessons.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.command_lessons import build_safe_command_lesson_registry, classify_training_command_safety, detect_forbidden_training_command_terms

def test_command_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_safe_command_lesson_registry(Path("."), prof)
    assert not df.empty
    assert classify_training_command_safety("python -m script")["is_safe"]
    assert not classify_training_command_safety("buy something")["is_safe"]
    assert "buy" in detect_forbidden_training_command_terms("buy something")
''')

with open("tests/test_report_lessons.py", "w", encoding="utf-8") as f:
    f.write('''from pathlib import Path
from local_training.training_config import get_default_local_training_profile
from local_training.report_lessons import build_report_reading_lesson_registry, build_report_reading_lesson

def test_report_lessons():
    prof = get_default_local_training_profile()
    df, sum = build_report_reading_lesson_registry(Path("."), prof)
    assert not df.empty
    l = build_report_reading_lesson("test", prof)
    assert "Yatırım tavsiyesi" in l.warnings[1]
''')
