import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_operator_supervision_sections(profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Komut çalıştırmadan önce boundary kontrolü", "content": "Sınırları aşan komut çalıştırılamaz."},
        {"title": "Status raporlarını okuma", "content": "Durum raporları düzenli incelenmeli."},
        {"title": "Quality warnings kontrolü", "content": "Tüm uyarılar manuel değerlendirilmeli."},
        {"title": "No-go/safe-go kontrolü", "content": "Uygulama güvenli mi?"},
        {"title": "Manual approval ledger güncelleme provası", "content": "Onay defterini güncelleme simülasyonu."},
        {"title": "Açık kararları takip etme", "content": "Açık durumları kapatma akışı."},
        {"title": "Escalation gerektiren durumları işaretleme", "content": "Escalation matrix kullanımı."},
        {"title": "Live/broker/deploy/advice yasaklarını koruma", "content": "Bu eylemler kesinlikle yasaktır."}
    ]

def build_operator_supervision_guide(profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_operator_supervision_sections(profile)
    lines = ["# Operator Supervision Guide", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\n".join(lines)
    return text, {"length": len(text), "sections": len(sections)}

def build_operator_supervision_checklist(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    data = [
        {"check_item": "Check live trading limits", "status": "Pending"},
        {"check_item": "Verify broker disconnection", "status": "Pending"}
    ]
    df = pd.DataFrame(data)
    return df, {"total_checks": len(df)}

def summarize_operator_supervision(guide_text: str, checklist_df: pd.DataFrame) -> dict:
    return {
        "guide_length": len(guide_text) if guide_text else 0,
        "checklist_size": len(checklist_df) if checklist_df is not None else 0
    }
