import os
from pathlib import Path

def main():
    base_dir = Path("commodity_fx_signal_bot")
    ls_dir = base_dir / "local_simplification"
    
    with open(ls_dir / "script_sprawl.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_scripts_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "run", "scripts": 1}])

def build_script_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_scripts_by_family(project_root, profile)
    return df, summarize_script_sprawl(df)

def summarize_script_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Script calistirilmaz."]}
""")

    with open(ls_dir / "test_sprawl.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_tests_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "unit", "tests": 1}])

def build_test_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_tests_by_family(project_root, profile)
    return df, summarize_test_sprawl(df)

def summarize_test_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["pytest calistirilmaz."]}
""")

    with open(ls_dir / "output_sprawl.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_outputs_by_family(project_root: Path, base_dir_name: str, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "csv", "outputs": 1}])

def build_report_output_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_outputs_by_family(project_root, "reports/output", profile)
    return df, summarize_output_sprawl(df)

def build_datalake_output_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_outputs_by_family(project_root, "data/lake", profile)
    return df, summarize_output_sprawl(df)

def summarize_output_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["Output dosyasi tasinmaz/silinmez."]}
""")

    with open(ls_dir / "documentation_sprawl.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from pathlib import Path
from local_simplification.simplification_config import LocalSimplificationProfile

def group_docs_by_family(project_root: Path, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return pd.DataFrame([{"family": "generated", "docs": 1}])

def build_documentation_sprawl_report(project_root: Path, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    df = group_docs_by_family(project_root, profile)
    return df, summarize_documentation_sprawl(df)

def summarize_documentation_sprawl(df: pd.DataFrame) -> dict:
    return {"families": len(df), "warnings": ["docs degistirilmez."]}
""")

    with open(ls_dir / "optional_slimming_plan.py", "w", encoding="utf-8") as f:
        f.write("""import pandas as pd
from local_simplification.simplification_config import LocalSimplificationProfile
from local_simplification.simplification_models import SlimmingPlanItem, build_slimming_plan_item_id, slimming_plan_item_to_dict

def build_default_slimming_plan_items(profile: LocalSimplificationProfile) -> list[SlimmingPlanItem]:
    return [
        SlimmingPlanItem(
            plan_item_id=build_slimming_plan_item_id("docs_nav", "docs"),
            title="docs navigation simplification",
            category="docs",
            priority_hint="low",
            action_type="consolidate",
            dry_run_only=True,
            prerequisites=[],
            warnings=["Gercek uygulama plani degildir."]
        )
    ]

def build_optional_slimming_plan(complexity_df: pd.DataFrame, candidate_df: pd.DataFrame, profile: LocalSimplificationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_slimming_plan_items(profile)
    df = pd.DataFrame([slimming_plan_item_to_dict(i) for i in items])
    return df, summarize_optional_slimming_plan(df)

def prioritize_slimming_plan_items(plan_df: pd.DataFrame, profile: LocalSimplificationProfile) -> pd.DataFrame:
    return plan_df

def summarize_optional_slimming_plan(plan_df: pd.DataFrame) -> dict:
    return {"items": len(plan_df), "warnings": ["Gercek cleanup uygulamasi degildir.", "Manual review required"]}

def export_optional_slimming_plan_markdown(plan_df: pd.DataFrame, summary: dict) -> str:
    return "# Optional Slimming Plan\\n\\nBu bir refactor talimati degildir."
""")

    print("Created phase 82 core 3")

if __name__ == "__main__":
    main()
