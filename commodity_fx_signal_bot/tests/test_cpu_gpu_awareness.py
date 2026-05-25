import pytest
from performance.performance_config import get_default_performance_profile
from performance.cpu_gpu_awareness import (
    detect_cpu_info,
    detect_memory_info,
    detect_gpu_info,
    detect_torch_cuda_info,
    build_cpu_gpu_awareness_report
)

def test_detect_cpu_info():
    info = detect_cpu_info()
    assert "platform" in info
    assert "cpu_count_logical" in info

def test_detect_memory_info():
    info = detect_memory_info()
    assert isinstance(info, dict)

def test_detect_torch_cuda_info():
    info = detect_torch_cuda_info()
    assert "warning" in info or "cuda_available" in info

def test_detect_gpu_info():
    info = detect_gpu_info()
    assert isinstance(info, dict)

def test_build_cpu_gpu_awareness_report():
    profile = get_default_performance_profile()
    df, summary = build_cpu_gpu_awareness_report(profile)
    assert not df.empty
    assert "cpu_count" in summary
    assert "gpu_detected" in summary
