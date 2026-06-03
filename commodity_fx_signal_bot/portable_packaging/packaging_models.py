import hashlib
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class EnvironmentSnapshot:
    snapshot_id: str
    created_at_utc: str
    os_name: str
    platform: str
    python_version: str
    executable: str
    cpu_count: Optional[int]
    memory_total_mb: Optional[float]
    gpu_available: Optional[bool]
    package_count: int
    warnings: List[str]

@dataclass
class DependencyRecord:
    dependency_id: str
    package_name: str
    installed_version: Optional[str]
    required_version: Optional[str]
    source: str
    import_detected: bool
    requirement_detected: bool
    optional: bool
    warnings: List[str]

@dataclass
class BundleArtifact:
    artifact_id: str
    relative_path: str
    artifact_label: str
    include_policy: str
    size_bytes: Optional[int]
    content_hash: Optional[str]
    safety_label: str
    warnings: List[str]

@dataclass
class InstallVerificationResult:
    check_id: str
    check_name: str
    status: str
    passed: bool
    details: Dict
    warnings: List[str]

@dataclass
class PortableBundleManifest:
    manifest_id: str
    profile_name: str
    created_at_utc: str
    dry_run: bool
    artifact_count: int
    included_artifacts: List[str]
    excluded_artifacts: List[str]
    environment_snapshot_id: Optional[str]
    requirements_artifacts: List[str]
    setup_guide_path: Optional[str]
    warnings: List[str]


def build_environment_snapshot_id(created_at_utc: str) -> str:
    raw = f"env_snap_{created_at_utc}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]

def build_dependency_id(package_name: str, source: str) -> str:
    raw = f"dep_{package_name}_{source}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]

def build_bundle_artifact_id(relative_path: str) -> str:
    raw = f"art_{relative_path}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]

def build_install_check_id(check_name: str) -> str:
    raw = f"chk_{check_name}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]

def build_portable_bundle_manifest_id(profile_name: str, created_at_utc: str) -> str:
    raw = f"pbm_{profile_name}_{created_at_utc}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


def environment_snapshot_to_dict(snapshot: EnvironmentSnapshot) -> Dict:
    return {
        "snapshot_id": snapshot.snapshot_id,
        "created_at_utc": snapshot.created_at_utc,
        "os_name": snapshot.os_name,
        "platform": snapshot.platform,
        "python_version": snapshot.python_version,
        "executable": snapshot.executable,
        "cpu_count": snapshot.cpu_count,
        "memory_total_mb": snapshot.memory_total_mb,
        "gpu_available": snapshot.gpu_available,
        "package_count": snapshot.package_count,
        "warnings": snapshot.warnings,
    }

def dependency_record_to_dict(record: DependencyRecord) -> Dict:
    return {
        "dependency_id": record.dependency_id,
        "package_name": record.package_name,
        "installed_version": record.installed_version,
        "required_version": record.required_version,
        "source": record.source,
        "import_detected": record.import_detected,
        "requirement_detected": record.requirement_detected,
        "optional": record.optional,
        "warnings": record.warnings,
    }

def bundle_artifact_to_dict(artifact: BundleArtifact) -> Dict:
    return {
        "artifact_id": artifact.artifact_id,
        "relative_path": artifact.relative_path,
        "artifact_label": artifact.artifact_label,
        "include_policy": artifact.include_policy,
        "size_bytes": artifact.size_bytes,
        "content_hash": artifact.content_hash,
        "safety_label": artifact.safety_label,
        "warnings": artifact.warnings,
    }

def install_verification_result_to_dict(result: InstallVerificationResult) -> Dict:
    return {
        "check_id": result.check_id,
        "check_name": result.check_name,
        "status": result.status,
        "passed": result.passed,
        "details": result.details,
        "warnings": result.warnings,
    }

def portable_bundle_manifest_to_dict(manifest: PortableBundleManifest) -> Dict:
    return {
        "manifest_id": manifest.manifest_id,
        "profile_name": manifest.profile_name,
        "created_at_utc": manifest.created_at_utc,
        "dry_run": manifest.dry_run,
        "artifact_count": manifest.artifact_count,
        "included_artifacts": manifest.included_artifacts,
        "excluded_artifacts": manifest.excluded_artifacts,
        "environment_snapshot_id": manifest.environment_snapshot_id,
        "requirements_artifacts": manifest.requirements_artifacts,
        "setup_guide_path": manifest.setup_guide_path,
        "warnings": manifest.warnings,
    }
