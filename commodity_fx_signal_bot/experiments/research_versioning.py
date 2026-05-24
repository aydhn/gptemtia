import json
import logging
import hashlib
import platform
import sys
import subprocess
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
from typing import Any

from experiments.experiment_models import ExperimentDefinition

logger = logging.getLogger(__name__)

def build_research_version_id(module_scope: list[str], timeframe: str, symbols: list[str], created_at_utc: str) -> str:
    scope = "_".join(sorted(module_scope))
    syms = "_".join(sorted(symbols))
    raw = f"{scope}_{timeframe}_{syms}_{created_at_utc}"
    h = hashlib.md5(raw.encode()).hexdigest()[:12]
    return f"rver_{h}"

def capture_config_snapshot(settings_obj: Any, include_sensitive: bool = False) -> dict:
    snapshot = {}
    for attr in dir(settings_obj):
        if attr.startswith("_"):
            continue
        val = getattr(settings_obj, attr)
        if callable(val):
            continue

        # Masking sensitive information
        if not include_sensitive:
            lower_attr = attr.lower()
            if any(s in lower_attr for s in ["token", "key", "password", "secret", "bot"]):
                snapshot[attr] = "***MASKED***"
                continue

        try:
            json.dumps(val)
            snapshot[attr] = val
        except TypeError:
            snapshot[attr] = str(val)
    return snapshot

def capture_environment_snapshot() -> dict:
    env_snapshot = {
        "python_version": sys.version,
        "platform": platform.platform(),
        "package_versions": {}
    }

    try:
        import pkg_resources
        for pkg in pkg_resources.working_set:
            env_snapshot["package_versions"][pkg.key] = pkg.version
    except ImportError:
        try:
            import importlib.metadata
            for dist in importlib.metadata.distributions():
                env_snapshot["package_versions"][dist.metadata["Name"].lower()] = dist.version
        except Exception:
            env_snapshot["package_versions"] = "Could not retrieve package versions."

    return env_snapshot

def capture_git_snapshot(project_root: Path) -> dict:
    git_snapshot = {
        "git_commit": "unknown",
        "dirty_tree": "unknown"
    }

    try:
        commit_res = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=False
        )
        if commit_res.returncode == 0:
            git_snapshot["git_commit"] = commit_res.stdout.strip()

        status_res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=project_root,
            capture_output=True,
            text=True,
            check=False
        )
        if status_res.returncode == 0:
            git_snapshot["dirty_tree"] = len(status_res.stdout.strip()) > 0
    except Exception as e:
        logger.warning(f"Could not capture git snapshot: {e}")

    return git_snapshot

def capture_data_snapshot(data_lake: Any, module_scope: list[str], timeframe: str) -> dict:
    # A simple mock snapshot. In a real system, we'd hash files or query data lake states.
    return {
        "module_scope": module_scope,
        "timeframe": timeframe,
        "status": "data snapshot taken"
    }

def build_research_version_record(experiment: ExperimentDefinition, data_lake: Any, settings_obj: Any, project_root: Path) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    version_id = build_research_version_id(
        experiment.module_scope,
        experiment.timeframe,
        experiment.symbols,
        now
    )

    record = {
        "version_id": version_id,
        "experiment_id": experiment.experiment_id,
        "created_at_utc": now,
        "module_scope": experiment.module_scope,
        "timeframe": experiment.timeframe,
        "symbols": experiment.symbols,
        "config_snapshot": capture_config_snapshot(settings_obj),
        "environment_snapshot": capture_environment_snapshot(),
        "git_snapshot": capture_git_snapshot(project_root),
        "data_snapshot": capture_data_snapshot(data_lake, experiment.module_scope, experiment.timeframe)
    }

    config_str = json.dumps(record["config_snapshot"], sort_keys=True)
    record["config_hash"] = hashlib.md5(config_str.encode()).hexdigest()

    return record

def research_version_record_to_dataframe(record: dict) -> pd.DataFrame:
    flat = {
        "version_id": record["version_id"],
        "experiment_id": record["experiment_id"],
        "created_at_utc": record["created_at_utc"],
        "module_scope": ",".join(record["module_scope"]),
        "timeframe": record["timeframe"],
        "symbols": ",".join(record["symbols"]),
        "config_hash": record.get("config_hash", ""),
        "git_commit": record.get("git_snapshot", {}).get("git_commit", "unknown"),
        "dirty_tree": record.get("git_snapshot", {}).get("dirty_tree", "unknown")
    }
    return pd.DataFrame([flat])
