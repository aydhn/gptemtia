import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from pathlib import Path
import pandas as pd
from local_timeline.backup_packaging_secrets_timeline import classify_backup_packaging_secrets_event, build_recovery_security_activity_summary

def test_classify_backup_packaging_secrets_event():
    assert classify_backup_packaging_secrets_event(Path("backup_a.txt"), Path(".")) == "backup_event"
    assert classify_backup_packaging_secrets_event(Path("packaging_a.txt"), Path(".")) == "packaging_event"
    assert classify_backup_packaging_secrets_event(Path("secret_a.txt"), Path(".")) == "secrets_event"
    assert classify_backup_packaging_secrets_event(Path("other.txt"), Path(".")) == "security_event"

def test_build_recovery_security_activity_summary():
    df = pd.DataFrame([{"relative_path": "backup_a.txt"}])
    summary = build_recovery_security_activity_summary(df)
    assert not summary.empty
    assert summary.iloc[0]['category'] == "backup_event"
