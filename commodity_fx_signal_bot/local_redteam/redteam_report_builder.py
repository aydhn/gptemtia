import pandas as pd

def build_redteam_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    report = "# LOCAL REDTEAM DOMAIN REGISTRY REPORT\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_redteam_rehearsal_packet_markdown_report(summary: dict, packet_text: str | None = None) -> str:
    report = "# FINAL LOCAL REDTEAM REHEARSAL PACKET\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    if packet_text:
        report += packet_text + "\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_misuse_scenario_library_markdown_report(summary: dict, scenario_df: pd.DataFrame | None = None) -> str:
    report = "# MISUSE SCENARIO LIBRARY\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_adversarial_prompt_checklist_markdown_report(summary: dict, check_df: pd.DataFrame | None = None) -> str:
    report = "# ADVERSARIAL PROMPT SAFETY CHECKLIST\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_safety_assurance_markdown_report(summary: dict, assurance_text: str | None = None) -> str:
    report = "# SAFETY ASSURANCE SUMMARY\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_redteam_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    report = "# REDTEAM QUALITY REPORT\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_redteam_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    report = "# REDTEAM STATUS REPORT\n\n"
    report += "> **UYARI:** Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\n\n"
    for k, v in summary.items():
        report += f"- **{k}**: {v}\n"
    return report

def build_redteam_disclaimer() -> str:
    return "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
