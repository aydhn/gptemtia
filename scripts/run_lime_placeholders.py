# -*- coding: utf-8 -*-
"""Phase 143: Run LIME Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.lime_placeholders import build_lime_placeholder_registry
from advanced_explainability_attribution.lime_execution_disabled import verify_lime_execution_disabled
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_lime, sum_lime = build_lime_placeholder_registry()
    data_lake.save_lime_placeholders(df_lime, sum_lime)

    df_dis, sum_dis = verify_lime_execution_disabled()

    print("=" * 70)
    print("PHASE 143: LIME PLACEHOLDERS & DISABLED EXECUTION REPORT")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total LIME Placeholders: {sum_lime['total_lime_placeholders']}")
    print(f"All Placeholder Only: {sum_lime['all_placeholder_only']}")
    print(f"All LIME Executed False: {sum_lime['all_lime_executed_false']}")
    print(f"All Disabled Enforced: {sum_dis['all_disabled']}")
    print(f"Policy Enforced: {sum_dis['all_policy_enforced']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
