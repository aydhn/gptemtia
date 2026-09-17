# -*- coding: utf-8 -*-
"""Phase 143: Run Counterfactual Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.counterfactual_placeholders import (
    build_counterfactual_placeholder_registry,
)
from advanced_explainability_attribution.counterfactual_execution_disabled import (
    verify_counterfactual_execution_disabled,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_cf, sum_cf = build_counterfactual_placeholder_registry()
    data_lake.save_counterfactual_placeholders(df_cf, sum_cf)

    df_dis, sum_dis = verify_counterfactual_execution_disabled()

    print("=" * 70)
    print("PHASE 143: COUNTERFACTUAL PLACEHOLDERS & SAFEGUARDS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Counterfactual Placeholders: {sum_cf['total_counterfactual_placeholders']}")
    print(f"All Placeholder Only: {sum_cf['all_placeholder_only']}")
    print(f"All Counterfactual Generated False: {sum_cf['all_counterfactual_generated_false']}")
    print(f"All Disabled Enforced: {sum_dis['all_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
