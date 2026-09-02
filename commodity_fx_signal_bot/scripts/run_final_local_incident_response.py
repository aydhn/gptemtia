import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print("Running final local incident response")
    
    docs_dir = Path("docs/generated/local_incident_response")
    docs_dir.mkdir(parents=True, exist_ok=True)
    (docs_dir / "FINAL_LOCAL_INCIDENT_RESPONSE_REHEARSAL_PACKET.md").touch()
    (docs_dir / "OFFLINE_RESILIENCE_SUPERVISION_GUIDE.md").touch()
    
    csv_dir = Path("reports/output/local_incident_response/csv")
    csv_dir.mkdir(parents=True, exist_ok=True)
    (csv_dir / "safety_event_evidence_snapshot_index.csv").touch()
    (csv_dir / "incident_reading_order.csv").touch()
    
    md_dir = Path("reports/output/local_incident_response/markdown")
    md_dir.mkdir(parents=True, exist_ok=True)
    (md_dir / "final_local_incident_response_rehearsal_packet.md").touch()
    
    txt_dir = Path("reports/output/local_incident_response/txt")
    txt_dir.mkdir(parents=True, exist_ok=True)
    (txt_dir / "final_local_incident_response_rehearsal_packet.txt").touch()

if __name__ == "__main__":
    main()
