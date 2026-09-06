"""Run script: Component Acceptance Reports for Regime Pipeline (Phases 127-132)."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_component_acceptance_markdown_report,
)
from reports.report_builder import (
    build_component_acceptance_text_report,
)


def main():
    print("Executing Phase 133 Regime Component Acceptance Reports (Phases 127-132)...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_comp, s_comp = pipeline.build_component_acceptance_reports(save=True)
    t_dep, s_dep = pipeline.build_dependency_acceptance_reports(save=True)

    print(f"Matrix Checks Passed: {s_comp['matrix']['passed_checks']}/{s_comp['matrix']['total_checks']}")
    print(f"Candidate State Checks Passed: {s_comp['candidate_state']['passed_checks']}/{s_comp['candidate_state']['total_checks']}")
    print(f"Pseudo State Checks Passed: {s_comp['pseudo_state']['passed_checks']}/{s_comp['pseudo_state']['total_checks']}")
    print(f"Transition Checks Passed: {s_comp['transition']['passed_checks']}/{s_comp['transition']['total_checks']}")
    print(f"Cross-Asset Checks Passed: {s_comp['cross_asset']['passed_checks']}/{s_comp['cross_asset']['total_checks']}")
    print(f"Macro/Event/News Checks Passed: {s_comp['macro_event_news']['passed_checks']}/{s_comp['macro_event_news']['total_checks']}")
    print(f"Validation Dependencies Satisfied: {s_dep['validation_dependencies']['satisfied_dependencies']}/{s_dep['validation_dependencies']['total_dependencies']}")
    print(f"Quality Dependencies Satisfied: {s_dep['quality_dependencies']['satisfied_dependencies']}/{s_dep['quality_dependencies']['total_dependencies']}")

    txt_rep = build_component_acceptance_text_report(s_comp["matrix"])
    md_rep = build_component_acceptance_markdown_report(s_comp["matrix"], t_comp["matrix"])

    print("\n--- Component Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 Regime Component Acceptance reports generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
