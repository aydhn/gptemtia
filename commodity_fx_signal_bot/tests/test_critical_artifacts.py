import pandas as pd
from backup_recovery.critical_artifacts import build_critical_artifact_registry

def test_build_critical_artifact_registry():
    df = pd.DataFrame([{"criticality": "critical_artifact"}, {"criticality": "other"}])
    res = build_critical_artifact_registry(df)
    assert len(res) == 1
