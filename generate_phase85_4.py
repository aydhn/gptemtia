import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")
TARGET_DIR = ROOT / "local_governance_control"

# risk_committee_rehearsal.py
with open(TARGET_DIR / "risk_committee_rehearsal.py", "w", encoding="utf-8") as f:
    f.write("""from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_risk_committee_rehearsal_sections(profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Risk committee rehearsal purpose", "content": "Offline risk komitesi provası."},
        {"title": "What is reviewed", "content": "Sistem sağlığı ve sınırlar."},
        {"title": "What cannot be approved", "content": "Gerçek yatırım kararları ve canlı operasyon onaylanamaz."},
        {"title": "No-go review", "content": "No-go koşullarının kontrolü."},
        {"title": "Quality/risk summaries", "content": "Kalite ve risk durumları."},
        {"title": "Manual approval ledger review", "content": "Onay defterinin incelenmesi."},
        {"title": "Escalation matrix review", "content": "Manuel eskalasyon akışı."},
        {"title": "Open decision review", "content": "Açık kararların provası."},
        {"title": "Follow-up action rehearsal", "content": "Takip eylemleri."},
        {"title": "Boundary statement", "content": "Bu doküman risk komitesi kararı değildir."}
    ]

def build_risk_committee_rehearsal_pack(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_risk_committee_rehearsal_sections(profile)
    lines = ["# Risk Committee Rehearsal Pack", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\\n".join(lines)
    return text, summarize_risk_committee_rehearsal_pack(text)

def summarize_risk_committee_rehearsal_pack(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_risk_committee_rehearsal_pack(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
""")

# risk_committee_templates.py
with open(TARGET_DIR / "risk_committee_templates.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_risk_committee_agenda_templates(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"agenda_item": "Review no-go conditions", "duration_mins": 15},
        {"agenda_item": "Review quality warnings", "duration_mins": 20},
        {"agenda_item": "Check manual approval ledger", "duration_mins": 15}
    ]
    return pd.DataFrame(data)

def build_default_risk_committee_decisions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"decision_id": "DEC-001", "decision": "Rehearsal completed", "status": "rehearsal_only"}
    ]
    return pd.DataFrame(data)

def build_risk_committee_agenda_template_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_risk_committee_agenda_templates(profile)
    return df, {"total_items": len(df)}

def build_risk_committee_decision_rehearsal_ledger(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_risk_committee_decisions(profile)
    return df, {"total_decisions": len(df)}

def summarize_risk_committee_templates(agenda_df: pd.DataFrame, decision_df: pd.DataFrame) -> dict:
    return {
        "agenda_items": len(agenda_df) if agenda_df is not None else 0,
        "decisions": len(decision_df) if decision_df is not None else 0
    }
""")

# operator_supervision.py
with open(TARGET_DIR / "operator_supervision.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
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
    text = "\\n".join(lines)
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
""")

# escalation_matrix.py
with open(TARGET_DIR / "escalation_matrix.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import EscalationItem, build_escalation_item_id, escalation_item_to_dict

def build_default_escalation_items(profile: LocalGovernanceControlProfile) -> list[EscalationItem]:
    return [
        EscalationItem(
            escalation_id=build_escalation_item_id("Safety Breach Attempt"),
            escalation_area="Safety",
            escalation_label="escalation_blocked_by_no_go",
            trigger_condition="Model output contains live trading claim.",
            recommended_manual_action="Halt operation and review logs.",
            warnings=["Bu otomatik bir süreç değildir."]
        ),
        EscalationItem(
            escalation_id=build_escalation_item_id("External API Request"),
            escalation_area="Network",
            escalation_label="escalation_external_approval_not_allowed",
            trigger_condition="Attempt to connect external service.",
            recommended_manual_action="Block request manually.",
            warnings=["External approval not allowed."]
        )
    ]

def build_escalation_matrix_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_escalation_items(profile)
    df = pd.DataFrame([escalation_item_to_dict(i) for i in items])
    return df, summarize_escalation_matrix(df)

def summarize_escalation_matrix(escalation_df: pd.DataFrame) -> dict:
    if escalation_df is None or escalation_df.empty:
        return {"total": 0}
    return {"total": len(escalation_df)}
""")
print("Done writing risk committee and supervision.")
