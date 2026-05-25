from dataclasses import dataclass
from typing import List

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class QualityGateProfile:
    name: str
    description: str
    run_pytest: bool = True
    run_import_validation: bool = True
    run_static_safety_scan: bool = True
    run_repo_hygiene: bool = True
    run_dependency_audit: bool = True
    run_smoke_tests: bool = True
    run_output_contracts: bool = True
    run_documentation_coverage: bool = True
    max_test_runtime_seconds: int = 900
    allow_network_calls: bool = False
    allow_live_commands: bool = False
    allow_broker_commands: bool = False
    allow_deploy_commands: bool = False
    allow_background_daemons: bool = False
    min_pass_rate: float = 0.85
    min_quality_score: float = 0.40
    release_candidate_dry_run: bool = True
    enabled: bool = True
    notes: str = ""

_PROFILES = {
    "balanced_local_quality_gate": QualityGateProfile(
        name="balanced_local_quality_gate",
        description="Balanced Local Quality Gate",
        run_pytest=True,
        run_import_validation=True,
        run_static_safety_scan=True,
        run_repo_hygiene=True,
        run_dependency_audit=True,
        run_smoke_tests=True,
        run_output_contracts=True,
        run_documentation_coverage=True,
        max_test_runtime_seconds=900,
        allow_network_calls=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        min_pass_rate=0.85,
        min_quality_score=0.40,
        release_candidate_dry_run=True,
        enabled=True,
        notes="Genel amaçlı local CI-like validation ve release candidate hazırlık profili.",
    ),
    "strict_local_quality_gate": QualityGateProfile(
        name="strict_local_quality_gate",
        description="Strict Local Quality Gate",
        run_pytest=True,
        run_import_validation=True,
        run_static_safety_scan=True,
        run_repo_hygiene=True,
        run_dependency_audit=True,
        run_smoke_tests=True,
        run_output_contracts=True,
        run_documentation_coverage=True,
        max_test_runtime_seconds=1800,
        allow_network_calls=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        min_pass_rate=0.95,
        min_quality_score=0.60,
        release_candidate_dry_run=True,
        enabled=True,
        notes="Daha sıkı test, safety ve release candidate kontrol profili.",
    ),
    "fast_local_quality_gate": QualityGateProfile(
        name="fast_local_quality_gate",
        description="Fast Local Quality Gate",
        run_pytest=True,
        run_import_validation=True,
        run_static_safety_scan=True,
        run_repo_hygiene=True,
        run_dependency_audit=False,
        run_smoke_tests=True,
        run_output_contracts=False,
        run_documentation_coverage=False,
        max_test_runtime_seconds=300,
        allow_network_calls=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        min_pass_rate=0.75,
        min_quality_score=0.40,
        release_candidate_dry_run=True,
        enabled=True,
        notes="Hızlı local kontrol ve temel kalite taraması profili.",
    ),
    "release_candidate_quality_gate": QualityGateProfile(
        name="release_candidate_quality_gate",
        description="Release Candidate Quality Gate",
        run_pytest=True,
        run_import_validation=True,
        run_static_safety_scan=True,
        run_repo_hygiene=True,
        run_dependency_audit=True,
        run_smoke_tests=True,
        run_output_contracts=True,
        run_documentation_coverage=True,
        max_test_runtime_seconds=1800,
        allow_network_calls=False,
        allow_live_commands=False,
        allow_broker_commands=False,
        allow_deploy_commands=False,
        allow_background_daemons=False,
        min_pass_rate=0.90,
        min_quality_score=0.55,
        release_candidate_dry_run=True,
        enabled=True,
        notes="Release candidate manifest, checklist ve package plan üretimine odaklı profil.",
    ),
}

def get_quality_gate_profile(name: str) -> QualityGateProfile:
    if name not in _PROFILES:
        raise ConfigError(f"Unknown profile: {name}")
    return _PROFILES[name]

def list_quality_gate_profiles(enabled_only: bool = True) -> List[QualityGateProfile]:
    if enabled_only:
        return [p for p in _PROFILES.values() if p.enabled]
    return list(_PROFILES.values())

def validate_quality_gate_profiles() -> None:
    for name, profile in _PROFILES.items():
        if profile.max_test_runtime_seconds <= 0:
            raise ConfigError(f"Profile {name} has max_test_runtime_seconds <= 0")
        if not (0.0 <= profile.min_pass_rate <= 1.0):
            raise ConfigError(f"Profile {name} has min_pass_rate outside 0-1")
        if not (0.0 <= profile.min_quality_score <= 1.0):
            raise ConfigError(f"Profile {name} has min_quality_score outside 0-1")
        if profile.allow_network_calls or profile.allow_live_commands or profile.allow_broker_commands or profile.allow_deploy_commands or profile.allow_background_daemons:
            raise ConfigError(f"Profile {name} has allow flags set to True")
        if not profile.release_candidate_dry_run:
            raise ConfigError(f"Profile {name} has release_candidate_dry_run set to False")
        run_flags = [
            profile.run_pytest,
            profile.run_import_validation,
            profile.run_static_safety_scan,
            profile.run_repo_hygiene,
            profile.run_dependency_audit,
            profile.run_smoke_tests,
            profile.run_output_contracts,
            profile.run_documentation_coverage,
        ]
        if not any(run_flags):
            raise ConfigError(f"Profile {name} must have at least one run flag set to True")

def get_default_quality_gate_profile() -> QualityGateProfile:
    from config.settings import settings
    return get_quality_gate_profile(settings.default_quality_gate_profile)
