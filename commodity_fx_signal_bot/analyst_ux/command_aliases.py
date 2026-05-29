import pandas as pd
from .ux_config import AnalystUXProfile
from .ux_models import CommandAlias, build_command_alias_id
from .ux_labels import validate_alias_type, validate_suggestion_safety

def _create_alias(alias_name: str, alias_type: str, command: str, desc: str, module: str, safety: str, queries: list) -> CommandAlias:
    validate_alias_type(alias_type)
    validate_suggestion_safety(safety)
    return CommandAlias(
        alias_id=build_command_alias_id(alias_name, module),
        alias_name=alias_name,
        alias_type=alias_type,
        command=command,
        description=desc,
        module_name=module,
        safety_label=safety,
        example_queries=queries,
        warnings=[]
    )

def build_status_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("status:final", "status_alias", "python -m scripts.run_final_review_status", "Check final review status", "final_review", "safe_offline_suggestion", ["final review durumunu kontrol et"]),
        _create_alias("status:quality", "status_alias", "python -m scripts.run_release_quality_gate_status", "Check quality gate status", "quality_gates", "safe_offline_suggestion", ["quality gate hatalarını görmek istiyorum"]),
        _create_alias("status:scenario", "status_alias", "python -m scripts.run_scenario_status", "Check scenario status", "scenarios", "safe_offline_suggestion", ["scenario durumunu getir"]),
        _create_alias("status:regression", "status_alias", "python -m scripts.run_scenario_regression_status", "Check regression status", "scenario_regression", "safe_offline_suggestion", ["regression durumu nedir"])
    ]

def build_report_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("report:final", "report_alias", "python -m scripts.run_final_system_review", "Generate final system review", "final_review", "safe_offline_suggestion", ["final system review üret"]),
        _create_alias("report:safety", "report_alias", "python -m scripts.run_safety_audit", "Generate safety audit", "final_review", "safe_offline_suggestion", ["safety audit raporu ver"]),
        _create_alias("report:quality", "report_alias", "python -m scripts.run_local_ci_validation", "Generate local CI validation", "quality_gates", "safe_offline_suggestion", ["lokal CI çalıştır"]),
        _create_alias("report:maintenance", "report_alias", "python -m scripts.run_storage_lifecycle_report", "Generate storage lifecycle report", "maintenance", "safe_offline_suggestion", ["bakım raporu"]),
        _create_alias("report:performance", "report_alias", "python -m scripts.run_performance_profile_report", "Generate performance profile", "performance", "safe_offline_suggestion", ["performans raporu üret"])
    ]

def build_query_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("query:knowledge", "query_alias", "python -m scripts.run_research_query --query \"<query>\"", "Query knowledge base", "knowledge_base", "safe_offline_suggestion", ["<query> hakkında ne biliyoruz"])
    ]

def build_scenario_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("demo:scenario", "scenario_alias", "python -m scripts.run_end_to_end_demo_report", "Run end to end demo", "scenarios", "safe_offline_suggestion", ["demo çalıştır"]),
        _create_alias("regression:demo", "scenario_alias", "python -m scripts.run_demo_acceptance_report", "Run demo acceptance", "scenario_regression", "safe_offline_suggestion", ["regression demo çalıştır"])
    ]

def build_quality_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("quality:check", "quality_alias", "python -m scripts.run_static_safety_scan", "Run safety scan", "quality_gates", "safe_offline_suggestion", ["güvenlik taraması yap"])
    ]

def build_maintenance_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("maintenance:dry_run", "maintenance_alias", "python -m scripts.run_cleanup_dry_run_report", "Run cleanup dry run", "maintenance", "safe_offline_suggestion", ["temizlik raporu"])
    ]

def build_documentation_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    if not profile.generate_aliases: return []
    return [
        _create_alias("docs:pack", "documentation_alias", "python -m scripts.run_documentation_pack_report", "Run documentation pack", "documentation", "safe_offline_suggestion", ["döküman paketi oluştur"])
    ]

def build_default_command_aliases(profile: AnalystUXProfile) -> list[CommandAlias]:
    aliases = []
    aliases.extend(build_status_aliases(profile))
    aliases.extend(build_report_aliases(profile))
    aliases.extend(build_query_aliases(profile))
    aliases.extend(build_scenario_aliases(profile))
    aliases.extend(build_quality_aliases(profile))
    aliases.extend(build_maintenance_aliases(profile))
    aliases.extend(build_documentation_aliases(profile))
    return aliases

def command_aliases_to_dataframe(aliases: list[CommandAlias]) -> pd.DataFrame:
    if not aliases: return pd.DataFrame()
    return pd.DataFrame([a.__dict__ for a in aliases])

def validate_command_aliases(aliases: list[CommandAlias]) -> dict:
    valid_count = 0
    blocked_count = 0
    for alias in aliases:
        if "live" in alias.command or "broker" in alias.command or "deploy" in alias.command or "daemon" in alias.command:
            blocked_count += 1
        else:
            valid_count += 1
    return {"valid_count": valid_count, "blocked_count": blocked_count, "passed": blocked_count == 0}
