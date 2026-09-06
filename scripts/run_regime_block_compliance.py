"""Phase 135: Run Regime Block Compliance Script.

Generates and audits compliance reports: non-signal, no-lookahead, metadata-only news,
forbidden columns, source preservation, and FeatureStore readiness.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_regime_acceptance.regime_acceptance_config import (
    get_default_regime_acceptance_profile,
)
from advanced_regime_acceptance.regime_block_compliance import (
    build_regime_block_non_signal_compliance_report,
    build_regime_block_no_lookahead_compliance_report,
    build_regime_block_metadata_only_news_compliance_report,
    build_regime_block_forbidden_column_compliance_report,
    build_regime_block_source_preservation_report,
    build_regime_block_featurestore_readiness_report,
)
from advanced_regime_acceptance.regime_block_safety_boundary import (
    build_regime_block_safety_boundary_report,
)
from advanced_regime_acceptance.regime_acceptance_report_builder import (
    build_regime_compliance_markdown_report,
)
from reports.report_builder import (
    build_regime_acceptance_compliance_text_report,
)


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_regime_acceptance_profile()

    df_nonsig, s_nonsig = build_regime_block_non_signal_compliance_report(profile)
    df_look, s_look = build_regime_block_no_lookahead_compliance_report(profile)
    df_news, s_news = build_regime_block_metadata_only_news_compliance_report(profile)
    df_forbid, s_forbid = build_regime_block_forbidden_column_compliance_report(profile)
    df_src, s_src = build_regime_block_source_preservation_report(profile)
    df_store, s_store = build_regime_block_featurestore_readiness_report(profile)
    df_safe, s_safe = build_regime_block_safety_boundary_report(profile)

    data_lake.save_regime_block_non_signal_compliance_report(df_nonsig, s_nonsig)
    data_lake.save_regime_block_no_lookahead_compliance_report(df_look, s_look)
    data_lake.save_regime_block_metadata_only_news_compliance_report(df_news, s_news)
    data_lake.save_regime_block_forbidden_column_compliance_report(df_forbid, s_forbid)
    data_lake.save_regime_block_source_preservation_report(df_src, s_src)
    data_lake.save_regime_block_featurestore_readiness_report(df_store, s_store)
    data_lake.save_regime_block_safety_boundary_report(df_safe, s_safe)

    md_comp = build_regime_compliance_markdown_report(s_nonsig, df_nonsig)
    txt_comp = build_regime_acceptance_compliance_text_report(s_nonsig, df_nonsig)

    out_dir = Path("reports/output/advanced_regime_acceptance")
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "compliance.md", "w", encoding="utf-8") as f:
        f.write(md_comp)
    with open(out_dir / "compliance.txt", "w", encoding="utf-8") as f:
        f.write(txt_comp)

    print("=" * 70)
    print("PHASE 135: REGIME BLOCK COMPLIANCE & SAFETY AUDIT")
    print("=" * 70)
    print(f"Non-Signal Compliant       : {s_nonsig['all_compliant']}")
    print(f"No-Lookahead Compliant     : {s_look['all_compliant']}")
    print(f"Metadata-Only News         : {s_news['all_compliant']}")
    print(f"Forbidden Columns Clean    : {s_forbid['all_compliant']}")
    print(f"Source Preservation Active : {s_src['all_compliant']}")
    print(f"FeatureStore Ready         : {s_store['all_compliant']}")
    print(f"Safety Boundaries Enforced : {s_safe['all_enforced']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
