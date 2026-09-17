# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Metric Placeholders Script.

Builds and persists robustness envelopes, distribution placeholders, and metric formula placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.robustness_envelope_placeholders import (
    build_robustness_envelope_placeholder_registry,
)
from advanced_monte_carlo_robustness.stability_band_placeholders import (
    build_stability_band_placeholder_registry,
)
from advanced_monte_carlo_robustness.confidence_interval_placeholders import (
    build_confidence_interval_placeholder_registry,
)
from advanced_monte_carlo_robustness.drawdown_distribution_placeholders import (
    build_drawdown_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.return_distribution_placeholders import (
    build_return_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.tail_risk_distribution_placeholders import (
    build_tail_risk_distribution_placeholder_registry,
)
from advanced_monte_carlo_robustness.worst_case_path_placeholders import (
    build_worst_case_path_placeholder_registry,
)
from advanced_monte_carlo_robustness.best_case_path_placeholders import (
    build_best_case_path_placeholder_registry,
)
from advanced_monte_carlo_robustness.median_case_path_placeholders import (
    build_median_case_path_placeholder_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_metric_placeholders import (
    build_monte_carlo_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.robustness_metric_placeholders import (
    build_robustness_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_stability_metric_placeholders import (
    build_parameter_stability_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.fragility_metric_placeholders import (
    build_fragility_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.distribution_metric_placeholders import (
    build_distribution_metric_placeholder_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_robustness_placeholder_markdown_report,
    build_monte_carlo_metric_placeholder_markdown_report,
)
from reports.report_builder import build_monte_carlo_metric_placeholders_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_env, s_env = build_robustness_envelope_placeholder_registry(profile)
    df_bnd, s_bnd = build_stability_band_placeholder_registry(profile)
    df_ci, s_ci = build_confidence_interval_placeholder_registry(profile)
    df_dd, s_dd = build_drawdown_distribution_placeholder_registry(profile)
    df_ret, s_ret = build_return_distribution_placeholder_registry(profile)
    df_tl, s_tl = build_tail_risk_distribution_placeholder_registry(profile)
    df_wc, s_wc = build_worst_case_path_placeholder_registry(profile)
    df_bc, s_bc = build_best_case_path_placeholder_registry(profile)
    df_med, s_med = build_median_case_path_placeholder_registry(profile)

    df_mc_m, s_mc_m = build_monte_carlo_metric_placeholder_registry(profile)
    df_rb_m, s_rb_m = build_robustness_metric_placeholder_registry(profile)
    df_ps_m, s_ps_m = build_parameter_stability_metric_placeholder_registry(profile)
    df_fg_m, s_fg_m = build_fragility_metric_placeholder_registry(profile)
    df_ds_m, s_ds_m = build_distribution_metric_placeholder_registry(profile)

    data_lake.save_robustness_envelope_placeholders(df_env, s_env)
    data_lake.save_stability_band_placeholders(df_bnd, s_bnd)
    data_lake.save_confidence_interval_placeholders(df_ci, s_ci)
    data_lake.save_drawdown_distribution_placeholders(df_dd, s_dd)
    data_lake.save_return_distribution_placeholders(df_ret, s_ret)
    data_lake.save_tail_risk_distribution_placeholders(df_tl, s_tl)
    data_lake.save_worst_case_path_placeholders(df_wc, s_wc)
    data_lake.save_best_case_path_placeholders(df_bc, s_bc)
    data_lake.save_median_case_path_placeholders(df_med, s_med)

    data_lake.save_monte_carlo_metric_placeholders(df_mc_m, s_mc_m)
    data_lake.save_robustness_metric_placeholders(df_rb_m, s_rb_m)
    data_lake.save_parameter_stability_metric_placeholders(df_ps_m, s_ps_m)
    data_lake.save_fragility_metric_placeholders(df_fg_m, s_fg_m)
    data_lake.save_distribution_metric_placeholders(df_ds_m, s_ds_m)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "robustness_envelopes.md", "w", encoding="utf-8") as f:
        f.write(build_robustness_placeholder_markdown_report(s_env, df_env))
    with open(out_dir / "metric_placeholders.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_metric_placeholder_markdown_report(s_mc_m, df_mc_m))
    with open(out_dir / "metric_placeholders.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_metric_placeholders_text_report(s_mc_m, df_mc_m))

    print("Monte Carlo envelopes, distributions, and metric placeholders successfully built.")


if __name__ == "__main__":
    main()
