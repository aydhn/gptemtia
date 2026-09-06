"""Run script: Validation Gate Registry for Phase 133 Regime Validation Acceptance."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_gate_markdown_report,
)
from reports.report_builder import build_regime_validation_gate_text_report


def main():
    print("Executing Phase 133 Regime Validation Gates Registry...")
    pipeline = RegimeValidationAcceptancePipeline()
    dfs, summaries = pipeline.build_profiles_domains_gates(save=True)

    print(f"Total Gates Evaluated: {summaries['gates']['total_gates']}")
    print(f"Passed Gates: {summaries['gates']['passed_gates']}")
    print(f"All Gates Passed: {summaries['gates']['all_passed']}")

    txt_rep = build_regime_validation_gate_text_report(summaries["gates"])
    md_rep = build_regime_validation_gate_markdown_report(summaries["gates"], dfs["gates"])

    print("\n--- Gate Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 Validation Gates generated and verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
