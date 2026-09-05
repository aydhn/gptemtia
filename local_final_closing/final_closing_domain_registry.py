import pandas as pd
from local_final_closing.final_closing_config import LocalFinalClosingProfile
from local_final_closing.final_closing_models import FinalClosingDomain, build_final_closing_domain_id, final_closing_domain_to_dict

def build_default_final_closing_domains(profile: LocalFinalClosingProfile) -> list[FinalClosingDomain]:
    return [
        FinalClosingDomain(
            domain_id=build_final_closing_domain_id("final_master_terminal_lock_domain"),
            domain_label="final_master_terminal_lock_domain",
            domain_name="Final Master Terminal Lock Rehearsal",
            description="Local/offline final master terminal lock rehearsal (NOT A REAL LOCK)",
            required_outputs=["final_master_terminal_lock_rehearsal"],
            warnings=["Domain registry official final closeout scope değildir.", "Local/offline/dry-run bağlamında açıklanmalı."]
        ),
        FinalClosingDomain(
            domain_id=build_final_closing_domain_id("project_constitution_domain"),
            domain_label="project_constitution_domain",
            domain_name="Ultimate Offline Project Constitution",
            description="Ultimate offline project constitution (NOT OFFICIAL CONSTITUTION)",
            required_outputs=["ultimate_offline_project_constitution"],
            warnings=["Domain registry official final closeout scope değildir.", "Local/offline/dry-run bağlamında açıklanmalı."]
        ),
        FinalClosingDomain(
            domain_id=build_final_closing_domain_id("non_production_seal_domain"),
            domain_label="non_production_seal_domain",
            domain_name="Final Non-Production Seal Rehearsal",
            description="Final non-production seal rehearsal (NOT OFFICIAL SEAL)",
            required_outputs=["final_non_production_seal_rehearsal"],
            warnings=["Domain registry official final closeout scope değildir.", "Local/offline/dry-run bağlamında açıklanmalı."]
        ),
        FinalClosingDomain(
            domain_id=build_final_closing_domain_id("terminal_archive_index_domain"),
            domain_label="terminal_archive_index_domain",
            domain_name="Local-Only Terminal Archive Index",
            description="Local-only terminal archive index (NOT A REAL ARCHIVE)",
            required_outputs=["local_only_terminal_archive_index"],
            warnings=["Domain registry official final closeout scope değildir.", "Local/offline/dry-run bağlamında açıklanmalı."]
        ),
        FinalClosingDomain(
            domain_id=build_final_closing_domain_id("closing_governance_super_binder_domain"),
            domain_label="closing_governance_super_binder_domain",
            domain_name="Closing Governance Super-Binder",
            description="Closing governance super-binder (NOT OFFICIAL ACCEPTANCE)",
            required_outputs=["closing_governance_super_binder"],
            warnings=["Domain registry official final closeout scope değildir.", "Local/offline/dry-run bağlamında açıklanmalı."]
        )
    ]

def summarize_final_closing_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0}
    return {
        "total_domains": len(domain_df)
    }

def build_final_closing_domain_registry(profile: LocalFinalClosingProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_final_closing_domains(profile)
    df = pd.DataFrame([final_closing_domain_to_dict(d) for d in domains])
    summary = summarize_final_closing_domains(df)
    return df, summary
