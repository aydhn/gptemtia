import pandas as pd
from portfolio_research.portfolio_config import PortfolioResearchProfile

def build_portfolio_disclaimer() -> str:
    return (
        "*** YASAL UYARI VE SISTEM NOTU ***\n"
        "Bu rapor offline portföy araştırması ve sanal sepet simülasyonu çıktısıdır.\n"
        "Burada yer alan 'allocation', 'basket', 'portfolio', 'weight', 'exposure' gibi\n"
        "kavramlar araştırma bağlamındadır; gerçek portföy yönetimi, gerçek para tahsisi,\n"
        "canlı emir, broker talimatı veya yatırım tavsiyesi DEĞİLDİR.\n"
        "Gecmis veri analizi gelecekteki performansin garantisi olamaz.\n"
        "************************************\n"
    )

def build_portfolio_markdown_report(summary: dict, tables: dict[str, pd.DataFrame], profile: PortfolioResearchProfile) -> str:
    md = [
        f"# Portfolio Research Report",
        f"**Profile:** {profile.name}",
        f"**Timeframe:** {summary.get('timeframe', '1d')}",
        f"**Generated:** {summary.get('created_at_utc', 'Unknown')}\n",
        build_portfolio_disclaimer(),
        f"## Summary",
        f"- Analyzed Symbols: {summary.get('symbol_count', 0)}",
        f"- Virtual Baskets Created: {summary.get('basket_count', 0)}",
    ]

    if "warnings" in summary and summary["warnings"]:
        md.append("\n## Warnings")
        for w in summary["warnings"]:
            md.append(f"- {w}")

    for table_name, df in tables.items():
        if df is not None and not df.empty:
            md.append(f"\n## {table_name.replace('_', ' ').title()}")
            md.append(df.to_markdown(index=False))

    return "\n".join(md)

def build_correlation_markdown_report(summary: dict, corr_df: pd.DataFrame, pair_df: pd.DataFrame, profile: PortfolioResearchProfile) -> str:
    md = [
        f"# Correlation Analysis Report",
        f"**Profile:** {profile.name}\n",
        build_portfolio_disclaimer(),
        f"## Summary",
        f"- Average Correlation: {summary.get('average_correlation', 'N/A')}",
        f"- High Correlation Pairs (>0.75): {summary.get('high_correlation_pair_count', 0)}",
    ]

    if not pair_df.empty:
        md.append("\n## Top Pairwise Correlations")
        md.append(pair_df.head(20).to_markdown(index=False))

    return "\n".join(md)

def build_diversification_markdown_report(summary: dict, diversification_df: pd.DataFrame | None, profile: PortfolioResearchProfile) -> str:
    md = [
        f"# Diversification Report",
        f"**Profile:** {profile.name}\n",
        build_portfolio_disclaimer(),
    ]

    if diversification_df is not None and not diversification_df.empty:
        md.append("\n## Virtual Basket Diversification")
        md.append(diversification_df.to_markdown(index=False))

    return "\n".join(md)

def build_virtual_basket_markdown_report(summary: dict, performance_df: pd.DataFrame, allocation_df: pd.DataFrame, profile: PortfolioResearchProfile) -> str:
    md = [
        f"# Virtual Basket Report",
        f"**Profile:** {profile.name}\n",
        build_portfolio_disclaimer(),
        f"## Virtual Basket Performance",
    ]

    if not performance_df.empty:
        md.append(performance_df.to_markdown(index=False))

    if not allocation_df.empty:
        md.append("\n## Virtual Allocations")
        md.append(allocation_df.to_markdown(index=False))

    return "\n".join(md)
