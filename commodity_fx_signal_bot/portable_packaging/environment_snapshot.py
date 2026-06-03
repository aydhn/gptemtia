import datetime
import os
import platform
import sys
import pandas as pd
from typing import Tuple, Dict, Any, Optional
from portable_packaging.packaging_models import EnvironmentSnapshot, build_environment_snapshot_id

def collect_python_runtime_info() -> Dict[str, str]:
    return {
        "python_version": platform.python_version(),
        "executable": sys.executable,
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
    }

def collect_platform_info() -> Dict[str, str]:
    return {
        "os_name": os.name,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "system": platform.system(),
        "release": platform.release(),
    }

def collect_memory_info() -> Dict[str, Any]:
    info = {"cpu_count": os.cpu_count(), "memory_total_mb": None}
    try:
        import psutil
        mem = psutil.virtual_memory()
        info["memory_total_mb"] = round(mem.total / (1024 * 1024), 2)
    except ImportError:
        pass
    return info

def collect_gpu_snapshot() -> Dict[str, Any]:
    gpu_available = None
    try:
        import torch
        gpu_available = torch.cuda.is_available()
    except ImportError:
        pass
    return {"gpu_available": gpu_available}

def collect_installed_packages_snapshot() -> pd.DataFrame:
    try:
        import pkg_resources
        installed_packages = pkg_resources.working_set
        data = [
            {"package_name": i.key, "installed_version": i.version}
            for i in installed_packages
        ]
    except ImportError:
        try:
            from importlib.metadata import distributions
            data = [
                {"package_name": dist.metadata["Name"].lower(), "installed_version": dist.version}
                for dist in distributions()
            ]
        except Exception:
            data = []

    return pd.DataFrame(data)

def build_environment_snapshot() -> Tuple[EnvironmentSnapshot, pd.DataFrame, Dict[str, Any]]:
    dt_str = datetime.datetime.utcnow().isoformat()
    snap_id = build_environment_snapshot_id(dt_str)

    runtime = collect_python_runtime_info()
    plat = collect_platform_info()
    mem = collect_memory_info()
    gpu = collect_gpu_snapshot()
    packages_df = collect_installed_packages_snapshot()

    warnings_list = []
    if mem["memory_total_mb"] is None:
        warnings_list.append("psutil not available; memory_total_mb is unknown.")

    snapshot = EnvironmentSnapshot(
        snapshot_id=snap_id,
        created_at_utc=dt_str,
        os_name=plat["os_name"],
        platform=plat["platform"],
        python_version=runtime["python_version"],
        executable=runtime["executable"],
        cpu_count=mem["cpu_count"],
        memory_total_mb=mem["memory_total_mb"],
        gpu_available=gpu["gpu_available"],
        package_count=len(packages_df),
        warnings=warnings_list,
    )

    summary = summarize_environment_snapshot(snapshot, packages_df)
    return snapshot, packages_df, summary

def summarize_environment_snapshot(snapshot: EnvironmentSnapshot, packages_df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "snapshot_id": snapshot.snapshot_id,
        "python_version": snapshot.python_version,
        "platform": snapshot.platform,
        "package_count": snapshot.package_count,
        "warnings": snapshot.warnings,
        "is_valid": len(packages_df) > 0,
    }
