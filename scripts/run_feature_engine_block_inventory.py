"""Phase 125: Run Feature Engine Block Inventory and Dependencies Script.

Builds block inventory across Phase 116-125 and maps dependency graphs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_inventory import (
    build_feature_engine_block_inventory_report,
)
from advanced_feature_factor_acceptance.feature_engine_block_dependencies import (
    build_feature_engine_block_dependency_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_feature_engine_inventory_markdown_report,
    build_feature_engine_dependency_markdown_report,
)
from reports.report_builder import build_feature_engine_inventory_text_report


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()

    df_inv, s_inv = build_feature_engine_block_inventory_report(profile)
    df_dep, s_dep = build_feature_engine_block_dependency_report(profile)

    data_lake.save_feature_engine_block_inventory_report(df_inv, s_inv)
    data_lake.save_feature_engine_block_dependency_report(df_dep, s_dep)

    md_inv = build_feature_engine_inventory_markdown_report(s_inv, df_inv)
    md_dep = build_feature_engine_dependency_markdown_report(s_dep, df_dep)
    txt_inv = build_feature_engine_inventory_text_report(s_inv, df_inv)

    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "inventory.md", "w", encoding="utf-8") as f:
        f.write(md_inv)
    with open(out_dir / "dependencies.md", "w", encoding="utf-8") as f:
        f.write(md_dep)
    with open(out_dir / "inventory.txt", "w", encoding="utf-8") as f:
        f.write(txt_inv)

    print("=" * 70)
    print("PHASE 125: FEATURE ENGINE BLOCK INVENTORY & DEPENDENCIES")
    print("=" * 70)
    print(f"Total Modules  : {s_inv['total_modules']}")
    print(f"Phase Range    : {s_inv['phase_range']}")
    print(f"All Passed     : {s_inv['all_passed']}")
    print(f"Total Scripts  : {s_inv['total_expected_scripts']}")
    print(f"Total Tests    : {s_inv['total_expected_tests']}")
    print(f"Total Edges    : {s_dep['total_dependencies']}")
    print(f"All Satisfied  : {s_dep['all_satisfied']}")
    print(f"Non-Signal     : {s_inv['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
