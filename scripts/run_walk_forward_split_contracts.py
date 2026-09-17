# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Split Contracts Script.

Builds and persists walk-forward, rolling, expanding, anchored, and purged split contracts.
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
    build_walk_forward_contract_markdown_report,
)
from reports.report_builder import build_walk_forward_contract_text_report


def main():
    settings = get_settings()
    profile = get_default_walk_forward_profile()
    pipeline = WalkForwardValidationPipeline(profile=profile)

    dfs, summaries = pipeline.build_split_contracts(save=True)

    md_report = build_walk_forward_contract_markdown_report(
        summaries["walk_forward"], dfs["walk_forward_contracts"]
    )
    txt_report = build_walk_forward_contract_text_report(
        summaries["walk_forward"], dfs["walk_forward_contracts"]
    )

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "walk_forward_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "walk_forward_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("Walk-forward split contracts successfully built and saved.")


if __name__ == "__main__":
    main()
