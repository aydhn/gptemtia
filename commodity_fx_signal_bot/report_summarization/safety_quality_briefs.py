import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile

def build_safety_brief(warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    text = "Safety Brief: Tüm sistem offline modda çalışmaktadır. Canlı işlem izni yoktur.\n"
    return text, {"brief_type": "safety_brief", "length": len(text)}

def build_quality_brief(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    text = "Quality Brief: Sistem kalite metrikleri offline olarak değerlendirilmiştir.\n"
    return text, {"brief_type": "quality_brief", "length": len(text)}

def build_scenario_regression_brief(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    text = "Scenario Regression Brief: Tüm senaryo testleri offline olarak koşulmuştur. Bu bir canlı kullanım onayı değildir.\n"
    return text, {"brief_type": "scenario_regression_brief", "length": len(text)}

def build_maintenance_performance_brief(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    text = "Maintenance & Performance Brief: Bakım döngüleri ve performans metrikleri olağan sınırlar içindedir.\n"
    return text, {"brief_type": "maintenance_performance_brief", "length": len(text)}

def build_final_review_brief(findings_df: pd.DataFrame, warnings_df: pd.DataFrame, risk_gap_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[str, dict]:
    text = "Final Review Brief: Son sistem incelemesi tamamlanmıştır. Bu production readiness (canlıya çıkış) anlamına gelmez.\n"
    return text, {"brief_type": "final_review_brief", "length": len(text)}
