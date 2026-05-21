import pandas as pd
from typing import Dict
from portfolio_regime.regime_config import PortfolioRegimeProfile

def build_regime_disclaimer() -> str:
    return "> **UYARI:** Bu rapor offline rejim bazlı portföy araştırması/sanal stres testi çıktısıdır; gerçek portföy yönetimi, canlı emir, broker talimatı veya yatırım tavsiyesi değildir.\n\n"

def build_regime_portfolio_markdown_report(summary: dict, tables: Dict[str, pd.DataFrame], profile: PortfolioRegimeProfile) -> str:
    report = "# Regime-Aware Portfolio Research Report\n\n"
    report += build_regime_disclaimer()
    report += f"**Profile:** {profile.name}\n\n"

    if 'symbol_returns' in tables and not tables['symbol_returns'].empty:
        report += "## Regime-Conditioned Symbol Returns\n\n"
        report += tables['symbol_returns'].to_markdown(index=False) + "\n\n"

    if 'basket_returns' in tables and not tables['basket_returns'].empty:
        report += "## Regime-Conditioned Basket Returns\n\n"
        report += tables['basket_returns'].to_markdown(index=False) + "\n\n"

    return report

def build_macro_scenario_markdown_report(summary: dict, sensitivity_df: pd.DataFrame, profile: PortfolioRegimeProfile) -> str:
    report = "# Macro Scenario Sensitivity Report\n\n"
    report += build_regime_disclaimer()
    report += f"**Profile:** {profile.name}\n\n"

    if not sensitivity_df.empty:
        report += "## Scenario Sensitivity\n\n"
        report += sensitivity_df.to_markdown(index=False) + "\n\n"

    return report

def build_stress_test_markdown_report(summary: dict, stress_tables: Dict[str, pd.DataFrame], profile: PortfolioRegimeProfile) -> str:
    report = "# Basket Stress Test Report\n\n"
    report += build_regime_disclaimer()
    report += f"**Profile:** {profile.name}\n\n"

    if 'scenario_stress' in stress_tables and not stress_tables['scenario_stress'].empty:
        report += "## Scenario Stress Tests\n\n"
        report += stress_tables['scenario_stress'].to_markdown(index=False) + "\n\n"

    if 'historical_stress' in stress_tables and not stress_tables['historical_stress'].empty:
        report += "## Historical Stress Tests\n\n"
        report += stress_tables['historical_stress'].to_markdown(index=False) + "\n\n"

    return report

def build_drawdown_cluster_markdown_report(summary: dict, cluster_df: pd.DataFrame, profile: PortfolioRegimeProfile) -> str:
    report = "# Drawdown Cluster Report\n\n"
    report += build_regime_disclaimer()
    report += f"**Profile:** {profile.name}\n\n"

    if not cluster_df.empty:
        report += "## Drawdown Clusters\n\n"
        report += cluster_df.to_markdown(index=False) + "\n\n"

    return report

def build_risk_regime_exposure_markdown_report(summary: dict, exposure_df: pd.DataFrame, profile: PortfolioRegimeProfile) -> str:
    report = "# Risk Regime Exposure Report\n\n"
    report += build_regime_disclaimer()
    report += f"**Profile:** {profile.name}\n\n"

    if not exposure_df.empty:
        report += "## Regime Exposure\n\n"
        report += exposure_df.to_markdown(index=False) + "\n\n"

    return report
