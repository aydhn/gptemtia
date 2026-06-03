from portable_packaging.bundle_manifest import (
    scan_bundle_artifacts,
    classify_bundle_artifact,
    decide_artifact_include_policy,
    build_portable_bundle_manifest
)
from portable_packaging.packaging_config import get_default_portable_packaging_profile

def test_bundle_manifest(tmp_path):
    (tmp_path / "app.py").write_text("")
    (tmp_path / ".env").write_text("")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/readme.md").write_text("")

    profile = get_default_portable_packaging_profile()
    df, sum = scan_bundle_artifacts(tmp_path, profile)

    assert not df.empty

    cls = classify_bundle_artifact(tmp_path / "app.py", tmp_path)
    assert cls == "source_artifact"

    pol = decide_artifact_include_policy(tmp_path / ".env", "config_artifact", profile)
    assert pol["policy"] == "exclude_secret"

    man = build_portable_bundle_manifest(profile, df, None)
    assert man.manifest_id
