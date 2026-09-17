# -*- coding: utf-8 -*-
"""Phase 154: Advanced Portfolio Optimization and Allocation Constraints Package.

Provides local/offline contract layer, objective function templates, allocation
constraints, solver placeholders, guards, and Phase 155 handoff infrastructure.
"""

from .portfolio_optimization_config import (
    PortfolioOptimizationProfile,
    get_portfolio_optimization_profile,
    get_default_portfolio_optimization_profile,
    list_portfolio_optimization_profiles,
    validate_portfolio_optimization_profiles,
)
from .portfolio_optimization_labels import (
    OPTIMIZATION_CONTRACT_READY,
    EXECUTION_CONTRACT_ONLY,
    ALL_DOMAINS,
)
from .portfolio_optimization_models import (
    PortfolioOptimizationProfileItem,
    PortfolioOptimizationContract,
    OptimizationObjectiveContract,
    AllocationConstraintContract,
    SolverContract,
    OptimizationMetricPlaceholder,
    OptimizationGuardItem,
    OptimizationDisabledExecutionItem,
    PortfolioOptimizationFinding,
    PortfolioOptimizationReadinessScore,
    PortfolioOptimizationManifest,
    PortfolioOptimizationManualReviewItem,
)

__version__ = "154.0.0"
__all__ = [
    "PortfolioOptimizationProfile",
    "get_portfolio_optimization_profile",
    "get_default_portfolio_optimization_profile",
    "list_portfolio_optimization_profiles",
    "validate_portfolio_optimization_profiles",
    "OPTIMIZATION_CONTRACT_READY",
    "EXECUTION_CONTRACT_ONLY",
    "ALL_DOMAINS",
    "PortfolioOptimizationProfileItem",
    "PortfolioOptimizationContract",
    "OptimizationObjectiveContract",
    "AllocationConstraintContract",
    "SolverContract",
    "OptimizationMetricPlaceholder",
    "OptimizationGuardItem",
    "OptimizationDisabledExecutionItem",
    "PortfolioOptimizationFinding",
    "PortfolioOptimizationReadinessScore",
    "PortfolioOptimizationManifest",
    "PortfolioOptimizationManualReviewItem",
]
