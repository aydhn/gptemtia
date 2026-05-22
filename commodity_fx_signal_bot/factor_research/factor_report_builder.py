import pandas as pd
from .factor_config import FactorResearchProfile

def build_factor_disclaimer() -> str:
    return (
        "*** YASAL UYARI VE DISCLAIMER ***\n\n"
        "Bu rapor offline factor research ve cross-sectional simülasyon çıktısıdır. "
        "Top/bottom bucket, leader/laggard, factor rank veya factor-neutral basket gibi "
        "ifadeler tamamen istatistiksel ve sanal (sentetik) analiz bağlamındadır.\n"
        "Bu rapor; gerçek long-short portföy, gerçek allocation, canlı emir, "
        "broker talimatı, gerçek pozisyon veya YATIRIM TAVSİYESİ DEĞİLDİR.\n"
        "Carry ve value proxy'leri, gerçek veriler eksik olduğunda "
        "yaklaşım (proxy) olarak hesaplanmıştır ve gerçek fundamental verileri yansıtmaz.\n\n"
    )

def build_factor_research_markdown_report(summary: dict, tables: dict[str, pd.DataFrame], profile: FactorResearchProfile) -> str:
    lines = [
        f"# Factor Research and Cross-Sectional Analysis Report ({summary.get('timeframe', '1d')})",
        build_factor_disclaimer(),
        f"**Profile:** {profile.name}",
        f"**Generated:** {summary.get('timestamp', 'Unknown')}",
        "",
        "## Universe Coverage",
        f"- Valid Symbols: {summary.get('universe_coverage', {}).get('valid_symbols', 0)}",
        ""
    ]

    if "composite_ranking" in tables and not tables["composite_ranking"].empty:
        lines.append("## Composite Factor Ranking (Top 10)")
        lines.append(tables["composite_ranking"].head(10).to_markdown(index=False))
        lines.append("")

    if "backtest_results" in tables and not tables["backtest_results"].empty:
        lines.append("## Factor Virtual Spreads (Top vs Bottom)")
        lines.append(tables["backtest_results"][["factor_id", "top_bucket_return", "bottom_bucket_return", "spread_return"]].to_markdown(index=False))
        lines.append("")

    return "\n".join(lines)

def build_factor_score_markdown_report(summary: dict, score_df: pd.DataFrame, profile: FactorResearchProfile) -> str:
    lines = [
        f"# Factor Score Report ({summary.get('timeframe', '1d')})",
        build_factor_disclaimer(),
        f"**Profile:** {profile.name}",
        ""
    ]
    if not score_df.empty:
        lines.append(score_df.head(20).to_markdown(index=False))
    return "\n".join(lines)

def build_factor_backtest_markdown_report(summary: dict, backtest_df: pd.DataFrame, profile: FactorResearchProfile) -> str:
    lines = [
        f"# Factor Backtest Report ({summary.get('timeframe', '1d')})",
        build_factor_disclaimer(),
        f"**Profile:** {profile.name}",
        ""
    ]
    if not backtest_df.empty:
        lines.append(backtest_df.to_markdown(index=False))
    return "\n".join(lines)

def build_factor_exposure_markdown_report(summary: dict, exposure_df: pd.DataFrame, profile: FactorResearchProfile) -> str:
    lines = [
        f"# Factor Exposure Report ({summary.get('timeframe', '1d')})",
        build_factor_disclaimer(),
        ""
    ]
    if not exposure_df.empty:
        lines.append(exposure_df.head(20).to_markdown(index=False))
    return "\n".join(lines)

def build_factor_neutral_markdown_report(summary: dict, neutral_df: pd.DataFrame, profile: FactorResearchProfile) -> str:
    lines = [
        f"# Factor Neutral Basket Report ({summary.get('timeframe', '1d')})",
        build_factor_disclaimer(),
        ""
    ]
    if not neutral_df.empty:
         lines.append(neutral_df.head(20).to_markdown(index=False))
    return "\n".join(lines)
