# -*- coding: utf-8 -*-
"""Phase 146: Run Backtest Engine Contracts Script.

Builds and verifies backtest engine contracts (event-driven, vectorized, portfolio,
multi-asset, regime-aware, cost-aware), data contracts, feature input contracts,
signal input contracts, and output contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.backtest_engine_contracts import (
    build_backtest_engine_contract_registry,
)
from advanced_realistic_backtest.event_driven_backtest_contracts import (
    build_event_driven_backtest_contract_registry,
)
from advanced_realistic_backtest.vectorized_backtest_contracts import (
    build_vectorized_backtest_contract_registry,
)
from advanced_realistic_backtest.portfolio_backtest_contracts import (
    build_portfolio_backtest_contract_registry,
)
from advanced_realistic_backtest.backtest_data_contracts import (
    build_backtest_data_contract_registry,
)
from advanced_realistic_backtest.backtest_feature_input_contracts import (
    build_backtest_feature_input_contract_registry,
)
from advanced_realistic_backtest.backtest_signal_input_contracts import (
    build_backtest_signal_input_contract_registry,
)
from advanced_realistic_backtest.backtest_output_contracts import (
    build_backtest_output_contract_registry,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_backtest_engine_contract_markdown_report,
)
from reports.report_builder import build_backtest_engine_contract_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_eng, s_eng = build_backtest_engine_contract_registry(profile)
    df_ev, s_ev = build_event_driven_backtest_contract_registry(profile)
    df_vec, s_vec = build_vectorized_backtest_contract_registry(profile)
    df_port, s_port = build_portfolio_backtest_contract_registry(profile)
    df_dt, s_dt = build_backtest_data_contract_registry(profile)
    df_feat, s_feat = build_backtest_feature_input_contract_registry(profile)
    df_sig, s_sig = build_backtest_signal_input_contract_registry(profile)
    df_out, s_out = build_backtest_output_contract_registry(profile)

    data_lake.save_backtest_engine_contract_registry(df_eng, s_eng)
    data_lake.save_event_driven_backtest_contract_registry(df_ev, s_ev)
    data_lake.save_vectorized_backtest_contract_registry(df_vec, s_vec)
    data_lake.save_portfolio_backtest_contract_registry(df_port, s_port)
    data_lake.save_backtest_data_contracts(df_dt, s_dt)
    data_lake.save_backtest_feature_input_contracts(df_feat, s_feat)
    data_lake.save_backtest_signal_input_contracts(df_sig, s_sig)
    data_lake.save_backtest_output_contracts(df_out, s_out)

    md_report = build_backtest_engine_contract_markdown_report(s_eng, df_eng)
    txt_report = build_backtest_engine_contract_text_report(s_eng, df_eng)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "engine_contracts.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "engine_contracts.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 146: BACKTEST ENGINE CONTRACTS")
    print("=" * 70)
    print(f"Total Engine Contracts : {s_eng.get('total_contracts')}")
    print(f"Event Types Handled    : {s_ev.get('total_event_types')}")
    print(f"Vectorized Engines     : {s_vec.get('total_vectorized_engines')}")
    print(f"Portfolio Constraints  : {s_port.get('total_portfolio_constraints')}")
    print(f"Data Schema Fields     : {s_dt.get('total_data_contracts')}")
    print(f"Feature Inputs         : {s_feat.get('total_feature_contracts')}")
    print(f"Signal Interfaces      : {s_sig.get('total_signal_contracts')}")
    print(f"Output Fields          : {s_out.get('total_output_contracts')}")
    print(f"Execution Allowed      : {s_eng.get('all_execution_blocked') is False}")
    print(f"Non-Signal             : {s_eng.get('non_signal')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
