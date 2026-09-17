# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Evaluation Validation Report Script.

Performs rigorous multi-stage validation, enforces safety boundaries,
and verifies Phase 152 handoff readiness.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_pipeline import (
    BenchmarkEvaluationPipeline,
)
from advanced_benchmark_evaluation.benchmark_evaluation_validation import (
    build_benchmark_evaluation_validation_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_safety_boundary import (
    build_benchmark_evaluation_safety_boundary,
)
from advanced_benchmark_evaluation.phase_152_handoff import (
    build_phase_152_backtest_acceptance_report_handoff_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_validation_markdown_report,
    build_benchmark_evaluation_safety_markdown_report,
    build_phase_152_handoff_markdown_report,
)
from reports.report_builder import (
    build_benchmark_evaluation_validation_text_report,
    build_benchmark_evaluation_safety_text_report,
    build_phase_152_handoff_text_report,
)


def main():
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()
    pipeline = BenchmarkEvaluationPipeline(data_lake=data_lake, project_root=project_root, profile=profile)

    t_rep, _ = pipeline.build_report_contracts(save=False)
    t_man, _ = pipeline.build_findings_scoring_manifest(save=False)
    combined = {**t_rep, **t_man}

    df_val, s_val = build_benchmark_evaluation_validation_report(combined, profile)
    df_safe, s_safe = build_benchmark_evaluation_safety_boundary(profile)
    df_hnd, s_hnd = build_phase_152_backtest_acceptance_report_handoff_report(profile)

    data_lake.save_benchmark_evaluation_validation_report(df_val, s_val)
    data_lake.save_benchmark_evaluation_safety_boundary(df_safe, s_safe)
    data_lake.save_phase_152_backtest_acceptance_report_handoff_report(df_hnd, s_hnd)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_validation_markdown_report(s_val, df_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_validation_text_report(s_val, df_val))

    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_safety_markdown_report(s_safe, df_safe))
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_safety_text_report(s_safe, df_safe))

    with open(out_dir / "phase_152_handoff.md", "w", encoding="utf-8") as f:
        f.write(build_phase_152_handoff_markdown_report(s_hnd, df_hnd))
    with open(out_dir / "phase_152_handoff.txt", "w", encoding="utf-8") as f:
        f.write(build_phase_152_handoff_text_report(s_hnd, df_hnd))

    print("=" * 70)
    print("PHASE 151: BENCHMARK EVALUATION VALIDATION & SAFETY REPORT")
    print("=" * 70)
    print(df_val.to_string(index=False))
    print("-" * 70)
    print(f"Validation Status: {s_val.get('status')}")
    print(f"Total Checks     : {s_val.get('total_checks')}")
    print(f"Passed Checks    : {s_val.get('passed_checks')}")
    print(f"Failed Checks    : {s_val.get('failed_checks')}")
    print(f"Phase 152 Handoff: {s_hnd.get('status')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
