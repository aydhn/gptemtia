# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Realism Governance Script.

Builds and persists transaction cost, slippage, fill model, liquidity, and timestamp
integrity realism registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.transaction_cost_realism_governance import (
    build_transaction_cost_realism_governance_registry,
)
from advanced_backtest_governance.slippage_realism_governance import (
    build_slippage_realism_governance_registry,
)
from advanced_backtest_governance.fill_model_realism_governance import (
    build_fill_model_realism_governance_registry,
)
from advanced_backtest_governance.liquidity_realism_governance import (
    build_liquidity_realism_governance_registry,
)
from advanced_backtest_governance.timestamp_integrity_governance import (
    build_timestamp_integrity_governance_registry,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_realism_governance_markdown_report,
)
from reports.report_builder import (
    build_backtest_realism_governance_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_cost, s_cost = build_transaction_cost_realism_governance_registry(profile)
    df_slip, s_slip = build_slippage_realism_governance_registry(profile)
    df_fill, s_fill = build_fill_model_realism_governance_registry(profile)
    df_liq, s_liq = build_liquidity_realism_governance_registry(profile)
    df_time, s_time = build_timestamp_integrity_governance_registry(profile)

    data_lake.save_transaction_cost_realism_governance(df_cost, s_cost)
    data_lake.save_slippage_realism_governance(df_slip, s_slip)
    data_lake.save_fill_model_realism_governance(df_fill, s_fill)
    data_lake.save_liquidity_realism_governance(df_liq, s_liq)
    data_lake.save_timestamp_integrity_governance(df_time, s_time)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "realism_governance.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_realism_governance_markdown_report(s_cost, df_cost))
    with open(out_dir / "realism_governance.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_realism_governance_text_report(s_cost, df_cost))

    print("Phase 150 execution realism governance registries successfully built.")


if __name__ == "__main__":
    main()
