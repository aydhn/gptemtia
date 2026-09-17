# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Evaluation Health Check Script.

Performs comprehensive health checks for Phase 151 directories, files,
imports, and negative invariant enforcement.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_health import (
    build_benchmark_evaluation_health_check,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_health_markdown_report,
)


def main():
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_health, s_health = build_benchmark_evaluation_health_check(project_root, profile)
    data_lake.save_benchmark_evaluation_health_check(df_health, s_health)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_health_markdown_report(s_health, df_health))

    print("=" * 70)
    print("PHASE 151: BENCHMARK EVALUATION HEALTH CHECK")
    print("=" * 70)
    print(df_health.to_string(index=False))
    print("-" * 70)
    print(f"Overall Health Status: {s_health.get('status')}")
    print(f"Total Checks         : {s_health.get('total_checks')}")
    print(f"Passed Checks        : {s_health.get('passed_checks')}")
    print(f"Failed Checks        : {s_health.get('failed_checks')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
