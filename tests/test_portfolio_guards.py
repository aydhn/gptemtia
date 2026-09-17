# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Guards."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.portfolio_no_lookahead_guards import (
    build_portfolio_no_lookahead_guard_registry,
    validate_portfolio_no_lookahead_columns,
)
from advanced_portfolio_construction.portfolio_allocation_claim_guards import (
    build_portfolio_allocation_claim_guard_registry,
    validate_portfolio_allocation_claims,
)
from advanced_portfolio_construction.portfolio_position_sizing_claim_guards import (
    build_portfolio_position_sizing_claim_guard_registry,
    validate_portfolio_position_sizing_claims,
)
from advanced_portfolio_construction.portfolio_investment_advice_guards import (
    build_portfolio_investment_advice_guard_registry,
    validate_portfolio_no_investment_advice,
)
from advanced_portfolio_construction.portfolio_risk_limit_claim_guards import (
    build_portfolio_risk_limit_claim_guard_registry,
    validate_portfolio_risk_limit_claims,
)
from advanced_portfolio_construction.portfolio_data_snooping_bias_guards import (
    build_portfolio_data_snooping_bias_guard_registry,
    validate_portfolio_data_snooping_claims,
)
from advanced_portfolio_construction.portfolio_overfitting_guards import (
    build_portfolio_overfitting_guard_registry,
    validate_portfolio_overfitting_claims,
)
from advanced_portfolio_construction.portfolio_multiple_testing_guards import (
    build_portfolio_multiple_testing_guard_registry,
    validate_portfolio_multiple_testing_claims,
)
from advanced_portfolio_construction.portfolio_metadata_only_news_guards import (
    build_portfolio_metadata_only_news_guard_registry,
    validate_portfolio_news_columns,
)
from advanced_portfolio_construction.portfolio_source_preservation_guards import (
    build_portfolio_source_preservation_guard_registry,
    validate_portfolio_source_preservation,
)
from advanced_portfolio_construction.portfolio_forbidden_column_policies import (
    build_portfolio_forbidden_column_policy_registry,
    validate_portfolio_forbidden_columns,
)


def test_lookahead_guard():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_portfolio_no_lookahead_guard_registry(profile)
    assert len(df) >= 3
    assert summary["all_active"] is True

    clean_res = validate_portfolio_no_lookahead_columns(["open", "high", "low", "close", "volume"])
    assert clean_res["is_clean"] is True
    assert clean_res["status"] == "PASS"

    dirty_res = validate_portfolio_no_lookahead_columns(["close", "future_return_5d"])
    assert dirty_res["is_clean"] is False
    assert dirty_res["status"] == "BLOCKED_BY_LOOKAHEAD_GUARD"


def test_allocation_and_sizing_claim_guards():
    clean_res = validate_portfolio_allocation_claims(["theoretical_weight_contract"])
    assert clean_res["is_clean"] is True

    viol_res = validate_portfolio_allocation_claims(["real_capital_deployed", "weights_enforced_live"])
    assert viol_res["is_clean"] is False
    assert viol_res["status"] == "BLOCKED_BY_ALLOCATION_CLAIM_GUARD"

    clean_sz = validate_portfolio_position_sizing_claims(["fractional_risk_parameter"])
    assert clean_sz["is_clean"] is True

    viol_sz = validate_portfolio_position_sizing_claims(["real_lot_sized"])
    assert viol_sz["is_clean"] is False
    assert viol_sz["status"] == "BLOCKED_BY_POSITION_SIZING_CLAIM_GUARD"


def test_investment_advice_guard():
    clean_text = "This report details portfolio contract parameters."
    assert validate_portfolio_no_investment_advice(clean_text)["is_clean"] is True

    dirty_text = "You should BUY NOW with guaranteed return."
    assert validate_portfolio_no_investment_advice(dirty_text)["is_clean"] is False


def test_risk_limit_and_bias_guards():
    assert validate_portfolio_risk_limit_claims(["broker_margin_enforced"])["is_clean"] is False
    assert validate_portfolio_data_snooping_claims(["cherry_picked_in_sample"])["is_clean"] is False
    assert validate_portfolio_overfitting_claims(["overfitted_weights"])["is_clean"] is False
    assert validate_portfolio_multiple_testing_claims(["p_hacked_weights"])["is_clean"] is False


def test_news_metadata_and_source_preservation():
    clean_cols = ["timestamp", "sentiment_score", "entity_mentions_count"]
    assert validate_portfolio_news_columns(clean_cols)["is_clean"] is True

    bad_cols = ["timestamp", "full_article_body", "raw_html"]
    assert validate_portfolio_news_columns(bad_cols)["is_clean"] is False

    assert validate_portfolio_source_preservation("read_only")["is_safe"] is True
    assert validate_portfolio_source_preservation("overwrite_raw")["is_safe"] is False


def test_forbidden_column_policy():
    clean_cols = ["symbol", "open", "close"]
    assert validate_portfolio_forbidden_columns(clean_cols)["is_clean"] is True

    bad_cols = ["symbol", "api_key", "broker_account_number"]
    assert validate_portfolio_forbidden_columns(bad_cols)["is_clean"] is False
