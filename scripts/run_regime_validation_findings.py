"""Run script: Findings, Manual Review Queue, and Acceptance Score Report."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_findings_markdown_report,
    build_regime_acceptance_score_markdown_report,
)
from reports.report_builder import (
    build_regime_validation_findings_text_report,
    build_regime_acceptance_score_text_report,
)


def main():
    print("Executing Phase 133 Findings, Manual Review, and Acceptance Scoring...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_fsm, s_fsm = pipeline.build_findings_scoring_manifest(save=True)

    print(f"Total Findings: {s_fsm['findings']['total_findings']}")
    print(f"Critical Blockers: {s_fsm['findings']['critical_blockers']}")
    print(f"Manual Review Queue Items: {s_fsm['manual_review']['total_queue_items']}")
    print(f"Overall Acceptance Score: {s_fsm['score']['overall_score']}")
    print(f"Score Tier: {s_fsm['score']['score_tier']}")

    txt_rep = build_regime_acceptance_score_text_report(s_fsm["score"])
    md_rep = build_regime_acceptance_score_markdown_report(s_fsm["score"], t_fsm["score"])

    print("\n--- Scoring Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 Findings, Manual Review Queue, and Score reports generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
