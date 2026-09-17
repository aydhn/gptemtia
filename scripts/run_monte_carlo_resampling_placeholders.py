# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Resampling Placeholders Script.

Builds and persists residual resampling, noise injection, and path perturbation placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.residual_resampling_placeholders import (
    build_residual_resampling_placeholder_registry,
)
from advanced_monte_carlo_robustness.noise_injection_placeholders import (
    build_noise_injection_placeholder_registry,
)
from advanced_monte_carlo_robustness.path_perturbation_placeholders import (
    build_path_perturbation_placeholder_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_resampling_placeholder_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_res, s_res = build_residual_resampling_placeholder_registry(profile)
    df_nse, s_nse = build_noise_injection_placeholder_registry(profile)
    df_pth, s_pth = build_path_perturbation_placeholder_registry(profile)

    data_lake.save_residual_resampling_placeholders(df_res, s_res)
    data_lake.save_noise_injection_placeholders(df_nse, s_nse)
    data_lake.save_path_perturbation_placeholders(df_pth, s_pth)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "resampling_placeholders.md", "w", encoding="utf-8") as f:
        f.write(build_resampling_placeholder_markdown_report(s_res, df_res))

    print("Monte Carlo resampling and perturbation placeholders successfully built.")


if __name__ == "__main__":
    main()
