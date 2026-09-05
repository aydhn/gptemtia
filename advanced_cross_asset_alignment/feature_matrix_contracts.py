from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_cross_asset_alignment.cross_asset_alignment_config import (
    CrossAssetAlignmentProfile,
    get_default_cross_asset_alignment_profile,
)
from advanced_cross_asset_alignment.cross_asset_alignment_models import (
    FeatureMatrixContract,
    build_feature_matrix_contract_id,
)


def build_default_feature_matrix_contracts(
    profile: CrossAssetAlignmentProfile | None = None,
) -> List[FeatureMatrixContract]:
    contracts = [
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("fx_base_cross_asset_matrix_contract"),
            matrix_name="fx_base_cross_asset_matrix_contract",
            base_domain="fx",
            aligned_domains=["commodity", "macro", "calendar", "news"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="fx_cross_asset",
            join_policy="join_policy_asof_backward",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("commodity_base_cross_asset_matrix_contract"),
            matrix_name="commodity_base_cross_asset_matrix_contract",
            base_domain="commodity",
            aligned_domains=["fx", "macro", "calendar", "news"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="commodity_cross_asset",
            join_policy="join_policy_asof_backward",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("macro_context_matrix_contract"),
            matrix_name="macro_context_matrix_contract",
            base_domain="macro",
            aligned_domains=["fx", "commodity"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="macro_context",
            join_policy="join_policy_asof_backward",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("calendar_event_context_matrix_contract"),
            matrix_name="calendar_event_context_matrix_contract",
            base_domain="calendar",
            aligned_domains=["fx", "commodity"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="calendar_context",
            join_policy="join_policy_event_window_placeholder",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("news_metadata_context_matrix_contract"),
            matrix_name="news_metadata_context_matrix_contract",
            base_domain="news",
            aligned_domains=["fx", "commodity"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="news_context",
            join_policy="join_policy_metadata_tag_link",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
        FeatureMatrixContract(
            contract_id=build_feature_matrix_contract_id("cross_domain_research_matrix_contract"),
            matrix_name="cross_domain_research_matrix_contract",
            base_domain="fx",
            aligned_domains=["commodity", "macro", "calendar", "news"],
            timestamp_field="normalized_timestamp",
            symbol_field="canonical_symbol",
            feature_namespace="cross_domain_research",
            join_policy="join_policy_asof_backward",
            no_lookahead_policy="backward_only_no_future",
            non_signal=True,
            manual_review_required=False,
        ),
    ]
    return contracts


def validate_feature_matrix_contract(contract: FeatureMatrixContract) -> Dict[str, Any]:
    issues = []
    if not contract.non_signal:
        issues.append("Feature matrix contract non_signal=True olmak zorundadır.")
    if "signal" in contract.matrix_name.lower():
        issues.append("Contract ismi 'signal' içeremez.")
    if "target" in contract.matrix_name.lower() or "prediction" in contract.matrix_name.lower():
        issues.append("Contract ismi 'target' veya 'prediction' içeremez.")
    if not contract.base_domain:
        issues.append("Base domain boş olamaz.")
    if not contract.aligned_domains:
        issues.append("Aligned domains listesi boş olamaz.")

    return {
        "contract_id": contract.contract_id,
        "is_valid": len(issues) == 0,
        "issues": issues,
    }


def build_feature_matrix_contract_registry(
    profile: CrossAssetAlignmentProfile | None = None,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    active_profile = profile or get_default_cross_asset_alignment_profile()
    contracts = build_default_feature_matrix_contracts(active_profile)
    rows = [c.to_dict() for c in contracts]
    df = pd.DataFrame(rows)
    summary = summarize_feature_matrix_contracts(df)
    summary["profile"] = active_profile.name
    return df, summary


DEFAULT_FEATURE_MATRIX_CONTRACTS: List[FeatureMatrixContract] = build_default_feature_matrix_contracts()


def summarize_feature_matrix_contracts(df: pd.DataFrame) -> Dict[str, Any]:
    if df.empty:
        return {"total_contracts": 0, "status": "EMPTY"}

    all_non_signal = bool(df["non_signal"].all()) if "non_signal" in df.columns else False
    all_backward_only = True
    if "no_lookahead_policy" in df.columns:
        all_backward_only = bool(df["no_lookahead_policy"].apply(lambda p: "backward" in str(p) or "no_future" in str(p)).all())
    return {
        "total_contracts": len(df),
        "matrix_names": list(df["matrix_name"]) if "matrix_name" in df.columns else [],
        "base_domains": list(df["base_domain"].unique()) if "base_domain" in df.columns else [],
        "all_non_signal": all_non_signal,
        "all_backward_only": all_backward_only,
        "status": "READY" if all_non_signal and all_backward_only else "SAFETY_VIOLATION",
    }

