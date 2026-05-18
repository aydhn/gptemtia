import pytest
from pathlib import Path
import json

from observability.structured_logger import StructuredLogger


def test_structured_logger_levels(tmp_path):
    log_dir = tmp_path / "logs"
    logger = StructuredLogger(component="data_lake", log_dir=log_dir, json_logs_enabled=True)

    # Generate some logs
    logger.info("startup", "System started")
    logger.warning("deprecated", "Deprecated feature used")
    logger.error("io_error", "File not found", metadata={"file": "test.txt"})
    logger.critical("fatal_error", "Out of memory")

    assert len(logger.records) == 4

    # Check levels
    assert logger.records[0].level == "INFO"
    assert logger.records[1].level == "WARNING"
    assert logger.records[2].level == "ERROR"
    assert logger.records[3].level == "CRITICAL"

    # Check JSON output
    json_file = log_dir / "data_lake.jsonl"
    assert json_file.exists()

    with open(json_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 4

        data = json.loads(lines[2])
        assert data["level"] == "ERROR"
        assert data["event_name"] == "io_error"
        assert data["metadata"]["file"] == "test.txt"


def test_structured_logger_dataframe():
    logger = StructuredLogger(component="config")

    logger.info("test1", "msg1")
    logger.error("test2", "msg2")

    df = logger.to_dataframe()
    assert len(df) == 2
    assert "timestamp_utc" in df.columns
    assert "level" in df.columns
    assert list(df["level"].values) == ["INFO", "ERROR"]


def test_structured_logger_masking():
    logger = StructuredLogger(component="config")

    record = logger.info("auth", "Sending to chat_id=1234567")

    assert "********" in record.message
    assert "1234567" not in record.message

    # Also verify metadata masking in dict conversion
    record2 = logger.info("auth2", "auth event", metadata={"bot_token": "abc:123"})
    from observability.observability_models import structured_log_record_to_dict
    d = structured_log_record_to_dict(record2)
    assert d["metadata"]["bot_token"] == "********"


def test_structured_logger_invalid_component():
    # It should fallback to unknown_component without crashing
    logger = StructuredLogger(component="invalid_component_xyz")
    assert logger.component == "unknown_component"
