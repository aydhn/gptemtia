import pytest
import pandas as pd
from notifications.message_templates import (
    build_header,
    build_disclaimer,
    build_section,
    build_table_like_lines
)

def test_build_header():
    header = build_header("Test", "info")
    assert "Test" in header
    assert "ℹ️" in header

def test_build_disclaimer():
    disclaimer = build_disclaimer()
    assert "simülasyon" in disclaimer
    assert "gerçek emir" in disclaimer

def test_build_section():
    section = build_section("Test Section", ["Line 1", "Line 2"])
    assert "Test Section" in section
    assert "Line 1" in section

def test_build_table_like_lines():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    lines = build_table_like_lines(df, ["A"], max_rows=2)
    assert len(lines) == 5 # Header, separator, 2 rows, "... (+1 satır)"
    assert "... (+1 satır)" in lines[-1]

def test_forbidden_trade_instruction_not_produced_by_templates():
    disclaimer = build_disclaimer()
    assert "BUY" not in disclaimer
    assert "SELL" not in disclaimer
    assert "EMİR GÖNDER" not in disclaimer
