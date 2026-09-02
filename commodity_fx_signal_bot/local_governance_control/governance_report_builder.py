import pandas as pd

def build_governance_disclaimer() -> str:
    return "Bu rapor offline/local governance rehearsal ve operator supervision çıktısıdır; gerçek yönetim kararı, risk komitesi onayı, compliance sign-off, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."

def build_governance_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    lines = [f"# Governance Domain Registry", "", build_governance_disclaimer(), ""]
    return "\n".join(lines)

def build_control_room_packet_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    lines = [f"# Control Room Packet", "", build_governance_disclaimer(), ""]
    if packet_text: lines.append(packet_text)
    return "\n".join(lines)

def build_executive_oversight_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    lines = [f"# Executive Oversight Packet", "", build_governance_disclaimer(), ""]
    if packet_text: lines.append(packet_text)
    return "\n".join(lines)

def build_manual_approval_ledger_markdown_report(summary: dict, approval_df: pd.DataFrame | None = None) -> str:
    lines = [f"# Manual Approval Ledger", "", build_governance_disclaimer(), ""]
    return "\n".join(lines)

def build_risk_committee_rehearsal_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    lines = [f"# Risk Committee Rehearsal", "", build_governance_disclaimer(), ""]
    if packet_text: lines.append(packet_text)
    return "\n".join(lines)

def build_governance_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    lines = [f"# Governance Quality Report", "", build_governance_disclaimer(), ""]
    return "\n".join(lines)

def build_governance_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    lines = [f"# Governance Status Report", "", build_governance_disclaimer(), ""]
    return "\n".join(lines)
