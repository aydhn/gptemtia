"""
Structured logger implementation for producing structured logs and tracking events.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any

import pandas as pd

from observability.logging_config import get_logger, mask_sensitive_values
from observability.observability_labels import validate_component_label
from observability.observability_models import StructuredLogRecord, structured_log_record_to_dict


class StructuredLogger:
    """Produces structured logs and tracks events."""

    def __init__(self, component: str, log_dir: Optional[Path] = None, json_logs_enabled: bool = False):
        try:
            validate_component_label(component)
        except ValueError:
            # Fallback to unknown if invalid but log the actual component in metadata
            component = "unknown_component"

        self.component = component
        self.logger = get_logger(component)
        self.log_dir = log_dir
        self.json_logs_enabled = json_logs_enabled
        self.records: List[StructuredLogRecord] = []

    def _get_utc_now_str(self) -> str:
        """Get current UTC time as ISO format string."""
        return datetime.now(timezone.utc).isoformat()

    def log_event(
        self,
        level: str,
        event_name: str,
        message: str,
        run_id: Optional[str] = None,
        symbol: Optional[str] = None,
        timeframe: Optional[str] = None,
        job_id: Optional[str] = None,
        error_category: Optional[str] = None,
        error_code: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> StructuredLogRecord:
        """Create a structured log record, output it via python logging, and optionally save as JSON."""

        # Ensure message is masked
        safe_message = mask_sensitive_values(message)

        record = StructuredLogRecord(
            timestamp_utc=self._get_utc_now_str(),
            level=level.upper(),
            component=self.component,
            event_name=event_name,
            message=safe_message,
            run_id=run_id,
            symbol=symbol,
            timeframe=timeframe,
            job_id=job_id,
            error_category=error_category,
            error_code=error_code,
            metadata=metadata or {},
        )

        self.records.append(record)

        # Route to standard Python logger
        log_msg = f"[{event_name}] {safe_message}"
        if level.upper() == "DEBUG":
            self.logger.debug(log_msg)
        elif level.upper() == "INFO":
            self.logger.info(log_msg)
        elif level.upper() == "WARNING":
            self.logger.warning(log_msg)
        elif level.upper() == "ERROR":
            self.logger.error(log_msg)
        elif level.upper() == "CRITICAL" or level.upper() == "FATAL":
            self.logger.critical(log_msg)

        # Optionally write JSON to file
        if self.json_logs_enabled and self.log_dir:
            self._write_json_log(record)

        return record

    def _write_json_log(self, record: StructuredLogRecord) -> None:
        """Append the structured record as a JSON line to the component's json log file."""
        if not self.log_dir:
            return

        self.log_dir.mkdir(parents=True, exist_ok=True)
        json_file = self.log_dir / f"{self.component}.jsonl"

        try:
            record_dict = structured_log_record_to_dict(record)
            with open(json_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(record_dict) + '\n')
        except Exception as e:
            self.logger.error(f"Failed to write JSON log: {str(e)}")

    def info(self, event_name: str, message: str, **kwargs) -> StructuredLogRecord:
        """Log an INFO level event."""
        return self.log_event(level="INFO", event_name=event_name, message=message, **kwargs)

    def warning(self, event_name: str, message: str, **kwargs) -> StructuredLogRecord:
        """Log a WARNING level event."""
        return self.log_event(level="WARNING", event_name=event_name, message=message, **kwargs)

    def error(self, event_name: str, message: str, **kwargs) -> StructuredLogRecord:
        """Log an ERROR level event."""
        return self.log_event(level="ERROR", event_name=event_name, message=message, **kwargs)

    def critical(self, event_name: str, message: str, **kwargs) -> StructuredLogRecord:
        """Log a CRITICAL level event."""
        return self.log_event(level="CRITICAL", event_name=event_name, message=message, **kwargs)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert the captured structured log records to a pandas DataFrame."""
        if not self.records:
            return pd.DataFrame()

        dicts = [structured_log_record_to_dict(r) for r in self.records]
        return pd.DataFrame(dicts)
