import pandas as pd
from portable_packaging.requirements_export import (
    build_requirements_minimal_export,
    build_requirements_frozen_export,
    build_optional_dependencies_note,
    save_requirements_exports
)

def test_requirements_export(tmp_path):
    df = pd.DataFrame([{"package_name": "pandas", "required_version": "2.0.0", "requirement_detected": True}])
    t, _ = build_requirements_minimal_export(df)
    assert "pandas==2.0.0" in t

    installed = pd.DataFrame([{"package_name": "pandas", "installed_version": "2.0.0"}])
    f, _ = build_requirements_frozen_export(installed)
    assert "LOCAL ENVIRONMENT SNAPSHOT" in f

    n = build_optional_dependencies_note(pd.DataFrame([{"optional": False}]))
    assert "No optional dependencies detected" in n

    save_requirements_exports(tmp_path, {"req.txt": "a"})
    assert (tmp_path / "req.txt").exists()
