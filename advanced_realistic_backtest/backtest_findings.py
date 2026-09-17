# -*- coding: utf-8 -*-
"""Phase 146: Backtest Findings.

Manages findings, audit notices, and policy violations detected within backtest contracts.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_realistic_backtest.realistic_backtest_config import RealisticBacktestProfile
from advanced_realistic_backtest.realistic_backtest_models import BacktestFinding

SAMPLE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FND-146-01",
        "finding_type": "backtest_execution_blocked_by_policy",
        "domain": "safety_domain",
        "severity_label": "INFO",
        "message": "Gercek backtest yurutumu guvenlik politikasi geregi engellenmis ve sozlesme modunda tutulmustur.",
        "recommendation": "Phase 146 sozlesmelerini inceleyiniz; gercek simulasyon Phase 147 ve sonrasi bloklara birakilmistir.",
        "manual_review_required": False,
    },
    {
        "finding_id": "FND-146-02",
        "finding_type": "cost_model_contract_ready",
        "domain": "transaction_cost_domain",
        "severity_label": "INFO",
        "message": "Komisyon, borsa ucreti ve alis-satis farki modelleri basariyla sozlesme modunda tanimlandi.",
        "recommendation": "Maliyet parametrelerini araci kurum tarifelerine gore insan gozuyle dogrulayiniz.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-146-03",
        "finding_type": "slippage_model_contract_ready",
        "domain": "slippage_model_domain",
        "severity_label": "INFO",
        "message": "Kayma modelleri basariyla sozlesme modunda tanimlandi; getiri garantisi uretilmemistir.",
        "recommendation": "Oynaklik ve likidite carpanlarini gozden geciriniz.",
        "manual_review_required": True,
    },
]


def create_backtest_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> BacktestFinding:
    """Helper to instantiate a type-safe BacktestFinding."""
    import uuid
    fid = f"FND-146-{uuid.uuid4().hex[:6].upper()}"
    return BacktestFinding(
        finding_id=fid,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_backtest_findings_registry(
    profile: RealisticBacktestProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame of findings."""
    rows = []
    for f in SAMPLE_FINDINGS:
        rows.append(
            {
                "finding_id": f["finding_id"],
                "finding_type": f["finding_type"],
                "domain": f["domain"],
                "severity_label": f["severity_label"],
                "message": f["message"],
                "recommendation": f["recommendation"],
                "manual_review_required": f["manual_review_required"],
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = summarize_backtest_findings(df)
    return df, summary


def summarize_backtest_findings(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize backtest findings."""
    total = len(df)
    critical = int((df["severity_label"] == "CRITICAL").sum()) if not df.empty else 0
    manual = int(df["manual_review_required"].sum()) if not df.empty else 0
    return {
        "total_findings": total,
        "critical_blockers": critical,
        "manual_review_required_count": manual,
        "non_signal": True,
    }
