"""Run script: Acceptance Manifest and Phase 134 Handoff Report."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_acceptance_manifest_markdown_report,
    build_phase_134_handoff_markdown_report,
)
from reports.report_builder import (
    build_regime_validation_acceptance_manifest_text_report,
    build_phase_134_handoff_text_report,
)


def main():
    print("Executing Phase 133 Acceptance Manifest and Phase 134 Handoff...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_fsm, s_fsm = pipeline.build_findings_scoring_manifest(save=True)
    t_hvs, s_hvs = pipeline.build_health_validation_safety_handoff(save=True)

    print(f"Manifest Name: {s_fsm['manifest']['manifest_name']}")
    print(f"Manifest Valid: {s_fsm['manifest']['manifest_valid']}")
    print(f"Handoff Total Items: {s_hvs['handoff']['total_items']}")
    print(f"Handoff Status: {s_hvs['handoff']['handoff_status']}")

    txt_rep = build_regime_validation_acceptance_manifest_text_report(s_fsm["manifest"])
    md_rep = build_regime_validation_acceptance_manifest_markdown_report(s_fsm["manifest"], t_fsm["manifest"])
    txt_hand = build_phase_134_handoff_text_report(s_hvs["handoff"])
    md_hand = build_phase_134_handoff_markdown_report(s_hvs["handoff"], t_hvs["handoff"])

    print("\n--- Manifest Summary ---")
    print(txt_rep)
    print("\n--- Phase 134 Handoff Summary ---")
    print(txt_hand)
    print("\nSUCCESS: Phase 133 Manifest and Phase 134 Handoff reports generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
