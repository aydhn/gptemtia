"""Reproducibility report builder."""
import pandas as pd

def build_reproducibility_disclaimer() -> str:
    return "\n\nBu rapor offline/local reproducibility dossier ve build-free reproduction governance ciktisidir; gercek build, CI/CD, Docker image, dependency install, official build attestation, production approval, canli sinyal, broker talimati, model deployment veya yatirim tavsiyesi degildir.\n"

def build_reproducibility_domain_registry_markdown_report(summary: dict, domain_df: pd.DataFrame | None = None) -> str:
    return "# Reproducibility Domain Registry\n" + build_reproducibility_disclaimer()

def build_reproducibility_dossier_markdown_report(summary: dict, dossier_text: str | None = None) -> str:
    return "# Final Local Reproducibility Dossier\n" + build_reproducibility_disclaimer()

def build_environment_replay_markdown_report(summary: dict, replay_text: str | None = None) -> str:
    return "# Environment Replay Manifest\n" + build_reproducibility_disclaimer()

def build_deterministic_runbook_markdown_report(summary: dict, runbook_text: str | None = None) -> str:
    return "# Deterministic Runbook\n" + build_reproducibility_disclaimer()

def build_build_free_reproduction_markdown_report(summary: dict, reproduction_text: str | None = None) -> str:
    return "# Build-Free Reproduction Layer\n" + build_reproducibility_disclaimer()

def build_reproducibility_governance_markdown_report(summary: dict, governance_text: str | None = None) -> str:
    return "# Terminal Reproducibility Governance Binder\n" + build_reproducibility_disclaimer()

def build_reproducibility_quality_markdown_report(summary: dict, quality: dict | None = None) -> str:
    return "# Reproducibility Quality Report\n" + build_reproducibility_disclaimer()

def build_reproducibility_status_markdown_report(summary: dict, status_df: pd.DataFrame | None = None) -> str:
    return "# Reproducibility Status\n" + build_reproducibility_disclaimer()
