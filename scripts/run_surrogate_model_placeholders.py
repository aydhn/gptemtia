# -*- coding: utf-8 -*-
"""Phase 143: Run Surrogate Model Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.surrogate_model_placeholders import (
    build_surrogate_model_placeholder_registry,
)
from advanced_explainability_attribution.surrogate_model_execution_disabled import (
    verify_surrogate_model_execution_disabled,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_surr, sum_surr = build_surrogate_model_placeholder_registry()
    data_lake.save_surrogate_model_placeholders(df_surr, sum_surr)

    df_dis, sum_dis = verify_surrogate_model_execution_disabled()

    print("=" * 70)
    print("PHASE 143: SURROGATE MODEL PLACEHOLDERS & SAFEGUARDS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Surrogate Placeholders: {sum_surr['total_surrogate_model_placeholders']}")
    print(f"All Placeholder Only: {sum_surr['all_placeholder_only']}")
    print(f"All Surrogate Executed False: {sum_surr['all_surrogate_executed_false']}")
    print(f"All Disabled Enforced: {sum_dis['all_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
