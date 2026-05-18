import pytest
import time

from observability.runtime_metrics import RuntimeMetricsCollector, runtime_timer

def test_start_stop_timer():
    collector = RuntimeMetricsCollector()
    metric_id = collector.start_timer("test_comp", "test_op")
    assert metric_id in collector._active_timers

    time.sleep(0.01) # ensure some duration
    metric = collector.stop_timer(metric_id)

    assert metric is not None
    assert metric.duration_seconds is not None
    assert metric.duration_seconds > 0
    assert metric.status == "success"
    assert len(collector.metrics) == 1

def test_context_manager():
    collector = RuntimeMetricsCollector()

    with runtime_timer("test_comp", "test_op", collector=collector):
        time.sleep(0.01)

    assert len(collector.metrics) == 1
    metric = collector.metrics[0]
    assert metric.duration_seconds > 0
    assert metric.status == "success"

def test_context_manager_error():
    collector = RuntimeMetricsCollector()

    with pytest.raises(ValueError):
        with runtime_timer("test_comp", "test_op", collector=collector):
            raise ValueError("Test error")

    assert len(collector.metrics) == 1
    metric = collector.metrics[0]
    assert metric.status == "error"
    assert metric.metadata["exception"] == "ValueError"

def test_summarize():
    collector = RuntimeMetricsCollector()

    collector.start_timer("comp1", "op1")
    m1 = list(collector._active_timers.keys())[0]
    time.sleep(0.01)
    collector.stop_timer(m1, status="success")

    collector.start_timer("comp1", "op2")
    m2 = list(collector._active_timers.keys())[0]
    time.sleep(0.02)
    collector.stop_timer(m2, status="error")

    summary = collector.summarize()
    assert summary["metric_count"] == 2
    assert "comp1" in summary["by_component"]
    assert summary["by_status"]["success"] == 1
    assert summary["by_status"]["error"] == 1
