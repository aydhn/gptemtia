"""Phase 125: Run Feature Engine Block Compliance Script.

Generates compliance reports for non-signal, no-lookahead, forbidden columns,
news metadata boundaries, source preservation, and feature store readiness.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_factor_acceptance.feature_factor_acceptance_config import (
    get_default_feature_factor_acceptance_profile,
)
from advanced_feature_factor_acceptance.feature_engine_block_compliance import (
    build_feature_engine_block_non_signal_compliance_report,
    build_feature_engine_block_no_lookahead_compliance_report,
    build_feature_engine_block_forbidden_column_compliance_report,
    build_feature_engine_block_news_metadata_only_compliance_report,
    build_feature_engine_block_source_preservation_report,
    build_feature_engine_block_feature_store_readiness_report,
)
from advanced_feature_factor_acceptance.feature_factor_acceptance_report_builder import (
    build_compliance_markdown_report,
)
from reports.report_builder import build_acceptance_compliance_text_report


def main():
    data_lake = DataLake()
    profile = get_default_feature_factor_acceptance_profile()

    df_ns, s_ns = build_feature_engine_block_non_signal_compliance_report(profile)
    df_la, s_la = build_feature_engine_block_no_lookahead_compliance_report(profile)
    df_fc, s_fc = build_feature_engine_block_forbidden_column_compliance_report(profile)
    df_nm, s_nm = build_feature_engine_block_news_metadata_only_compliance_report(profile)
    df_sp, s_sp = build_feature_engine_block_source_preservation_report(profile)
    df_sr, s_sr = build_feature_engine_block_feature_store_readiness_report(profile)

    data_lake.save_feature_engine_block_non_signal_compliance_report(df_ns, s_ns)
    data_lake.save_feature_engine_block_no_lookahead_compliance_report(df_la, s_la)
    data_lake.save_feature_engine_block_forbidden_column_compliance_report(df_fc, s_fc)
    data_lake.save_feature_engine_block_news_metadata_only_compliance_report(df_nm, s_nm)
    data_lake.save_feature_engine_block_source_preservation_report(df_sp, s_sp)
    data_lake.save_feature_engine_block_feature_store_readiness_report(df_sr, s_sr)

    md_ns = build_compliance_markdown_report(s_ns, df_ns)
    txt_ns = build_acceptance_compliance_text_report(s_ns, df_ns)

    out_dir = Path("reports/output/advanced_feature_factor_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "compliance_non_signal.md", "w", encoding="utf-8") as f:
        f.write(md_ns)
    with open(out_dir / "compliance_non_signal.txt", "w", encoding="utf-8") as f:
        f.write(txt_ns)

    print("=" * 70)
    print("PHASE 125: FEATURE ENGINE BLOCK COMPLIANCE AUDIT")
    print("=" * 70)
    print(f"Non-Signal Compliant       : {s_ns['compliant_modules']}/{s_ns['total_modules_audited']}")
    print(f"No-Lookahead Compliant     : {s_la['compliant_modules']}/{s_la['total_modules_audited']}")
    print(f"Forbidden Columns Blocked  : {s_fc['compliant_modules']}/{s_fc['total_modules_audited']}")
    print(f"News Metadata Compliant    : {s_nm['compliant_modules']}/{s_nm['total_modules_audited']}")
    print(f"Source Preserved Modules   : {s_sp['compliant_modules']}/{s_sp['total_modules_audited']}")
    print(f"Store Aligned Modules      : {s_sr['aligned_modules']}/{s_sr['total_modules_audited']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
