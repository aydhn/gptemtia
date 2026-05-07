"""
Parameter grid generator for validation.
"""

import itertools
import logging
from typing import Any

from validation.validation_models import ParameterSet, build_parameter_set_id

logger = logging.getLogger(__name__)


def build_default_parameter_grid() -> dict[str, list[Any]]:
    """Builds a minimal default parameter grid."""
    return {
        "backtest_profile": ["balanced_candidate_backtest"]
    }


def build_profile_parameter_grid() -> dict[str, list[Any]]:
    """Builds a parameter grid with common profile combinations."""
    return {
        "backtest_profile": [
            "balanced_candidate_backtest",
            "conservative_candidate_backtest",
            "wide_swing_candidate_backtest"
        ],
        "strategy_profile": ["balanced_strategy_selection", "conservative_strategy_selection"],
        "rule_profile": ["balanced_rule_evaluation", "conservative_rule_evaluation"],
        "risk_profile": ["balanced_pretrade_risk", "conservative_pretrade_risk"],
        "sizing_profile": ["balanced_theoretical_sizing", "conservative_theoretical_sizing"],
        "level_profile": ["balanced_theoretical_levels", "conservative_theoretical_levels"]
    }


def validate_parameter_grid(grid: dict[str, list[Any]]) -> dict:
    """Validates that the parameter grid is well-formed."""
    if not isinstance(grid, dict):
        return {"valid": False, "reason": "Grid must be a dictionary."}

    for key, values in grid.items():
        if not isinstance(values, list):
            return {"valid": False, "reason": f"Values for key {key} must be a list."}
        if len(values) == 0:
            return {"valid": False, "reason": f"Values list for key {key} is empty."}

    return {"valid": True, "reason": ""}


def generate_parameter_sets(grid: dict[str, list[Any]], max_combinations: int = 50) -> list[ParameterSet]:
    """
    Generates all combinations of parameters from the grid, limited by max_combinations.
    """
    valid_res = validate_parameter_grid(grid)
    if not valid_res["valid"]:
        logger.warning(f"Invalid parameter grid: {valid_res['reason']}. Returning default.")
        grid = build_default_parameter_grid()

    if not grid:
        logger.warning("Empty parameter grid. Returning empty parameter set.")
        # Single default parameter set
        return [ParameterSet(
            parameter_set_id=build_parameter_set_id({}),
            parameters={},
            description="Empty default parameters"
        )]

    keys = list(grid.keys())
    values_lists = [grid[k] for k in keys]

    combinations = list(itertools.product(*values_lists))

    if len(combinations) > max_combinations:
        logger.warning(f"Parameter grid produces {len(combinations)} combinations. Limiting to {max_combinations}.")
        combinations = combinations[:max_combinations]

    parameter_sets = []
    for combo in combinations:
        params_dict = {keys[i]: combo[i] for i in range(len(keys))}
        param_set_id = build_parameter_set_id(params_dict)

        desc_parts = [f"{k}={v}" for k, v in params_dict.items()]
        desc = ", ".join(desc_parts)

        parameter_sets.append(ParameterSet(
            parameter_set_id=param_set_id,
            parameters=params_dict,
            description=desc
        ))

    return parameter_sets


def summarize_parameter_sets(parameter_sets: list[ParameterSet]) -> dict:
    """Provides a summary of the generated parameter sets."""
    if not parameter_sets:
        return {"count": 0, "keys": []}

    keys = list(parameter_sets[0].parameters.keys())
    return {
        "count": len(parameter_sets),
        "keys": keys,
        "sample_descriptions": [p.description for p in parameter_sets[:3]]
    }
