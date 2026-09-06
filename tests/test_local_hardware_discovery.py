"""Test suite for Phase 136 Local Hardware Discovery."""

import pytest
from advanced_gpu_ml_runtime.local_hardware_discovery import (
    build_local_hardware_discovery_report,
    safe_collect_platform_info,
    safe_collect_python_info,
)


def test_safe_collect_platform_and_python_info():
    plat = safe_collect_platform_info()
    assert "os_name" in plat
    assert "architecture" in plat

    py = safe_collect_python_info()
    assert "python_version" in py
    assert "python_implementation" in py


def test_build_local_hardware_discovery_report():
    df, summary = build_local_hardware_discovery_report()
    assert not df.empty
    assert summary["total_items"] > 0
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["official_approval"] is False
    assert summary["production_ready"] is False
    assert summary["broker_ready"] is False
