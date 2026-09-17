# -*- coding: utf-8 -*-
"""Phase 148: Stress Findings Registry.

Records and summarizes governance and compliance findings in the stress testing contract layer.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_stress_testing.stress_testing_config import StressTestingProfile
from advanced_stress_testing.stress_testing_models import StressFinding

DEFAULT_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FIND_STRESS_001",
        "finding_type": "contract_only_operational_mode",
        "domain": "stress_testing_domain",
        "severity_label": "INFO",
        "message": "Phase 148 stres testi ve senaryo katmanı salt sözleşme (contract-only) modunda çalışmaktadır.",
        "recommendation": "Gerçek stres testi yürütülmemeli; contract ve placeholder seviyesinde kalınmalıdır.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FIND_STRESS_002",
        "finding_type": "zero_live_trading_enforced",
        "domain": "safety_domain",
        "severity_label": "INFO",
        "message": "Canlı emir iletimi, aracı kurum bağlantısı ve AL/SAT sinyali üretimi kesin olarak devre dışıdır.",
        "recommendation": "Sistem güvenliğini ve negatif değişmezleri korumaya devam edin.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FIND_STRESS_003",
        "finding_type": "metric_calculation_placeholder_mode",
        "domain": "stress_metric_placeholder_domain",
        "severity_label": "INFO",
        "message": "Stres PnL, VaR, ES ve drawdown hesaplamaları formül yer tutucusu olarak yapılandırılmıştır.",
        "recommendation": "Gerçek metrik hesaplaması yapmayın; Phase 149 Monte Carlo hazırlığına odaklanın.",
        "manual_review_required": True,
    },
]


def create_stress_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> StressFinding:
    """Helper to instantiate a valid StressFinding dataclass."""
    finding_id = f"FIND_{abs(hash(finding_type + message)) % 100000:05d}"
    return StressFinding(
        finding_id=finding_id,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_stress_findings_registry(
    profile: StressTestingProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build a DataFrame registry of all stress testing findings."""
    rows: List[Dict[str, Any]] = []
    for f in DEFAULT_FINDINGS:
        finding = StressFinding(
            finding_id=f["finding_id"],
            finding_type=f["finding_type"],
            domain=f["domain"],
            severity_label=f["severity_label"],
            message=f["message"],
            recommendation=f["recommendation"],
            manual_review_required=f["manual_review_required"],
        )
        rows.append(
            {
                "finding_id": finding.finding_id,
                "finding_type": finding.finding_type,
                "domain": finding.domain,
                "severity_label": finding.severity_label,
                "message": finding.message,
                "recommendation": finding.recommendation,
                "manual_review_required": finding.manual_review_required,
                "non_signal": True,
                "local_only": True,
            }
        )
    df = pd.DataFrame(rows)
    critical_count = int((df["severity_label"] == "CRITICAL").sum()) if not df.empty else 0
    summary = {
        "total_findings": len(df),
        "critical_count": critical_count,
        "all_manual_review_required": bool(df["manual_review_required"].all()) if not df.empty else True,
        "non_signal": True,
    }
    return df, summary
