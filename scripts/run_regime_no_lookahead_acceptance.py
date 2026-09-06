"""Run script: No-Lookahead, Timestamp Order, Backward-Asof, and Forbidden Column Acceptance."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_no_lookahead_acceptance_markdown_report,
)
from reports.report_builder import (
    build_no_lookahead_acceptance_text_report,
)


def main():
    print("Executing Phase 133 Regime No-Lookahead and Temporal Acceptance Reports...")
    pipeline = RegimeValidationAcceptancePipeline()
    dfs, summaries = pipeline.build_core_acceptance_reports(save=True)

    print(f"No-Lookahead Checks Passed: {summaries['no_lookahead']['passed_checks']}/{summaries['no_lookahead']['total_checks']}")
    print(f"Timestamp Order Checks Passed: {summaries['timestamp_order']['passed_checks']}/{summaries['timestamp_order']['total_checks']}")
    print(f"Backward Asof Checks Passed: {summaries['backward_asof']['passed_checks']}/{summaries['backward_asof']['total_checks']}")
    print(f"Forbidden Column Rules Active: {summaries['forbidden_columns']['total_forbidden_rules']}")

    txt_rep = build_no_lookahead_acceptance_text_report(summaries["no_lookahead"])
    md_rep = build_no_lookahead_acceptance_markdown_report(summaries["no_lookahead"], dfs["no_lookahead"])

    print("\n--- No-Lookahead Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 No-Lookahead and Temporal Acceptance reports generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
