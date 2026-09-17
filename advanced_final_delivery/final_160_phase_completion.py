# -*- coding: utf-8 -*-
"""Phase 160: 160-Phase Plan Completion Official Declaration.

Generates the official completion registry declaring the successful closure of the
entire 160-phase development plan at contract, governance, documentation, and acceptance levels.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_delivery.final_delivery_config import (
    FinalDeliveryProfile,
    get_default_final_delivery_profile,
)
from advanced_final_delivery.final_delivery_labels import (
    FINAL_COMPLETION_DOMAIN,
    PHASE_160_COMPLETED,
    FULL_ADVANCED_BOT_FINAL_DELIVERY_READY,
)
from advanced_final_delivery.final_delivery_models import Final160PhaseCompletionItem


def build_final_160_phase_completion_report(
    profile: FinalDeliveryProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build 160-phase completion report DataFrame and summary."""
    active_profile = profile or get_default_final_delivery_profile()

    item = Final160PhaseCompletionItem(
        current_phase=active_profile.current_phase,
        target_final_phase=active_profile.target_final_phase,
        next_phase=active_profile.next_phase,
    )

    rows = [{
        "current_phase": item.current_phase,
        "target_final_phase": item.target_final_phase,
        "next_phase": item.next_phase,
        "plan_status": item.plan_status,
        "mvp_block_status": item.mvp_block_status,
        "advanced_block_status": item.advanced_block_status,
        "backtest_acceptance_block_status": item.backtest_acceptance_block_status,
        "portfolio_acceptance_block_status": item.portfolio_acceptance_block_status,
        "full_system_integration_status": item.full_system_integration_status,
        "final_hardening_status": item.final_hardening_status,
        "final_delivery_status": item.final_delivery_status,
        "local_only": item.local_only,
        "dry_run": item.dry_run,
        "non_production": item.non_production,
        "research_only": item.research_only,
        "live_trading_ready": item.live_trading_ready,
        "broker_ready": item.broker_ready,
        "production_ready": item.production_ready,
        "investment_advice": item.investment_advice,
        "signal_generation": item.signal_generation,
        "model_prediction": item.model_prediction,
        "deployment": item.deployment,
        "manual_review_required": item.manual_review_required,
        "final_delivery_completed": item.final_delivery_completed,
        "domain": item.domain,
        "status": PHASE_160_COMPLETED,
    }]

    df = pd.DataFrame(rows)
    summary = {
        "current_phase": item.current_phase,
        "target_final_phase": item.target_final_phase,
        "next_phase": item.next_phase,
        "plan_status": item.plan_status,
        "mvp_block_status": item.mvp_block_status,
        "advanced_block_status": item.advanced_block_status,
        "backtest_acceptance_block_status": item.backtest_acceptance_block_status,
        "portfolio_acceptance_block_status": item.portfolio_acceptance_block_status,
        "full_system_integration_status": item.full_system_integration_status,
        "final_hardening_status": item.final_hardening_status,
        "final_delivery_status": item.final_delivery_status,
        "phase_160_completed": True,
        "final_plan_closed": True,
        "declaration": (
            "160 fazlık plan local/offline, dry-run, non-production, non-signal, no-broker ve "
            "no-investment-advice sınırları içinde contract/governance/documentation/acceptance "
            "düzeyinde tamamlanmıştır. Bu final teslim canlı trading, broker bağlantısı, "
            "production deployment, kesin AL/SAT sinyali veya yatırım tavsiyesi değildir."
        ),
        "status": PHASE_160_COMPLETED,
    }
    return df, summary


def summarize_final_160_phase_completion(df: pd.DataFrame) -> dict:
    """Summarize 160 phase completion."""
    return {
        "phase_160_completed": True,
        "final_plan_closed": True,
        "status": PHASE_160_COMPLETED,
    }
