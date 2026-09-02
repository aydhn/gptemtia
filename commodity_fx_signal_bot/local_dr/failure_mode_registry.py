
import pandas as pd
from local_dr.dr_config import LocalDRProfile
from local_dr.dr_models import FailureMode

def build_default_failure_modes(profile: LocalDRProfile) -> list[FailureMode]:
    return [FailureMode(failure_id="fm1", domain_label="archive_restore_dr", failure_name="missing_archive_manifest", severity="failure_critical", detection_hint="", manual_response="", prevention_hint="", warnings=[])]

def classify_failure_severity(failure_name: str, domain_label: str) -> str:
    return "failure_critical"

def build_failure_mode_registry(profile: LocalDRProfile) -> tuple[pd.DataFrame, dict]:
    modes = build_default_failure_modes(profile)
    df = pd.DataFrame([m.__dict__ for m in modes])
    return df, {"total": len(modes)}

def summarize_failure_modes(failure_df: pd.DataFrame) -> dict:
    return {"total": len(failure_df)}
