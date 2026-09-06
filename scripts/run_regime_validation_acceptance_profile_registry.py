"""Run script: Profile and Domain Registry for Phase 133 Regime Validation Acceptance."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_regime_validation_acceptance_profile_markdown_report,
)
from reports.report_builder import build_regime_validation_acceptance_text_report


def main():
    print("Executing Phase 133 Regime Validation Acceptance Profile and Domain Registry...")
    pipeline = RegimeValidationAcceptancePipeline()
    dfs, summaries = pipeline.build_profiles_domains_gates(save=True)

    print(f"Profiles Registered: {len(dfs['profiles'])}")
    print(f"Domains Registered: {len(dfs['domains'])}")
    print(f"Gates Registered: {len(dfs['gates'])}")

    txt_rep = build_regime_validation_acceptance_text_report(summaries["profiles"])
    md_rep = build_regime_validation_acceptance_profile_markdown_report(summaries["profiles"], dfs["profiles"])

    print("\n--- Profile Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 Profiles and Domains generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
