"""Phase 122: Run Technical Factor Families Script."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_factor_metadata.factor_metadata_config import get_default_factor_metadata_profile
from advanced_factor_metadata.technical_factor_families import build_technical_factor_family_registry
from advanced_factor_metadata.trend_factor_families import build_trend_factor_family_registry
from advanced_factor_metadata.momentum_factor_families import build_momentum_factor_family_registry
from advanced_factor_metadata.volatility_factor_families import build_volatility_factor_family_registry
from advanced_factor_metadata.mean_reversion_factor_families import build_mean_reversion_factor_family_registry
from advanced_factor_metadata.return_factor_families import build_return_factor_family_registry
from advanced_factor_metadata.quote_microstructure_factor_placeholders import build_quote_microstructure_factor_placeholder_registry
from advanced_factor_metadata.factor_metadata_report_builder import build_technical_factor_markdown_report


def main():
    settings = get_settings()
    data_lake = DataLake()
    profile = get_default_factor_metadata_profile()

    df_tech, s_tech = build_technical_factor_family_registry(profile)
    df_trend, s_trend = build_trend_factor_family_registry(profile)
    df_mom, s_mom = build_momentum_factor_family_registry(profile)
    df_vol, s_vol = build_volatility_factor_family_registry(profile)
    df_mr, s_mr = build_mean_reversion_factor_family_registry(profile)
    df_ret, s_ret = build_return_factor_family_registry(profile)
    df_quote, s_quote = build_quote_microstructure_factor_placeholder_registry(profile)

    data_lake.save_technical_factor_family_registry(df_tech, s_tech)
    data_lake.save_trend_factor_family_registry(df_trend, s_trend)
    data_lake.save_momentum_factor_family_registry(df_mom, s_mom)
    data_lake.save_volatility_factor_family_registry(df_vol, s_vol)
    data_lake.save_mean_reversion_factor_family_registry(df_mr, s_mr)
    data_lake.save_return_factor_family_registry(df_ret, s_ret)
    data_lake.save_quote_microstructure_factor_placeholder_registry(df_quote, s_quote)

    md_report = build_technical_factor_markdown_report(s_tech, df_tech)
    reports_dir = Path("reports/output/advanced_factor_metadata")
    reports_dir.mkdir(parents=True, exist_ok=True)
    with open(reports_dir / "technical_factor_families.md", "w", encoding="utf-8") as f:
        f.write(md_report)

    print("=" * 70)
    print("PHASE 122: TECHNICAL FACTOR FAMILIES")
    print("=" * 70)
    print(f"Technical Factors    : {s_tech['total_factors']}")
    print(f"Trend Factors        : {s_trend['total_factors']}")
    print(f"Momentum Factors     : {s_mom['total_factors']}")
    print(f"Volatility Factors   : {s_vol['total_factors']}")
    print(f"Mean Reversion       : {s_mr['total_factors']}")
    print(f"Return Factors       : {s_ret['total_factors']}")
    print(f"Quote Microstructure : {s_quote['total_factors']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
