"""Phase 122: Run Factor Metadata Manifest and Governance Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.factor_metadata_manifest import build_factor_metadata_manifest
from advanced_factor_metadata.factor_manual_review_registry import build_factor_manual_review_registry
from advanced_factor_metadata.factor_non_signal_policies import build_factor_non_signal_policy_registry
from advanced_factor_metadata.factor_forbidden_claims import build_factor_forbidden_claim_registry
from advanced_factor_metadata.phase_123_handoff import build_phase_123_feature_quality_drift_handoff_report
from advanced_factor_metadata.factor_metadata_report_builder import (
    build_factor_manifest_markdown_report,
    build_phase_123_handoff_markdown_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_manf, s_manf = build_factor_metadata_manifest(profile)
    df_rev, s_rev = build_factor_manual_review_registry(profile)
    df_nsp, s_nsp = build_factor_non_signal_policy_registry(profile)
    df_fc, s_fc = build_factor_forbidden_claim_registry(profile)
    df_ho, s_ho = build_phase_123_feature_quality_drift_handoff_report(profile)

    data_lake.save_factor_metadata_manifest(df_manf, s_manf)
    data_lake.save_factor_manual_review_registry(df_rev, s_rev)
    data_lake.save_factor_non_signal_policy_registry(df_nsp, s_nsp)
    data_lake.save_factor_forbidden_claim_registry(df_fc, s_fc)
    data_lake.save_phase_123_feature_quality_drift_handoff_report(df_ho, s_ho)

    md_manf = build_factor_manifest_markdown_report(s_manf, df_manf)
    md_ho = build_phase_123_handoff_markdown_report(s_ho, df_ho)

    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "factor_metadata_manifest.md", "w", encoding="utf-8") as f:
        f.write(md_manf)
    with open(reports_dir / "phase_123_drift_handoff.md", "w", encoding="utf-8") as f:
        f.write(md_ho)

    print("=" * 70)
    print("PHASE 122: FACTOR METADATA MANIFEST AND GOVERNANCE")
    print("=" * 70)
    print(f"Total Manifest Items : {s_manf['total_manifest_items']}")
    print(f"All Non-Signal       : {s_manf['all_non_signal']}")
    print(f"Zero Predictions     : {s_manf['zero_target_or_prediction']}")
    print(f"Source Preserved     : {s_manf['all_source_preserved']}")
    print(f"Manual Review Items  : {s_rev['total_review_items']}")
    print(f"Non-Signal Policies  : {s_nsp['total_policies']}")
    print(f"Forbidden Patterns   : {s_fc['total_forbidden_claims']}")
    print(f"Phase 123 Handoff    : {s_ho['handoff_status']} ({s_ho['total_items']} items)")
    print("=" * 70)


if __name__ == "__main__":
    main()
