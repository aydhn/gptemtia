import pytest
from local_post_completion_preservation.preservation_models import *

def test_models():
    assert build_preservation_domain_id("test") == "dom_test"
    item = EvidenceVaultItem("id", "name", "area", "path", "status", 1, False, [])
    d = evidence_vault_item_to_dict(item)
    assert "evidence_id" in d
