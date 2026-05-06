import pandas as pd
from typing import Any
from .condition_models import RuleCondition, RuleTemplate


class RuleEngine:
    def __init__(self, templates: list[RuleTemplate] | None = None):
        self.templates = templates or []

    def evaluate_condition(
        self,
        condition: RuleCondition,
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> dict:
        context_snapshot = context_snapshot or {}

        val: Any = None
        warning = ""

        if condition.left in row:
            val = row[condition.left]
        elif condition.left in context_snapshot:
            val = context_snapshot[condition.left]
        else:
            warning = f"Column/key '{condition.left}' not found in row or context"

        passed = False
        if val is not None and not pd.isna(val):
            try:
                op = condition.operator
                right = condition.right

                if op == "gt":
                    passed = float(val) > float(right)
                elif op == "gte":
                    passed = float(val) >= float(right)
                elif op == "lt":
                    passed = float(val) < float(right)
                elif op == "lte":
                    passed = float(val) <= float(right)
                elif op == "eq":
                    passed = val == right
                elif op == "neq":
                    passed = val != right
                elif op == "between":
                    passed = float(right[0]) <= float(val) <= float(right[1])
                elif op == "abs_gt":
                    passed = abs(float(val)) > float(right)
                elif op == "abs_lt":
                    passed = abs(float(val)) < float(right)
                elif op == "is_true":
                    passed = bool(val) is True
                elif op == "is_false":
                    passed = bool(val) is False
                elif op == "contains":
                    passed = str(right) in str(val)
                elif op == "not_contains":
                    passed = str(right) not in str(val)
            except (ValueError, TypeError) as e:
                warning = f"Evaluation error: {e}"
                passed = False

        return {
            "condition_name": condition.name,
            "passed": passed,
            "required": condition.required,
            "weight": condition.weight,
            "left": condition.left,
            "operator": condition.operator,
            "right": condition.right,
            "observed_value": val,
            "warning": warning,
        }

    def evaluate_template(
        self,
        template: RuleTemplate,
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> dict:
        required_passed = 0
        required_failed = 0
        passed_conds = []
        failed_conds = []
        warnings = []

        total_weight = 0.0
        passed_weight = 0.0

        for cond in template.conditions:
            res = self.evaluate_condition(cond, row, context_snapshot)
            if res["warning"]:
                warnings.append(res["warning"])

            total_weight += cond.weight
            if res["passed"]:
                passed_weight += cond.weight
                passed_conds.append(cond.name)
                if cond.required:
                    required_passed += 1
            else:
                failed_conds.append(cond.name)
                if cond.required:
                    required_failed += 1

        match_score = (passed_weight / total_weight) if total_weight > 0 else 0.0

        matched = (
            required_failed == 0
            and len(passed_conds) >= template.min_required_conditions
        )
        partial_match = required_failed == 0 and len(passed_conds) > 0 and not matched

        return {
            "rule_id": template.rule_id,
            "strategy_family": template.strategy_family,
            "rule_group": template.rule_group,
            "condition_label": template.condition_label,
            "matched": matched,
            "partial_match": partial_match,
            "match_score": match_score,
            "required_conditions_passed": required_passed,
            "required_conditions_failed": required_failed,
            "passed_conditions": passed_conds,
            "failed_conditions": failed_conds,
            "warnings": warnings,
        }

    def evaluate_templates(
        self,
        templates: list[RuleTemplate],
        row: pd.Series,
        context_snapshot: dict | None = None,
    ) -> list[dict]:
        return [self.evaluate_template(t, row, context_snapshot) for t in templates]
