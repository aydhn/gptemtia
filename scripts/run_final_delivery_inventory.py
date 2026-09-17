# -*- coding: utf-8 -*-
"""Phase 160: Run Final Delivery Inventory Script.

Builds and persists module, script, test, docs, report, DataLake, and FeatureStore inventories.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_delivery.final_delivery_config import (
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_module_inventory import (
    build_final_delivery_module_inventory_registry,
)
from advanced_final_delivery.final_delivery_script_inventory import (
    build_final_delivery_script_inventory_registry,
)
from advanced_final_delivery.final_delivery_test_inventory import (
    build_final_delivery_test_inventory_registry,
)
from advanced_final_delivery.final_delivery_docs_inventory import (
    build_final_delivery_docs_inventory_registry,
)
from advanced_final_delivery.final_delivery_report_inventory import (
    build_final_delivery_report_inventory_registry,
)
from advanced_final_delivery.final_delivery_data_lake_inventory import (
    build_final_delivery_data_lake_inventory_registry,
)
from advanced_final_delivery.final_delivery_feature_store_inventory import (
    build_final_delivery_feature_store_inventory_registry,
)
from advanced_final_delivery.final_delivery_report_builder import (
    build_final_delivery_inventory_markdown_report,
)
from reports.report_builder import (
    build_final_delivery_inventory_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_delivery_profile()

    df_mod, s_mod = build_final_delivery_module_inventory_registry(profile)
    df_scr, s_scr = build_final_delivery_script_inventory_registry(profile)
    df_tst, s_tst = build_final_delivery_test_inventory_registry(profile)
    df_doc, s_doc = build_final_delivery_docs_inventory_registry(profile)
    df_rep, s_rep = build_final_delivery_report_inventory_registry(profile)
    df_dl, s_dl = build_final_delivery_data_lake_inventory_registry(profile)
    df_fs, s_fs = build_final_delivery_feature_store_inventory_registry(profile)

    if "--no-save" not in sys.argv and settings.final_delivery_save_reports:
        data_lake.save_final_delivery_module_inventory_registry(df_mod, s_mod)
        data_lake.save_final_delivery_script_inventory_registry(df_scr, s_scr)
        data_lake.save_final_delivery_test_inventory_registry(df_tst, s_tst)
        data_lake.save_final_delivery_docs_inventory_registry(df_doc, s_doc)
        data_lake.save_final_delivery_report_inventory_registry(df_rep, s_rep)

    out_dir = Path("reports/output/advanced_final_delivery")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_inv = build_final_delivery_inventory_markdown_report(s_mod, df_mod)
    txt_inv = build_final_delivery_inventory_text_report(s_mod, df_mod)

    if "--no-save" not in sys.argv:
        with open(out_dir / "inventory.md", "w", encoding="utf-8") as f:
            f.write(md_inv)
        with open(out_dir / "inventory.txt", "w", encoding="utf-8") as f:
            f.write(txt_inv)

    print("=" * 70)
    print("PHASE 160: FINAL DELIVERY INVENTORIES INITIALIZED")
    print("=" * 70)
    print(f"Modules: {s_mod['module_package_count']} | Script Categories: {s_scr['script_category_count']}")
    print(f"Test Suites: {s_tst['test_suite_count']} | Docs: {s_doc['docs_count']}")
    print(f"Status: {s_mod['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
