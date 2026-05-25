import platform
import os
import subprocess
import pandas as pd
from typing import Dict, Tuple

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from .performance_config import PerformanceProfile

def detect_cpu_info() -> dict:
    info = {
        "platform": platform.platform(),
        "os_name": os.name,
        "python_version": platform.python_version(),
        "cpu_count_logical": os.cpu_count(),
    }
    if PSUTIL_AVAILABLE:
        info["cpu_count_physical"] = psutil.cpu_count(logical=False)
        info["cpu_freq_max_mhz"] = getattr(psutil.cpu_freq(), 'max', None) if hasattr(psutil, 'cpu_freq') and psutil.cpu_freq() else None
    return info

def detect_memory_info() -> dict:
    if PSUTIL_AVAILABLE:
        mem = psutil.virtual_memory()
        return {
            "total_memory_gb": mem.total / (1024 ** 3),
            "available_memory_gb": mem.available / (1024 ** 3),
            "memory_percent_used": mem.percent
        }
    return {"warning": "psutil not available, cannot detect memory info"}

def detect_torch_cuda_info() -> dict:
    try:
        import torch
        return {
            "torch_version": torch.__version__,
            "cuda_available": torch.cuda.is_available(),
            "device_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
            "device_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() and torch.cuda.device_count() > 0 else None
        }
    except ImportError:
        return {"warning": "torch not available"}

def detect_nvidia_smi_info(timeout_seconds: int = 5) -> dict:
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            gpus = []
            for line in lines:
                parts = line.split(', ')
                if len(parts) == 3:
                    gpus.append({
                        "name": parts[0],
                        "memory_total": parts[1],
                        "memory_free": parts[2]
                    })
            return {"nvidia_smi_gpus": gpus}
        else:
            return {"warning": f"nvidia-smi failed: {result.stderr}"}
    except FileNotFoundError:
        return {"warning": "nvidia-smi not found"}
    except subprocess.TimeoutExpired:
        return {"warning": "nvidia-smi timed out"}
    except Exception as e:
        return {"warning": f"nvidia-smi error: {str(e)}"}

def detect_gpu_info() -> dict:
    info = {}
    info.update(detect_torch_cuda_info())
    info.update(detect_nvidia_smi_info())
    return info

def build_cpu_gpu_awareness_report(profile: PerformanceProfile) -> Tuple[pd.DataFrame, Dict]:
    records = []

    cpu_info = detect_cpu_info()
    for k, v in cpu_info.items():
        records.append({"component": "CPU/OS", "key": k, "value": str(v)})

    mem_info = detect_memory_info()
    for k, v in mem_info.items():
        records.append({"component": "Memory", "key": k, "value": str(v)})

    gpu_info = {}
    if profile.detect_gpu:
        gpu_info = detect_gpu_info()
        for k, v in gpu_info.items():
            records.append({"component": "GPU", "key": k, "value": str(v)})

        has_gpu = gpu_info.get("cuda_available", False) or "nvidia_smi_gpus" in gpu_info
        if not has_gpu:
            records.append({"component": "GPU", "key": "status", "value": "gpu_optional_unavailable_or_unused"})

    df = pd.DataFrame(records)

    summary = {
        "cpu_count": cpu_info.get("cpu_count_logical", 0),
        "total_memory_gb": mem_info.get("total_memory_gb", 0) if "total_memory_gb" in mem_info else 0,
        "gpu_detected": gpu_info.get("cuda_available", False) or "nvidia_smi_gpus" in gpu_info if profile.detect_gpu else False
    }

    return df, summary
