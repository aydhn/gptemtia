
import config.paths as paths

def main():
    print("Running local knowledge reuse kit...")
    paths.ensure_project_directories()
    (paths.LOCAL_REUSE_DOCS_DIR / "LOCAL_KNOWLEDGE_REUSE_KIT.md").touch()
    (paths.LOCAL_REUSE_DOCS_DIR / "FUTURE_PROJECT_PROMPT_STARTER_PACK.md").touch()
    
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_starter_checklist.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_directory_blueprint.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "future_project_test_blueprint.csv").touch()
    
    (paths.LOCAL_REUSE_REPORTS_MD_DIR / "local_knowledge_reuse_kit.md").touch()
    (paths.LOCAL_REUSE_REPORTS_TXT_DIR / "local_knowledge_reuse_kit.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
