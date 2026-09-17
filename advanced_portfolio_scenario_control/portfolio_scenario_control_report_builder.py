# -*- coding: utf-8 -*-
"""Phase 156: Portfolio Scenario Control Markdown Report Builder."""

from typing import Any, Dict
import pandas as pd
from .portfolio_scenario_control_config import PortfolioScenarioControlProfile

SCENARIO_CONTROL_DISCLAIMER = (
    "UYARI: Bu rapor Phase 156 Portfolio Scenario Testing and Drawdown Control sozlesme ciktisidir. "
    "Gercek senaryo yurumesi, senaryo PnL hesaplamasi, portfoy duzeltmesi, gercek drawdown hesaplamasi, "
    "kademeli risk azaltma/hedge emirleri, broker baglantisi, canli trading veya yatirim tavsiyesi degildir. "
    "Cevrimdisi ve yerel arastirma sozlesme katmanidir."
)

def build_portfolio_scenario_control_markdown_report(
    summary: Dict[str, Any],
    profile: PortfolioScenarioControlProfile = None,
) -> str:
    md = [
        "# Phase 156: Portfolio Scenario Testing and Drawdown Control Report",
        "",
        f"> **YASAL UYARI VE GUVENLIK SINIRI:** {SCENARIO_CONTROL_DISCLAIMER}",
        "",
        "## 1. Profile and Execution Mode",
        f"- **Active Profile:** `{summary.get('profile_name', 'balanced_local_portfolio_scenario_control_contracts')}`",
        f"- **Current Phase:** 156 | **Next Phase:** 157 | **Target Final Phase:** 160",
        f"- **Dry-Run Default:** True | **Contract Only:** True | **Live Execution:** False",
        "",
        "## 2. Invariant Status",
        f"- **Scenario PnL Executed:** False",
        f"- **Drawdown Control Executed:** False",
        f"- **Portfolio Adjustment Generated:** False",
        f"- **Broker Interaction:** False",
        "",
        "## 3. Readiness Score & Handoff",
        f"- **Readiness Score:** {summary.get('overall_score', 1.0)}",
        f"- **Phase 157 Handoff Status:** READY",
        "",
    ]
    return "\n".join(md)
