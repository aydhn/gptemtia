# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Result Boundaries Script.

Builds and persists result reporting contracts, metric/performance claim boundaries,
and disclosure placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_result_reporting_contracts import (
    build_backtest_result_reporting_contract_registry,
)
from advanced_backtest_governance.backtest_metric_claim_boundaries import (
    build_backtest_metric_claim_boundary_registry,
)
from advanced_backtest_governance.backtest_performance_claim_boundaries import (
    build_backtest_performance_claim_boundary_registry,
)
from advanced_backtest_governance.backtest_result_disclosure_placeholders import (
    build_backtest_result_disclosure_placeholder_registry,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_result_reporting_markdown_report,
    build_backtest_claim_boundary_markdown_report,
)
from reports.report_builder import (
    build_backtest_result_reporting_text_report,
    build_backtest_claim_boundary_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_rep, s_rep = build_backtest_result_reporting_contract_registry(profile)
    df_met, s_met = build_backtest_metric_claim_boundary_registry(profile)
    df_perf, s_perf = build_backtest_performance_claim_boundary_registry(profile)
    df_disc, s_disc = build_backtest_result_disclosure_placeholder_registry(profile)

    data_lake.save_backtest_result_reporting_contracts(df_rep, s_rep)
    data_lake.save_backtest_metric_claim_boundaries(df_met, s_met)
    data_lake.save_backtest_performance_claim_boundaries(df_perf, s_perf)
    data_lake.save_backtest_result_disclosure_placeholders(df_disc, s_disc)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "result_reporting.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_result_reporting_markdown_report(s_rep, df_rep))
    with open(out_dir / "result_reporting.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_result_reporting_text_report(s_rep, df_rep))
    with open(out_dir / "claim_boundaries.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_claim_boundary_markdown_report(s_met, df_met))
    with open(out_dir / "claim_boundaries.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_claim_boundary_text_report(s_met, df_met))

    print("Phase 150 result reporting and claim boundaries successfully built.")


if __name__ == "__main__":
    main()
