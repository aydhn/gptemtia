# -*- coding: utf-8 -*-
"""Phase 143: Run SHAP Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.shap_placeholders import build_shap_placeholder_registry
from advanced_explainability_attribution.shap_execution_disabled import verify_shap_execution_disabled
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_shap, sum_shap = build_shap_placeholder_registry()
    data_lake.save_shap_placeholders(df_shap, sum_shap)

    df_dis, sum_dis = verify_shap_execution_disabled()

    print("=" * 70)
    print("PHASE 143: SHAP PLACEHOLDERS & DISABLED EXECUTION REPORT")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total SHAP Placeholders: {sum_shap['total_shap_placeholders']}")
    print(f"All Placeholder Only: {sum_shap['all_placeholder_only']}")
    print(f"All SHAP Executed False: {sum_shap['all_shap_executed_false']}")
    print(f"All Disabled Enforced: {sum_dis['all_disabled']}")
    print(f"Policy Enforced: {sum_dis['all_policy_enforced']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
