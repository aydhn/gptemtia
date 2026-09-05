"""Phase 125: Run Feature Factor Acceptance Health Check Script.

Runs system health verification across all 10 feature engine packages and registries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_health import (
    build_feature_factor_acceptance_health_check,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_health_markdown_report,
)


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()
    root = Path(__file__).resolve().parent.parent

    df_hlth, s_hlth = build_feature_factor_acceptance_health_check(root, profile)
    data_lake.save_feature_factor_acceptance_health_check(df_hlth, s_hlth)

    md_hlth = build_health_markdown_report(s_hlth, df_hlth)
    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "health_check.md", "w", encoding="utf-8") as f:
        f.write(md_hlth)

    print("=" * 70)
    print("PHASE 125: HEALTH CHECK REPORT")
    print("=" * 70)
    print(f"Overall Health : {s_hlth['health_status']}")
    print(f"Total Checks   : {s_hlth['total_checks']}")
    print(f"Passed Checks  : {s_hlth['passed_checks']}")
    print(f"Failed Checks  : {s_hlth['failed_checks']}")
    print(f"Non-Signal     : {s_hlth['non_signal']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
