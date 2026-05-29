import pytest
from analyst_ux.ux_config import get_default_analyst_ux_profile
from analyst_ux.cheat_sheets import (
    build_command_cheat_sheet, build_safe_query_examples,
    build_module_quick_reference, build_operator_shortcuts_reference
)
import pandas as pd

def test_cheat_sheets():
    profile = get_default_analyst_ux_profile()

    cmd_sheet = build_command_cheat_sheet(pd.DataFrame([{"alias_name": "x", "command": "y", "description": "z"}]), profile)
    assert "Command Cheat Sheet" in cmd_sheet
    assert "AL/SAT örnekleri yok" in cmd_sheet

    query_sheet = build_safe_query_examples(profile)
    assert "Yatırım tavsiyesi üretmeyen" in query_sheet

    ref_sheet = build_module_quick_reference(profile)
    assert "final_review" in ref_sheet

    op_sheet = build_operator_shortcuts_reference(pd.DataFrame([{"name": "a", "purpose": "b"}]), profile)
    assert "Operator Shortcuts" in op_sheet
