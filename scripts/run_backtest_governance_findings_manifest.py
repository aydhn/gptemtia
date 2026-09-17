# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Findings and Manifest Script.

Builds and persists findings, manual review queue, readiness scoring, and the master manifest.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_findings import (
    build_backtest_governance_findings_registry,
)
from advanced_backtest_governance.backtest_governance_manual_review import (
    build_backtest_governance_manual_review_queue,
)
from advanced_backtest_governance.backtest_governance_readiness_scoring import (
    build_backtest_governance_readiness_score_report,
)
from advanced_backtest_governance.backtest_governance_manifest import (
    build_backtest_governance_manifest,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_governance_findings_markdown_report,
    build_backtest_governance_readiness_markdown_report,
    build_backtest_governance_manifest_markdown_report,
)
from reports.report_builder import (
    build_backtest_governance_findings_text_report,
    build_backtest_governance_readiness_text_report,
    build_backtest_governance_manifest_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_find, s_find = build_backtest_governance_findings_registry(profile)
    df_queue, s_queue = build_backtest_governance_manual_review_queue(profile)
    df_score, s_score = build_backtest_governance_readiness_score_report(profile, findings_df=df_find)
    df_man, s_man = build_backtest_governance_manifest(profile)

    data_lake.save_backtest_governance_findings(df_find, s_find)
    data_lake.save_backtest_governance_manual_review_queue(df_queue, s_queue)
    data_lake.save_backtest_governance_readiness_score_report(df_score, s_score)
    data_lake.save_backtest_governance_manifest(df_man, s_man)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "findings.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_findings_markdown_report(s_find, df_find))
    with open(out_dir / "findings.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_findings_text_report(s_find, df_find))
    with open(out_dir / "readiness_score.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_readiness_markdown_report(s_score, df_score))
    with open(out_dir / "readiness_score.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_readiness_text_report(s_score, df_score))
    with open(out_dir / "manifest.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_manifest_markdown_report(s_man, df_man))
    with open(out_dir / "manifest.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_manifest_text_report(s_man, df_man))

    print("Phase 150 findings, manual review queue, readiness scoring, and manifest successfully built.")


if __name__ == "__main__":
    main()
