# -*- coding: utf-8 -*-
"""Phase 143: Run Attribution Drift Linkage Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.attribution_drift_linkage import (
    build_attribution_drift_linkage_registry,
)
from advanced_explainability_attribution.drift_explainability_linkage import (
    build_drift_explainability_linkage_registry,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_link, sum_link = build_attribution_drift_linkage_registry()
    df_dlink, sum_dlink = build_drift_explainability_linkage_registry()
    data_lake.save_attribution_drift_linkage(df_link, sum_link)

    print("=" * 70)
    print("PHASE 143: ATTRIBUTION DRIFT LINKAGE CONTRACTS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total Attribution Drift Linkages: {sum_link['total_drift_linkages']}")
    print(f"Total Drift Explainability Linkages: {sum_dlink['total_drift_linkages']}")
    print(f"All Linkage Contracts: {sum_link['all_linkage_contract']}")
    print(f"All Drift Calculations Disabled: {sum_link['all_drift_calculated_false']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
