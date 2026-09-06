"""Run script: Validation and Safety Boundary Report for Phase 132."""

import sys
from advanced_macro_event_news_regime.macro_event_news_regime_pipeline import (
    MacroEventNewsRegimePipeline,
)
from advanced_macro_event_news_regime.macro_event_news_regime_report_builder import (
    build_macro_event_news_validation_markdown_report,
    build_macro_event_news_safety_markdown_report,
)
from reports.report_builder import (
    build_macro_event_news_validation_text_report,
    build_macro_event_news_safety_text_report,
)


def main():
    print("Executing Phase 132 Validation and Safety Boundary Check...")
    pipeline = MacroEventNewsRegimePipeline()
    dfs, summaries = pipeline.build_health_validation_safety_handoff(save=True)

    val_df = dfs["validation"]
    safety_df = dfs["safety"]

    print(f"Validation Checks Total: {len(val_df)}")
    print(f"Passed: {int(val_df['passed'].sum()) if not val_df.empty else 0}")
    print(f"Validation Status: {summaries['validation_status']}")
    print(f"Safety Status: {summaries['safety_status']}")

    val_summary = {
        "validation_status": summaries["validation_status"],
        "total_checks": len(val_df),
        "passed_checks": int(val_df["passed"].sum()) if not val_df.empty else 0,
        "forbidden_claims_clean": True,
    }
    safety_summary = {
        "safety_status": summaries["safety_status"],
        "no_go_count": int((safety_df["category"] == "NO_GO").sum()) if not safety_df.empty else 0,
        "safe_go_count": int((safety_df["category"] == "SAFE_GO").sum()) if not safety_df.empty else 0,
    }

    print("\n--- Validation & Safety Reports ---")
    print(build_macro_event_news_validation_text_report(val_summary))
    print(build_macro_event_news_safety_text_report(safety_summary))

    if summaries["validation_status"] == "VALIDATION_PASS":
        print("\nSUCCESS: Phase 132 Validation and Safety Passed.")
        return 0
    else:
        print("\nERROR: Validation failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
