"""Test suite for Phase 139 Dry-Run Training Execution Blocks."""

from advanced_gpu_training_governance.gpu_training_governance_config import (
    get_default_gpu_training_governance_profile,
)
from advanced_gpu_training_governance.dry_run_training_execution_blocks import (
    FORBIDDEN_EXECUTION_KEYWORDS,
    build_dry_run_training_execution_block_report,
    summarize_dry_run_training_execution_blocks,
    validate_training_execution_block,
)


def test_build_dry_run_training_execution_block_report():
    profile = get_default_gpu_training_governance_profile()
    df, summary = build_dry_run_training_execution_block_report(profile)

    assert len(df) == len(FORBIDDEN_EXECUTION_KEYWORDS)
    assert summary["total_keywords_checked"] == len(df)
    assert summary["all_blocked"] is True
    assert summary["all_dry_run"] is True
    assert summary["non_signal"] is True


def test_validate_training_execution_block():
    assert validate_training_execution_block("safe query without keywords")["blocked"] is False

    for kw in FORBIDDEN_EXECUTION_KEYWORDS:
        res = validate_training_execution_block(f"please run {kw} now")
        assert res["blocked"] is True
        assert kw in res["detected_keywords"]
        assert res["real_training_executed"] is False
        assert res["model_fit_executed"] is False
        assert res["non_signal"] is True
