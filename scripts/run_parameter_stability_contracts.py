# -*- coding: utf-8 -*-
"""Phase 149: Run Parameter Stability Contracts Script.

Builds and persists parameter stability, sensitivity, perturbation contracts, and fragility placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.parameter_stability_contracts import (
    build_parameter_stability_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_sensitivity_contracts import (
    build_parameter_sensitivity_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_perturbation_contracts import (
    build_parameter_perturbation_contract_registry,
)
from advanced_monte_carlo_robustness.parameter_grid_stability_placeholders import (
    build_parameter_grid_stability_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_surface_placeholders import (
    build_parameter_surface_placeholder_registry,
)
from advanced_monte_carlo_robustness.parameter_fragility_placeholders import (
    build_parameter_fragility_placeholder_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_parameter_stability_markdown_report,
)
from reports.report_builder import build_parameter_stability_contracts_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_stab, s_stab = build_parameter_stability_contract_registry(profile)
    df_sens, s_sens = build_parameter_sensitivity_contract_registry(profile)
    df_pert, s_pert = build_parameter_perturbation_contract_registry(profile)
    df_grid, s_grid = build_parameter_grid_stability_placeholder_registry(profile)
    df_surf, s_surf = build_parameter_surface_placeholder_registry(profile)
    df_frag, s_frag = build_parameter_fragility_placeholder_registry(profile)

    data_lake.save_parameter_stability_contracts(df_stab, s_stab)
    data_lake.save_parameter_sensitivity_contracts(df_sens, s_sens)
    data_lake.save_parameter_perturbation_contracts(df_pert, s_pert)
    data_lake.save_parameter_grid_stability_placeholders(df_grid, s_grid)
    data_lake.save_parameter_surface_placeholders(df_surf, s_surf)
    data_lake.save_parameter_fragility_placeholders(df_frag, s_frag)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "parameter_stability.md", "w", encoding="utf-8") as f:
        f.write(build_parameter_stability_markdown_report(s_stab, df_stab))
    with open(out_dir / "parameter_stability.txt", "w", encoding="utf-8") as f:
        f.write(build_parameter_stability_contracts_text_report(s_stab, df_stab))

    print("Parameter stability and sensitivity contracts successfully built.")


if __name__ == "__main__":
    main()
