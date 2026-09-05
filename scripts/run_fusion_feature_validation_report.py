import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.storage.data_lake import DataLake
from advanced_feature_fusion.fusion_feature_validation import validate_all_fusion_feature_components
from advanced_feature_fusion.fusion_feature_report_builder import (
    build_fusion_feature_markdown_report,
    build_fusion_feature_text_report,
)


def main():
    data_lake = DataLake()

    val_res = validate_all_fusion_feature_components()

    summary_data = {
        "status": "VALID" if val_res["valid"] else "INVALID",
        "current_phase": 120,
        "next_phase": 121,
        "target_final_phase": 160,
        "readiness_score": 1.0 if val_res["valid"] else 0.0,
        "handoff_ready": val_res["valid"],
        "domain_count": val_res["domains_count"],
        "metadata_feature_count": 17,
        "contract_count": 5,
        "policy_count": val_res["policies_checked"],
    }

    md_report = build_fusion_feature_markdown_report(summary_data)
    txt_report = build_fusion_feature_text_report(summary_data)

    data_lake.save_fusion_feature_report_markdown(md_report)
    data_lake.save_fusion_feature_report_text(txt_report)

    print("=" * 70)
    print("PHASE 120: FUSION FEATURE VALIDATION REPORT")
    print("=" * 70)
    print(f"Validation Status : {'VALID' if val_res['valid'] else 'INVALID'}")
    print(f"Profiles Checked  : {val_res['profiles_count']}")
    print(f"Domains Checked   : {val_res['domains_count']}")
    print(f"Policies Checked  : {val_res['policies_checked']}")
    print(f"Report Markdown   : Saved to data lake")
    print(f"Report Plaintext  : Saved to data lake")
    print("=" * 70)


if __name__ == "__main__":
    main()
