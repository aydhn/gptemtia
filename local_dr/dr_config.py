from dataclasses import dataclass, field
from typing import Optional

@dataclass
class LocalDRProfile:
    name: str
    description: str
    language: str = "tr"
    dry_run_default: bool = True
    allow_real_restore: bool = False
    scan_domains: bool = True
    scan_tabletops: bool = True
    scan_drills: bool = True
    scan_failures: bool = True
    max_checks: int = 300000
    min_resilience_score: float = 0.40
    enabled: bool = True
    notes: Optional[str] = None

balanced_local_dr = LocalDRProfile(
    name="balanced_local_dr",
    description="Balanced profile for DR capabilities",
)

strict_dr_boundary = LocalDRProfile(
    name="strict_dr_boundary",
    description="Strict boundary for DR capabilities",
    min_resilience_score=0.80,
)

restore_traceability_focus = LocalDRProfile(
    name="restore_traceability_focus",
    description="Focus on traceability for restore",
)

failure_playbook_focus = LocalDRProfile(
    name="failure_playbook_focus",
    description="Focus on failure playbooks",
)

PROFILES = {
    "balanced_local_dr": balanced_local_dr,
    "strict_dr_boundary": strict_dr_boundary,
    "restore_traceability_focus": restore_traceability_focus,
    "failure_playbook_focus": failure_playbook_focus,
}

def get_local_dr_profile(name: str) -> LocalDRProfile:
    if name not in PROFILES:
        raise ValueError(f"Profile {name} not found")
    return PROFILES[name]

def list_local_dr_profiles(enabled_only: bool = True) -> list[LocalDRProfile]:
    return [p for p in PROFILES.values() if not enabled_only or p.enabled]

def validate_local_dr_profiles() -> None:
    for name, p in PROFILES.items():
        if p.name != name:
            raise ValueError(f"Profile name mismatch: {p.name} != {name}")

def get_default_local_dr_profile() -> LocalDRProfile:
    return balanced_local_dr
