# -*- coding: utf-8 -*-
"""Phase 149: Run Monte Carlo Findings and Manifest Script.

Builds and persists manual review queue, findings registry, readiness score, and master manifest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_monte_carlo_robustness.monte_carlo_config import (
    get_default_monte_carlo_profile,
)
from advanced_monte_carlo_robustness.monte_carlo_manual_review import (
    build_monte_carlo_manual_review_queue,
)
from advanced_monte_carlo_robustness.monte_carlo_findings import (
    build_monte_carlo_findings_registry,
)
from advanced_monte_carlo_robustness.monte_carlo_readiness_scoring import (
    build_monte_carlo_readiness_score_report,
)
from advanced_monte_carlo_robustness.monte_carlo_manifest import (
    build_monte_carlo_robustness_manifest,
)
from advanced_monte_carlo_robustness.monte_carlo_report_builder import (
    build_monte_carlo_findings_markdown_report,
    build_monte_carlo_readiness_score_markdown_report,
    build_monte_carlo_manifest_markdown_report,
)
from reports.report_builder import (
    build_monte_carlo_findings_text_report,
    build_monte_carlo_readiness_score_text_report,
    build_monte_carlo_manifest_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_monte_carlo_profile()

    df_rev, s_rev = build_monte_carlo_manual_review_queue(profile)
    df_find, s_find = build_monte_carlo_findings_registry(profile)
    df_score, s_score = build_monte_carlo_readiness_score_report(profile, findings_df=df_find)
    df_man, s_man = build_monte_carlo_robustness_manifest(profile)

    data_lake.save_monte_carlo_manual_review_queue(df_rev, s_rev)
    data_lake.save_monte_carlo_findings_registry(df_find, s_find)
    data_lake.save_monte_carlo_readiness_score_report(df_score, s_score)
    data_lake.save_monte_carlo_robustness_manifest(df_man, s_man)

    out_dir = Path("reports/output/advanced_monte_carlo_robustness")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_findings_markdown_report(s_find, df_find))
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_findings_text_report(s_find, df_find))
    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_readiness_score_markdown_report(s_score, df_score))
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_readiness_score_text_report(s_score, df_score))
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_manifest_markdown_report(s_man, df_man))
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(build_monte_carlo_manifest_text_report(s_man, df_man))

    print("Monte Carlo findings, readiness score, and manifest successfully built.")


if __name__ == "__main__":
    main()
