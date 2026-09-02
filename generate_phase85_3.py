import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")
TARGET_DIR = ROOT / "local_governance_control"

# control_room_packet.py
with open(TARGET_DIR / "control_room_packet.py", "w", encoding="utf-8") as f:
    f.write("""from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_control_room_sections(project_root: Path, profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Local governance control room rehearsal packet."},
        {"title": "Bu paket ne değildir?", "content": "Gerçek dashboard veya üretim onayı değildir."},
        {"title": "Governance rehearsal overview", "content": "Tüm süreçler offline provadır."},
        {"title": "Executive oversight summary", "content": "Yönetimsel gözden geçirme simülasyonu."},
        {"title": "Manual approval ledger summary", "content": "Manuel onay defteri simülasyonu."},
        {"title": "Risk committee rehearsal summary", "content": "Risk komitesi provası özeti."},
        {"title": "Operator supervision summary", "content": "Operatör gözetimi kılavuz özeti."},
        {"title": "Escalation matrix summary", "content": "Manuel escalation akışı."},
        {"title": "No-go/safe-go summary", "content": "Güvenlik sınırları kontrolü."},
        {"title": "Evidence and reading order", "content": "Kanıt dokümanları okuma sırası."},
        {"title": "Open decisions", "content": "Açık kararlar listesi."},
        {"title": "Manual review requirements", "content": "Gözden geçirme gereksinimleri."},
        {"title": "Final boundary statement", "content": "Canlı emir veya broker işlemi yapılmamıştır."}
    ]

def build_final_local_governance_control_room_packet(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_control_room_sections(project_root, profile)
    lines = ["# Final Local Governance Control Room Packet", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\\n".join(lines)
    return text, summarize_control_room_packet(text)

def summarize_control_room_packet(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_control_room_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
""")

# executive_oversight.py
with open(TARGET_DIR / "executive_oversight.py", "w", encoding="utf-8") as f:
    f.write("""from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def build_executive_oversight_sections(project_root: Path, profile: LocalGovernanceControlProfile) -> list[dict]:
    return [
        {"title": "Executive recap", "content": "Yönetici özeti provası."},
        {"title": "System boundary recap", "content": "Sistem sınırlarının kontrolü."},
        {"title": "Safety recap", "content": "Güvenlik incelemesi."},
        {"title": "Readiness summary", "content": "Hazırlık skoru özeti."},
        {"title": "Quality summary", "content": "Kalite skoru özeti."},
        {"title": "Usability/performance/simplification recap", "content": "Geçmiş faz analizleri."},
        {"title": "Acceptance/delivery/archival/closure/reuse recap", "content": "Teslimat özeti."},
        {"title": "Key unresolved items", "content": "Çözülmemiş maddeler."},
        {"title": "Key risks", "content": "Temel riskler."},
        {"title": "Manual oversight recommendations", "content": "Yönetimsel inceleme önerileri."}
    ]

def build_executive_oversight_packet(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[str, dict]:
    sections = build_executive_oversight_sections(project_root, profile)
    lines = ["# Executive Oversight Packet", ""]
    for s in sections:
        lines.append(f"## {s['title']}")
        lines.append(s["content"])
        lines.append("")
    text = "\\n".join(lines)
    return text, summarize_executive_oversight_packet(text)

def summarize_executive_oversight_packet(text: str) -> dict:
    if not text:
        return {"length": 0, "sections": 0}
    return {"length": len(text), "sections": text.count("## ")}

def save_executive_oversight_packet(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
""")

# manual_approval_ledger.py
with open(TARGET_DIR / "manual_approval_ledger.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile
from .governance_control_models import ManualApprovalItem, build_manual_approval_id, manual_approval_item_to_dict

def build_default_manual_approval_items(profile: LocalGovernanceControlProfile) -> list[ManualApprovalItem]:
    scopes = [
        "safe usage reviewed",
        "no-go/safe-go reviewed",
        "quality warnings reviewed",
        "generated docs reviewed",
        "DataLake output reviewed",
        "delivery package reviewed",
        "archival/provenance reviewed",
        "closure dossier reviewed",
        "performance budget reviewed",
        "usability path reviewed",
        "simplification candidates reviewed"
    ]
    items = []
    for s in scopes:
        items.append(ManualApprovalItem(
            approval_id=build_manual_approval_id("Rehearsal", s),
            approval_name="Manual Review Rehearsal",
            approval_scope=s,
            approval_status="approval_rehearsal_pending",
            evidence_refs=["doc_evidence"],
            decision_note="Offline rehearsal review required.",
            manual_review_required=True,
            warnings=["Bu gerçek bir onay değildir."]
        ))
    return items

def build_manual_approval_ledger(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_manual_approval_items(profile)
    df = pd.DataFrame([manual_approval_item_to_dict(i) for i in items])
    summary = summarize_manual_approval_ledger(df)
    return df, summary

def summarize_manual_approval_ledger(approval_df: pd.DataFrame) -> dict:
    if approval_df is None or approval_df.empty:
        return {"total": 0}
    return {
        "total": len(approval_df),
        "pending": len(approval_df[approval_df["approval_status"] == "approval_rehearsal_pending"])
    }
""")

# approval_checklists.py
with open(TARGET_DIR / "approval_checklists.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_approval_checklists(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"checklist_name": "Safety Checks", "item": "No live trading claim", "required": True},
        {"checklist_name": "Safety Checks", "item": "No production approval claim", "required": True},
        {"checklist_name": "Quality Checks", "item": "Documentation up to date", "required": True}
    ]
    return pd.DataFrame(data)

def build_manual_approval_checklist_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_approval_checklists(profile)
    return df, summarize_approval_checklists(df)

def summarize_approval_checklists(checklist_df: pd.DataFrame) -> dict:
    if checklist_df is None or checklist_df.empty:
        return {"total": 0}
    return {"total": len(checklist_df), "checklists": checklist_df["checklist_name"].nunique()}
""")
print("Done writing packet builders.")
