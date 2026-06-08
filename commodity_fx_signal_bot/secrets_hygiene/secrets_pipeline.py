
from pathlib import Path
import pandas as pd
from typing import Tuple, Optional
from config.settings import Settings
from secrets_hygiene.secrets_config import SecretsHygieneProfile, get_default_secrets_hygiene_profile
from secrets_hygiene.sensitive_file_scanner import build_sensitive_file_scan_report
from secrets_hygiene.env_template_auditor import audit_env_template
from secrets_hygiene.credential_boundary import audit_credential_boundaries
from secrets_hygiene.private_data_scanner import scan_project_for_private_data
from secrets_hygiene.remediation_recommendations import build_secret_remediation_recommendations, recommendations_to_dataframe, summarize_secret_recommendations
from secrets_hygiene.secrets_quality import build_secrets_quality_report
from secrets_hygiene.secrets_safety import build_secrets_safety_report

class SecretsHygienePipeline:
    def __init__(self, data_lake, settings: Settings, project_root: Path, profile: Optional[SecretsHygieneProfile] = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_secrets_hygiene_profile()

    def build_sensitive_file_scan_report(self, save: bool = True) -> Tuple[dict[str, pd.DataFrame], dict]:
        tables, summary = build_sensitive_file_scan_report(self.project_root, self.profile)
        if save and hasattr(self.data_lake, 'save_sensitive_file_inventory'): self.data_lake.save_sensitive_file_inventory(tables.get("inventory", pd.DataFrame()), summary)
        if save and hasattr(self.data_lake, 'save_secret_pattern_findings'): self.data_lake.save_secret_pattern_findings(tables.get("patterns", pd.DataFrame()), summary)
        if save and hasattr(self.data_lake, 'save_high_entropy_findings'): self.data_lake.save_high_entropy_findings(tables.get("entropy", pd.DataFrame()), summary)
        return tables, summary

    def build_env_template_audit_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = audit_env_template(self.project_root, self.profile)
        if save and hasattr(self.data_lake, 'save_env_template_audit'): self.data_lake.save_env_template_audit(df, summary)
        return df, summary

    def build_credential_boundary_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = audit_credential_boundaries(self.project_root, None, self.profile)
        if save and hasattr(self.data_lake, 'save_credential_boundary_report'): self.data_lake.save_credential_boundary_report(df, summary)
        return df, summary

    def build_private_data_protection_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df, summary = scan_project_for_private_data(self.project_root, self.profile)
        if save and hasattr(self.data_lake, 'save_private_data_protection_report'): self.data_lake.save_private_data_protection_report(df, summary)
        return df, summary

    def build_secret_remediation_report(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        recs = build_secret_remediation_recommendations(pd.DataFrame(), None, self.profile)
        df = recommendations_to_dataframe(recs)
        summary = summarize_secret_recommendations(df)
        if save and hasattr(self.data_lake, 'save_secret_remediation_recommendations'): self.data_lake.save_secret_remediation_recommendations(df, summary)
        return df, summary

    def build_secrets_quality_report(self, save: bool = True) -> Tuple[dict, dict]:
        summary = {}
        q = build_secrets_quality_report(summary, None, None, None, None, self.profile)
        safety_df, _ = build_secrets_safety_report({}, self.profile)
        if save and hasattr(self.data_lake, 'save_secrets_quality'): self.data_lake.save_secrets_quality(self.profile.name, q)
        if save and hasattr(self.data_lake, 'save_secrets_safety_report'): self.data_lake.save_secrets_safety_report(safety_df, {})
        return q, {"safety_checks": len(safety_df)}

    def build_secrets_hygiene_status(self, save: bool = True) -> Tuple[pd.DataFrame, dict]:
        df = pd.DataFrame([{"component": "secrets_hygiene", "status": "ok"}])
        return df, {"status": "ok"}
