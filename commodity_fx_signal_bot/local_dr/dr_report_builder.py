
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def build_dr_disclaimer() -> str:
    return "Bu rapor offline/local disaster-recovery tabletop ve restore drill simulation çıktısıdır; gerçek restore, cloud DR, production incident-response, canlı sinyal, broker talimatı, model deployment, production scheduler, resmi SLA veya yatırım tavsiyesi değildir. Bulgular manuel tatbikat ve resilience planlaması amaçlıdır."

def build_dr_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# DR Domain Registry",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Domainler",
        ""
    ]
    if domain_df is not None:
        lines.append(domain_df.to_markdown(index=False))
    return "\n".join(lines)

def build_tabletop_scenarios_markdown_report(summary: dict, scenario_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# DR Tabletop Scenarios",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Senaryolar",
        ""
    ]
    if scenario_df is not None:
        lines.append(scenario_df.to_markdown(index=False))
    return "\n".join(lines)

def build_restore_drill_simulation_markdown_report(summary: dict, drill_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# DR Restore Drill Simulation",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Tatbikatlar",
        ""
    ]
    if drill_df is not None:
        lines.append(drill_df.to_markdown(index=False))
    return "\n".join(lines)

def build_failure_mode_playbooks_markdown_report(summary: dict, playbook_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# DR Failure Mode Playbooks",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Playbooks",
        ""
    ]
    if playbook_df is not None:
        lines.append(playbook_df.to_markdown(index=False))
    return "\n".join(lines)

def build_incident_rehearsal_binder_markdown_report(summary: dict, binder_text: str | None = None) -> str:
    lines = [
        "# DR Incident Rehearsal Binder",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## İçerik",
        ""
    ]
    if binder_text is not None:
        lines.append(binder_text)
    return "\n".join(lines)

def build_dr_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    lines = [
        "# DR Quality Report",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Kalite Kontrolleri",
        ""
    ]
    if quality is not None:
        lines.append(str(quality))
    return "\n".join(lines)

def build_dr_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    lines = [
        "# DR Status Report",
        "",
        f"> **UYARI:** {build_dr_disclaimer()}",
        "",
        "## Özeti",
        "",
        str(summary),
        "",
        "## Durum",
        ""
    ]
    if status_df is not None:
        lines.append(status_df.to_markdown(index=False))
    return "\n".join(lines)
