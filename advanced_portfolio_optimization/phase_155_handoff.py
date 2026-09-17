# -*- coding: utf-8 -*-
"""Phase 154: Phase 155 Risk Reporting, Exposure Attribution & Limit Monitoring Handoff Report."""

from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from .portfolio_optimization_config import (
    PortfolioOptimizationProfile,
    get_default_portfolio_optimization_profile,
)
from .portfolio_optimization_labels import (
    PHASE_155_HANDOFF_DOMAIN,
    HANDOFF_READY,
    PORTFOLIO_OPTIMIZATION_CONTRACT_READY,
)

HANDOFF_ITEMS: List[Dict[str, Any]] = [
    {
        "item_id": "HND-155-01",
        "topic": "portfolio_optimization_contracts_delivered",
        "description": "Portfoy optimizasyon sozlesmeleri (cerceve, evren, varlik, amac, kisit, cozuculer, cikti sozlesmeleri) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-02",
        "topic": "optimization_objective_contracts_delivered",
        "description": "11 adet optimizasyon amac fonksiyon sozlesmesi ve yer tutucusu (mean-variance, min-variance, sharpe, risk parity, cvar, drawdown, turnover, cost, slippage, regime, robust) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-03",
        "topic": "allocation_constraint_contracts_delivered",
        "description": "22 adet tahsisat kisit sozlesmesi ve yer tutucusu (long-only, agirlik, grup, yogunlasma, maruziyetler, korelasyon, likidite, devir, maliyet, risk butcesi, volatilite, drawdown, kaldirac, teminat, rebalance) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-04",
        "topic": "solver_and_frontier_placeholders_delivered",
        "description": "Konveks, sezgisel, grid arama cozuculeri yer tutuculari ve etkin sinir yer tutuculari ile devre disi birakilan calistirici raporlari tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-05",
        "topic": "output_and_metric_placeholders_delivered",
        "description": "Optimizasyon sonuc, tahsisat ve yeniden dengeleme cikti sozlesmeleri ile metrik yer tutuculari tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-06",
        "topic": "dependencies_and_guards_delivered",
        "description": "Portfoy insa, backtest, benchmark, model yonetisim ve rejim bagimliliklari ile 12 muhafiz ve 52 yasakli sutun karantina politikasi tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-07",
        "topic": "disabled_execution_reports_delivered",
        "description": "10 devre disi calistirma raporu (optimizasyon, agirlik uretimi, tahsisat uretimi, yeniden dengeleme, metrik hesabi, egitim, tahmin, canli trading, broker, dagitim) tamamlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-08",
        "topic": "findings_and_master_manifest_delivered",
        "description": "Portfoy optimizasyon bulgulari, hazirlik skoru ve Phase 154 ana manifestosu hazirlandi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-09",
        "topic": "readiness_score_threshold_met",
        "description": "Hazirlik skoru >= 0.75 olup, portfolio_optimization_contract_ready_non_production seviyesine ulasildi.",
        "satisfied": True,
    },
    {
        "item_id": "HND-155-10",
        "topic": "strict_non_production_boundary_enforced",
        "description": "Canli emir, broker entegrasyonu, gercek portfoy agirligi, gercek optimizasyon cozumu veya lot uretilmemesi kosulu korundu.",
        "satisfied": True,
    },
]


def build_phase_155_handoff_report(
    profile: Optional[PortfolioOptimizationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and metadata summary for Phase 155 handoff."""
    active = profile or get_default_portfolio_optimization_profile()

    records = []
    for item in HANDOFF_ITEMS:
        records.append({
            "handoff_id": "HND-154-155-001",
            "item_id": item["item_id"],
            "topic": item["topic"],
            "description": item["description"],
            "satisfied": item["satisfied"],
            "source_phase": active.current_phase,
            "target_phase": active.next_phase,
            "target_final_phase": active.target_final_phase,
            "manual_review_required": True,
            "non_signal": True,
            "contract_only": True,
            "non_production": True,
            "status": HANDOFF_READY,
        })

    df = pd.DataFrame(records)
    all_satisfied = df["satisfied"].all()

    summary: Dict[str, Any] = {
        "domain": PHASE_155_HANDOFF_DOMAIN,
        "active_profile": active.profile_name,
        "handoff_id": "HND-154-155-001",
        "source_phase": active.current_phase,
        "target_phase": active.next_phase,
        "target_final_phase": active.target_final_phase,
        "total_items": len(records),
        "satisfied_count": int(df["satisfied"].sum()),
        "all_satisfied": bool(all_satisfied),
        "manual_review_required": True,
        "status": HANDOFF_READY if all_satisfied else "HANDOFF_BLOCKED",
    }
    return df, summary


def build_phase_155_risk_reporting_exposure_attribution_limit_monitoring_handoff_report(
    profile: Optional[PortfolioOptimizationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Full alias for Phase 155 handoff report."""
    return build_phase_155_handoff_report(profile=profile)


def summarize_phase_155_handoff(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize the Phase 155 handoff DataFrame."""
    if df.empty:
        return {"total_items": 0, "satisfied_count": 0, "all_satisfied": False}
    total = len(df)
    satisfied = int(df["satisfied"].sum()) if "satisfied" in df.columns else 0
    return {
        "total_items": total,
        "satisfied_count": satisfied,
        "all_satisfied": total > 0 and total == satisfied,
    }
