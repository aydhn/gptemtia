# -*- coding: utf-8 -*-
"""Phase 143: Run Permutation Importance Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.permutation_importance_placeholders import (
    build_permutation_importance_placeholder_registry,
)
from advanced_explainability_attribution.permutation_importance_disabled import (
    verify_permutation_importance_disabled,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_perm, sum_perm = build_permutation_importance_placeholder_registry()
    data_lake.save_permutation_importance_placeholders(df_perm, sum_perm)

    df_dis, sum_dis = verify_permutation_importance_disabled()

    print("=" * 70)
    print("PHASE 143: PERMUTATION IMPORTANCE PLACEHOLDERS & SAFEGUARDS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Permutation Placeholders: {sum_perm['total_permutation_importance_placeholders']}")
    print(f"All Placeholder Only: {sum_perm['all_placeholder_only']}")
    print(f"All Permutation Executed False: {sum_perm['all_permutation_executed_false']}")
    print(f"All Disabled Enforced: {sum_dis['all_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
