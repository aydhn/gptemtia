# -*- coding: utf-8 -*-
"""Phase 150: Run Backtest Governance Validation Report Script.

Validates contract conformance, bias controls, and safety boundaries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_backtest_governance.backtest_governance_config import (
    get_default_backtest_governance_profile,
)
from advanced_backtest_governance.backtest_governance_profile_registry import (
    build_backtest_governance_profile_registry,
)
from advanced_backtest_governance.backtest_governance_contracts import (
    build_backtest_governance_contract_registry,
)
from advanced_backtest_governance.backtest_bias_control_contracts import (
    build_backtest_bias_control_contract_registry,
)
from advanced_backtest_governance.backtest_governance_manifest import (
    build_backtest_governance_manifest,
)
from advanced_backtest_governance.backtest_governance_validation import (
    build_backtest_governance_validation_report,
)
from advanced_backtest_governance.backtest_governance_report_builder import (
    build_backtest_governance_validation_markdown_report,
)
from reports.report_builder import (
    build_backtest_governance_validation_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_backtest_governance_profile()

    df_prof, _ = build_backtest_governance_profile_registry(profile)
    df_cntr, _ = build_backtest_governance_contract_registry(profile)
    df_bias, _ = build_backtest_bias_control_contract_registry(profile)
    df_man, _ = build_backtest_governance_manifest(profile)

    df_val, s_val = build_backtest_governance_validation_report(
        profile,
        validation_data={
            "profile_registry": df_prof,
            "contracts": df_cntr,
            "bias_controls": df_bias,
            "manifest": df_man,
        },
    )

    data_lake.save_backtest_governance_validation_report(df_val, s_val)

    out_dir = Path("reports/output/advanced_backtest_governance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation_report.md", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_validation_markdown_report(s_val))
    with open(out_dir / "validation_report.txt", "w", encoding="utf-8") as f:
        f.write(build_backtest_governance_validation_text_report(s_val, df_val))

    print("=" * 70)
    print("PHASE 150: BACKTEST GOVERNANCE VALIDATION REPORT")
    print("=" * 70)
    print(df_val.to_string(index=False))
    print("-" * 70)
    print(f"Validation Status: {s_val.get('validation_status')}")
    print(f"All Passed       : {s_val.get('all_validations_passed')}")
    print("=" * 70)


if __name__ == "__main__":
    main()
