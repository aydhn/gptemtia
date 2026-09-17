# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Accounting and Lifecycle Script.

Builds PnL accounting contracts, cash/position ledgers, leverage/margin placeholders,
trade and position lifecycles, corporate actions, currency conversion, and metric placeholders.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.pnl_accounting_contracts import (
    build_pnl_accounting_contract_registry,
)
from advanced_realistic_backtest.cash_position_accounting_contracts import (
    build_cash_position_accounting_contract_registry,
)
from advanced_realistic_backtest.leverage_margin_placeholders import (
    build_leverage_margin_placeholder_registry,
)
from advanced_realistic_backtest.trade_lifecycle_contracts import (
    build_trade_lifecycle_contract_registry,
)
from advanced_realistic_backtest.position_lifecycle_contracts import (
    build_position_lifecycle_contract_registry,
)
from advanced_realistic_backtest.corporate_action_placeholders import (
    build_corporate_action_placeholder_registry,
)
from advanced_realistic_backtest.currency_conversion_placeholders import (
    build_currency_conversion_placeholder_registry,
)
from advanced_realistic_backtest.backtest_metric_placeholders import (
    build_backtest_metric_placeholder_registry,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_pnl, s_pnl = build_pnl_accounting_contract_registry(profile)
    df_cash, s_cash = build_cash_position_accounting_contract_registry(profile)
    df_lev, s_lev = build_leverage_margin_placeholder_registry(profile)
    df_trade, s_trade = build_trade_lifecycle_contract_registry(profile)
    df_pos, s_pos = build_position_lifecycle_contract_registry(profile)
    df_corp, s_corp = build_corporate_action_placeholder_registry(profile)
    df_fx, s_fx = build_currency_conversion_placeholder_registry(profile)
    df_met, s_met = build_backtest_metric_placeholder_registry(profile)

    data_lake.save_pnl_accounting_contracts(df_pnl, s_pnl)
    data_lake.save_cash_position_accounting_contracts(df_cash, s_cash)
    data_lake.save_leverage_margin_placeholders(df_lev, s_lev)
    data_lake.save_trade_lifecycle_contracts(df_trade, s_trade)
    data_lake.save_position_lifecycle_contracts(df_pos, s_pos)
    data_lake.save_corporate_action_placeholders(df_corp, s_corp)
    data_lake.save_currency_conversion_placeholders(df_fx, s_fx)
    data_lake.save_backtest_metric_placeholders(df_met, s_met)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "accounting_lifecycle.txt", "w", encoding="utf-8") as f:
        f.write("PHASE 146: ACCOUNTING & LIFECYCLE SUMMARY\n")
        f.write(f"PnL Standards: {s_pnl.get('total_pnl_standards', len(df_pnl))}\n")
        f.write(f"Cash/Position Ledgers: {s_cash.get('total_ledgers', len(df_cash))}\n")
        f.write(f"Trade States: {s_trade.get('total_trade_states', len(df_trade))}\n")
        f.write(f"Position States: {s_pos.get('total_position_states', len(df_pos))}\n")
        f.write(f"Metrics (Placeholders): {s_met.get('total_metric_placeholders', len(df_met))}\n")

    print("=" * 70)
    print("PHASE 146: ACCOUNTING AND LIFECYCLE")
    print("=" * 70)
    print(f"PnL Standards          : {len(df_pnl)}")
    print(f"Cash/Position Ledgers  : {len(df_cash)}")
    print(f"Margin Placeholders    : {len(df_lev)}")
    print(f"Trade States           : {len(df_trade)}")
    print(f"Position States        : {len(df_pos)}")
    print(f"Corporate Actions      : {len(df_corp)}")
    print(f"Currency Conversions   : {len(df_fx)}")
    print(f"Metric Placeholders    : {len(df_met)}")
    print(f"Local Only             : True")
    print(f"Non-Signal             : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
