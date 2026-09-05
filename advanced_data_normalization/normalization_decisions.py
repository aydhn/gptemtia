from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile
from advanced_data_normalization.data_normalization_models import (
    NormalizationDecision,
    NormalizationFinding,
    build_normalization_decision_id,
)


def create_normalization_decision(
    finding: NormalizationFinding,
    decision_type: str = "manual_review_required",
    decision_note: str = "",
) -> NormalizationDecision:
    return NormalizationDecision(
        decision_id=build_normalization_decision_id(finding.finding_id),
        finding_id=finding.finding_id,
        rule_id=finding.rule_id,
        decision_type=decision_type,
        decision_note=decision_note or f"Decision for {finding.finding_id}: {decision_type}",
        source_preserved=True,
        destructive_action_allowed=False,
        lineage_required=True,
        future_phase_owner="Phase 114",
    )


def normalization_decision_to_dict(decision: NormalizationDecision) -> Dict[str, Any]:
    return decision.to_dict()


def build_normalization_decision_registry(
    findings_df: pd.DataFrame,
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    if not findings_df.empty:
        for _, row in findings_df.iterrows():
            fid = row.get("finding_id", "unknown_finding")
            rid = row.get("rule_id", "unknown_rule")
            status = row.get("status_label", "normalization_manual_review_required")
            is_manual = row.get("manual_review_required", True)
            dec_type = "manual_review_required" if is_manual else "applied_canonical_mapping"
            note = f"Finding {fid} resolved as {dec_type}. Source intact, lineage logged for Phase 114."

            dec = NormalizationDecision(
                decision_id=build_normalization_decision_id(fid),
                finding_id=fid,
                rule_id=rid,
                decision_type=dec_type,
                decision_note=note,
                source_preserved=True,
                destructive_action_allowed=False,
                lineage_required=True,
                future_phase_owner="Phase 114",
            )
            records.append(dec.to_dict())

    df = pd.DataFrame.from_records(records)
    summary = summarize_normalization_decisions(df)
    return df, summary


def summarize_normalization_decisions(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_decisions": len(df),
        "source_preserved_all": bool(df["source_preserved"].all()) if "source_preserved" in df.columns and len(df) > 0 else True,
        "destructive_action_zero": bool((~df["destructive_action_allowed"]).all()) if "destructive_action_allowed" in df.columns and len(df) > 0 else True,
        "lineage_required_all": bool(df["lineage_required"].all()) if "lineage_required" in df.columns and len(df) > 0 else True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
