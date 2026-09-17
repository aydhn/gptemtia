# -*- coding: utf-8 -*-
"""Phase 146: Realistic Backtest, Transaction Cost and Slippage Modeling Package.

Provides contract-based backtesting specifications, order simulation mechanics,
transaction cost models, slippage models, execution realism placeholders,
bias and lookahead guards, and safe handoff to Phase 147.
"""

from advanced_realistic_backtest.realistic_backtest_config import (
    RealisticBacktestProfile,
    get_default_realistic_backtest_profile,
    get_realistic_backtest_profile,
    list_realistic_backtest_profiles,
    validate_realistic_backtest_profiles,
)
from advanced_realistic_backtest.realistic_backtest_models import (
    BacktestEngineContract,
    BacktestFinding,
    BacktestGuardItem,
    BacktestManualReviewItem,
    BacktestReadinessScore,
    OrderSimulationContract,
    RealisticBacktestManifest,
    RealisticBacktestProfileItem,
    SlippageModelContract,
    TransactionCostModelContract,
)
from advanced_realistic_backtest.realistic_backtest_pipeline import (
    RealisticBacktestPipeline,
)

__all__ = [
    "RealisticBacktestProfile",
    "get_default_realistic_backtest_profile",
    "get_realistic_backtest_profile",
    "list_realistic_backtest_profiles",
    "validate_realistic_backtest_profiles",
    "RealisticBacktestProfileItem",
    "BacktestEngineContract",
    "OrderSimulationContract",
    "TransactionCostModelContract",
    "SlippageModelContract",
    "BacktestGuardItem",
    "BacktestFinding",
    "BacktestManualReviewItem",
    "BacktestReadinessScore",
    "RealisticBacktestManifest",
    "RealisticBacktestPipeline",
]
