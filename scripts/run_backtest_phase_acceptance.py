# -*- coding: utf-8 -*-
"""Phase 152: Run Phase Acceptance Script.

Builds and verifies acceptance registries for Phases 146 through 151.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.phase_146_realistic_backtest_acceptance import (
    build_phase_146_realistic_backtest_acceptance_registry,
)
from advanced_backtest_acceptance.phase_147_walk_forward_oos_acceptance import (
    build_phase_147_walk_forward_oos_acceptance_registry,
)
from advanced_backtest_acceptance.phase_148_stress_testing_acceptance import (
    build_phase_148_stress_testing_acceptance_registry,
)
from advanced_backtest_acceptance.phase_149_monte_carlo_acceptance import (
    build_phase_149_monte_carlo_acceptance_registry,
)
from advanced_backtest_acceptance.phase_150_backtest_governance_acceptance import (
    build_phase_150_backtest_governance_acceptance_registry,
)
from advanced_backtest_acceptance.phase_151_benchmark_evaluation_acceptance import (
    build_phase_151_benchmark_evaluation_acceptance_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_phase_acceptance_markdown_report,
)
from reports.report_builder import build_backtest_phase_acceptance_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_acceptance_profile()

    df_146, s_146 = build_phase_146_realistic_backtest_acceptance_registry(profile)
    df_147, s_147 = build_phase_147_walk_forward_oos_acceptance_registry(profile)
    df_148, s_148 = build_phase_148_stress_testing_acceptance_registry(profile)
    df_149, s_149 = build_phase_149_monte_carlo_acceptance_registry(profile)
    df_150, s_150 = build_phase_150_backtest_governance_acceptance_registry(profile)
    df_151, s_151 = build_phase_151_benchmark_evaluation_acceptance_registry(profile)

    data_lake.save_phase_146_realistic_backtest_acceptance_registry(df_146, s_146)
    data_lake.save_phase_147_walk_forward_oos_acceptance_registry(df_147, s_147)
    data_lake.save_phase_148_stress_testing_acceptance_registry(df_148, s_148)
    data_lake.save_phase_149_monte_carlo_acceptance_registry(df_149, s_149)
    data_lake.save_phase_150_backtest_governance_acceptance_registry(df_150, s_150)
    data_lake.save_phase_151_benchmark_evaluation_acceptance_registry(df_151, s_151)

    out_dir = Path("reports/output/advanced_backtest_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    for tag, (df, s) in [
        ("phase_146", (df_146, s_146)),
        ("phase_147", (df_147, s_147)),
        ("phase_148", (df_148, s_148)),
        ("phase_149", (df_149, s_149)),
        ("phase_150", (df_150, s_150)),
        ("phase_151", (df_151, s_151)),
    ]:
        md = build_phase_acceptance_markdown_report(s, df)
        txt = build_backtest_phase_acceptance_text_report(s, df)
        with open(out_dir / f"{tag}_acceptance.md", "w", encoding="utf-8") as f:
            f.write(md)
        with open(out_dir / f"{tag}_acceptance.txt", "w", encoding="utf-8") as f:
            f.write(txt)

    print("=" * 70)
    print("PHASE 152: CONSOLIDATED PHASE 146-151 ACCEPTANCE")
    print("=" * 70)
    print(f"Phase 146 (Realistic Backtest)  : {s_146['passed_checks']}/{s_146['total_checks']} PASS")
    print(f"Phase 147 (Walk-Forward OOS)    : {s_147['passed_checks']}/{s_147['total_checks']} PASS")
    print(f"Phase 148 (Stress Testing)      : {s_148['passed_checks']}/{s_148['total_checks']} PASS")
    print(f"Phase 149 (Monte Carlo)         : {s_149['passed_checks']}/{s_149['total_checks']} PASS")
    print(f"Phase 150 (Backtest Governance) : {s_150['passed_checks']}/{s_150['total_checks']} PASS")
    print(f"Phase 151 (Benchmark Eval)      : {s_151['passed_checks']}/{s_151['total_checks']} PASS")
    print(f"Non-Signal                      : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
