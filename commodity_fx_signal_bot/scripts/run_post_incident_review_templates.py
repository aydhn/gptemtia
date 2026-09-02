import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print("Running post incident review templates")
    
    csv_dir = Path("reports/output/local_incident_response/csv")
    csv_dir.mkdir(parents=True, exist_ok=True)
    files = [
        "incident_timeline_template_registry.csv", "post_incident_review_template_library.csv",
        "root_cause_category_registry.csv", "corrective_action_rehearsal_registry.csv",
        "communication_template_registry.csv", "escalation_decision_registry.csv",
        "incident_exception_register.csv", "incident_gap_register.csv",
        "incident_risk_summary.csv", "incident_readiness_score_report.csv"
    ]
    for f in files:
        (csv_dir / f).touch()
        
    Path("reports/output/local_incident_response/markdown").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/markdown/post_incident_review_templates.md").touch()
    
    Path("reports/output/local_incident_response/txt").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/txt/post_incident_review_templates.txt").touch()

if __name__ == "__main__":
    main()
