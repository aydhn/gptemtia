"""Run script: Validation Report for Phase 131 Cross-Asset Regime Context Expansion."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)


def main():
    print("Executing Phase 131 Cross-Asset Regime Validation Report...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_health_validation_safety_handoff(save=True)

    s_val = summaries["validation"]
    total = s_val.get("total_checks", 0)
    passed = s_val.get("passed_checks", 0)
    failed = s_val.get("failed_checks", 0)
    pass_rate = (passed / total) if total > 0 else 0.0

    print(f"Validation Status: {s_val.get('validation_status', 'UNKNOWN')}")
    print(f"Total Rules Checked: {total}")
    print(f"Passed Rules: {passed}")
    print(f"Failed Rules: {failed}")
    print(f"Pass Rate: {pass_rate:.2%}")

    if not s_val.get("all_passed", False):
        print("ERROR: Validation checks failed for Phase 131.")
        return 1

    print("\nSUCCESS: Phase 131 Cross-Asset Regime Validation Report PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
