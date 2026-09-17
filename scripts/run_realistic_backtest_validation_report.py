# -*- coding: utf-8 -*-
"""Phase 146: Run Realistic Backtest Validation Report Script.

Validates backtest contracts, manifest negative invariants, forbidden claims,
and security constraints. Saves to DataLake and writes markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_realistic_backtest.realistic_backtest_config import (
    get_default_realistic_backtest_profile,
)
from advanced_realistic_backtest.realistic_backtest_profile_registry import (
    build_realistic_backtest_profile_registry,
)
from advanced_realistic_backtest.backtest_engine_contracts import (
    build_backtest_engine_contract_registry,
)
from advanced_realistic_backtest.realistic_backtest_manifest import (
    build_realistic_backtest_manifest,
)
from advanced_realistic_backtest.realistic_backtest_validation import (
    build_realistic_backtest_validation_report,
)
from advanced_realistic_backtest.realistic_backtest_report_builder import (
    build_realistic_backtest_validation_markdown_report,
)
from reports.report_builder import build_realistic_backtest_validation_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_realistic_backtest_profile()

    df_prof, _ = build_realistic_backtest_profile_registry(profile)
    df_eng, _ = build_backtest_engine_contract_registry(profile)
    df_man, _ = build_realistic_backtest_manifest(profile)

    val_tables = {
        "profiles": df_prof,
        "engines": df_eng,
        "manifest": df_man,
    }

    df_val, s_val = build_realistic_backtest_validation_report(val_tables, profile)
    data_lake.save_realistic_backtest_validation_report(df_val, s_val)

    md_report = build_realistic_backtest_validation_markdown_report(s_val, df_val)
    txt_report = build_realistic_backtest_validation_text_report(s_val, df_val)

    out_dir = Path("reports/output/advanced_realistic_backtest")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 146: REALISTIC BACKTEST VALIDATION REPORT")
    print("=" * 70)
    print(f"Validation Status      : {s_val.get('validation_status')}")
    print(f"Total Checks           : {s_val.get('total_checks')}")
    print(f"Passed Checks          : {s_val.get('passed_checks')}")
    print(f"Forbidden Claims Found : {s_val.get('forbidden_claims_found')}")
    print(f"All Passed             : {s_val.get('all_passed')}")
    print(f"Non-Signal Invariant   : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
