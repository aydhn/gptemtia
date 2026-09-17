# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Execution and Cost Models Script.

Builds order simulation contracts, fill models, execution price models,
commission models, fee models, spread models, slippage models, transaction cost models,
and execution realism placeholders (market impact, latency, liquidity, partial fill,
rejected order, order book depth).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.order_simulation_contracts import (
    build_order_simulation_contract_registry,
)
from advanced_realistic_backtest.fill_model_contracts import (
    build_fill_model_contract_registry,
)
from advanced_realistic_backtest.execution_price_model_contracts import (
    build_execution_price_model_contract_registry,
)
from advanced_realistic_backtest.commission_model_contracts import (
    build_commission_model_contract_registry,
)
from advanced_realistic_backtest.fee_model_contracts import (
    build_fee_model_contract_registry,
)
from advanced_realistic_backtest.spread_model_contracts import (
    build_spread_model_contract_registry,
)
from advanced_realistic_backtest.slippage_model_contracts import (
    build_slippage_model_contract_registry,
)
from advanced_realistic_backtest.transaction_cost_models import (
    build_transaction_cost_model_registry,
)
from advanced_realistic_backtest.transaction_cost_components import (
    build_transaction_cost_component_registry,
)
from advanced_realistic_backtest.market_impact_placeholders import (
    build_market_impact_placeholder_registry,
)
from advanced_realistic_backtest.latency_placeholders import (
    build_latency_placeholder_registry,
)
from advanced_realistic_backtest.liquidity_constraint_placeholders import (
    build_liquidity_constraint_placeholder_registry,
)
from advanced_realistic_backtest.partial_fill_placeholders import (
    build_partial_fill_placeholder_registry,
)
from advanced_realistic_backtest.rejected_order_placeholders import (
    build_rejected_order_placeholder_registry,
)
from advanced_realistic_backtest.order_book_depth_placeholders import (
    build_order_book_depth_placeholder_registry,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_order_simulation_contract_markdown_report,
    build_transaction_cost_model_markdown_report,
    build_slippage_model_markdown_report,
    build_execution_realism_markdown_report,
)
from reports.report_builder import (
    build_order_simulation_contract_text_report,
    build_transaction_cost_model_text_report,
    build_slippage_model_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_ord, s_ord = build_order_simulation_contract_registry(profile)
    df_fill, s_fill = build_fill_model_contract_registry(profile)
    df_prc, s_prc = build_execution_price_model_contract_registry(profile)
    df_comm, s_comm = build_commission_model_contract_registry(profile)
    df_fee, s_fee = build_fee_model_contract_registry(profile)
    df_sprd, s_sprd = build_spread_model_contract_registry(profile)
    df_slip, s_slip = build_slippage_model_contract_registry(profile)
    df_cst, s_cst = build_transaction_cost_model_registry(profile)
    df_cmp, s_cmp = build_transaction_cost_component_registry(profile)

    df_mi, s_mi = build_market_impact_placeholder_registry(profile)
    df_lat, s_lat = build_latency_placeholder_registry(profile)
    df_liq, s_liq = build_liquidity_constraint_placeholder_registry(profile)
    df_pf, s_pf = build_partial_fill_placeholder_registry(profile)
    df_rej, s_rej = build_rejected_order_placeholder_registry(profile)
    df_ob, s_ob = build_order_book_depth_placeholder_registry(profile)

    data_lake.save_order_simulation_contract_registry(df_ord, s_ord)
    data_lake.save_fill_model_contract_registry(df_fill, s_fill)
    data_lake.save_execution_price_model_contract_registry(df_prc, s_prc)
    data_lake.save_commission_model_contract_registry(df_comm, s_comm)
    data_lake.save_fee_model_contract_registry(df_fee, s_fee)
    data_lake.save_spread_model_contract_registry(df_sprd, s_sprd)
    data_lake.save_slippage_model_contract_registry(df_slip, s_slip)
    data_lake.save_transaction_cost_model_registry(df_cst, s_cst)
    data_lake.save_transaction_cost_component_registry(df_cmp, s_cmp)

    data_lake.save_market_impact_placeholders(df_mi, s_mi)
    data_lake.save_latency_placeholders(df_lat, s_lat)
    data_lake.save_liquidity_constraint_placeholders(df_liq, s_liq)
    data_lake.save_partial_fill_placeholders(df_pf, s_pf)
    data_lake.save_rejected_order_placeholders(df_rej, s_rej)
    data_lake.save_order_book_depth_placeholders(df_ob, s_ob)

    md_ord = build_order_simulation_contract_markdown_report(s_ord, df_ord)
    txt_ord = build_order_simulation_contract_text_report(s_ord, df_ord)
    md_cst = build_transaction_cost_model_markdown_report(s_cst, df_cst)
    txt_cst = build_transaction_cost_model_text_report(s_cst, df_cst)
    md_slip = build_slippage_model_markdown_report(s_slip, df_slip)
    txt_slip = build_slippage_model_text_report(s_slip, df_slip)
    md_realism = build_execution_realism_markdown_report(s_mi, df_mi)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "order_simulation.md", "w", encoding="utf-8") as f:
        f.write(md_ord)
    with open(out_dir / "order_simulation.txt", "w", encoding="utf-8") as f:
        f.write(txt_ord)
    with open(out_dir / "transaction_costs.md", "w", encoding="utf-8") as f:
        f.write(md_cst)
    with open(out_dir / "transaction_costs.txt", "w", encoding="utf-8") as f:
        f.write(txt_cst)
    with open(out_dir / "slippage_models.md", "w", encoding="utf-8") as f:
        f.write(md_slip)
    with open(out_dir / "slippage_models.txt", "w", encoding="utf-8") as f:
        f.write(txt_slip)
    with open(out_dir / "execution_realism.md", "w", encoding="utf-8") as f:
        f.write(md_realism)

    print("=" * 70)
    print("PHASE 146: EXECUTION AND COST MODELS")
    print("=" * 70)
    print(f"Order Types Simulated  : {s_ord.get('total_order_types')}")
    print(f"Fill Models            : {s_fill.get('total_fill_models')}")
    print(f"Price Models           : {s_prc.get('total_price_models')}")
    print(f"Commission Models      : {s_comm.get('total_commission_models')}")
    print(f"Fee Models             : {s_fee.get('total_fee_models')}")
    print(f"Spread Models          : {s_sprd.get('total_spread_models')}")
    print(f"Slippage Models        : {s_slip.get('total_slippage_models')}")
    print(f"Cost Formulas          : {s_cst.get('total_cost_models')}")
    print(f"Broker Order Sent      : {s_ord.get('broker_orders_sent')}")
    print(f"Live Order Sent        : {s_ord.get('live_orders_sent')}")
    print(f"Non-Signal             : {s_ord.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
