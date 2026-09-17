# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Evaluation Master Status Script.

Executes the full Phase 151 Benchmark Comparison and Strategy Evaluation Reports pipeline,
compiles master status, validates safety boundaries, checks Phase 152 handoff readiness,
and saves all reports to DataLake and output directories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_pipeline import (
    BenchmarkEvaluationPipeline,
)


def main():
    settings = get_settings()
    profile = get_default_benchmark_evaluation_profile()
    pipeline = BenchmarkEvaluationPipeline(profile=profile)

    status_df, summary = pipeline.build_benchmark_evaluation_status(save=True)

    print("=" * 70)
    print("PHASE 151: BENCHMARK EVALUATION & STRATEGY REPORTS MASTER STATUS")
    print("=" * 70)
    print(status_df.to_string(index=False))
    print("-" * 70)
    print(f"Phase                 : {summary.get('current_phase', 151)}")
    print(f"Target Final Phase    : 160")
    print(f"Next Phase            : {summary.get('next_phase', 152)}")
    print(f"Profile               : {profile.profile_name}")
    print(f"All Stages Ready      : {summary.get('all_stages_ready')}")
    print(f"Phase Status          : {summary.get('status')}")
    print(f"Non-Signal Invariant  : {summary.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
