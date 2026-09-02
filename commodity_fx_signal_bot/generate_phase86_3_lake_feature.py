import os
import re

def update_data_lake():
    path = "data/storage/data_lake.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    methods = """
    # Phase 86: Local RedTeam Methods
    def save_redteam_profile_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_PROFILES / "redteam_profile_registry.csv", summary)

    def load_redteam_profile_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_PROFILES / "redteam_profile_registry.csv")

    def save_redteam_domain_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_DOMAINS / "redteam_domain_registry.csv", summary)

    def load_redteam_domain_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_DOMAINS / "redteam_domain_registry.csv")

    def save_final_local_redteam_rehearsal_packet(self, text: str, summary: dict | None = None) -> Path:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET / "final_local_redteam_rehearsal_packet.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            self._save_summary(path, summary)
        return path

    def load_final_local_redteam_rehearsal_packet(self) -> str:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET / "final_local_redteam_rehearsal_packet.txt"
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def save_misuse_scenario_library(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS / "misuse_scenario_library.csv", summary)

    def load_misuse_scenario_library(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS / "misuse_scenario_library.csv")

    def save_abuse_case_simulation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_ABUSE_CASES / "abuse_case_simulation_registry.csv", summary)

    def load_abuse_case_simulation_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_ABUSE_CASES / "abuse_case_simulation_registry.csv")

    def save_adversarial_prompt_safety_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST / "adversarial_prompt_safety_checklist.csv", summary)

    def load_adversarial_prompt_safety_checklist(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST / "adversarial_prompt_safety_checklist.csv")

    def save_prompt_injection_risk_pattern_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_PROMPT_INJECTION / "prompt_injection_risk_pattern_registry.csv", summary)

    def load_prompt_injection_risk_pattern_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_PROMPT_INJECTION / "prompt_injection_risk_pattern_registry.csv")

    def save_unsafe_output_pattern_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS / "unsafe_output_pattern_registry.csv", summary)

    def load_unsafe_output_pattern_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS / "unsafe_output_pattern_registry.csv")

    def save_forbidden_capability_request_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES / "forbidden_capability_request_registry.csv", summary)

    def load_forbidden_capability_request_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES / "forbidden_capability_request_registry.csv")

    def save_boundary_violation_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS / "boundary_violation_scenario_registry.csv", summary)

    def load_boundary_violation_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS / "boundary_violation_scenario_registry.csv")

    def save_live_trading_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_LIVE_TRADING / "live_trading_misuse_scenario_registry.csv", summary)

    def load_live_trading_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_LIVE_TRADING / "live_trading_misuse_scenario_registry.csv")

    def save_broker_execution_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_BROKER_EXECUTION / "broker_execution_misuse_scenario_registry.csv", summary)

    def load_broker_execution_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_BROKER_EXECUTION / "broker_execution_misuse_scenario_registry.csv")

    def save_investment_advice_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE / "investment_advice_misuse_scenario_registry.csv", summary)

    def load_investment_advice_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE / "investment_advice_misuse_scenario_registry.csv")

    def save_model_deployment_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT / "model_deployment_misuse_scenario_registry.csv", summary)

    def load_model_deployment_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT / "model_deployment_misuse_scenario_registry.csv")

    def save_secret_exposure_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE / "secret_exposure_misuse_scenario_registry.csv", summary)

    def load_secret_exposure_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE / "secret_exposure_misuse_scenario_registry.csv")

    def save_file_action_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_FILE_ACTIONS / "file_action_misuse_scenario_registry.csv", summary)

    def load_file_action_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_FILE_ACTIONS / "file_action_misuse_scenario_registry.csv")

    def save_cloud_publish_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH / "cloud_publish_misuse_scenario_registry.csv", summary)

    def load_cloud_publish_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH / "cloud_publish_misuse_scenario_registry.csv")

    def save_external_llm_api_misuse_scenario_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API / "external_llm_api_misuse_scenario_registry.csv", summary)

    def load_external_llm_api_misuse_scenario_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API / "external_llm_api_misuse_scenario_registry.csv")

    def save_safety_response_expectation_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safety_response_expectation_registry.csv", summary)

    def load_safety_response_expectation_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safety_response_expectation_registry.csv")

    def save_safe_refusal_template_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_refusal_template_registry.csv", summary)

    def load_safe_refusal_template_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_refusal_template_registry.csv")

    def save_safe_redirect_pattern_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_redirect_pattern_registry.csv", summary)

    def load_safe_redirect_pattern_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES / "safe_redirect_pattern_registry.csv")

    def save_manual_escalation_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION / "manual_escalation_checklist.csv", summary)

    def load_manual_escalation_checklist(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION / "manual_escalation_checklist.csv")

    def save_human_review_abuse_case_checklist(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_HUMAN_REVIEW / "human_review_abuse_case_checklist.csv", summary)

    def load_human_review_abuse_case_checklist(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_HUMAN_REVIEW / "human_review_abuse_case_checklist.csv")

    def save_redteam_reading_order(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_READING_ORDER / "redteam_reading_order.csv", summary)

    def load_redteam_reading_order(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_READING_ORDER / "redteam_reading_order.csv")

    def save_safety_assurance_summary(self, text: str, summary: dict | None = None) -> Path:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_summary.txt"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        if summary:
            self._save_summary(path, summary)
        return path

    def load_safety_assurance_summary(self) -> str:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_summary.txt"
        if not path.exists():
            return ""
        return path.read_text(encoding="utf-8")

    def save_safety_assurance_evidence_index(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_evidence_index.csv", summary)

    def load_safety_assurance_evidence_index(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE / "safety_assurance_evidence_index.csv")

    def save_safety_coverage_matrix(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_COVERAGE / "safety_coverage_matrix.csv", summary)

    def load_safety_coverage_matrix(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_COVERAGE / "safety_coverage_matrix.csv")

    def save_safety_blindspot_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_BLINDSPOTS / "safety_blindspot_register.csv", summary)

    def load_safety_blindspot_register(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_BLINDSPOTS / "safety_blindspot_register.csv")

    def save_safety_non_goals_registry(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_NON_GOALS / "safety_non_goals_registry.csv", summary)

    def load_safety_non_goals_registry(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_NON_GOALS / "safety_non_goals_registry.csv")

    def save_redteam_no_go_safe_go_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO / "redteam_no_go_safe_go_summary.csv", summary)

    def load_redteam_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO / "redteam_no_go_safe_go_summary.csv")

    def save_redteam_exception_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_EXCEPTIONS / "redteam_exception_register.csv", summary)

    def load_redteam_exception_register(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_EXCEPTIONS / "redteam_exception_register.csv")

    def save_redteam_gap_register(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_GAPS / "redteam_gap_register.csv", summary)

    def load_redteam_gap_register(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_GAPS / "redteam_gap_register.csv")

    def save_redteam_risk_summary(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_RISKS / "redteam_risk_summary.csv", summary)

    def load_redteam_risk_summary(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_RISKS / "redteam_risk_summary.csv")

    def save_redteam_readiness_score_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_SCORING / "redteam_readiness_score_report.csv", summary)

    def load_redteam_readiness_score_report(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_SCORING / "redteam_readiness_score_report.csv")

    def save_redteam_validation_report(self, df: pd.DataFrame, summary: dict | None = None) -> Path:
        return self._save_artifact(df, ProjectPaths.LAKE_LOCAL_REDTEAM_VALIDATION / "redteam_validation_report.csv", summary)

    def load_redteam_validation_report(self) -> pd.DataFrame:
        return self._load_artifact(ProjectPaths.LAKE_LOCAL_REDTEAM_VALIDATION / "redteam_validation_report.csv")

    def save_redteam_quality(self, profile_name: str, quality: dict) -> Path:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_QUALITY / f"{profile_name}_quality.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(quality, f, indent=4, ensure_ascii=False)
        return path

    def load_redteam_quality(self, profile_name: str) -> dict:
        path = ProjectPaths.LAKE_LOCAL_REDTEAM_QUALITY / f"{profile_name}_quality.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_local_redteam_report(self, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        path = ProjectPaths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON / f"{profile_name}_redteam_report.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        import json
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        if markdown:
            md_path = ProjectPaths.REPORT_OUTPUT_LOCAL_REDTEAM_MARKDOWN / f"{profile_name}_redteam_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)
        return path

    def load_local_redteam_report(self, profile_name: str) -> dict:
        path = ProjectPaths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON / f"{profile_name}_redteam_report.json"
        if not path.exists():
            return {}
        import json
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def list_local_redteam_reports(self) -> pd.DataFrame:
        reports = []
        path = ProjectPaths.REPORT_OUTPUT_LOCAL_REDTEAM_JSON
        if path.exists():
            for file in path.glob("*_redteam_report.json"):
                reports.append({"report": file.name})
        import pandas as pd
        return pd.DataFrame(reports)
"""
    if "save_redteam_profile_registry" not in content:
        content = re.sub(r'(\n\s*def _load_metadata.*)', methods + r'\1', content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated data_lake.py")

def update_feature_store():
    path = "ml/feature_store.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    methods = """
    # Phase 86: Local RedTeam Methods
    def load_redteam_profile_registry(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_profile_registry()

    def load_redteam_domain_registry(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_domain_registry()

    def load_final_local_redteam_rehearsal_packet(self) -> str:
        return self.data_lake.load_final_local_redteam_rehearsal_packet()

    def load_misuse_scenario_library(self) -> pd.DataFrame:
        return self.data_lake.load_misuse_scenario_library()

    def load_abuse_case_simulation_registry(self) -> pd.DataFrame:
        return self.data_lake.load_abuse_case_simulation_registry()

    def load_adversarial_prompt_safety_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_adversarial_prompt_safety_checklist()

    def load_prompt_injection_risk_pattern_registry(self) -> pd.DataFrame:
        return self.data_lake.load_prompt_injection_risk_pattern_registry()

    def load_unsafe_output_pattern_registry(self) -> pd.DataFrame:
        return self.data_lake.load_unsafe_output_pattern_registry()

    def load_forbidden_capability_request_registry(self) -> pd.DataFrame:
        return self.data_lake.load_forbidden_capability_request_registry()

    def load_boundary_violation_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_boundary_violation_scenario_registry()

    def load_live_trading_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_live_trading_misuse_scenario_registry()

    def load_broker_execution_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_broker_execution_misuse_scenario_registry()

    def load_investment_advice_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_investment_advice_misuse_scenario_registry()

    def load_model_deployment_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_model_deployment_misuse_scenario_registry()

    def load_secret_exposure_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_secret_exposure_misuse_scenario_registry()

    def load_file_action_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_file_action_misuse_scenario_registry()

    def load_cloud_publish_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_cloud_publish_misuse_scenario_registry()

    def load_external_llm_api_misuse_scenario_registry(self) -> pd.DataFrame:
        return self.data_lake.load_external_llm_api_misuse_scenario_registry()

    def load_safety_response_expectation_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safety_response_expectation_registry()

    def load_safe_refusal_template_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safe_refusal_template_registry()

    def load_safe_redirect_pattern_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safe_redirect_pattern_registry()

    def load_manual_escalation_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_manual_escalation_checklist()

    def load_human_review_abuse_case_checklist(self) -> pd.DataFrame:
        return self.data_lake.load_human_review_abuse_case_checklist()

    def load_redteam_reading_order(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_reading_order()

    def load_safety_assurance_summary(self) -> str:
        return self.data_lake.load_safety_assurance_summary()

    def load_safety_assurance_evidence_index(self) -> pd.DataFrame:
        return self.data_lake.load_safety_assurance_evidence_index()

    def load_safety_coverage_matrix(self) -> pd.DataFrame:
        return self.data_lake.load_safety_coverage_matrix()

    def load_safety_blindspot_register(self) -> pd.DataFrame:
        return self.data_lake.load_safety_blindspot_register()

    def load_safety_non_goals_registry(self) -> pd.DataFrame:
        return self.data_lake.load_safety_non_goals_registry()

    def load_redteam_no_go_safe_go_summary(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_no_go_safe_go_summary()

    def load_redteam_exception_register(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_exception_register()

    def load_redteam_gap_register(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_gap_register()

    def load_redteam_risk_summary(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_risk_summary()

    def load_redteam_readiness_score_report(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_readiness_score_report()

    def load_redteam_validation_report(self) -> pd.DataFrame:
        return self.data_lake.load_redteam_validation_report()

    def load_redteam_quality(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_redteam_quality(profile_name or "balanced_local_redteam")

    def load_local_redteam_report(self, profile_name: str | None = None) -> dict:
        return self.data_lake.load_local_redteam_report(profile_name or "balanced_local_redteam")

    def list_available_local_redteam_reports(self) -> dict:
        df = self.data_lake.list_local_redteam_reports()
        return df.to_dict(orient="records") if not df.empty else {}
"""
    if "load_redteam_profile_registry" not in content:
        # Append to FeatureStore class
        content += methods
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated feature_store.py")

def update_report_builder():
    path = "reports/report_builder.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    methods = """
    # Phase 86: Local RedTeam Reports
    def build_redteam_domain_registry_text_report(self, summary: dict, domain_df: pd.DataFrame | None = None) -> str:
        report = "LOCAL REDTEAM DOMAIN REGISTRY REPORT\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_redteam_rehearsal_packet_text_report(self, summary: dict, packet_text: str | None = None) -> str:
        report = "FINAL LOCAL REDTEAM REHEARSAL PACKET\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        if packet_text:
            report += packet_text + "\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_misuse_scenario_library_text_report(self, summary: dict, scenario_df: pd.DataFrame | None = None) -> str:
        report = "MISUSE SCENARIO LIBRARY\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_adversarial_prompt_checklist_text_report(self, summary: dict, check_df: pd.DataFrame | None = None) -> str:
        report = "ADVERSARIAL PROMPT SAFETY CHECKLIST\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_safety_assurance_text_report(self, summary: dict, assurance_text: str | None = None) -> str:
        report = "SAFETY ASSURANCE SUMMARY\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_redteam_quality_text_report(self, summary: dict, quality: dict | None = None) -> str:
        report = "REDTEAM QUALITY REPORT\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report

    def build_redteam_status_report(self, status_df: pd.DataFrame, summary: dict) -> str:
        report = "REDTEAM STATUS REPORT\\n"
        report += "="*40 + "\\n\\n"
        report += "Bu çıktı offline/local red-team rehearsal ve safety assurance raporudur. Gerçek adversarial attack, jailbreak, exploit, credential exfiltration, production safety approval, canlı emir, broker talimatı, model deployment veya yatırım tavsiyesi değildir.\\n\\n"
        for k, v in summary.items():
            report += f"{k}: {v}\\n"
        return report
"""
    if "build_redteam_domain_registry_text_report" not in content:
        content += methods
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated report_builder.py")

if __name__ == "__main__":
    update_data_lake()
    update_feature_store()
    update_report_builder()
