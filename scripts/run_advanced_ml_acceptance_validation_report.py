# -*- coding: utf-8 -*-
"""Phase 145: Run Advanced ML Acceptance Validation Report Script.

Builds validation and safety boundary compliance reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_ml_acceptance.advanced_ml_acceptance_config import (
    get_default_advanced_ml_acceptance_profile,
)
from advanced_ml_acceptance.advanced_ml_acceptance_validation import (
    build_advanced_ml_acceptance_validation_report,
)
from advanced_ml_acceptance.advanced_ml_acceptance_safety_boundary import (
    build_advanced_ml_acceptance_safety_boundary,
)
from advanced_ml_acceptance.advanced_ml_acceptance_report_builder import (
    build_advanced_ml_acceptance_validation_markdown_report,
    build_advanced_ml_acceptance_safety_markdown_report,
)
from reports.report_builder import (
    build_advanced_ml_acceptance_validation_text_report,
    build_advanced_ml_acceptance_safety_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_advanced_ml_acceptance_profile()

    df_val, s_val = build_advanced_ml_acceptance_validation_report({}, profile)
    df_sft, s_sft = build_advanced_ml_acceptance_safety_boundary(profile)

    data_lake.save_advanced_ml_acceptance_validation_report(df_val, s_val)
    data_lake.save_advanced_ml_acceptance_safety_boundary(df_sft, s_sft)

    out_dir = Path("reports/output/advanced_ml_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_validation_markdown_report(s_val, df_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_validation_text_report(s_val, df_val))

    with open(out_dir / "safety_boundary.md", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_safety_markdown_report(s_sft, df_sft))
    with open(out_dir / "safety_boundary.txt", "w", encoding="utf-8") as f:
        f.write(build_advanced_ml_acceptance_safety_text_report(s_sft, df_sft))

    print("=" * 70)
    print("PHASE 145: ACCEPTANCE VALIDATION & SAFETY AUDIT")
    print("=" * 70)
    print(f"Validation Rules Passed : {s_val['passed_rules']}/{s_val['total_rules']}")
    print(f"Safety No-Go Rules      : {s_sft['no_go_count']}")
    print(f"Safety Safe-Go Rules    : {s_sft['safe_go_count']}")
    print(f"Validation Status       : {s_val['status']}")
    print(f"Safety Status           : {s_sft['status']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
