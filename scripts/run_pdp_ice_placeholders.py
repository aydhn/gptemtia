# -*- coding: utf-8 -*-
"""Phase 143: Run PDP and ICE Placeholders Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_explainability_attribution.partial_dependence_placeholders import (
    build_partial_dependence_placeholder_registry,
)
from advanced_explainability_attribution.ice_placeholders import (
    build_ice_placeholder_registry,
)
from advanced_explainability_attribution.pdp_ice_execution_disabled import (
    verify_pdp_ice_execution_disabled,
)
from reports.report_builder import ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER


def main():
    data_lake = DataLake()
    df_pdp, sum_pdp = build_partial_dependence_placeholder_registry()
    df_ice, sum_ice = build_ice_placeholder_registry()
    data_lake.save_pdp_ice_placeholders(df_pdp, sum_pdp)

    df_dis, sum_dis = verify_pdp_ice_execution_disabled()

    print("=" * 70)
    print("PHASE 143: PDP & ICE PLACEHOLDERS AND DISABLED SAFEGUARDS")
    print("=" * 70)
    print(ADVANCED_EXPLAINABILITY_ATTRIBUTION_TEXT_REPORT_DISCLAIMER)
    print("-" * 70)
    print(f"Total PDP Placeholders: {sum_pdp['total_pdp_placeholders']}")
    print(f"Total ICE Placeholders: {sum_ice['total_ice_placeholders']}")
    print(f"All Placeholder Only: {sum_pdp['all_placeholder_only'] and sum_ice['all_placeholder_only']}")
    print(f"All PDP/ICE Disabled: {sum_dis['all_disabled']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
