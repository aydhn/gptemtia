"""Phase 125: Run Feature Factor Acceptance Validation Report Script.

Validates registries, gates, manifests, and ensures absence of forbidden claims.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_pipeline import (
    FeatureFactorAcceptancePipeline,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_validation_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()
    pipeline = FeatureFactorAcceptancePipeline(data_lake=data_lake, profile=profile)

    tables, summaries = pipeline.build_health_validation_status(save=True)
    df_val = tables["validation"]
    s_val = summaries["validation"]

    md_val = build_validation_markdown_report(s_val, df_val)
    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(md_val)

    print("=" * 70)
    print("PHASE 125: VALIDATION & SAFETY AUDIT")
    print("=" * 70)
    print(f"Validation Status    : {s_val['validation_status']}")
    print(f"Total Rules Verified : {s_val['total_rules']}")
    print(f"Passed Rules         : {s_val['passed_rules']}")
    print(f"Forbidden Claims     : {s_val['forbidden_claims_detected']}")
    print(f"Non-Signal           : {s_val['non_signal']}")
    print(f"Official Approval    : {s_val['official_approval']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
