# -*- coding: utf-8 -*-
"""Phase 151: Run Benchmark Evaluation Findings and Manifest Script.

Builds and persists benchmark evaluation dependencies, evidence, manual review queue,
findings registry, readiness scoring, and signs the Phase 151 manifest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_benchmark_evaluation.benchmark_evaluation_config import (
    get_default_benchmark_evaluation_profile,
)
from advanced_benchmark_evaluation.benchmark_evaluation_dependencies import (
    build_benchmark_evaluation_dependency_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_validation_evidence import (
    build_benchmark_evaluation_validation_evidence_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manual_review import (
    build_benchmark_evaluation_manual_review_queue,
)
from advanced_benchmark_evaluation.benchmark_evaluation_findings import (
    build_benchmark_evaluation_findings_registry,
)
from advanced_benchmark_evaluation.benchmark_evaluation_readiness_scoring import (
    build_benchmark_evaluation_readiness_score_report,
)
from advanced_benchmark_evaluation.benchmark_evaluation_manifest import (
    build_benchmark_evaluation_manifest,
)
from advanced_benchmark_evaluation.benchmark_evaluation_report_builder import (
    build_benchmark_evaluation_manifest_markdown_report,
)
from reports.report_builder import (
    build_benchmark_evaluation_manifest_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_benchmark_evaluation_profile()

    df_dep, s_dep = build_benchmark_evaluation_dependency_registry(profile)
    df_evid, s_evid = build_benchmark_evaluation_validation_evidence_registry(profile)
    df_rev, s_rev = build_benchmark_evaluation_manual_review_queue(profile)
    df_find, s_find = build_benchmark_evaluation_findings_registry(profile)
    df_score, s_score = build_benchmark_evaluation_readiness_score_report(profile)
    df_man, s_man = build_benchmark_evaluation_manifest(profile)

    data_lake.save_benchmark_evaluation_dependencies(df_dep, s_dep)
    data_lake.save_benchmark_evaluation_validation_evidence(df_evid, s_evid)
    data_lake.save_benchmark_evaluation_manual_review_queue(df_rev, s_rev)
    data_lake.save_benchmark_evaluation_findings_registry(df_find, s_find)
    data_lake.save_benchmark_evaluation_readiness_score_report(df_score, s_score)
    data_lake.save_benchmark_evaluation_manifest(df_man, s_man)

    out_dir = Path("reports/output/advanced_benchmark_evaluation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_manifest_markdown_report(s_man, df_man))
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(build_benchmark_evaluation_manifest_text_report(s_man, df_man))

    print("Phase 151 findings, readiness scoring, and manifest successfully built and signed.")


if __name__ == "__main__":
    main()
