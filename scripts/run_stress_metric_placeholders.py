# -*- coding: utf-8 -*-
"""Phase 148: Run Stress Metric Placeholders Script.

Builds and persists stress, scenario, and robustness metric placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_stress_testing.stress_testing_config import (
    get_default_stress_testing_profile,
)
from advanced_stress_testing.stress_metric_placeholders import (
    build_stress_metric_placeholder_registry,
)
from advanced_stress_testing.scenario_metric_placeholders import (
    build_scenario_metric_placeholder_registry,
)
from advanced_stress_testing.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_stress_testing.stress_testing_report_builder import (
    build_stress_metric_placeholder_markdown_report,
)
from reports.report_builder import build_stress_metric_placeholder_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_stress_testing_profile()

    df_stress, s_stress = build_stress_metric_placeholder_registry(profile)
    df_scen, s_scen = build_scenario_metric_placeholder_registry(profile)
    df_rob, s_rob = build_robustness_metric_placeholder_registry(profile)

    data_lake.save_stress_metric_placeholder_registry(df_stress, s_stress)
    data_lake.save_scenario_metric_placeholder_registry(df_scen, s_scen)
    data_lake.save_robustness_metric_placeholder_registry(df_rob, s_rob)

    summary = {
        "total_stress_metrics": len(df_stress) + len(df_scen) + len(df_rob),
        "stress_metrics_count": len(df_stress),
        "scenario_metrics_count": len(df_scen),
        "robustness_metrics_count": len(df_rob),
    }

    md_report = build_stress_metric_placeholder_markdown_report(summary, df_stress)
    txt_report = build_stress_metric_placeholder_text_report(summary, df_stress)

    out_dir = Path("reports/output/advanced_stress_testing")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "metric_placeholders.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "metric_placeholders.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Stress and scenario metric placeholders successfully built and persisted.")


if __name__ == "__main__":
    main()
