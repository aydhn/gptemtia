
from dataclasses import dataclass
import pandas as pd

@dataclass(frozen=True)
class LocalDRProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_restore: bool = False
    allow_real_backup: bool = False
    allow_auto_recovery: bool = False
    allow_file_modification: bool = False
    allow_file_deletion: bool = False
    allow_file_move: bool = False
    allow_overwrite: bool = False
    allow_cloud_upload: bool = False
    allow_external_dr_service: bool = False
    allow_external_llm: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    allow_real_market_download: bool = False
    scan_archive_outputs: bool = True
    scan_backup_outputs: bool = True
    scan_docs: bool = True
    scan_reports: bool = True
    scan_data_lake: bool = True
    scan_configs: bool = True
    scan_scripts: bool = True
    scan_tests: bool = True
    scan_cross_layer_outputs: bool = True
    scan_security_layers: bool = True
    max_checks: int = 300000
    restore_drill_review_days: int = 90
    tabletop_review_days: int = 180
    min_resilience_score: float = 0.40
    min_quality_score: float = 0.40
    enabled: bool = True
    notes: str = ""

def get_local_dr_profile(name: str) -> LocalDRProfile:
    if name == "balanced_local_dr":
        return LocalDRProfile(name="balanced_local_dr", description="", notes="Genel amaçlı local/offline disaster-recovery tabletop ve restore drill simulation profili.")
    if name == "strict_dr_boundary":
        return LocalDRProfile(name="strict_dr_boundary", description="", max_checks=200000, restore_drill_review_days=60, tabletop_review_days=120, min_resilience_score=0.60, min_quality_score=0.60, notes="Real restore, real backup, cloud DR, destructive action, secret boundary ve incident rehearsal kontrollerini sıkılaştıran profil.")
    if name == "restore_traceability_focus":
        return LocalDRProfile(name="restore_traceability_focus", description="", notes="Archive/backup restore traceability, restore-readiness ve integrity rehearsal odaklı profil.")
    if name == "failure_playbook_focus":
        return LocalDRProfile(name="failure_playbook_focus", description="", notes="Failure-mode registry, incident playbooks ve tabletop senaryoları odaklı profil.")
    raise ValueError(f"Unknown profile: {name}")

def list_local_dr_profiles(enabled_only: bool = True) -> list[LocalDRProfile]:
    return [get_local_dr_profile("balanced_local_dr")]

def validate_local_dr_profiles() -> None:
    pass

def get_default_local_dr_profile() -> LocalDRProfile:
    return get_local_dr_profile("balanced_local_dr")
