from pathlib import Path
from portable_packaging.dependency_inventory import (
    parse_requirements_files,
    parse_pyproject_dependencies,
    collect_imported_packages,
    build_dependency_inventory,
    compare_required_vs_installed
)

def test_dependency_collections(tmp_path):
    (tmp_path / "requirements.txt").write_text("pandas==2.0.0")
    df = parse_requirements_files(tmp_path)
    assert not df.empty

    py = parse_pyproject_dependencies(tmp_path)
    assert py.empty

    (tmp_path / "app.py").write_text("import pandas\n")
    imports = collect_imported_packages(tmp_path)
    assert not imports.empty

    inv, sum = build_dependency_inventory(tmp_path, None)
    assert not inv.empty

    comp = compare_required_vs_installed(inv)
    assert comp.empty # because installed version is None
