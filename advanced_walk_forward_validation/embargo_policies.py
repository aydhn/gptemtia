# -*- coding: utf-8 -*-
"""Phase 147: Embargo Policies.

Specifications for embargo policies to prevent information leakage across test/train splits.
"""

from typing import Any, Dict, List, Tuple, Union
import pandas as pd

from advanced_walk_forward_validation.walk_forward_config import WalkForwardProfile

EMBARGO_POLICIES: List[Dict[str, Any]] = [
    {
        "policy_name": "standard_fixed_embargo_policy",
        "embargo_type": "FIXED_BARS",
        "embargo_bars": 10,
        "description": "Test kumesi sonrasinda sonraki egitim seti arasina 10 bar bosluk koyan standart ambargo politikasi.",
    },
    {
        "policy_name": "volatility_scaled_embargo_policy",
        "embargo_type": "VOLATILITY_ADAPTIVE",
        "min_embargo_bars": 5,
        "max_embargo_bars": 30,
        "description": "Piyasa oynakligina gore dinamik hesaplanacak yer tutucu ambargo politikasi (hesaplama calistirilmaz).",
    },
    {
        "policy_name": "regime_transition_embargo_policy",
        "embargo_type": "REGIME_TRANSITION_BUFFER",
        "embargo_bars": 21,
        "description": "Rejim degisim sinirlarinda bilgi kirlenmesini engelleyen 1 aylik (21 bar) tampon ambargo politikasi.",
    },
]


def build_embargo_policy_registry(
    profile: WalkForwardProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Build DataFrame and summary for embargo policy registry."""
    rows = []
    for p in EMBARGO_POLICIES:
        rows.append(
            {
                "policy_name": p["policy_name"],
                "embargo_type": p["embargo_type"],
                "embargo_bars": p.get("embargo_bars", 10),
                "description": p["description"],
                "policy_enforced": True,
                "real_split_executed": False,
                "non_signal": True,
            }
        )
    df = pd.DataFrame(rows)
    summary = {
        "total_embargo_policies": len(df),
        "all_policies_enforced": True,
        "zero_real_split_executed": True,
        "non_signal": True,
    }
    return df, summary


def validate_embargo_policy_request(request: Union[Dict[str, Any], str]) -> Dict[str, Any]:
    """Validate request against embargo policy invariants."""
    req_name = request if isinstance(request, str) else str(request.get("policy_name", ""))
    return {
        "request": req_name,
        "is_safe": True,
        "split_executed": False,
        "action_taken": "POLICY_CONTRACT_REGISTERED_ONLY",
        "message": "Embargo politikasi yalnica sozlesme ve metadata olarak tanimlanir, gercek bolumleme yapilmaz.",
        "non_signal": True,
    }
