"""Run script: Health Check for Phase 133 Regime Validation Acceptance."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_acceptance_profile_markdown_report,
)


def main():
    print("Executing Phase 133 Regime Validation Acceptance Health Check...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_hvs, s_hvs = pipeline.build_health_validation_safety_handoff(save=True)

    print(f"Health Status: {s_hvs['health']['health_status']}")
    print(f"Total Subsystems: {s_hvs['health']['total_subsystems']}")
    print(f"Healthy Subsystems: {s_hvs['health']['healthy_subsystems']}")
    print(f"All Healthy: {s_hvs['health']['all_healthy']}")

    if not s_hvs["health"]["all_healthy"]:
        print("\nWARNING: Some subsystems reported degraded status.")
        return 1

    print("\nSUCCESS: Phase 133 Regime Validation Acceptance subsystem is HEALTHY.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
