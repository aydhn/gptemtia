# -*- coding: utf-8 -*-
"""Phase 147: Run Validation Bias Guards Script.

Builds and persists no-lookahead, purge, embargo, data snooping, overfitting, and survivorship guards.
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
    build_validation_guard_markdown_report,
)
from reports.report_builder import build_validation_guard_text_report


def main():
    settings = get_settings()
    profile = get_default_walk_forward_profile()
    pipeline = WalkForwardValidationPipeline(profile=profile)

    dfs, summaries = pipeline.build_dependencies_and_guards(save=True)

    md_report = build_validation_guard_markdown_report(
        summaries["no_lookahead"], dfs["no_lookahead_guards"]
    )
    txt_report = build_validation_guard_text_report(
        summaries["no_lookahead"], dfs["no_lookahead_guards"]
    )

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "guards.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "guards.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Validation bias guards successfully built and saved.")


if __name__ == "__main__":
    main()
