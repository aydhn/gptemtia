# -*- coding: utf-8 -*-
"""Phase 147: Run OOS Benchmark Contracts Script.

Builds and persists benchmark universe, baseline, and comparison contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_pipeline import (
    WalkForwardValidationPipeline,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_benchmark_contract_markdown_report,
)
from reports.report_builder import build_benchmark_contract_text_report


def main():
    settings = get_settings()
    profile = get_default_walk_forward_profile()
    pipeline = WalkForwardValidationPipeline(profile=profile)

    dfs, summaries = pipeline.build_oos_benchmark_contracts(save=True)

    md_report = build_benchmark_contract_markdown_report(
        summaries["benchmarks"], dfs["oos_benchmark_contracts"]
    )
    txt_report = build_benchmark_contract_text_report(
        summaries["benchmarks"], dfs["oos_benchmark_contracts"]
    )

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "benchmark_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "benchmark_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("OOS benchmark contracts successfully built and saved.")


if __name__ == "__main__":
    main()
