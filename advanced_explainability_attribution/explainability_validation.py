# -*- coding: utf-8 -*-
"""Phase 143: Explainability Validation Suite."""

from typing import Any, Dict, List, Optional
from advanced_explainability_attribution.explainability_config import (
    ExplainabilityProfile,
    get_explainability_profile,
)
from advanced_explainability_attribution.explainability_report_contracts import (
    build_explainability_report_contracts,
)
from advanced_explainability_attribution.feature_attribution_contracts import (
    build_feature_attribution_contracts,
)
from advanced_explainability_attribution.explainability_forbidden_column_policies import (
    check_forbidden_columns,
)


def validate_explainability_layer(
    profile: Optional[ExplainabilityProfile] = None,
) -> Dict[str, Any]:
    """Validate all Phase 143 explainability contracts, rules, and invariants."""
    prof = profile or get_explainability_profile()

    df_reports, sum_reports = build_explainability_report_contracts(prof)
    df_attrib, sum_attrib = build_feature_attribution_contracts(prof)

    validation_items: List[Dict[str, Any]] = []

    # 1. Report contract invariants
    c1 = (
        not df_reports["explainability_calculation_allowed"].any()
        and not df_reports["attribution_calculation_allowed"].any()
        and not df_reports["metric_calculation_allowed"].any()
        and not df_reports["model_action_allowed"].any()
        and not df_reports["signal_generation_allowed"].any()
        and df_reports["non_signal_required"].all()
    )
    validation_items.append({
        "rule": "report_contract_invariants",
        "passed": bool(c1),
        "detail": "all report contracts disallow calculation, model actions and signals",
    })

    # 2. Attribution contract invariants
    c2 = (
        not df_attrib["attribution_calculation_allowed"].any()
        and not df_attrib["shap_execution_allowed"].any()
        and not df_attrib["lime_execution_allowed"].any()
        and not df_attrib["permutation_importance_allowed"].any()
        and df_attrib["non_signal_required"].all()
    )
    validation_items.append({
        "rule": "attribution_contract_invariants",
        "passed": bool(c2),
        "detail": "all attribution contracts disallow SHAP, LIME, permutation and signals",
    })

    # 3. Forbidden column validation
    valid_cols = ["brent_crude_close", "gold_volume", "macro_cpi_rate", "news_metadata_count"]
    ok_valid, _ = check_forbidden_columns(valid_cols, prof)
    invalid_cols = ["future_price", "article_body", "sentiment_score", "trade_signal"]
    ok_invalid, viols = check_forbidden_columns(invalid_cols, prof)
    c3 = ok_valid and not ok_invalid and len(viols) == 4
    validation_items.append({
        "rule": "forbidden_column_policy",
        "passed": bool(c3),
        "detail": "forbidden columns correctly identified and rejected",
    })

    all_passed = all(item["passed"] for item in validation_items)
    return {
        "status": "PASS" if all_passed else "FAIL",
        "all_passed": all_passed,
        "validations": validation_items,
        "current_phase": 143,
        "next_phase": 144,
        "target_final_phase": 160,
    }
