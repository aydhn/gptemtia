from pathlib import Path
from advanced_feature_grid.feature_grid_health import build_feature_grid_health_check, summarize_feature_grid_health


def test_feature_grid_health():
    project_root = Path(__file__).resolve().parent.parent
    df, summary = build_feature_grid_health_check(project_root)

    assert not df.empty
    assert summary["all_healthy"] is True
    assert summary["health_status"] == "HEALTHY"
    assert summary["unhealthy_components"] == 0
