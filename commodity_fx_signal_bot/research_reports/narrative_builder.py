from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile

def build_disclaimer_text() -> str:
    return "Bu rapor offline araştırma/simülasyon çıktısıdır; gerçek emir, canlı sinyal veya yatırım tavsiyesi değildir."

def build_technical_narrative(summary: dict) -> str:
    if not summary:
        return "Teknik özet bulunmamaktadır."
    return f"Araştırma bağlamında teknik görünüm {summary.get('strongest_signal_context', 'belirsiz')} olarak değerlendirilmiştir."

def build_risk_level_narrative(summary: dict) -> str:
    if not summary:
        return "Risk seviye özeti bulunmamaktadır."
    return f"Simülasyon çıktısına göre {summary.get('risk_candidate_count', 0)} risk adayı tespit edilmiştir."

def build_backtest_narrative(summary: dict) -> str:
    if not summary:
        return "Backtest özeti bulunmamaktadır."
    return f"Geçmiş testlerde {summary.get('trade_count', 0)} işlem simüle edilmiş, kazanma oranı {summary.get('win_rate', 0.0):.2f} olmuştur."

def build_performance_narrative(summary: dict) -> str:
    if not summary:
        return "Performans özeti bulunmamaktadır."
    return f"Performans analizinde Sharpe oranı {summary.get('sharpe_ratio', 0.0):.2f} olarak hesaplanmıştır."

def build_validation_narrative(summary: dict) -> str:
    if not summary:
        return "Doğrulama özeti bulunmamaktadır."
    return f"Walk-forward doğrulamasında robustness skoru {summary.get('robustness_score', 0.0):.2f} seviyesindedir."

def build_ml_narrative(summary: dict) -> str:
    if not summary:
        return "ML özeti bulunmamaktadır."
    return f"ML araştırması bağlamında entegrasyon {summary.get('ml_context_available', False)} durumundadır."

def build_paper_narrative(summary: dict) -> str:
    if not summary:
        return "Paper özeti bulunmamaktadır."
    return f"Sanal paper ortamında {summary.get('virtual_order_count', 0)} sanal emir üretilmiştir."

def build_quality_narrative(summary: dict) -> str:
    if not summary:
        return "Kalite özeti bulunmamaktadır."
    return f"Sistem kalite raporu {summary.get('report_quality_score', 0.0):.2f} skora sahiptir."

def build_symbol_narrative(snapshot: SymbolResearchSnapshot, profile: ResearchReportProfile) -> str:
    parts = []
    parts.append(f"{snapshot.symbol} için Araştırma Özeti")

    if profile.include_technical_summary:
        parts.append(build_technical_narrative(snapshot.technical_summary))
    if profile.include_risk_level_summary:
        parts.append(build_risk_level_narrative(snapshot.risk_level_summary))
    if profile.include_backtest_summary:
        parts.append(build_backtest_narrative(snapshot.backtest_summary))
    if profile.include_performance_summary:
        parts.append(build_performance_narrative(snapshot.performance_summary))
    if profile.include_validation_summary:
        parts.append(build_validation_narrative(snapshot.validation_summary))
    if profile.include_ml_summary:
        parts.append(build_ml_narrative(snapshot.ml_summary))
    if profile.include_paper_summary:
        parts.append(build_paper_narrative(snapshot.paper_summary))
    if profile.include_quality_summary:
        parts.append(build_quality_narrative(snapshot.quality_summary))

    return "\n\n".join(parts)

def build_universe_narrative(ranking_summary: dict) -> str:
    return f"Toplam {ranking_summary.get('total_symbols_ranked', 0)} sembol araştırma metriklerine göre sıralanmıştır. En yüksek araştırma skoru {ranking_summary.get('top_symbol', 'bulunamadı')} sembolüne aittir."
