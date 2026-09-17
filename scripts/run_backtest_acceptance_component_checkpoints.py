# -*- coding: utf-8 -*-
"""Phase 152: Run Backtest Acceptance Component Checkpoints Script.

Builds component and checkpoint registries and saves them to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_acceptance.backtest_acceptance_config import (
    get_default_backtest_acceptance_profile,
)
from advanced_backtest_acceptance.backtest_acceptance_component_registry import (
    build_backtest_acceptance_component_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_component_checkpoints import (
    build_backtest_acceptance_component_checkpoint_registry,
)
from advanced_backtest_acceptance.backtest_acceptance_report_builder import (
    build_backtest_acceptance_component_markdown_report,
)
from reports.report_builder import build_backtest_acceptance_component_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_acceptance_profile()

    df_cmp, s_cmp = build_backtest_acceptance_component_registry(profile)
    df_chk, s_chk = build_backtest_acceptance_component_checkpoint_registry(profile)

    data_lake.save_backtest_acceptance_component_registry(df_cmp, s_cmp)
    data_lake.save_backtest_acceptance_component_checkpoint_registry(df_chk, s_chk)

    md_report = build_backtest_acceptance_component_markdown_report(s_cmp, df_cmp)
    txt_report = build_backtest_acceptance_component_text_report(s_cmp, df_cmp)

    out_dir = Path("reports/output/advanced_backtest_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "components.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "components.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 152: BACKTEST ACCEPTANCE COMPONENTS & CHECKPOINTS")
    print("=" * 70)
    print(f"Total Components  : {s_cmp['total_components']}")
    print(f"Total Checkpoints : {s_chk['total_checkpoints']}")
    print(f"All Contract Only : {s_cmp['all_contract_only']}")
    print(f"All Non-Prod      : {s_cmp['all_non_production']}")
    print(f"Manual Review     : {s_chk['manual_review_required']}")
    print(f"Non-Signal        : {s_cmp['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
