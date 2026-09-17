# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Robustness Contracts Script.

Builds and persists Monte Carlo robustness, bootstrap, and resampling contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_robustness_contracts import (
    build_monte_carlo_robustness_contract_registry,
)
from advanced_monte_carlo_robustness.bootstrap_simulation_contracts import (
    build_bootstrap_simulation_contract_registry,
)
from advanced_monte_carlo_robustness.block_bootstrap_contracts import (
    build_block_bootstrap_contract_registry,
)
from advanced_monte_carlo_robustness.stationary_bootstrap_contracts import (
    build_stationary_bootstrap_contract_registry,
)
from advanced_monte_carlo_robustness.return_path_resampling_contracts import (
    build_return_path_resampling_contract_registry,
)
from advanced_monte_carlo_robustness.trade_sequence_reshuffling_contracts import (
    build_trade_sequence_reshuffling_contract_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_contract_markdown_report,
    build_bootstrap_contract_markdown_report,
)
from reports.report_builder import (
    build_monte_carlo_contracts_text_report,
    build_bootstrap_simulation_contracts_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_core, s_core = build_monte_carlo_robustness_contract_registry(profile)
    df_boot, s_boot = build_bootstrap_simulation_contract_registry(profile)
    df_blk, s_blk = build_block_bootstrap_contract_registry(profile)
    df_stat, s_stat = build_stationary_bootstrap_contract_registry(profile)
    df_path, s_path = build_return_path_resampling_contract_registry(profile)
    df_trd, s_trd = build_trade_sequence_reshuffling_contract_registry(profile)

    data_lake.save_monte_carlo_robustness_contracts(df_core, s_core)
    data_lake.save_bootstrap_simulation_contracts(df_boot, s_boot)
    data_lake.save_block_bootstrap_contracts(df_blk, s_blk)
    data_lake.save_stationary_bootstrap_contracts(df_stat, s_stat)
    data_lake.save_return_path_resampling_contracts(df_path, s_path)
    data_lake.save_trade_sequence_reshuffling_contracts(df_trd, s_trd)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "contracts.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_contract_markdown_report(s_core, df_core))
    with open(out_dir / "contracts.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_contracts_text_report(s_core, df_core))
    with open(out_dir / "bootstrap_contracts.md", "w", encoding="utf-8") as f:
        f.write(build_bootstrap_contract_markdown_report(s_boot, df_boot))
    with open(out_dir / "bootstrap_contracts.txt", "w", encoding="utf-8") as f:
        f.write(build_bootstrap_simulation_contracts_text_report(s_boot, df_boot))

    print("Monte Carlo robustness and bootstrap contracts successfully built.")


if __name__ == "__main__":
    main()
