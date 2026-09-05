"""Run script: Health Check for Phase 131 Cross-Asset Regime Context Expansion."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)


def main():
    print("Executing Phase 131 Subsystem Health Check...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_health_validation_safety_handoff(save=True)

    s_hlth = summaries["health"]
    print(f"Overall Health: {s_hlth['overall_status']}")
    print(f"Total Checks: {s_hlth['total_checks']}")
    print(f"Healthy Checks: {s_hlth['healthy_checks']}")
    print(f"Degraded Checks: {s_hlth['degraded_checks']}")

    if not s_hlth["all_healthy"]:
        print("WARNING: Some subsystems are degraded.")
        return 1

    print("\nSUCCESS: All Phase 131 Subsystems verified HEALTHY.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
