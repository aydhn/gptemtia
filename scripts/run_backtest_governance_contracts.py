# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Contracts Script.

Builds and persists Phase 150 backtest governance contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_contracts import (
    build_backtest_governance_contract_registry,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_governance_contract_markdown_report,
)
from reports.report_builder import (
    build_backtest_governance_contract_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_cntr, s_cntr = build_backtest_governance_contract_registry(profile)

    data_lake.save_backtest_governance_contracts(df_cntr, s_cntr)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "governance_contracts.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_contract_markdown_report(s_cntr, df_cntr))
    with open(out_dir / "governance_contracts.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_contract_text_report(s_cntr, df_cntr))

    print("Phase 150 backtest governance contracts successfully built.")


if __name__ == "__main__":
    main()
