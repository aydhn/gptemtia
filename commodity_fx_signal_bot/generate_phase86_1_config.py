import os

def update_settings():
    path = "config/settings.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    redteam_fields = """
    # Phase 86 - Local RedTeam Settings
    local_redteam_enabled: bool = True
    default_local_redteam_profile: str = "balanced_local_redteam"
    local_redteam_default_language: str = "tr"
    local_redteam_dry_run_default: bool = True
    local_redteam_allow_real_attack: bool = False
    local_redteam_allow_jailbreak_generation: bool = False
    local_redteam_allow_exploit_generation: bool = False
    local_redteam_allow_prompt_injection_payloads: bool = False
    local_redteam_allow_credential_exfiltration: bool = False
    local_redteam_allow_live_security_testing: bool = False
    local_redteam_allow_telemetry: bool = False
    local_redteam_allow_dashboard_creation: bool = False
    local_redteam_allow_gui_creation: bool = False
    local_redteam_allow_tui_creation: bool = False
    local_redteam_allow_cloud_upload: bool = False
    local_redteam_allow_package_publish: bool = False
    local_redteam_allow_external_service: bool = False
    local_redteam_allow_external_llm: bool = False
    local_redteam_allow_file_modification: bool = False
    local_redteam_allow_file_deletion: bool = False
    local_redteam_allow_file_move: bool = False
    local_redteam_allow_overwrite: bool = False
    local_redteam_allow_safety_certification_claim: bool = False
    local_redteam_allow_compliance_signoff: bool = False
    local_redteam_allow_production_safety_approval_claim: bool = False
    local_redteam_allow_live_trading_claim: bool = False
    local_redteam_allow_broker_readiness_claim: bool = False
    local_redteam_allow_investment_advice: bool = False
    local_redteam_allow_model_deployment_claim: bool = False
    local_redteam_scan_docs: bool = True
    local_redteam_scan_reports: bool = True
    local_redteam_scan_data_lake: bool = True
    local_redteam_scan_scripts: bool = True
    local_redteam_scan_tests: bool = True
    local_redteam_scan_generated_docs: bool = True
    local_redteam_scan_governance_outputs: bool = True
    local_redteam_scan_usability_outputs: bool = True
    local_redteam_scan_safety_outputs: bool = True
    local_redteam_max_items: int = 500000
    local_redteam_max_scenarios: int = 10000
    local_redteam_min_readiness_score: float = 0.40
    local_redteam_min_quality_score: float = 0.40
    local_redteam_save_reports: bool = True
"""
    if "local_redteam_enabled" not in content:
        import re
        content = re.sub(r'(class Settings:.*?)(\n\s*def )', r'\1' + redteam_fields + r'\2', content, flags=re.DOTALL)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated settings.py")

def update_env_example():
    path = ".env.example"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "LOCAL_REDTEAM_ENABLED" not in content:
        content += """
LOCAL_REDTEAM_ENABLED=true
DEFAULT_LOCAL_REDTEAM_PROFILE=balanced_local_redteam
LOCAL_REDTEAM_DEFAULT_LANGUAGE=tr
LOCAL_REDTEAM_DRY_RUN_DEFAULT=true
LOCAL_REDTEAM_ALLOW_REAL_ATTACK=false
LOCAL_REDTEAM_ALLOW_JAILBREAK_GENERATION=false
LOCAL_REDTEAM_ALLOW_EXPLOIT_GENERATION=false
LOCAL_REDTEAM_ALLOW_PROMPT_INJECTION_PAYLOADS=false
LOCAL_REDTEAM_ALLOW_CREDENTIAL_EXFILTRATION=false
LOCAL_REDTEAM_ALLOW_LIVE_SECURITY_TESTING=false
LOCAL_REDTEAM_ALLOW_TELEMETRY=false
LOCAL_REDTEAM_ALLOW_DASHBOARD_CREATION=false
LOCAL_REDTEAM_ALLOW_GUI_CREATION=false
LOCAL_REDTEAM_ALLOW_TUI_CREATION=false
LOCAL_REDTEAM_ALLOW_CLOUD_UPLOAD=false
LOCAL_REDTEAM_ALLOW_PACKAGE_PUBLISH=false
LOCAL_REDTEAM_ALLOW_EXTERNAL_SERVICE=false
LOCAL_REDTEAM_ALLOW_EXTERNAL_LLM=false
LOCAL_REDTEAM_ALLOW_FILE_MODIFICATION=false
LOCAL_REDTEAM_ALLOW_FILE_DELETION=false
LOCAL_REDTEAM_ALLOW_FILE_MOVE=false
LOCAL_REDTEAM_ALLOW_OVERWRITE=false
LOCAL_REDTEAM_ALLOW_SAFETY_CERTIFICATION_CLAIM=false
LOCAL_REDTEAM_ALLOW_COMPLIANCE_SIGNOFF=false
LOCAL_REDTEAM_ALLOW_PRODUCTION_SAFETY_APPROVAL_CLAIM=false
LOCAL_REDTEAM_ALLOW_LIVE_TRADING_CLAIM=false
LOCAL_REDTEAM_ALLOW_BROKER_READINESS_CLAIM=false
LOCAL_REDTEAM_ALLOW_INVESTMENT_ADVICE=false
LOCAL_REDTEAM_ALLOW_MODEL_DEPLOYMENT_CLAIM=false
LOCAL_REDTEAM_SCAN_DOCS=true
LOCAL_REDTEAM_SCAN_REPORTS=true
LOCAL_REDTEAM_SCAN_DATA_LAKE=true
LOCAL_REDTEAM_SCAN_SCRIPTS=true
LOCAL_REDTEAM_SCAN_TESTS=true
LOCAL_REDTEAM_SCAN_GENERATED_DOCS=true
LOCAL_REDTEAM_SCAN_GOVERNANCE_OUTPUTS=true
LOCAL_REDTEAM_SCAN_USABILITY_OUTPUTS=true
LOCAL_REDTEAM_SCAN_SAFETY_OUTPUTS=true
LOCAL_REDTEAM_MAX_ITEMS=500000
LOCAL_REDTEAM_MAX_SCENARIOS=10000
LOCAL_REDTEAM_MIN_READINESS_SCORE=0.40
LOCAL_REDTEAM_MIN_QUALITY_SCORE=0.40
LOCAL_REDTEAM_SAVE_REPORTS=true
"""
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated .env.example")

def update_paths():
    path = "config/paths.py"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    redteam_paths = """
    LAKE_LOCAL_REDTEAM = DATA_LAKE_DIR / "local_redteam"
    LAKE_LOCAL_REDTEAM_PROFILES = LAKE_LOCAL_REDTEAM / "profiles"
    LAKE_LOCAL_REDTEAM_DOMAINS = LAKE_LOCAL_REDTEAM / "domains"
    LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET = LAKE_LOCAL_REDTEAM / "rehearsal_packet"
    LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS = LAKE_LOCAL_REDTEAM / "misuse_scenarios"
    LAKE_LOCAL_REDTEAM_ABUSE_CASES = LAKE_LOCAL_REDTEAM / "abuse_cases"
    LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST = LAKE_LOCAL_REDTEAM / "adversarial_checklist"
    LAKE_LOCAL_REDTEAM_PROMPT_INJECTION = LAKE_LOCAL_REDTEAM / "prompt_injection"
    LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS = LAKE_LOCAL_REDTEAM / "unsafe_outputs"
    LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES = LAKE_LOCAL_REDTEAM / "forbidden_capabilities"
    LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS = LAKE_LOCAL_REDTEAM / "boundary_violations"
    LAKE_LOCAL_REDTEAM_LIVE_TRADING = LAKE_LOCAL_REDTEAM / "live_trading"
    LAKE_LOCAL_REDTEAM_BROKER_EXECUTION = LAKE_LOCAL_REDTEAM / "broker_execution"
    LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE = LAKE_LOCAL_REDTEAM / "investment_advice"
    LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT = LAKE_LOCAL_REDTEAM / "model_deployment"
    LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE = LAKE_LOCAL_REDTEAM / "secret_exposure"
    LAKE_LOCAL_REDTEAM_FILE_ACTIONS = LAKE_LOCAL_REDTEAM / "file_actions"
    LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH = LAKE_LOCAL_REDTEAM / "cloud_publish"
    LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API = LAKE_LOCAL_REDTEAM / "external_llm_api"
    LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES = LAKE_LOCAL_REDTEAM / "safety_responses"
    LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION = LAKE_LOCAL_REDTEAM / "manual_escalation"
    LAKE_LOCAL_REDTEAM_HUMAN_REVIEW = LAKE_LOCAL_REDTEAM / "human_review"
    LAKE_LOCAL_REDTEAM_READING_ORDER = LAKE_LOCAL_REDTEAM / "reading_order"
    LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE = LAKE_LOCAL_REDTEAM / "safety_assurance"
    LAKE_LOCAL_REDTEAM_COVERAGE = LAKE_LOCAL_REDTEAM / "coverage"
    LAKE_LOCAL_REDTEAM_BLINDSPOTS = LAKE_LOCAL_REDTEAM / "blindspots"
    LAKE_LOCAL_REDTEAM_NON_GOALS = LAKE_LOCAL_REDTEAM / "non_goals"
    LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO = LAKE_LOCAL_REDTEAM / "no_go_safe_go"
    LAKE_LOCAL_REDTEAM_EXCEPTIONS = LAKE_LOCAL_REDTEAM / "exceptions"
    LAKE_LOCAL_REDTEAM_GAPS = LAKE_LOCAL_REDTEAM / "gaps"
    LAKE_LOCAL_REDTEAM_RISKS = LAKE_LOCAL_REDTEAM / "risks"
    LAKE_LOCAL_REDTEAM_SCORING = LAKE_LOCAL_REDTEAM / "scoring"
    LAKE_LOCAL_REDTEAM_VALIDATION = LAKE_LOCAL_REDTEAM / "validation"
    LAKE_LOCAL_REDTEAM_QUALITY = LAKE_LOCAL_REDTEAM / "quality"
    
    REPORT_OUTPUT_LOCAL_REDTEAM = REPORTS_OUTPUT_DIR / "local_redteam"
    REPORT_OUTPUT_LOCAL_REDTEAM_CSV = REPORT_OUTPUT_LOCAL_REDTEAM / "csv"
    REPORT_OUTPUT_LOCAL_REDTEAM_MARKDOWN = REPORT_OUTPUT_LOCAL_REDTEAM / "markdown"
    REPORT_OUTPUT_LOCAL_REDTEAM_TXT = REPORT_OUTPUT_LOCAL_REDTEAM / "txt"
    REPORT_OUTPUT_LOCAL_REDTEAM_JSON = REPORT_OUTPUT_LOCAL_REDTEAM / "json"
    
    DOCS_GENERATED_LOCAL_REDTEAM = DOCS_DIR / "generated" / "local_redteam"
"""
    if "LAKE_LOCAL_REDTEAM" not in content:
        import re
        content = re.sub(r'(class ProjectPaths:.*?)(\n\s*@classmethod)', r'\1' + redteam_paths + r'\2', content, flags=re.DOTALL)
        
        dir_list_str = ",\n            cls.LAKE_LOCAL_REDTEAM,\n            cls.LAKE_LOCAL_REDTEAM_PROFILES,\n            cls.LAKE_LOCAL_REDTEAM_DOMAINS,\n            cls.LAKE_LOCAL_REDTEAM_REHEARSAL_PACKET,\n            cls.LAKE_LOCAL_REDTEAM_MISUSE_SCENARIOS,\n            cls.LAKE_LOCAL_REDTEAM_ABUSE_CASES,\n            cls.LAKE_LOCAL_REDTEAM_ADVERSARIAL_CHECKLIST,\n            cls.LAKE_LOCAL_REDTEAM_PROMPT_INJECTION,\n            cls.LAKE_LOCAL_REDTEAM_UNSAFE_OUTPUTS,\n            cls.LAKE_LOCAL_REDTEAM_FORBIDDEN_CAPABILITIES,\n            cls.LAKE_LOCAL_REDTEAM_BOUNDARY_VIOLATIONS,\n            cls.LAKE_LOCAL_REDTEAM_LIVE_TRADING,\n            cls.LAKE_LOCAL_REDTEAM_BROKER_EXECUTION,\n            cls.LAKE_LOCAL_REDTEAM_INVESTMENT_ADVICE,\n            cls.LAKE_LOCAL_REDTEAM_MODEL_DEPLOYMENT,\n            cls.LAKE_LOCAL_REDTEAM_SECRET_EXPOSURE,\n            cls.LAKE_LOCAL_REDTEAM_FILE_ACTIONS,\n            cls.LAKE_LOCAL_REDTEAM_CLOUD_PUBLISH,\n            cls.LAKE_LOCAL_REDTEAM_EXTERNAL_LLM_API,\n            cls.LAKE_LOCAL_REDTEAM_SAFETY_RESPONSES,\n            cls.LAKE_LOCAL_REDTEAM_MANUAL_ESCALATION,\n            cls.LAKE_LOCAL_REDTEAM_HUMAN_REVIEW,\n            cls.LAKE_LOCAL_REDTEAM_READING_ORDER,\n            cls.LAKE_LOCAL_REDTEAM_SAFETY_ASSURANCE,\n            cls.LAKE_LOCAL_REDTEAM_COVERAGE,\n            cls.LAKE_LOCAL_REDTEAM_BLINDSPOTS,\n            cls.LAKE_LOCAL_REDTEAM_NON_GOALS,\n            cls.LAKE_LOCAL_REDTEAM_NO_GO_SAFE_GO,\n            cls.LAKE_LOCAL_REDTEAM_EXCEPTIONS,\n            cls.LAKE_LOCAL_REDTEAM_GAPS,\n            cls.LAKE_LOCAL_REDTEAM_RISKS,\n            cls.LAKE_LOCAL_REDTEAM_SCORING,\n            cls.LAKE_LOCAL_REDTEAM_VALIDATION,\n            cls.LAKE_LOCAL_REDTEAM_QUALITY,\n            cls.REPORT_OUTPUT_LOCAL_REDTEAM,\n            cls.REPORT_OUTPUT_LOCAL_REDTEAM_CSV,\n            cls.REPORT_OUTPUT_LOCAL_REDTEAM_MARKDOWN,\n            cls.REPORT_OUTPUT_LOCAL_REDTEAM_TXT,\n            cls.REPORT_OUTPUT_LOCAL_REDTEAM_JSON,\n            cls.DOCS_GENERATED_LOCAL_REDTEAM\n        ]"
        
        content = re.sub(r'(\s*cls\.DOCS_GENERATED_LOCAL_USABILITY\s*\])', dir_list_str.replace("LOCAL_USABILITY", "LOCAL_GOVERNANCE_CONTROL"), content)
        # Instead of regex that might fail on directory structure, let's just append to the return list directly via string replace
        content = content.replace("cls.DOCS_GENERATED_LOCAL_USABILITY\n        ]", "cls.DOCS_GENERATED_LOCAL_USABILITY" + dir_list_str)
        content = content.replace("cls.DOCS_GENERATED_LOCAL_GOVERNANCE_CONTROL\n        ]", "cls.DOCS_GENERATED_LOCAL_GOVERNANCE_CONTROL" + dir_list_str)
        content = content.replace("cls.DOCS_GENERATED_LOCAL_ACCEPTANCE\n        ]", "cls.DOCS_GENERATED_LOCAL_ACCEPTANCE" + dir_list_str)
        
        # If it doesn't match above, use regex on return list
        content = re.sub(r'(return\s*\[[^]]+)(\n\s*\])', r'\1' + dir_list_str.replace("]", "") + r'\2', content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated paths.py")

if __name__ == "__main__":
    update_settings()
    update_env_example()
    update_paths()
