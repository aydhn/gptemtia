import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile
from local_simplification.simplification_models import SimplificationDomain, build_simplification_domain_id, simplification_domain_to_dict
from local_simplification.simplification_labels import validate_simplification_domain_label

def build_default_simplification_domains(profile: LocalSimplificationProfile) -> list[SimplificationDomain]:
    domains = [
        SimplificationDomain(
            domain_id=build_simplification_domain_id("complexity_map_domain"),
            domain_label="complexity_map_domain",
            domain_name="Final Modular Complexity Map",
            description="Offline/local modular complexity mapping (read-only).",
            required_reports=["final_modular_complexity_map.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("module_family_complexity_domain"),
            domain_label="module_family_complexity_domain",
            domain_name="Module Family Complexity",
            description="Module family complexity grouping.",
            required_reports=["module_family_complexity_report.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("sprawl_analysis_domain"),
            domain_label="sprawl_analysis_domain",
            domain_name="Sprawl Analysis",
            description="Sprawl analysis across layers.",
            required_reports=["script_sprawl_report.csv", "test_sprawl_report.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("optional_slimming_domain"),
            domain_label="optional_slimming_domain",
            domain_name="Optional Slimming Plan",
            description="Dry-run only slimming candidates.",
            required_reports=["optional_slimming_plan.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("consolidation_candidate_domain"),
            domain_label="consolidation_candidate_domain",
            domain_name="Consolidation Candidates",
            description="Safe and duplicate pattern consolidation candidates.",
            required_reports=["safe_consolidation_candidate_registry.csv", "duplicate_pattern_consolidation_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("naming_simplification_domain"),
            domain_label="naming_simplification_domain",
            domain_name="Naming Simplification",
            description="Naming convention simplifications.",
            required_reports=["naming_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("config_simplification_domain"),
            domain_label="config_simplification_domain",
            domain_name="Config Simplification",
            description="Config structure simplifications.",
            required_reports=["config_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("datalake_simplification_domain"),
            domain_label="datalake_simplification_domain",
            domain_name="DataLake Simplification",
            description="DataLake method simplifications.",
            required_reports=["datalake_method_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("script_cli_simplification_domain"),
            domain_label="script_cli_simplification_domain",
            domain_name="Script CLI Simplification",
            description="Script arguments and CLI simplifications.",
            required_reports=["script_cli_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("test_suite_simplification_domain"),
            domain_label="test_suite_simplification_domain",
            domain_name="Test Suite Simplification",
            description="Test suite and fixture simplifications.",
            required_reports=["test_suite_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("docs_navigation_domain"),
            domain_label="docs_navigation_domain",
            domain_name="Docs Navigation Simplification",
            description="Docs navigation structure simplifications.",
            required_reports=["docs_navigation_simplification_candidate_registry.csv"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("repo_ergonomics_domain"),
            domain_label="repo_ergonomics_domain",
            domain_name="Repo Ergonomics",
            description="Repo ergonomics guide and onboarding.",
            required_reports=["repo_ergonomics_rehearsal_guide.txt"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("maintainability_seed_domain"),
            domain_label="maintainability_seed_domain",
            domain_name="Maintainability Seed",
            description="Maintainability improvement seed for future rehearsal.",
            required_reports=["local_maintainability_improvement_seed.txt"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
        SimplificationDomain(
            domain_id=build_simplification_domain_id("quality_validation_domain"),
            domain_label="quality_validation_domain",
            domain_name="Quality & Validation",
            description="Simplification validation and quality scoring.",
            required_reports=["simplification_validation_report.csv", "simplification_quality_report.txt"],
            warnings=["Bu domain official architecture simplification scope degildir."]
        ),
    ]
    for d in domains:
        validate_simplification_domain_label(d.domain_label)
    return domains

def build_simplification_domain_registry(profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    domains = build_default_simplification_domains(profile)
    df = pd.DataFrame([simplification_domain_to_dict(d) for d in domains])
    summary = summarize_simplification_domains(df)
    return df, summary

def summarize_simplification_domains(domain_df: pd.DataFrame) -> dict:
    if domain_df is None or domain_df.empty:
        return {"total_domains": 0, "warnings": []}
    return {
        "total_domains": len(domain_df),
        "domains": domain_df["domain_label"].tolist(),
        "warnings": ["Bu registry official architecture simplification scope degildir."]
    }
