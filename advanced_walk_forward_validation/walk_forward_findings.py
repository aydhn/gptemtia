# -*- coding: utf-8 -*-
"""Phase 147: Walk-Forward Findings Registry.

Manages findings, issue tracking, and policy enforcement records for the walk-forward layer.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile
from advanced_walk_forward_validation.walk_forward_models import WalkForwardFinding

SAMPLE_FINDINGS: List[Dict[str, Any]] = [
    {
        "finding_id": "FND-WF-01",
        "finding_type": "contract_isolation_verified",
        "domain": "SPLIT_CONTRACT",
        "severity_label": "INFO",
        "message": "Zaman serisi bolumleme sozlesmelerinin hedef/etiket uretmedigi dogrulandi.",
        "recommendation": "Contract-only durumunu Phase 148 handoff asamasina kadar koruyun.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-WF-02",
        "finding_type": "bias_guards_active",
        "domain": "BIAS_CONTROL",
        "severity_label": "INFO",
        "message": "Data snooping, lookahead ve survivorship muhafizlarinin tumu aktif durumda.",
        "recommendation": "Yasakli kolon listesine yeni turetilmis getiri ozellikleri eklendiginde kontrol saglayin.",
        "manual_review_required": True,
    },
    {
        "finding_id": "FND-WF-03",
        "finding_type": "execution_strictly_disabled",
        "domain": "EXECUTION_SAFETY",
        "severity_label": "INFO",
        "message": "Canli islem, broker, egitim, cikarim ve metrik hesaplama yollarinin tumu kilitli.",
        "recommendation": "Sifir canli emir prensibine kesinlikle sadik kalin.",
        "manual_review_required": True,
    },
]


def create_walk_forward_finding(
    finding_type: str,
    domain: str,
    severity_label: str,
    message: str,
    recommendation: str,
    manual_review_required: bool = True,
) -> WalkForwardFinding:
    """Create a structured finding instance."""
    import uuid
    fid = f"FND-{uuid.uuid4().hex[:6].upper()}"
    return WalkForwardFinding(
        finding_id=fid,
        finding_type=finding_type,
        domain=domain,
        severity_label=severity_label,
        message=message,
        recommendation=recommendation,
        manual_review_required=manual_review_required,
    )


def build_walk_forward_findings_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for walk-forward findings registry."""
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
    critical_count = len(df[df["severity_label"] == "CRITICAL"]) if not df.empty else 0
    summary = {
        "total_findings": len(df),
        "critical_count": critical_count,
        "has_critical_blockers": critical_count > 0,
        "non_signal": True,
    }
    return df, summary
