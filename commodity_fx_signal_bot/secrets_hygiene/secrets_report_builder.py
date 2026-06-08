
import pandas as pd
from typing import Optional

def build_secrets_disclaimer() -> str: return "Bu çıktı offline/local secrets hygiene raporudur. Gerçek secret değeri, canlı emir, broker talimatı, gerçek pozisyon, model deployment, cloud vault entegrasyonu, production scheduler, otomatik trade onayı veya yatırım tavsiyesi içermez.\n\n"

def build_sensitive_file_scan_markdown_report(summary: dict, inventory_df: Optional[pd.DataFrame] = None, findings_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Sensitive File Scan Report\n", build_secrets_disclaimer()]
    lines.append(f"- **Total Files**: {summary.get('inventory', {}).get('total_files', 0)}")
    lines.append(f"- **Pattern Findings**: {summary.get('pattern_findings_count', 0)}")
    lines.append(f"- **Entropy Findings**: {summary.get('entropy_findings_count', 0)}\n")
    return "\n".join(lines)

def build_env_template_audit_markdown_report(summary: dict, env_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Env Template Audit Report\n", build_secrets_disclaimer()]
    lines.append(f"- **Total Variables**: {summary.get('total_variables', 0)}")
    lines.append(f"- **Realistic Secrets Found**: {summary.get('realistic_secrets_found', 0)}\n")
    return "\n".join(lines)

def build_credential_boundary_markdown_report(summary: dict, boundary_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Credential Boundary Report\n", build_secrets_disclaimer()]
    lines.append(f"- **Failed Boundaries**: {summary.get('failed_boundaries', 0)}")
    lines.append(f"- **Findings**: {summary.get('total_findings_in_boundaries', 0)}\n")
    return "\n".join(lines)

def build_private_data_protection_markdown_report(summary: dict, private_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Private Data Protection Report\n", build_secrets_disclaimer()]
    lines.append(f"- **Total Findings**: {summary.get('total_private_findings', 0)}\n")
    return "\n".join(lines)

def build_secret_remediation_markdown_report(summary: dict, recommendations_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Secret Remediation Recommendations\n", build_secrets_disclaimer()]
    lines.append(f"- **Total Recommendations**: {summary.get('total_recommendations', 0)}")
    lines.append(f"- **Destructive**: {summary.get('destructive_count', 0)}\n")
    return "\n".join(lines)

def build_secrets_quality_markdown_report(summary: dict, quality: Optional[dict] = None) -> str:
    lines = ["# Secrets Quality Report\n", build_secrets_disclaimer()]
    q = quality or {}
    lines.append(f"- **Passed**: {q.get('passed', False)}")
    lines.append(f"- **Warnings**: {q.get('warning_count', 0)}\n")
    return "\n".join(lines)

def build_secrets_hygiene_status_markdown_report(summary: dict, status_df: Optional[pd.DataFrame] = None) -> str:
    lines = ["# Secrets Hygiene Status\n", build_secrets_disclaimer()]
    return "\n".join(lines)
