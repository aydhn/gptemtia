from pathlib import Path
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.data_lineage_health import (
    build_data_lineage_health_check,
    summarize_data_lineage_health,
)


def test_data_lineage_health():
    project_root = Path(__file__).resolve().parent.parent
    profile = get_default_data_lineage_profile()
    df, summary = build_data_lineage_health_check(project_root, profile)

    assert len(df) >= 40
    assert summary["overall_status"] == "PASS"
    assert summary["failed_checks"] == 0
