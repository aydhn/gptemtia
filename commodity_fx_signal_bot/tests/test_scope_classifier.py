from pathlib import Path
from backup_recovery.scope_classifier import classify_backup_scope, detect_secret_or_sensitive_path
from backup_recovery.backup_config import get_default_backup_recovery_profile

def test_classify_backup_scope():
    prof = get_default_backup_recovery_profile()
    assert detect_secret_or_sensitive_path(Path(".env")) == True
    assert classify_backup_scope(Path(".env"), Path("."), prof) == "excluded_secret_scope"
    assert classify_backup_scope(Path("config/settings.py"), Path("."), prof) == "config_template_scope"
