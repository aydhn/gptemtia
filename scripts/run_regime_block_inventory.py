"""Phase 135: Run Regime Block Inventory Script.

Builds module inventory, dependency reports, and persists to DataLake.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_inventory import (
    build_regime_block_inventory_report,
)
from advanced_regime_acceptance.regime_block_dependencies import (
    build_regime_block_dependency_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_block_inventory_markdown_report,
    build_regime_block_dependency_markdown_report,
)
from reports.report_builder import (
    build_regime_block_inventory_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_inv, s_inv = build_regime_block_inventory_report(profile)
    df_dep, s_dep = build_regime_block_dependency_report(profile)

    data_lake.save_regime_block_inventory_report(df_inv, s_inv)
    data_lake.save_regime_block_dependency_report(df_dep, s_dep)

    md_inv = build_regime_block_inventory_markdown_report(s_inv, df_inv)
    md_dep = build_regime_block_dependency_markdown_report(s_dep, df_dep)
    txt_inv = build_regime_block_inventory_text_report(s_inv, df_inv)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "inventory.md", "w", encoding="utf-8") as f:
        f.write(md_inv)
    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(md_dep)
    with open(out_dir / "inventory.txt", "w", encoding="utf-8") as f:
        f.write(txt_inv)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK INVENTORY & DEPENDENCY REPORT")
    print("=" * 70)
    print(f"Total Modules       : {s_inv['total_modules']}")
    print(f"Phase Range         : {s_inv['phase_range']}")
    print(f"Expected Scripts    : {s_inv['total_expected_scripts']}")
    print(f"Expected Tests      : {s_inv['total_expected_tests']}")
    print(f"Dependency Steps    : {s_dep['total_dependency_steps']}")
    print(f"All Satisfied       : {s_dep['all_satisfied']}")
    print(f"Flow                : {s_dep['flow']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
