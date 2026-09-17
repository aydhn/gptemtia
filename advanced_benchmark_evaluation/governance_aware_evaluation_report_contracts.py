# -*- coding: utf-8 -*-
"""Phase 151: Governance-Aware Evaluation Report Contracts Module.

Defines reporting contracts enforcing audit trails, evidence linkage, and operator sign-offs.
Strictly non-production and offline.
"""

from typing import Any, Dict, List, Tuple
import pandas as pd

from advanced_benchmark_evaluation.benchmark_evaluation_config import BenchmarkEvaluationProfile
from advanced_benchmark_evaluation.benchmark_evaluation_labels import (
    LABEL_GOVERNANCE_AWARE_EVALUATION_DOMAIN,
    STATUS_EVALUATION_CONTRACT_READY,
)

GOVERNANCE_EVALUATION_CONTRACTS: List[Dict[str, Any]] = [
    {
        "contract_id": "GOV_EVAL_AUDIT_TRAIL",
        "contract_name": "Immutable Evaluation Audit Trail Contract",
        "governance_pillar": "audit_traceability",
        "upstream_phase_ref": "phase_150_audit_policies",
        "metric_placeholder_ref": "governance_evidence_placeholder",
        "description": "Değişmez zaman damgalı değerlendirme konfigürasyonu ve kod sürüm kaydı sözleşmesi.",
    },
    {
        "contract_id": "GOV_EVAL_EVIDENCE_LINKAGE",
        "contract_name": "Multi-Phase Evidence Linkage Contract",
        "governance_pillar": "evidence_validation",
        "upstream_phase_ref": "phase_150_evidence_policies",
        "metric_placeholder_ref": "governance_evidence_placeholder",
        "description": "Phase 146-150 arası doğrulama kanıtlarının değerlendirme raporuna çapraz bağlanması.",
    },
    {
        "contract_id": "GOV_EVAL_OPERATOR_REVIEW_GATE",
        "contract_name": "Operator Sign-Off Boundary Contract",
        "governance_pillar": "human_in_the_loop",
        "upstream_phase_ref": "phase_150_manual_review_gates",
        "metric_placeholder_ref": "governance_evidence_placeholder",
        "description": "Otomatik onay yasağı ve operatör manuel inceleme şartı sözleşmesi.",
    },
    {
        "contract_id": "GOV_EVAL_NON_PRODUCTION_PERIMETER",
        "contract_name": "Non-Production Research Perimeter Contract",
        "governance_pillar": "safety_boundary",
        "upstream_phase_ref": "phase_150_safety_boundary",
        "metric_placeholder_ref": "governance_evidence_placeholder",
        "description": "Rapor çıktılarının yalnızca iç araştırma amaçlı olduğunu garanti eden çevre sözleşmesi.",
    },
]


def build_governance_aware_evaluation_report_contract_registry(
    profile: BenchmarkEvaluationProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame registry of governance-aware evaluation report contracts."""
    rows: List[Dict[str, Any]] = []

    for c in GOVERNANCE_EVALUATION_CONTRACTS:
        rows.append(
            {
                "contract_id": c["contract_id"],
                "contract_name": c["contract_name"],
                "governance_pillar": c["governance_pillar"],
                "upstream_phase_ref": c["upstream_phase_ref"],
                "metric_placeholder_ref": c["metric_placeholder_ref"],
                "description": c["description"],
                "production_approval_allowed": False,
                "broker_ready_allowed": False,
                "status": STATUS_EVALUATION_CONTRACT_READY,
                "non_signal": True,
            }
        )

    df = pd.DataFrame(rows)
    summary = {
        "domain": LABEL_GOVERNANCE_AWARE_EVALUATION_DOMAIN,
        "total_contracts": len(df),
        "all_production_approvals_disabled": True,
        "status": STATUS_EVALUATION_CONTRACT_READY,
        "non_signal": True,
    }
    return df, summary
