from pathlib import Path
import pandas as pd
from datetime import datetime, timezone
from security.security_config import SecurityProfile, get_default_security_profile
from security.security_models import SecurityAuditSummary, build_security_audit_id
from security.secret_hygiene import build_secret_hygiene_report
from security.config_hardening import build_config_hardening_report
from security.safe_defaults import build_safe_defaults_report
from security.permission_boundaries import build_permission_boundary_report
from security.path_safety import build_path_safety_report
from security.log_redaction import build_log_redaction_report
from security.dependency_security import build_dependency_security_report
from security.file_permissions import build_file_permission_report
from security.token_scanner import TokenLeakScanner
from security.readiness_audit import build_production_readiness_audit
from security.security_quality import build_security_quality_report

class SecurityAuditPipeline:
    def __init__(self, data_lake: object, settings: object, profile: SecurityProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.profile = profile or get_default_security_profile()
        self.project_root = Path(__file__).parent.parent.resolve()

    def run_secret_hygiene_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_secret_hygiene_report(self.project_root, self.settings, self.profile)
        if save and hasattr(self.data_lake, "save_secret_hygiene_report"): self.data_lake.save_secret_hygiene_report(df, s)
        return df, s
    def run_config_hardening_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_config_hardening_report(self.settings, self.profile)
        if save and hasattr(self.data_lake, "save_config_hardening_report"): self.data_lake.save_config_hardening_report(df, s)
        return df, s
    def run_safe_defaults_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_safe_defaults_report(self.settings, self.profile)
        if save and hasattr(self.data_lake, "save_safe_defaults_report"): self.data_lake.save_safe_defaults_report(df, s)
        return df, s
    def run_permission_boundary_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_permission_boundary_report(self.project_root, self.settings, self.profile)
        if save and hasattr(self.data_lake, "save_permission_boundary_report"): self.data_lake.save_permission_boundary_report(df, s)
        return df, s
    def run_path_safety_check(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_path_safety_report(self.project_root, self.data_lake, self.profile)
        if save and hasattr(self.data_lake, "save_path_safety_report"): self.data_lake.save_path_safety_report(df, s)
        return df, s
    def run_token_leak_scan(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        scanner = TokenLeakScanner(self.profile)
        df, s = scanner.scan_directory(self.project_root)
        if save and hasattr(self.data_lake, "save_token_scan_report"): self.data_lake.save_token_scan_report(df, s)
        return df, s
    def run_readiness_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df, s = build_production_readiness_audit(pd.DataFrame(), {}, self.profile)
        if save and hasattr(self.data_lake, "save_readiness_audit"): self.data_lake.save_readiness_audit(df, s)
        return df, s
    def run_full_security_audit(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        all_dfs, all_summaries = [], {}

        df, s = self.run_secret_hygiene_check(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["secret_hygiene"] = s

        df, s = self.run_config_hardening_check(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["config_hardening"] = s

        df, s = self.run_safe_defaults_check(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["safe_defaults"] = s

        df, s = self.run_permission_boundary_check(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["permission_boundary"] = s

        df, s = self.run_path_safety_check(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["path_safety"] = s

        df, s = build_log_redaction_report(self.project_root, self.profile)
        if not df.empty: all_dfs.append(df)
        all_summaries["log_redaction"] = s

        df, s = build_dependency_security_report(self.project_root, self.profile)
        if not df.empty: all_dfs.append(df)
        all_summaries["dependency_security"] = s

        df, s = build_file_permission_report(self.project_root, self.project_root/"data/lake", self.project_root/"reports", self.profile)
        if not df.empty: all_dfs.append(df)
        all_summaries["file_permission"] = s

        df, s = self.run_token_leak_scan(save=False)
        if not df.empty: all_dfs.append(df)
        all_summaries["token_leak"] = s

        full_df = pd.concat(all_dfs, ignore_index=True) if all_dfs else pd.DataFrame(columns=["finding_id", "severity", "blocking"])
        r_df, r_s = build_production_readiness_audit(full_df, all_summaries, self.profile)
        all_summaries["readiness"] = r_s
        q_s = build_security_quality_report(full_df, all_summaries)

        summary = SecurityAuditSummary(
            audit_id=build_security_audit_id(self.profile.name), profile_name=self.profile.name,
            created_at_utc=datetime.now(timezone.utc).isoformat(), total_findings=len(full_df),
            critical_count=len(full_df[full_df["severity"] == "critical"]) if not full_df.empty else 0,
            high_count=0, medium_count=0, low_count=0,
            blocking_count=len(full_df[full_df["blocking"] == True]) if not full_df.empty else 0,
            security_status="security_passed", readiness_label=r_s["readiness_label"], readiness_score=r_s["readiness_score"],
            warnings=q_s.get("warnings", [])
        )

        sum_dict = {"audit_summary": summary.__dict__, "component_summaries": all_summaries, "quality": q_s}
        if save and hasattr(self.data_lake, "save_security_audit_report"):
             self.data_lake.save_security_audit_report(summary.audit_id, full_df, sum_dict)
             self.data_lake.save_readiness_audit(r_df, r_s)
             self.data_lake.save_security_quality(summary.audit_id, q_s)
        return full_df, sum_dict
