import pandas as pd

def build_maintenance_checklist() -> pd.DataFrame:
    data = [
        {"task": "pytest çalıştır", "category": "test"},
        {"task": "security audit çalıştır", "category": "security"},
        {"task": "system healthcheck çalıştır", "category": "health"},
        {"task": "import smoke test çalıştır", "category": "dx"},
        {"task": "CLI help audit çalıştır", "category": "dx"},
        {"task": "docs audit çalıştır", "category": "dx"},
        {"task": "dependency check dry-run çalıştır", "category": "dependency"},
        {"task": "notification dry-run test çalıştır", "category": "notification"},
        {"task": "data/lake backup planını kontrol et", "category": "data"},
        {"task": ".env dosyasını commit etme", "category": "security"},
        {"task": "model artifacts git dışında kalsın", "category": "git"}
    ]
    return pd.DataFrame(data)

def build_release_readiness_checklist() -> pd.DataFrame:
    return pd.DataFrame([{"task": "Check version", "status": "pending"}])

def build_phase_completion_checklist(phase_number: int) -> pd.DataFrame:
    return pd.DataFrame([{"task": f"Complete phase {phase_number}", "status": "pending"}])

def build_local_backup_recommendations() -> list[str]:
    return ["Backup data/lake regularly", "Keep .env secure"]

def build_maintenance_report() -> tuple[pd.DataFrame, dict]:
    df = build_maintenance_checklist()
    return df, {"total_tasks": len(df)}
