"""Phase 134 Script: Run Regime FeatureStore Profile & Domain Registry.

Generates profile and domain registries, saving CSV, Markdown, and TXT outputs.
"""

from pathlib import Path
from advanced_regime_featurestore_integration.regime_featurestore_config import (
    get_default_regime_featurestore_profile,
)
from advanced_regime_featurestore_integration.regime_featurestore_profile_registry import (
    build_regime_featurestore_profile_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_domain_registry import (
    build_regime_featurestore_domain_registry,
)
from advanced_regime_featurestore_integration.regime_featurestore_report_builder import (
    build_regime_featurestore_profile_markdown_report,
)
from reports.report_builder import build_regime_featurestore_text_report
from data.storage.data_lake import DataLake


def main() -> None:
    data_lake = DataLake()
    profile = get_default_regime_featurestore_profile()

    p_df, p_sum = build_regime_featurestore_profile_registry(profile)
    d_df, d_sum = build_regime_featurestore_domain_registry(profile)

    data_lake.save_regime_featurestore_profile_registry(p_df, p_sum)
    data_lake.save_regime_featurestore_domain_registry(d_df, d_sum)

    # Save Markdown & TXT reports
    out_dir = Path("reports/output/advanced_regime_featurestore_integration")
    out_dir.mkdir(parents=True, exist_ok=True)

    md_content = build_regime_featurestore_profile_markdown_report(p_sum, p_df)
    txt_content = build_regime_featurestore_text_report(p_sum, p_df)

    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)

    with open(out_dir / "markdown" / "profile_registry.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    with open(out_dir / "txt" / "profile_registry.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)

    print(f"Phase 134: Profile and Domain registries generated successfully ({len(p_df)} profiles, {len(d_df)} domains).")


if __name__ == "__main__":
    main()
