
import pandas as pd
from local_dr.dr_config import LocalDRProfile

def build_missing_artifact_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_corrupted_report_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_broken_datalake_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_missing_dependency_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_broken_documentation_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_failed_quality_gate_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_failed_cross_layer_incident_playbook(profile: LocalDRProfile) -> tuple[str, dict]:
    return "playbook", {}
def build_all_incident_playbooks(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    return pd.DataFrame([{"playbooks": "dummy"}]), {"total": 1}
