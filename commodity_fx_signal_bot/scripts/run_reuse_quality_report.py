
import config.paths as paths

def main():
    print("Running reuse quality report...")
    paths.ensure_project_directories()
    
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_validation_report.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_JSON_DIR / "reuse_quality_report.json").touch()
    (paths.LOCAL_REUSE_REPORTS_MD_DIR / "reuse_quality_report.md").touch()
    (paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reuse_quality_report.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
