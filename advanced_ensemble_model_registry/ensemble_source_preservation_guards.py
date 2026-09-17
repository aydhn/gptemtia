# -*- coding: utf-8 -*-
"""Phase 140: Ensemble Source Preservation Guards."""

from typing import Any, Dict


def build_ensemble_source_preservation_guards() -> Dict[str, Any]:
    """Build ensemble source preservation guard specifications.
    
    Returns:
        Dict[str, Any]: Source preservation guards dictionary.
    """
    return {
        "source_immutability_guard": {
            "guard_name": "source_immutability_guard",
            "enforced": True,
            "raw_sources_preserved": True,
            "destructive_mutation_allowed": False,
            "non_signal": True,
        },
        "schema_preservation_guard": {
            "guard_name": "schema_preservation_guard",
            "enforced": True,
            "original_column_names_preserved": True,
            "silent_type_casting_blocked": True,
            "non_signal": True,
        },
        "audit_traceability_guard": {
            "guard_name": "audit_traceability_guard",
            "enforced": True,
            "upstream_lake_refs_preserved": True,
            "lineage_hash_verified": True,
            "non_signal": True,
        },
    }


def validate_ensemble_source_preservation_guards(guards: Dict[str, Any]) -> bool:
    """Validate that source preservation guards are active.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        bool: True if valid and preserves sources, False otherwise.
    """
    if not isinstance(guards, dict) or len(guards) == 0:
        return False
    for name, guard in guards.items():
        if not isinstance(guard, dict):
            return False
        if not guard.get("enforced", False):
            return False
        if guard.get("destructive_mutation_allowed", False):
            return False
        if not guard.get("non_signal", False):
            return False
    return True


def summarize_ensemble_source_preservation_guards(guards: Dict[str, Any]) -> Dict[str, Any]:
    """Summarize source preservation guards.
    
    Args:
        guards: Dict of guards.
        
    Returns:
        Dict[str, Any]: Summary dictionary.
    """
    return {
        "total_guards": len(guards),
        "guard_names": list(guards.keys()),
        "all_guards_enforced": all(g.get("enforced", False) for g in guards.values()),
        "raw_sources_preserved": True,
        "destructive_mutations_blocked": True,
        "dry_run": True,
        "non_signal": True,
    }
