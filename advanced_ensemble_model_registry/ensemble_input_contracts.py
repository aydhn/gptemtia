# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Input Contracts."""

from typing import Any, Dict, List


def build_ensemble_input_contracts() -> Dict[str, Any]:
    """Build ensemble input contracts for non-executing ensemble strategies.
    
    Returns:
        Dict[str, Any]: Registered ensemble input contracts.
    """
    contracts: Dict[str, Any] = {
        "voting_input_contract": {
            "strategy": "voting",
            "required_candidate_inputs": ["candidate_prediction_placeholder"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
        "blending_input_contract": {
            "strategy": "blending",
            "required_candidate_inputs": ["holdout_metadata_prediction_contract"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
        "stacking_input_contract": {
            "strategy": "stacking",
            "required_candidate_inputs": ["oof_metadata_contract_ref"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
        "averaging_input_contract": {
            "strategy": "averaging",
            "required_candidate_inputs": ["candidate_prediction_placeholder"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
        "rank_aggregation_input_contract": {
            "strategy": "rank_aggregation",
            "required_candidate_inputs": ["candidate_prediction_placeholder"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
        "meta_model_input_contract": {
            "strategy": "meta_model",
            "required_candidate_inputs": ["candidate_metadata_matrix_ref"],
            "expected_input_type": "metadata_contract_ref",
            "temporal_alignment_required": True,
            "no_lookahead_guaranteed": True,
            "metadata_only_news_guaranteed": True,
            "source_preserved": True,
            "contains_target": False,
            "contains_signal": False,
            "non_signal": True,
        },
    }
    return contracts


def validate_ensemble_input_contracts(contracts: Dict[str, Any]) -> bool:
    """Validate ensemble input contracts.
    
    Args:
        contracts: Dict of input contracts to validate.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(contracts, dict) or len(contracts) == 0:
        return False
    for name, spec in contracts.items():
        if not isinstance(spec, dict):
            return False
        if not spec.get("non_signal", False):
            return False
        if not spec.get("no_lookahead_guaranteed", False):
            return False
        if not spec.get("metadata_only_news_guaranteed", False):
            return False
        if spec.get("contains_signal", True):
            return False
    return True


def summarize_ensemble_input_contracts(contracts: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize ensemble input contracts.
    
    Args:
        contracts: Dict of input contracts.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_contracts": len(contracts),
        "contract_names": list(contracts.keys()),
        "strategies": [c.get("strategy") for c in contracts.values()],
        "all_no_lookahead": all(c.get("no_lookahead_guaranteed", False) for c in contracts.values()),
        "all_non_signal": all(c.get("non_signal", False) for c in contracts.values()),
        "dry_run": True,
    }
