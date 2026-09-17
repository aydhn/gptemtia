# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Package Contracts Script.

Builds and persists package contracts and system component registry.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_package_contracts import (
    build_final_delivery_package_contract_registry,
)
from advanced_final_delivery.final_delivery_component_registry import (
    build_final_delivery_component_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_package_markdown_report,
    build_final_delivery_component_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_package_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_pc, s_pc = build_final_delivery_package_contract_registry(profile)
    df_cmp, s_cmp = build_final_delivery_component_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_package_contract_registry(df_pc, s_pc)
        data_lake.save_final_delivery_component_registry(df_cmp, s_cmp)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_package = build_final_delivery_package_markdown_report(s_pc, df_pc)
    txt_package = build_final_delivery_package_text_report(s_pc, df_pc)
    md_cmp = build_final_delivery_component_markdown_report(s_cmp, df_cmp)

    if "--no-save" not in sys.argv:
        with open(out_dir / "package_contracts.md", "w", encoding="utf-8") as f:
            f.write(md_package)
        with open(out_dir / "package_contracts.txt", "w", encoding="utf-8") as f:
            f.write(txt_package)
        with open(out_dir / "components.md", "w", encoding="utf-8") as f:
            f.write(md_cmp)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY PACKAGE CONTRACTS INITIALIZED")
    print("=" * 70)
    print(f"Contracts: {s_pc['contract_count']} | Components: {s_cmp['component_count']}")
    print(f"Status: {s_pc['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
