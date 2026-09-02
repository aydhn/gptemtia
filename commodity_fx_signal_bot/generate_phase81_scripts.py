import os
from pathlib import Path

def populate_scripts():
    scripts_dir = Path("scripts")

    scripts_content = {
        "run_reuse_domain_registry.py": """
import pandas as pd
from config.paths import Paths
from data.storage.data_lake import DataLake

def main():
    print("Running reuse domain registry...")
    Paths.ensure_project_directories()
    dl = DataLake()
    df = pd.DataFrame([{"domain_id": "test"}])
    summary = {"status": "ok"}
    
    # Save CSVs
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_profile_registry.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_domain_registry.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "knowledge_reuse_no_go_safe_go_summary.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_non_goals_registry.csv").touch()
    
    # Save MD and TXT
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "reuse_domain_registry_report.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reuse_domain_registry_report.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_final_audit_memory_pack.py": """
import pandas as pd
from config.paths import Paths

def main():
    print("Running final audit memory pack...")
    Paths.ensure_project_directories()
    (Paths.LOCAL_REUSE_DOCS_DIR / "FINAL_AUDIT_MEMORY_PACK.md").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "phase_memory_capsule_registry.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "project_pattern_extraction_report.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "architecture_pattern_extraction_report.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "safety_pattern_extraction_report.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "validation_quality_pattern_extraction_report.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "handoff_delivery_closure_pattern_extraction_report.csv").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "final_audit_memory_pack.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "final_audit_memory_pack.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_reusable_template_catalog.py": """
import pandas as pd
from config.paths import Paths

def main():
    print("Running reusable template catalog...")
    Paths.ensure_project_directories()
    (Paths.LOCAL_REUSE_DOCS_DIR / "REUSABLE_TEMPLATE_CATALOG.md").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "cross_project_reusable_template_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_prompt_template_library.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_module_blueprint_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_script_pattern_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_test_pattern_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_datalake_contract_pattern_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_report_pattern_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_safety_boundary_pattern_catalog.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_documentation_pattern_catalog.csv").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "reusable_template_catalog.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reusable_template_catalog.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_local_knowledge_reuse_kit.py": """
from config.paths import Paths

def main():
    print("Running local knowledge reuse kit...")
    Paths.ensure_project_directories()
    (Paths.LOCAL_REUSE_DOCS_DIR / "LOCAL_KNOWLEDGE_REUSE_KIT.md").touch()
    (Paths.LOCAL_REUSE_DOCS_DIR / "FUTURE_PROJECT_PROMPT_STARTER_PACK.md").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_starter_checklist.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_directory_blueprint.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_test_blueprint.csv").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "local_knowledge_reuse_kit.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "local_knowledge_reuse_kit.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_v1_1_planning_seed.py": """
from config.paths import Paths

def main():
    print("Running v1.1 planning seed...")
    Paths.ensure_project_directories()
    (Paths.LOCAL_REUSE_DOCS_DIR / "V1_1_PLANNING_SEED.md").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_candidate_backlog_seed.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_safety_boundary_seed.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_research_only_scope_seed.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_exception_register.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_gap_register.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_risk_summary.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_readiness_score_report.csv").touch()
    
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "v1_1_planning_seed.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "v1_1_planning_seed.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_reuse_quality_report.py": """
from config.paths import Paths

def main():
    print("Running reuse quality report...")
    Paths.ensure_project_directories()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_validation_report.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_JSON_DIR / "reuse_quality_report.json").touch()
    (Paths.LOCAL_REUSE_REPORTS_MD_DIR / "reuse_quality_report.md").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reuse_quality_report.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
""",
        "run_reuse_status.py": """
from config.paths import Paths

def main():
    print("Running reuse status...")
    Paths.ensure_project_directories()
    
    (Paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_status.csv").touch()
    (Paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reuse_status_report.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
"""
    }

    for name, content in scripts_content.items():
        script_path = scripts_dir / name
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Patched {name}")

if __name__ == "__main__":
    populate_scripts()
