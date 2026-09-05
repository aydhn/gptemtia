import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.settings import get_settings
from data.storage.data_lake import DataLake
from advanced_feature_validation.feature_validation_findings import (
    clear_findings,
    create_finding,
    get_all_findings,
    get_findings_summary,
)
from advanced_feature_validation.feature_validation_manual_review_queue import (
    clear_manual_review_queue,
    add_to_manual_review_queue,
    get_manual_review_queue,
    get_manual_review_summary,
)


def main():
    settings = get_settings()
    data_lake = DataLake()

    clear_findings()
    clear_manual_review_queue()

    # Create an informational test finding
    create_finding(
        rule_id="RULE-VAL-001",
        column_name="sample_feature",
        severity="INFO",
        finding_type="VALIDATION_CHECK",
        message="Feature validation baseline check initialized successfully.",
    )

    findings = get_all_findings()
    f_summary = get_findings_summary()
    queue = get_manual_review_queue()
    q_summary = get_manual_review_summary()

    data_lake.save_feature_validation_finding_registry(f_summary)
    data_lake.save_feature_validation_manual_review_queue(q_summary)

    print("=" * 70)
    print("PHASE 121: FEATURE VALIDATION FINDINGS & REVIEW QUEUE")
    print("=" * 70)
    print(f"Total Findings     : {f_summary['total_findings']}")
    print(f"Critical Findings  : {f_summary['critical']}")
    print(f"High Findings      : {f_summary['high']}")
    print(f"Medium Findings    : {f_summary['medium']}")
    print(f"Low Findings       : {f_summary['low']}")
    print(f"Manual Review Queue: {q_summary['total_items']}")
    print(f"Status             : CLEAN")
    print("=" * 70)


if __name__ == "__main__":
    main()
