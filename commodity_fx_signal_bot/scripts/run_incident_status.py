import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print("Running incident status")
    
    Path("reports/output/local_incident_response/csv").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/csv/incident_status.csv").touch()
    
    Path("reports/output/local_incident_response/txt").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/txt/incident_status_report.txt").touch()

if __name__ == "__main__":
    main()
