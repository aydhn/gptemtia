import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=str, default="balanced_local_incident_response")
    args = parser.parse_args()
    print("Running safety event register with profile:", args.profile)
    
    csv_dir = Path("reports/output/local_incident_response/csv")
    csv_dir.mkdir(parents=True, exist_ok=True)
    
    files = [
        "safety_event_register.csv", "safety_event_taxonomy.csv",
        "incident_severity_taxonomy.csv", "incident_triage_checklist.csv",
        "incident_classification_registry.csv", "boundary_breach_event_registry.csv",
        "unsafe_output_event_registry.csv", "forbidden_capability_request_event_registry.csv",
        "secret_exposure_event_registry.csv", "file_action_event_registry.csv",
        "cloud_publish_event_registry.csv", "live_trading_broker_misuse_event_registry.csv",
        "model_deployment_event_registry.csv", "external_llm_api_event_registry.csv"
    ]
    for f in files:
        (csv_dir / f).touch()
        
    Path("reports/output/local_incident_response/markdown").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/markdown/safety_event_register.md").touch()
    
    Path("reports/output/local_incident_response/txt").mkdir(parents=True, exist_ok=True)
    Path("reports/output/local_incident_response/txt/safety_event_register.txt").touch()

if __name__ == "__main__":
    main()
