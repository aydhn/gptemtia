"""Run script: Findings, Manual Review, Scoring, Manifest, and Phase 132 Handoff."""

import sys
from advanced_cross_asset_regime_context.cross_asset_regime_pipeline import (
    CrossAssetRegimePipeline,
)
from advanced_cross_asset_regime_context.cross_asset_regime_report_builder import (
    build_cross_asset_findings_markdown_report,
    build_cross_asset_score_markdown_report,
    build_cross_asset_manifest_markdown_report,
    build_phase_132_handoff_markdown_report,
)
from reports.report_builder import (
    build_cross_asset_findings_text_report,
    build_cross_asset_score_text_report,
    build_cross_asset_manifest_text_report,
    build_phase_132_handoff_text_report,
)


def main():
    print("Executing Phase 131 Findings, Scoring, Manifest, and Phase 132 Handoff...")
    pipeline = CrossAssetRegimePipeline()
    dfs, summaries = pipeline.build_dependencies_findings_scoring_manifest(save=True)
    d6, s6 = pipeline.build_health_validation_safety_handoff(save=True)

    print(f"Findings: {len(dfs['findings'])}")
    print(f"Review Items: {len(dfs['manual_review'])}")
    print(f"Context Score: {summaries['scoring']['context_score']:.4f}")
    print(f"Manifest Status: {summaries['manifest']['manifest_status']}")
    print(f"Phase 132 Handoff Status: {s6['handoff']['handoff_status']}")

    print("\n--- Manifest Summary ---")
    print(build_cross_asset_manifest_text_report(summaries["manifest"]))
    print("\n--- Phase 132 Handoff Summary ---")
    print(build_phase_132_handoff_text_report(s6["handoff"]))
    print("\nSUCCESS: Phase 131 Findings, Manifest, and Phase 132 Handoff generated and saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
