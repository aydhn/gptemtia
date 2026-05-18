"""
Runtime metrics collector for tracking pipeline and operation execution times.
"""

import time
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Tuple

import pandas as pd

from observability.observability_models import RuntimeMetric, runtime_metric_to_dict


class RuntimeMetricsCollector:
    """Collects and summarizes execution metrics for offline operations."""

    def __init__(self):
        self.metrics: List[RuntimeMetric] = []
        self._active_timers: Dict[str, Tuple[float, RuntimeMetric]] = {}

    def _get_utc_now_str(self) -> str:
        """Get current UTC time as ISO format string."""
        return datetime.now(timezone.utc).isoformat()

    def start_timer(
        self,
        component: str,
        operation: str,
        symbol: Optional[str] = None,
        timeframe: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Start a timer for an operation and return a metric_id."""
        metric_id = f"timer_{uuid.uuid4().hex[:8]}"

        metric = RuntimeMetric(
            metric_id=metric_id,
            component=component,
            operation=operation,
            started_at_utc=self._get_utc_now_str(),
            finished_at_utc=None,
            duration_seconds=None,
            status="running",
            symbol=symbol,
            timeframe=timeframe,
            metadata=metadata or {}
        )

        self._active_timers[metric_id] = (time.perf_counter(), metric)
        return metric_id

    def stop_timer(self, metric_id: str, status: str = "success", metadata: Optional[Dict[str, Any]] = None) -> Optional[RuntimeMetric]:
        """Stop a timer and record the metric."""
        if metric_id not in self._active_timers:
            return None

        start_time, metric = self._active_timers.pop(metric_id)
        end_time = time.perf_counter()

        duration = end_time - start_time
        # Prevent negative durations due to clock adjustments (though perf_counter should be monotonic)
        duration = max(0.0, duration)

        metric.finished_at_utc = self._get_utc_now_str()
        metric.duration_seconds = duration
        metric.status = status

        if metadata:
            metric.metadata.update(metadata)

        self.record_metric(metric)
        return metric

    def record_metric(self, metric: RuntimeMetric) -> None:
        """Directly record an already completed metric."""
        if metric.duration_seconds is not None and metric.duration_seconds < 0:
            metric.duration_seconds = 0.0
        self.metrics.append(metric)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert collected metrics to a DataFrame."""
        if not self.metrics:
            return pd.DataFrame()

        dicts = [runtime_metric_to_dict(m) for m in self.metrics]
        return pd.DataFrame(dicts)

    def summarize(self) -> Dict[str, Any]:
        """Generate a summary of the collected metrics."""
        if not self.metrics:
            return {
                "metric_count": 0,
                "total_duration_seconds": 0.0,
                "avg_duration_seconds": 0.0,
                "max_duration_seconds": 0.0,
                "by_component": {},
                "by_status": {},
                "slowest_operations": [],
            }

        df = self.to_dataframe()

        # Filter to completed metrics with duration
        completed = df[df['duration_seconds'].notnull()].copy()

        if completed.empty:
            return {
                "metric_count": len(df),
                "total_duration_seconds": 0.0,
                "avg_duration_seconds": 0.0,
                "max_duration_seconds": 0.0,
                "by_component": {},
                "by_status": df['status'].value_counts().to_dict(),
                "slowest_operations": [],
            }

        by_component = completed.groupby('component')['duration_seconds'].agg(['count', 'sum', 'mean']).to_dict(orient='index')
        by_status = df['status'].value_counts().to_dict()

        # Get top 5 slowest operations
        slowest_df = completed.nlargest(5, 'duration_seconds')
        slowest_ops = [
            {
                "operation": row['operation'],
                "component": row['component'],
                "duration_seconds": row['duration_seconds'],
                "symbol": row['symbol']
            }
            for _, row in slowest_df.iterrows()
        ]

        return {
            "metric_count": len(df),
            "total_duration_seconds": float(completed['duration_seconds'].sum()),
            "avg_duration_seconds": float(completed['duration_seconds'].mean()),
            "max_duration_seconds": float(completed['duration_seconds'].max()),
            "by_component": {k: {sk: float(sv) for sk, sv in v.items()} for k, v in by_component.items()},
            "by_status": by_status,
            "slowest_operations": slowest_ops,
        }


# Global instance for shared use if desired
global_metrics_collector = RuntimeMetricsCollector()


@contextmanager
def runtime_timer(
    component: str,
    operation: str,
    symbol: Optional[str] = None,
    timeframe: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    collector: Optional[RuntimeMetricsCollector] = None
):
    """Context manager for timing an operation."""
    metrics_collector = collector or global_metrics_collector
    metric_id = metrics_collector.start_timer(component, operation, symbol, timeframe, metadata)

    try:
        yield metrics_collector
        metrics_collector.stop_timer(metric_id, status="success")
    except Exception as e:
        metrics_collector.stop_timer(metric_id, status="error", metadata={"exception": type(e).__name__})
        raise
