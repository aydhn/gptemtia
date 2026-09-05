import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.feature_validation_rule_registry import (
    get_feature_validation_rule_registry,
    get_feature_validation_rules_summary,
)
from advanced_feature_validation.forbidden_feature_columns import get_forbidden_feature_columns
from advanced_feature_validation.no_lookahead_rules import get_no_lookahead_rules


def main():
    settings = get_settings()
    data_lake = DataLake()

    rules = get_feature_validation_rule_registry()
    summary = get_feature_validation_rules_summary()
    forbidden = get_forbidden_feature_columns()
    no_lookahead = get_no_lookahead_rules()

    data_lake.save_feature_validation_rule_registry(summary)
    data_lake.save_forbidden_feature_column_registry(forbidden)
    data_lake.save_no_lookahead_rule_registry(no_lookahead)

    print("=" * 70)
    print("PHASE 121: FEATURE VALIDATION RULES & FORBIDDEN COLUMNS")
    print("=" * 70)
    print(f"Total Rules           : {summary['total_rules']}")
    print(f"Enabled Rules         : {summary['enabled_rules']}")
    print(f"Forbidden Columns     : {len(forbidden)}")
    print(f"No-Lookahead Rules    : {len(no_lookahead)}")
    print(f"Current Phase         : {summary['current_phase']}")
    print(f"Destructive Allowed   : False")
    print("=" * 70)


if __name__ == "__main__":
    main()
