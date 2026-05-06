from dataclasses import dataclass

@dataclass(frozen=True)
class RuleCondition:
    name: str
    left: str
    operator: str
    right: float | int | str | bool | tuple | list
    weight: float = 1.0
    required: bool = False
    description: str = ""

@dataclass(frozen=True)
class RuleTemplate:
    rule_id: str
    name: str
    strategy_family: str
    rule_group: str
    condition_label: str
    description: str
    conditions: tuple[RuleCondition, ...]
    preferred_regimes: tuple[str, ...] = ()
    avoided_regimes: tuple[str, ...] = ()
    preferred_asset_classes: tuple[str, ...] = ()
    min_required_conditions: int = 1
    enabled: bool = True
    notes: str = ""

_SUPPORTED_OPERATORS = [
    "gt", "gte", "lt", "lte", "eq", "neq", "between",
    "abs_gt", "abs_lt", "is_true", "is_false", "contains", "not_contains"
]

def list_supported_operators() -> list[str]:
    return list(_SUPPORTED_OPERATORS)

def validate_rule_condition(condition: RuleCondition) -> None:
    if condition.operator not in _SUPPORTED_OPERATORS:
        raise ValueError(f"Unsupported operator '{condition.operator}' in rule condition '{condition.name}'")
    if condition.operator == "between":
        if not isinstance(condition.right, (tuple, list)) or len(condition.right) != 2:
            raise ValueError(f"Operator 'between' requires 'right' to be a tuple/list of length 2 in '{condition.name}'")
    if condition.weight < 0.0:
        raise ValueError(f"Weight must be non-negative in '{condition.name}'")

def validate_rule_template(template: RuleTemplate) -> None:
    if not template.rule_id:
        raise ValueError("rule_id cannot be empty")
    if template.min_required_conditions < 0:
        raise ValueError(f"min_required_conditions must be >= 0 in template '{template.rule_id}'")
    for condition in template.conditions:
        validate_rule_condition(condition)
