# -*- coding: utf-8 -*-
"""Unit tests for Phase 153 Portfolio Limit Contracts & Placeholders."""

from advanced_portfolio_construction.portfolio_construction_config import (
    get_default_portfolio_construction_profile,
)
from advanced_portfolio_construction.concentration_limit_contracts import (
    build_concentration_limit_contract_registry,
)
from advanced_portfolio_construction.exposure_limit_contracts import (
    build_exposure_limit_contract_registry,
)
from advanced_portfolio_construction.leverage_limit_placeholders import (
    build_leverage_limit_placeholder_registry,
)
from advanced_portfolio_construction.margin_limit_placeholders import (
    build_margin_limit_placeholder_registry,
)
from advanced_portfolio_construction.notional_limit_placeholders import (
    build_notional_limit_placeholder_registry,
)
from advanced_portfolio_construction.currency_exposure_limit_placeholders import (
    build_currency_exposure_limit_placeholder_registry,
)
from advanced_portfolio_construction.cross_asset_exposure_limit_placeholders import (
    build_cross_asset_exposure_limit_placeholder_registry,
)
from advanced_portfolio_construction.sector_group_exposure_placeholders import (
    build_sector_group_exposure_placeholder_registry,
)


def test_concentration_limit_contracts():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_concentration_limit_contract_registry(profile)
    assert len(df) >= 3
    assert df["contract_only"].all() == True
    assert df["actual_limits_assigned"].all() == False


def test_exposure_limit_contracts():
    profile = get_default_portfolio_construction_profile()
    df, summary = build_exposure_limit_contract_registry(profile)
    assert len(df) >= 4
    assert df["contract_only"].all() == True
    assert df["actual_limits_assigned"].all() == False


def test_leverage_and_margin_placeholders():
    profile = get_default_portfolio_construction_profile()
    df_lev, _ = build_leverage_limit_placeholder_registry(profile)
    df_mrg, _ = build_margin_limit_placeholder_registry(profile)
    assert len(df_lev) >= 3
    assert len(df_mrg) >= 3
    assert df_lev["real_leverage_enforced"].all() == False
    assert df_mrg["real_margin_calculated"].all() == False


def test_notional_and_currency_placeholders():
    profile = get_default_portfolio_construction_profile()
    df_not, _ = build_notional_limit_placeholder_registry(profile)
    df_ccy, _ = build_currency_exposure_limit_placeholder_registry(profile)
    assert len(df_not) >= 3
    assert len(df_ccy) >= 3
    assert df_not["real_notional_computed"].all() == False
    assert df_ccy["real_currency_hedging_applied"].all() == False


def test_cross_asset_and_sector_placeholders():
    profile = get_default_portfolio_construction_profile()
    df_xast, _ = build_cross_asset_exposure_limit_placeholder_registry(profile)
    df_sec, _ = build_sector_group_exposure_placeholder_registry(profile)
    assert len(df_xast) >= 3
    assert len(df_sec) >= 3
    assert df_xast["real_cross_asset_hedging"].all() == False
    assert df_sec["real_sector_rebalancing"].all() == False
