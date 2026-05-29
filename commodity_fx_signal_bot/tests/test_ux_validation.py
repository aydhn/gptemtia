import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.ux_validation import build_ux_validation_report
import pandas as pd

def test_ux_validation():
    profile = get_default_analyst_ux_profile()

    # Empty tables should fail validation or just return passed false
    df, summary = build_ux_validation_report({}, profile)
    assert not summary["passed"]

    tables = {
        "aliases": pd.DataFrame([{"alias_id": "1", "command": "cmd", "safety_label": "safe"}]),
        "intents": pd.DataFrame([{"id": "1"}]),
        "suggestions": pd.DataFrame([{"safety_label": "safe"}]),
        "prompts": pd.DataFrame([{"warnings": ["offline disclaimer"]}]),
        "shortcuts": pd.DataFrame([{"id": "1"}])
    }

    df, summary = build_ux_validation_report(tables, profile)
    assert summary["passed"]
