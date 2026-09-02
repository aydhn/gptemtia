
import config.paths as paths

def main():
    print("Running v1.1 planning seed...")
    paths.ensure_project_directories()
    (paths.LOCAL_REUSE_DOCS_DIR / "V1_1_PLANNING_SEED.md").touch()
    
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_candidate_backlog_seed.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_safety_boundary_seed.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "v1_1_research_only_scope_seed.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_exception_register.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_gap_register.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_risk_summary.csv").touch()
    (paths.LOCAL_REUSE_REPORTS_CSV_DIR / "reuse_readiness_score_report.csv").touch()
    
    (paths.LOCAL_REUSE_REPORTS_MD_DIR / "v1_1_planning_seed.md").touch()
    (paths.LOCAL_REUSE_REPORTS_TXT_DIR / "v1_1_planning_seed.txt").touch()
    print("Done.")

if __name__ == "__main__":
    main()
