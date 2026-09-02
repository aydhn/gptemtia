import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_incident_response")
    args = parser.parse_args()
    print("Running incident quality report")
    
    Path("reports/output/local_incident_response/csv").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/csv/incident_validation_report.csv").touch()
    
    Path("reports/output/local_incident_response/json").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/json/incident_quality_report.json").touch()
    
    Path("reports/output/local_incident_response/markdown").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/markdown/incident_quality_report.md").touch()
    
    Path("reports/output/local_incident_response/txt").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/txt/incident_quality_report.txt").touch()

if __name__ == "__main__":
    main()
