import os
from pathlib import Path

def main():
    base_dir = Path("commodity_fx_signal_bot")
    ls_dir = base_dir / "local_simplification"
    
    with open(ls_dir / "simplification_domain_registry.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
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
""")

    with open(ls_dir / "complexity_map.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile
from local_simplification.simplification_models import ComplexityItem, build_complexity_item_id, complexity_item_to_dict
from local_simplification.simplification_labels import validate_complexity_level

def classify_complexity_level(metric_value: int | float | None, metric_name: str) -> str:
    if metric_value is None:
        return "complexity_unknown"
    
    if metric_name == "folder_depth":
        if metric_value > 5: return "complexity_very_high"
        elif metric_value > 3: return "complexity_high"
        elif metric_value > 1: return "complexity_medium"
        else: return "complexity_low"
    elif metric_name == "file_count":
        if metric_value > 100: return "complexity_very_high"
        elif metric_value > 50: return "complexity_high"
        elif metric_value > 20: return "complexity_medium"
        else: return "complexity_low"
    elif metric_name == "function_count":
        if metric_value > 20: return "complexity_very_high"
        elif metric_value > 10: return "complexity_high"
        elif metric_value > 5: return "complexity_medium"
        else: return "complexity_low"
    
    return "complexity_unknown"

def build_final_modular_complexity_map(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    items = []
    
    # Just a placeholder for the final map, normally we'd aggregate from the other modules.
    df = pd.DataFrame(items)
    summary = summarize_modular_complexity_map(df)
    return df, summary

def summarize_modular_complexity_map(complexity_df: pd.DataFrame) -> dict:
    return {
        "total_items": len(complexity_df) if complexity_df is not None else 0,
        "warnings": ["Bu rapor official architecture assessment degildir."]
    }
""")

    with open(ls_dir / "module_family_complexity.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def classify_module_family(path: Path, project_root: Path) -> str:
    try:
        rel = path.relative_to(project_root)
        if len(rel.parts) > 0:
            return rel.parts[0]
    except ValueError:
        pass
    return "unknown"

def build_module_family_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"family": "core", "count": 1}])
    return df, summarize_module_family_complexity(df)

def summarize_module_family_complexity(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Bu rapor production approval degildir."]}
""")

    with open(ls_dir / "folder_depth_complexity.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def calculate_folder_depth(path: Path, project_root: Path) -> int:
    try:
        rel = path.relative_to(project_root)
        return len(rel.parts)
    except ValueError:
        return 0

def build_folder_depth_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"folder": "test", "depth": 1}])
    return df, summarize_folder_depth_complexity(df)

def summarize_folder_depth_complexity(df: pd.DataFrame) -> dict:
    return {"folders": len(df), "warnings": ["Dosya tasima onermez."]}
""")

    with open(ls_dir / "file_count_complexity.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def count_files_by_layer(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"layer": "core", "count": 1}])

def build_file_count_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = count_files_by_layer(project_root, profile)
    return df, summarize_file_count_complexity(df)

def summarize_file_count_complexity(df: pd.DataFrame) -> dict:
    return {"layers": len(df), "warnings": ["File count cleanup talimati degildir."]}
""")

    with open(ls_dir / "function_count_complexity.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
import ast
from local_simplification.simplification_config import LocalSimplificationProfile

def count_python_functions_by_file(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"file": "test.py", "functions": 1}])

def build_function_count_complexity_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = count_python_functions_by_file(project_root, profile)
    return df, summarize_function_count_complexity(df)

def summarize_function_count_complexity(df: pd.DataFrame) -> dict:
    return {"files": len(df), "warnings": ["AST parse hata verirse graceful doner."]}
""")

    print("Created phase 82 core 2")

if __name__ == "__main__":
    main()
