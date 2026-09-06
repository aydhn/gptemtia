"""Run script: Validation and Safety Boundary Report for Phase 133."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_acceptance_validation_markdown_report,
    build_regime_validation_acceptance_safety_markdown_report,
)
from reports.report_builder import (
    build_regime_validation_acceptance_safety_text_report,
)


def main():
    print("Executing Phase 133 Validation and Safety Boundary Report...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_hvs, s_hvs = pipeline.build_health_validation_safety_handoff(save=True)

    print(f"Validation Status: {s_hvs['validation']['status']}")
    print(f"Validation Checks: {s_hvs['validation']['passed_checks']}/{s_hvs['validation']['total_checks']}")
    print(f"Safety Status: {s_hvs['safety']['safety_status']}")
    print(f"NO-GO Boundaries Active: {s_hvs['safety']['no_go_count']}")
    print(f"SAFE-GO Principles Active: {s_hvs['safety']['safe_go_count']}")

    txt_safe = build_regime_validation_acceptance_safety_text_report(s_hvs["safety"])
    md_val = build_regime_validation_acceptance_validation_markdown_report(s_hvs["validation"], t_hvs["validation"])
    md_safe = build_regime_validation_acceptance_safety_markdown_report(s_hvs["safety"], t_hvs["safety"])

    print("\n--- Safety Boundary Summary ---")
    print(txt_safe)
    print("\nSUCCESS: Phase 133 Validation and Safety reports generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
