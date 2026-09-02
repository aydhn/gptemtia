import pandas as pd
from typing import Tuple
from local_dr.dr_config import LocalDRProfile

def build_missing_artifact_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Missing Artifact", {"incident": "missing_artifact", "steps": 3}

def build_corrupted_report_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Corrupted Report", {"incident": "corrupted_report", "steps": 3}

def build_broken_datalake_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Broken Datalake", {"incident": "broken_datalake", "steps": 4}

def build_missing_dependency_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Missing Dependency", {"incident": "missing_dependency", "steps": 2}

def build_broken_documentation_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Broken Documentation", {"incident": "broken_documentation", "steps": 2}

def build_failed_quality_gate_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Failed Quality Gate", {"incident": "failed_quality_gate", "steps": 3}

def build_failed_cross_layer_incident_playbook(profile: LocalDRProfile) -> Tuple[str, dict]:
    return "Playbook: Failed Cross Layer", {"incident": "failed_cross_layer", "steps": 3}

def build_all_incident_playbooks(profile: LocalDRProfile) -> Tuple[pd.DataFrame, dict]:
    playbooks = [
        build_missing_artifact_incident_playbook(profile)[1],
        build_corrupted_report_incident_playbook(profile)[1],
        build_broken_datalake_incident_playbook(profile)[1],
        build_missing_dependency_incident_playbook(profile)[1],
        build_broken_documentation_incident_playbook(profile)[1],
        build_failed_quality_gate_incident_playbook(profile)[1],
        build_failed_cross_layer_incident_playbook(profile)[1],
    ]
    df = pd.DataFrame(playbooks)
    summary = {"total_playbooks": len(playbooks)}
    return df, summary
