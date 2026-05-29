from dataclasses import dataclass
import hashlib

@dataclass
class ScenarioRegressionDefinition:
    regression_id: str
    scenario_id: str
    regression_type: str
    name: str
    description: str
    expected_outputs: list[str]
    golden_output_ids: list[str]
    snapshot_ids: list[str]
    required: bool
    warnings: list[str]

@dataclass
class GoldenOutputRecord:
    golden_id: str
    scenario_id: str
    output_name: str
    output_type: str
    path: str
    content_hash: str | None
    schema_hash: str | None
    row_count: int | None
    created_at_utc: str
    synthetic_only: bool
    warnings: list[str]

@dataclass
class SnapshotRecord:
    snapshot_id: str
    scenario_id: str
    snapshot_name: str
    artifact_type: str
    path: str
    content_hash: str | None
    schema_hash: str | None
    row_count: int | None
    captured_at_utc: str
    warnings: list[str]

@dataclass
class SnapshotDiff:
    diff_id: str
    scenario_id: str
    baseline_snapshot_id: str
    current_snapshot_id: str
    diff_label: str
    numeric_diff_score: float | None
    text_similarity_score: float | None
    schema_changed: bool
    row_count_changed: bool
    warnings: list[str]

@dataclass
class ReplayResult:
    replay_id: str
    scenario_id: str
    replay_status: str
    started_at_utc: str
    finished_at_utc: str | None
    deterministic_seed: int
    output_hashes: dict
    matched_golden_outputs: bool
    warnings: list[str]

@dataclass
class RegressionFailure:
    failure_id: str
    scenario_id: str
    regression_type: str
    severity: str
    title: str
    description: str
    recommended_action: str
    blocking: bool
    warnings: list[str]

def build_regression_id(scenario_id: str, regression_type: str) -> str:
    hash_input = f"{scenario_id}_{regression_type}".encode("utf-8")
    return f"reg_{hashlib.md5(hash_input).hexdigest()[:12]}"

def build_golden_output_id(scenario_id: str, output_name: str) -> str:
    hash_input = f"{scenario_id}_{output_name}".encode("utf-8")
    return f"gold_{hashlib.md5(hash_input).hexdigest()[:12]}"

def build_snapshot_id(scenario_id: str, snapshot_name: str, captured_at_utc: str | None = None) -> str:
    hash_input = f"{scenario_id}_{snapshot_name}_{captured_at_utc or ''}".encode("utf-8")
    return f"snap_{hashlib.md5(hash_input).hexdigest()[:12]}"

def build_snapshot_diff_id(baseline_snapshot_id: str, current_snapshot_id: str) -> str:
    hash_input = f"{baseline_snapshot_id}_{current_snapshot_id}".encode("utf-8")
    return f"diff_{hashlib.md5(hash_input).hexdigest()[:12]}"

def build_replay_id(scenario_id: str, started_at_utc: str) -> str:
    hash_input = f"{scenario_id}_{started_at_utc}".encode("utf-8")
    return f"rep_{hashlib.md5(hash_input).hexdigest()[:12]}"

def build_regression_failure_id(scenario_id: str, title: str) -> str:
    hash_input = f"{scenario_id}_{title}".encode("utf-8")
    return f"fail_{hashlib.md5(hash_input).hexdigest()[:12]}"

def scenario_regression_definition_to_dict(item: ScenarioRegressionDefinition) -> dict:
    return {
        "regression_id": item.regression_id,
        "scenario_id": item.scenario_id,
        "regression_type": item.regression_type,
        "name": item.name,
        "description": item.description,
        "expected_outputs": ",".join(item.expected_outputs),
        "golden_output_ids": ",".join(item.golden_output_ids),
        "snapshot_ids": ",".join(item.snapshot_ids),
        "required": item.required,
        "warnings": ";".join(item.warnings),
    }

def golden_output_record_to_dict(record: GoldenOutputRecord) -> dict:
    return {
        "golden_id": record.golden_id,
        "scenario_id": record.scenario_id,
        "output_name": record.output_name,
        "output_type": record.output_type,
        "path": record.path,
        "content_hash": record.content_hash,
        "schema_hash": record.schema_hash,
        "row_count": record.row_count,
        "created_at_utc": record.created_at_utc,
        "synthetic_only": record.synthetic_only,
        "warnings": ";".join(record.warnings),
    }

def snapshot_record_to_dict(record: SnapshotRecord) -> dict:
    return {
        "snapshot_id": record.snapshot_id,
        "scenario_id": record.scenario_id,
        "snapshot_name": record.snapshot_name,
        "artifact_type": record.artifact_type,
        "path": record.path,
        "content_hash": record.content_hash,
        "schema_hash": record.schema_hash,
        "row_count": record.row_count,
        "captured_at_utc": record.captured_at_utc,
        "warnings": ";".join(record.warnings),
    }

def snapshot_diff_to_dict(diff: SnapshotDiff) -> dict:
    return {
        "diff_id": diff.diff_id,
        "scenario_id": diff.scenario_id,
        "baseline_snapshot_id": diff.baseline_snapshot_id,
        "current_snapshot_id": diff.current_snapshot_id,
        "diff_label": diff.diff_label,
        "numeric_diff_score": diff.numeric_diff_score,
        "text_similarity_score": diff.text_similarity_score,
        "schema_changed": diff.schema_changed,
        "row_count_changed": diff.row_count_changed,
        "warnings": ";".join(diff.warnings),
    }

def replay_result_to_dict(result: ReplayResult) -> dict:
    return {
        "replay_id": result.replay_id,
        "scenario_id": result.scenario_id,
        "replay_status": result.replay_status,
        "started_at_utc": result.started_at_utc,
        "finished_at_utc": result.finished_at_utc,
        "deterministic_seed": result.deterministic_seed,
        "matched_golden_outputs": result.matched_golden_outputs,
        "warnings": ";".join(result.warnings),
    }

def regression_failure_to_dict(failure: RegressionFailure) -> dict:
    return {
        "failure_id": failure.failure_id,
        "scenario_id": failure.scenario_id,
        "regression_type": failure.regression_type,
        "severity": failure.severity,
        "title": failure.title,
        "description": failure.description,
        "recommended_action": failure.recommended_action,
        "blocking": failure.blocking,
        "warnings": ";".join(failure.warnings),
    }
