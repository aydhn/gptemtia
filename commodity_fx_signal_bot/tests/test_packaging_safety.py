from portable_packaging.packaging_safety import (
    scan_bundle_for_secret_risk,
    scan_packaging_outputs_for_forbidden_terms,
    validate_no_publish_or_deploy_paths,
    validate_manifest_only_data_policy
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile
import pandas as pd
from pathlib import Path

def test_packaging_safety():
    profile = get_default_portable_packaging_profile()

    df, s = scan_bundle_for_secret_risk(pd.DataFrame(), Path("."))
    assert s["secrets_found"] == 0

    terms = scan_packaging_outputs_for_forbidden_terms("package publish")
    assert "package publish" in terms["forbidden_terms_found"]

    terms = scan_packaging_outputs_for_forbidden_terms("package publish yoktur")
    assert "package publish" not in terms["forbidden_terms_found"]

    assert validate_no_publish_or_deploy_paths(pd.DataFrame())["valid"]
    assert validate_manifest_only_data_policy(pd.DataFrame(), profile)["valid"]
