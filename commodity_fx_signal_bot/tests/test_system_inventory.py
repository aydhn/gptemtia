import pytest
from pathlib import Path
from final_review.system_inventory import (
    build_module_inventory, build_script_inventory, build_test_inventory,
    build_report_inventory, build_full_system_inventory
)

@pytest.fixture
def project_root():
    return Path(__file__).resolve().parent.parent

def test_system_inventory_builders(project_root):
    assert not build_module_inventory(project_root).empty
    assert not build_script_inventory(project_root).empty
    assert not build_test_inventory(project_root).empty
    assert not build_report_inventory(project_root).empty

    tables, summary = build_full_system_inventory(project_root)
    assert "modules" in tables
    assert "module_count" in summary
