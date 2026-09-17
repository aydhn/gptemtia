# -*- coding: utf-8 -*-
"""Phase 143: Run Feature Attribution Contracts Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.feature_attribution_contracts import (
    build_feature_attribution_contracts,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df, summary = build_feature_attribution_contracts()
    data_lake.save_feature_attribution_contracts(df, summary)

    print("=" * 70)
    print("PHASE 143: FEATURE ATTRIBUTION CONTRACTS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Attribution Contracts: {summary['total_attribution_contracts']}")
    print(f"All Zero Calculation: {summary['all_zero_calculation']}")
    print(f"All Zero SHAP: {summary['all_zero_shap']}")
    print(f"All Zero LIME: {summary['all_zero_lime']}")
    print(f"All Non-Signal: {summary['all_non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
