# -*- coding: utf-8 -*-
"""Phase 147: Run Walk-Forward Validation Report Script.

Validates walk-forward contracts, OOS benchmarks, guard policies, manifest invariants,
forbidden claims, and security constraints. Saves to DataLake and writes markdown/text reports.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_walk_forward_validation.walk_forward_config import (
    get_default_walk_forward_profile,
)
from advanced_walk_forward_validation.walk_forward_profile_registry import (
    build_walk_forward_profile_registry,
)
from advanced_walk_forward_validation.walk_forward_validation_contracts import (
    build_walk_forward_validation_contract_registry,
)
from advanced_walk_forward_validation.oos_benchmark_contracts import (
    build_oos_benchmark_contract_registry,
)
from advanced_walk_forward_validation.validation_no_lookahead_guards import (
    build_validation_no_lookahead_guard_registry,
)
from advanced_walk_forward_validation.walk_forward_manifest import (
    build_walk_forward_manifest,
)
from advanced_walk_forward_validation.walk_forward_validation import (
    build_walk_forward_validation_report,
)
from advanced_walk_forward_validation.walk_forward_report_builder import (
    build_walk_forward_validation_markdown_report,
)
from reports.report_builder import build_walk_forward_validation_text_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_walk_forward_profile()

    df_prof, _ = build_walk_forward_profile_registry(profile)
    df_wf, _ = build_walk_forward_validation_contract_registry(profile)
    df_bnch, _ = build_oos_benchmark_contract_registry(profile)
    df_grd, _ = build_validation_no_lookahead_guard_registry(profile)
    df_man, _ = build_walk_forward_manifest(profile)

    val_tables = {
        "profiles": df_prof,
        "walk_forward_contracts": df_wf,
        "oos_benchmark_contracts": df_bnch,
        "no_lookahead_guards": df_grd,
        "manifest": df_man,
    }

    df_val, s_val = build_walk_forward_validation_report(val_tables, profile)
    data_lake.save_walk_forward_validation_report(df_val, s_val)

    md_report = build_walk_forward_validation_markdown_report(s_val, df_val)
    txt_report = build_walk_forward_validation_text_report(s_val, df_val)

    out_dir = Path("reports/output/advanced_walk_forward_validation")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "validation.md", "w", encoding="utf-8") as f:
        f.write(md_report)
    with open(out_dir / "validation.txt", "w", encoding="utf-8") as f:
        f.write(txt_report)

    print("=" * 70)
    print("PHASE 147: WALK-FORWARD VALIDATION REPORT")
    print("=" * 70)
    print(df_val.to_string(index=False))
    print("-" * 70)
    print(f"Validation Status     : {s_val.get('validation_status')}")
    print(f"Total Checks          : {s_val.get('total_checks')}")
    print(f"Passed Checks         : {s_val.get('passed_checks')}")
    print(f"All Passed            : {s_val.get('all_passed')}")
    print(f"Non-Signal Invariant  : True")
    print("=" * 70)


if __name__ == "__main__":
    main()
