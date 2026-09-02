import os
from pathlib import Path

BASE_DIR = Path("commodity_fx_signal_bot")

def write_file(path_str, content):
    p = BASE_DIR / path_str
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {p}")

write_file("tests/test_delivery_config.py", '''
import pytest
from local_delivery.delivery_config import get_local_delivery_profile, list_local_delivery_profiles, validate_local_delivery_profiles, get_default_local_delivery_profile, ConfigError

def test_validate_local_delivery_profiles():
    validate_local_delivery_profiles()

def test_get_default_local_delivery_profile():
    p = get_default_local_delivery_profile()
    assert p.name == "balanced_local_delivery"
    assert p.dry_run_default is True

def test_list_profiles():
    assert len(list_local_delivery_profiles()) > 0

def test_unknown_profile():
    with pytest.raises(ConfigError):
        get_local_delivery_profile("unknown")
''')

write_file("tests/test_delivery_labels.py", '''
import pytest
from local_delivery.delivery_labels import list_delivery_domain_labels, list_delivery_item_labels, list_delivery_status_labels, list_transfer_readiness_labels, list_delivery_risk_labels
from local_delivery.delivery_labels import validate_delivery_domain_label, validate_delivery_status

def test_label_lists():
    assert len(list_delivery_domain_labels()) > 0
    assert len(list_delivery_item_labels()) > 0
    assert len(list_delivery_status_labels()) > 0
    assert len(list_transfer_readiness_labels()) > 0
    assert len(list_delivery_risk_labels()) > 0

def test_validate_labels():
    validate_delivery_domain_label("bundle_manifest_domain")
    validate_delivery_status("delivery_ready_for_rehearsal")
    with pytest.raises(ValueError):
        validate_delivery_domain_label("invalid")
''')

write_file("tests/test_delivery_models.py", '''
from local_delivery.delivery_models import build_delivery_domain_id, build_delivery_item_id, build_delivery_trace_id, build_delivery_checklist_id, build_delivery_finding_id
from local_delivery.delivery_models import DeliveryDomain, delivery_domain_to_dict

def test_model_ids():
    assert build_delivery_domain_id("test") == build_delivery_domain_id("test")
    assert build_delivery_item_id("path", "lbl") == build_delivery_item_id("path", "lbl")
    assert build_delivery_trace_id("src", "tgt") == build_delivery_trace_id("src", "tgt")

def test_model_to_dict():
    d = DeliveryDomain("id", "lbl", "name", "desc", [], [])
    res = delivery_domain_to_dict(d)
    assert res["domain_id"] == "id"
''')

write_file("tests/test_delivery_domain_registry.py", '''
from local_delivery.delivery_domain_registry import build_delivery_domain_registry
from local_delivery.delivery_config import get_default_local_delivery_profile

def test_build_delivery_domain_registry():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_domain_registry(prof)
    assert not df.empty
    assert summary["total_domains"] > 0
''')

write_file("tests/test_bundle_manifest.py", '''
from local_delivery.bundle_manifest import build_final_delivery_bundle_manifest, build_delivery_bundle_manifest_items
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_manifest():
    prof = get_default_local_delivery_profile()
    man, val = build_final_delivery_bundle_manifest(Path("."), prof)
    assert "local_only_delivery_statement" in man
    df, sum2 = build_delivery_bundle_manifest_items(Path("."), prof)
    assert not df.empty
''')

write_file("tests/test_handoff_package_index.py", '''
from local_delivery.handoff_package_index import build_handoff_package_index, classify_handoff_item_label, classify_handoff_source_layer
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_index():
    prof = get_default_local_delivery_profile()
    df, summary = build_handoff_package_index(Path("."), prof)
    assert summary is dict or isinstance(summary, dict)

def test_classify_labels():
    lbl = classify_handoff_item_label(Path("docs/readme.md"), Path("."))
    assert lbl == "delivery_doc_item"
''')

write_file("tests/test_portable_reviewer_guide.py", '''
from local_delivery.portable_reviewer_guide import build_portable_reviewer_archive_guide
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd
from pathlib import Path

def test_build_guide():
    prof = get_default_local_delivery_profile()
    text, summary = build_portable_reviewer_archive_guide(Path("."), pd.DataFrame(), prof)
    assert isinstance(text, str)
    assert "Review Order" in text
''')

write_file("tests/test_transfer_checklist.py", '''
from local_delivery.transfer_checklist import build_final_local_transfer_checklist
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_checklist():
    prof = get_default_local_delivery_profile()
    df, summary = build_final_local_transfer_checklist(Path("."), prof)
    assert not df.empty
''')

write_file("tests/test_delivery_rehearsal_binder.py", '''
from local_delivery.delivery_rehearsal_binder import build_delivery_rehearsal_binder
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_binder():
    prof = get_default_local_delivery_profile()
    text, summary = build_delivery_rehearsal_binder({}, pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), prof)
    assert isinstance(text, str)
''')

write_file("tests/test_recipient_orientation.py", '''
from local_delivery.recipient_orientation import build_recipient_orientation_guide
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_orientation():
    prof = get_default_local_delivery_profile()
    text, summary = build_recipient_orientation_guide(Path("."), prof)
    assert isinstance(text, str)
''')

write_file("tests/test_delivery_evidence_map.py", '''
from local_delivery.delivery_evidence_map import build_delivery_evidence_map
from local_delivery.delivery_config import get_default_local_delivery_profile
from pathlib import Path

def test_build_evidence_map():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_evidence_map(Path("."), prof)
    assert not df.empty
''')

write_file("tests/test_artifact_trace_matrix.py", '''
from local_delivery.artifact_trace_matrix import build_delivery_artifact_trace_matrix
from local_delivery.delivery_config import get_default_local_delivery_profile
import pandas as pd

def test_build_trace_matrix():
    prof = get_default_local_delivery_profile()
    df, summary = build_delivery_artifact_trace_matrix(pd.DataFrame(), pd.DataFrame(), prof)
    assert not df.empty
''')

