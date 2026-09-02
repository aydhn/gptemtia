
import config.paths as paths

def main():
    print("Running reuse status...")
    paths.ensure_project_directories()
    
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_status.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_TXT_DIR / "reuse_status_report.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
