import pytest
import pandas as pd
from analyst_ux.ux_report_builder import (
    build_alias_markdown_report, build_safe_command_suggestion_markdown_report,
    build_prompt_pack_markdown_report, build_productivity_checklist_markdown_report,
    build_task_board_markdown_report
)

def test_report_builders():
    df = pd.DataFrame([{"test": "data"}])

    alias_md = build_alias_markdown_report({}, df)
    assert "offline analyst UX/productivity" in alias_md

    sugg_md = build_safe_command_suggestion_markdown_report({}, df)
    assert "yatırım tavsiyesi değildir" in sugg_md

    pack_md = build_prompt_pack_markdown_report({}, df)
    assert "production scheduler" in pack_md

    check_md = build_productivity_checklist_markdown_report({}, df)
    assert "gerçek emir" in check_md

    task_md = build_task_board_markdown_report({}, df)
    assert "otomatik trade" in task_md.lower() or "yatırım tavsiyesi" in task_md.lower()
