"""Phase 124 Feature Store Non-Signal Policies."""

import re
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

from advanced_feature_store_integration.feature_store_integration_config import (
    FeatureStoreIntegrationProfile,
    get_default_feature_store_integration_profile,
)

FORBIDDEN_CLAIM_PATTERNS: List[str] = [
    r"\b(buy|sell|al|sat)\b",
    r"\b(long|short)\b",
    r"\b(signal|sinyal)\b",
    r"\b(target|label|hedef|etiket)\b",
    r"\b(prediction|tahmin)\b",
    r"\b(recommendation|tavsiye)\b",
    r"\b(future_return|forward_return|next_return)\b",
    r"\b(official approval|resmi onay)\b",
    r"\b(production ready|canli hazir)\b",
    r"\b(broker ready)\b",
]

NON_SIGNAL_POLICIES = [
    {
        "policy_id": "NSP_001",
        "policy_name": "feature_store_is_not_signal",
        "description": "Feature store kayıtları salt araştırma metaverisidir; hiçbir şekilde alım satım sinyali olarak yorumlanamaz.",
        "status": "active",
        "enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "NSP_002",
        "policy_name": "no_directional_claims",
        "description": "Özellik veya faktör değerlerinden yönsel getiri veya fiyat artış/azalış iddiası üretilemez.",
        "status": "active",
        "enforced": True,
        "non_signal": True,
    },
    {
        "policy_id": "NSP_003",
        "policy_name": "no_production_approval_claim",
        "description": "Feature store entegrasyon durumu canlıya geçiş, model dağıtımı veya resmi onay anlamına gelmez.",
        "status": "active",
        "enforced": True,
        "non_signal": True,
    },
]

SAFE_DISCLAIMER_PATTERNS: List[str] = [
    r"\bnon[-_]signal\b",
    r"\bnon[-_]directional\b",
    r"\bnon[-_]predictive\b",
    r"\bnot\s+a\s+signal\b",
    r"\bno\s+signal\b",
    r"\bno\s+recommendation\b",
    r"\bno\s+target\b",
    r"\bno\s+prediction\b",
]


def sanitize_safe_disclaimers(text: str) -> str:
    """Mask safe disclaimer phrases so they are not flagged as forbidden claims."""
    cleaned = text.lower()
    for sp in SAFE_DISCLAIMER_PATTERNS:
        cleaned = re.sub(sp, " ", cleaned)
    return cleaned


def validate_feature_store_non_signal_text(text: str) -> Dict[str, Any]:
    """Scan text for forbidden signal, directional, or approval claims."""
    findings = []
    cleaned = sanitize_safe_disclaimers(text)
    for pat in FORBIDDEN_CLAIM_PATTERNS:
        match = re.search(pat, cleaned)
        if match:
            findings.append(match.group(0))

    return {
        "text_sample": text[:80],
        "is_compliant": len(findings) == 0,
        "findings": findings,
        "non_signal": len(findings) == 0,
    }


def build_feature_store_non_signal_policy_registry(
    profile: Optional[FeatureStoreIntegrationProfile] = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build registry of non-signal policies."""
    records = list(NON_SIGNAL_POLICIES)
    df = pd.DataFrame(records)
    summary = {
        "total_policies": len(records),
        "forbidden_patterns_count": len(FORBIDDEN_CLAIM_PATTERNS),
        "non_signal": True,
        "source_preserved": True,
    }
    return df, summary


def summarize_feature_store_non_signal_policies(df: pd.DataFrame) -> Dict[str, Any]:
    """Summarize non-signal policies."""
    return {
        "total_policies": len(df) if not df.empty else 0,
        "non_signal": True,
    }
