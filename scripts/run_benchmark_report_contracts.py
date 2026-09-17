# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Report Contracts Script.

Builds and persists benchmark comparison report contracts, universe contracts, and baseline contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_comparison_report_contracts import (
    build_benchmark_comparison_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_universe_report_contracts import (
    build_benchmark_universe_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_baseline_report_contracts import (
    build_benchmark_baseline_report_contract_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_report_contract_markdown_report,
)
from reports.report_builder import (
    build_benchmark_comparison_report_contract_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_bc, s_bc = build_benchmark_comparison_report_contract_registry(profile)
    df_bu, s_bu = build_benchmark_universe_report_contract_registry(profile)
    df_bb, s_bb = build_benchmark_baseline_report_contract_registry(profile)

    data_lake.save_benchmark_comparison_report_contract_registry(df_bc, s_bc)
    data_lake.save_benchmark_universe_report_contract_registry(df_bu, s_bu)
    data_lake.save_benchmark_baseline_report_contract_registry(df_bb, s_bb)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "benchmark_report_contracts.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_report_contract_markdown_report(s_bc, df_bc))
    with open(out_dir / "benchmark_report_contracts.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_comparison_report_contract_text_report(s_bc, df_bc))

    print("Phase 151 benchmark report contracts successfully built and saved.")


if __name__ == "__main__":
    main()
