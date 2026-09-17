# -*- coding: utf-8 -*-
"""Phase 159: Run Final Inventory Reports Script.

Builds and persists inventories of scripts, tests, docs, reports, data lake,
feature store, system components, disabled execution, safety boundaries, and review gates.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_final_hardening.final_hardening_config import (
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_script_inventory import (
    build_final_script_inventory_registry,
)
from advanced_final_hardening.final_test_inventory import (
    build_final_test_inventory_registry,
)
from advanced_final_hardening.final_docs_inventory import (
    build_final_docs_inventory_registry,
)
from advanced_final_hardening.final_report_inventory import (
    build_final_report_inventory_registry,
)
from advanced_final_hardening.final_system_component_inventory import (
    build_final_system_component_inventory_registry,
)
from advanced_final_hardening.final_disabled_execution_inventory import (
    build_final_disabled_execution_inventory_registry,
)
from advanced_final_hardening.final_safety_boundary_inventory import (
    build_final_safety_boundary_inventory_registry,
)
from advanced_final_hardening.final_manual_review_gate_inventory import (
    build_final_manual_review_gate_inventory_registry,
)
from advanced_final_hardening.final_hardening_report_builder import (
    build_final_inventory_markdown_report,
)
from reports.report_builder import (
    build_final_inventory_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_final_hardening_profile()

    df_scr, s_scr = build_final_script_inventory_registry(profile)
    df_tst, s_tst = build_final_test_inventory_registry(profile)
    df_doc, s_doc = build_final_docs_inventory_registry(profile)
    df_rep, s_rep = build_final_report_inventory_registry(profile)
    df_cmp, s_cmp = build_final_system_component_inventory_registry(profile)
    df_dis, s_dis = build_final_disabled_execution_inventory_registry(profile)
    df_sb, s_sb = build_final_safety_boundary_inventory_registry(profile)
    df_mrg, s_mrg = build_final_manual_review_gate_inventory_registry(profile)

    data_lake.save_final_script_inventory_registry(df_scr, s_scr)
    data_lake.save_final_test_inventory_registry(df_tst, s_tst)
    data_lake.save_final_docs_inventory_registry(df_doc, s_doc)
    data_lake.save_final_report_inventory_registry(df_rep, s_rep)
    data_lake.save_final_system_component_inventory_registry(df_cmp, s_cmp)
    data_lake.save_final_disabled_execution_inventory_registry(df_dis, s_dis)
    data_lake.save_final_safety_boundary_inventory_registry(df_sb, s_sb)

    out_dir = Path("reports/output/advanced_final_hardening")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_report = build_final_inventory_markdown_report(s_cmp, df_cmp)
    txt_report = build_final_inventory_text_report(s_cmp, df_cmp)

    with open(out_dir / "inventories.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "inventories.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 159: FINAL INVENTORY REGISTRIES INITIALIZED")
    print("=" * 70)
    print(f"Scripts: {s_scr['script_count']} | Tests: {s_tst['test_count']} | Docs: {s_doc['docs_count']}")
    print(f"Components: {s_cmp['component_count']} | Disabled Actions: {s_dis['disabled_action_count']}")
    print(f"Safety Boundaries: {s_sb['boundary_count']} | Review Gates: {s_mrg['gate_count']}")
    print(f"Status: {s_cmp['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
