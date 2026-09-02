
import pandas as pd
import config.paths as paths

def main():
    print("Running reusable template catalog...")
    paths.ensure_project_directories()
    (paths.LOCAL_REUSE_DOCS_DIR / "REUSABLE_TEMPLATE_CATALOG.md").touch()
    
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "cross_project_reusable_template_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_prompt_template_library.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_module_blueprint_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_script_pattern_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_test_pattern_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_datalake_contract_pattern_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_report_pattern_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_safety_boundary_pattern_catalog.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reusable_documentation_pattern_catalog.csv").touch()
    
    (paths.LOCAL_REUSE_REPORTS_MD_DIR / "reusable_template_catalog.md").touch()
    (paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reusable_template_catalog.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
