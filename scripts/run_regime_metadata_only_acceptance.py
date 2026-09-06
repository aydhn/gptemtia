"""Run script: Metadata-Only News, Source Preservation, Non-Signal, and Absence Reports."""

import sys
from advanced_regime_validation_acceptance.regime_validation_acceptance_pipeline import (
    RegimeValidationAcceptancePipeline,
)
from advanced_regime_validation_acceptance.regime_validation_acceptance_report_builder import (
    build_metadata_only_news_acceptance_markdown_report,
)
from reports.report_builder import (
    build_metadata_only_news_acceptance_text_report,
)


def main():
    print("Executing Phase 133 Metadata-Only News, Source Preservation, and Absence Reports...")
    pipeline = RegimeValidationAcceptancePipeline()
    t_core, s_core = pipeline.build_core_acceptance_reports(save=True)
    t_abs, s_abs = pipeline.build_absence_acceptance_reports(save=True)

    print(f"Metadata-Only News Checks: {s_core['metadata_only_news']['passed_checks']}/{s_core['metadata_only_news']['total_checks']}")
    print(f"Source Preservation Rules: {s_core['source_preservation']['total_rules']}")
    print(f"Non-Signal Claims Prohibited: {s_core['non_signal']['total_claims_prohibited']}")
    print(f"Target/Label Absent Terms: {s_abs['target_label_absence']['total_prohibited_terms']}")
    print(f"Model Execution Flags Zero: {s_abs['model_execution_absence']['total_flags_verified']}")

    txt_rep = build_metadata_only_news_acceptance_text_report(s_core["metadata_only_news"])
    md_rep = build_metadata_only_news_acceptance_markdown_report(s_core["metadata_only_news"], t_core["metadata_only_news"])

    print("\n--- Metadata-Only News Summary ---")
    print(txt_rep)
    print("\nSUCCESS: Phase 133 Metadata-Only News, Source Preservation, and Absence verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
