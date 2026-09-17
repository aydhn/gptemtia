# -*- coding: utf-8 -*-
"""Phase 154: Portfolio Optimization Manual Review Queue.

Provides 10 operator checkpoints requiring explicit human oversight before Phase 155.
"""

from typing import Dict, Tuple
import pandas as pd
from .portfolio_optimization_config import PortfolioOptimizationProfile, get_default_portfolio_optimization_profile

MANUAL_REVIEW_CHECKPOINTS = [
    ("MR_154_01", "optimization_contracts", "Optimizasyon Sozlesmeleri", "11 sozlesmenin amac ve kisit baglantilarini incele"),
    ("MR_154_02", "objective_contracts", "Amac Sozlesmeleri", "Mean-variance, Sharpe, CVaR vb. formullerini denetle"),
    ("MR_154_03", "allocation_constraints", "Tahsisat Kisitlari", "22 tahsisat kisitinin sinirlarini incele"),
    ("MR_154_04", "solver_placeholders", "Cozucu Yer Tutuculari", "Cozucu sozlesmelerinin stub modda oldugunu dogrula"),
    ("MR_154_05", "efficient_frontier_placeholders", "Etkin Sinir", "Etkin sinirin gercek nokta icermedigini teyit et"),
    ("MR_154_06", "output_contracts", "Cikti Sozlesmeleri", "Ciktilarin agirlik veya emir icermedigini teyit et"),
    ("MR_154_07", "claim_guards", "Iddia Muhafizlari", "Tahsisat, agirlik ve rebalance iddia muhafizlarini denetle"),
    ("MR_154_08", "investment_advice_guards", "Yatirim Tavsiyesi Muhafizi", "Non-advisory statuyu dogrula"),
    ("MR_154_09", "disabled_execution_reports", "Devre Disi Raporlar", "10 engelleme raporunun aktif oldugunu incele"),
    ("MR_154_10", "phase_155_handoff", "Phase 155 Devir Sartlari", "Risk Raporlama fazina gecis onkosullarini onayla"),
]


def build_portfolio_optimization_manual_review_queue(
    profile: PortfolioOptimizationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build manual review queue table."""
    records = []
    for chk_id, domain, target, desc in MANUAL_REVIEW_CHECKPOINTS:
        records.append({
            "checkpoint_id": chk_id,
            "domain": domain,
            "review_target": target,
            "description": desc,
            "status": "PENDING_OPERATOR_REVIEW",
            "recommendation": "Operator manual inspection required before proceeding to next phase",
            "is_blocking": True,
        })
    df = pd.DataFrame(records)
    summary = {
        "checkpoint_count": len(records),
        "pending_count": len(records),
        "manual_review_required": True,
    }
    return df, summary
