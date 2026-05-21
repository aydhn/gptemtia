import re

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

regime_report_builders = """

def build_regime_portfolio_text_report(summary: dict, tables: dict[str, pd.DataFrame] | None = None) -> str:
    \"\"\"Builds regime portfolio text report.\"\"\"
    report = "REGIME-AWARE PORTFOLIO RESEARCH REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    report += f"Profile: {summary.get('profile', 'Unknown')}\\n\\n"
    return report

def build_macro_scenario_sensitivity_text_report(summary: dict, sensitivity_df: pd.DataFrame | None = None) -> str:
    \"\"\"Builds macro scenario sensitivity text report.\"\"\"
    report = "MACRO SCENARIO SENSITIVITY REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    return report

def build_basket_stress_test_text_report(summary: dict, stress_df: pd.DataFrame | None = None) -> str:
    \"\"\"Builds basket stress test text report.\"\"\"
    report = "BASKET STRESS TEST REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    return report

def build_drawdown_cluster_text_report(summary: dict, cluster_df: pd.DataFrame | None = None, recovery_df: pd.DataFrame | None = None) -> str:
    \"\"\"Builds drawdown cluster text report.\"\"\"
    report = "DRAWDOWN CLUSTER REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    return report

def build_risk_regime_exposure_text_report(summary: dict, exposure_df: pd.DataFrame | None = None) -> str:
    \"\"\"Builds risk regime exposure text report.\"\"\"
    report = "RISK REGIME EXPOSURE REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    return report

def build_portfolio_regime_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    \"\"\"Builds portfolio regime status text report.\"\"\"
    report = "PORTFOLIO REGIME STATUS REPORT\\n"
    report += "=" * 50 + "\\n"
    report += "UYARI: Bu çıktı offline rejim bazlı portföy araştırması/sanal stres testi raporudur. Gerçek allocation, canlı emir, broker talimatı, gerçek pozisyon veya yatırım tavsiyesi değildir.\\n\\n"
    return report

"""

with open("commodity_fx_signal_bot/reports/report_builder.py", "a") as f:
    f.write(regime_report_builders)
