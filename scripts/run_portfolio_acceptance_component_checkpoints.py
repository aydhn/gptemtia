# -*- coding: utf-8 -*-
"""Phase 157: Run Portfolio Acceptance Component Checkpoints Script.

Builds and persists component registry and component checkpoints for the portfolio block.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_portfolio_acceptance.portfolio_acceptance_config import (
    get_default_portfolio_acceptance_profile,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_registry import (
    build_portfolio_acceptance_component_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_component_checkpoints import (
    build_portfolio_acceptance_component_checkpoint_registry,
)
from advanced_portfolio_acceptance.portfolio_acceptance_report_builder import (
    build_portfolio_acceptance_component_markdown_report,
)
from reports.report_builder import (
    build_portfolio_acceptance_component_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_portfolio_acceptance_profile()

    df_cmp, s_cmp = build_portfolio_acceptance_component_registry(profile)
    df_chk, s_chk = build_portfolio_acceptance_component_checkpoint_registry(profile)

    data_lake.save_portfolio_acceptance_component_registry(df_cmp, s_cmp)
    data_lake.save_portfolio_acceptance_component_checkpoint_registry(df_chk, s_chk)

    out_dir = Path("reports/output/advanced_portfolio_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_portfolio_acceptance_component_markdown_report(s_cmp, df_cmp)
    txt_report = build_portfolio_acceptance_component_text_report(s_cmp, df_cmp)

    with open(out_dir / "components.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "components.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 157: PORTFOLIO ACCEPTANCE COMPONENTS & CHECKPOINTS")
    print("=" * 70)
    print(f"Total Components   : {s_cmp['total_components']}")
    print(f"Phases Covered     : {s_cmp['phases_covered']}")
    print(f"Total Checkpoints  : {s_chk['total_checkpoints']}")
    print(f"Contract Only      : {s_cmp['all_contract_only']}")
    print(f"Non-Production     : {s_cmp['all_non_production']}")
    print(f"Production Ready   : False")
    print(f"Broker Ready       : False")
    print("=" * 70)


if __name__ == "__main__":
    main()
