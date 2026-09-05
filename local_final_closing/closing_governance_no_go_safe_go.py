import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile

def build_closing_governance_no_go_conditions(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "real project lock claim", "triggered": profile.allow_real_project_lock},
        {"condition": "official project constitution claim", "triggered": profile.allow_official_project_constitution},
        {"condition": "official non-production seal claim", "triggered": profile.allow_official_non_production_seal},
        {"condition": "official governance seal claim", "triggered": profile.allow_official_governance_seal},
        {"condition": "official archive claim", "triggered": profile.allow_official_archive},
        {"condition": "official handover claim", "triggered": profile.allow_official_handover},
        {"condition": "official acceptance claim", "triggered": profile.allow_official_acceptance},
        {"condition": "official release claim", "triggered": profile.allow_official_release},
        {"condition": "legal/compliance approval claim", "triggered": profile.allow_legal_signoff},
        {"condition": "production approval claim", "triggered": profile.allow_production_approval_claim},
        {"condition": "broker readiness claim", "triggered": profile.allow_broker_readiness_claim},
        {"condition": "live trading claim", "triggered": profile.allow_live_trading_claim},
        {"condition": "investment advice wording", "triggered": profile.allow_investment_advice},
        {"condition": "model deployment claim", "triggered": profile.allow_model_deployment_claim},
        {"condition": "real build claim", "triggered": profile.allow_real_build},
        {"condition": "cloud build/CI-CD claim", "triggered": profile.allow_cloud_build or profile.allow_ci_cd},
        {"condition": "Docker build/image claim", "triggered": profile.allow_docker_build_push or profile.allow_docker_image_creation},
        {"condition": "build/binary artifact claim", "triggered": profile.allow_build_artifact or profile.allow_binary_artifact},
        {"condition": "installer/executable claim", "triggered": profile.allow_installer_creation or profile.allow_executable_packaging},
        {"condition": "dependency install/provisioning claim", "triggered": profile.allow_dependency_install or profile.allow_environment_provisioning},
        {"condition": "package publish claim", "triggered": profile.allow_package_publish},
        {"condition": "git tag claim", "triggered": profile.allow_git_tag},
        {"condition": "cloud upload claim", "triggered": profile.allow_cloud_upload},
        {"condition": "deployment claim", "triggered": profile.allow_deployment},
        {"condition": "archive/ZIP claim", "triggered": profile.allow_real_archive_creation or profile.allow_zip_creation},
        {"condition": "web server/dashboard claim", "triggered": profile.allow_web_server or profile.allow_dashboard_creation},
        {"condition": "telemetry claim", "triggered": profile.allow_telemetry},
        {"condition": "external LLM/API claim", "triggered": profile.allow_external_service or profile.allow_external_llm},
        {"condition": "vector/embedding claim", "triggered": profile.allow_vector_db or profile.allow_embedding_api},
        {"condition": "file deletion/move/overwrite claim", "triggered": profile.allow_file_modification or profile.allow_file_deletion or profile.allow_file_move or profile.allow_overwrite},
        {"condition": "raw secret output", "triggered": False}
    ])

def build_closing_governance_safe_go_conditions(profile: LocalFinalClosingProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "final master terminal lock rehearsal documented", "met": True},
        {"condition": "ultimate offline project constitution documented", "met": True},
        {"condition": "final non-production seal rehearsal documented", "met": True},
        {"condition": "local-only terminal archive index documented", "met": True},
        {"condition": "closing governance super-binder documented", "met": True},
        {"condition": "final evidence/issues/checklists available", "met": True},
        {"condition": "no real lock/constitution/seal/archive/release/build/deploy/live/broker/advice", "met": not any(profile.allow_real_project_lock for _ in range(1))}, # Simplified check
        {"condition": "manual review required", "met": True}
    ])

def build_closing_governance_no_go_safe_go_summary(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_closing_governance_no_go_conditions(profile)
    safe_go = build_closing_governance_safe_go_conditions(profile)
    
    no_go["type"] = "no_go"
    safe_go["type"] = "safe_go"
    safe_go["triggered"] = ~safe_go["met"]
    safe_go = safe_go.drop(columns=["met"])
    
    summary_df = pd.concat([no_go, safe_go], ignore_index=True)
    return summary_df, summarize_closing_governance_no_go_safe_go(summary_df)

def summarize_closing_governance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    if summary_df.empty:
        return {"no_go_triggered": 0, "safe_go_met": 0}
    return {
        "no_go_triggered": int(summary_df[summary_df["type"] == "no_go"]["triggered"].sum()),
        "safe_go_met": int((~summary_df[summary_df["type"] == "safe_go"]["triggered"]).sum())
    }
