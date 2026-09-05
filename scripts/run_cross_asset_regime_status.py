"""Run script: Status Overview for Phase 131 Cross-Asset Regime Context Expansion."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)


def main():
    print("=" * 70)
    print("PHASE 131 STATUS: CROSS-ASSET REGIME CONTEXT EXPANSION")
    print("=" * 70)

    pipeline = CrossAssetRegimePipeline()
    results = pipeline.run_all(save=True)

    summaries = results["summaries"]
    s_pipe = summaries.get("pipeline", {})
    s_hlth = summaries.get("health", {})
    s_val = summaries.get("validation", {})
    s_safe = summaries.get("safety", {})
    s_hnd = summaries.get("handoff", {})

    print(f"Current Phase:        {s_pipe.get('current_phase', 131)}")
    print(f"Next Phase:           {s_pipe.get('next_phase', 132)}")
    print(f"Target Final Phase:   {s_pipe.get('target_final_phase', 160)}")
    print(f"Non-Signal Policy:    {s_pipe.get('non_signal', True)}")
    print(f"Health Status:        {s_hlth.get('overall_status', 'UNKNOWN')}")
    print(f"Validation Status:    {s_val.get('validation_status', 'UNKNOWN')}")
    print(f"Safety Checks:        {s_safe.get('no_go_count', 0)} enforced")
    print(f"Handoff Ready:        {s_hnd.get('all_ready', False)}")
    print("=" * 70)
    print(f"Total Tables Produced: {len(results.get('dataframes', {}))}")
    for name, df in results.get("dataframes", {}).items():
        print(f"  - {name}: {len(df)} rows, {len(df.columns)} cols")
    print("=" * 70)

    all_ok = (
        s_hlth.get("all_healthy", False)
        and s_val.get("all_passed", False)
        and s_safe.get("all_no_go_enforced", False)
        and s_hnd.get("all_ready", False)
    )
    if not all_ok:
        print("PHASE 131 STATUS: ISSUES DETECTED")
        return 1

    print("PHASE 131 STATUS: ALL SUBSYSTEMS GREEN AND READY FOR PHASE 132.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
