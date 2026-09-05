from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.transformation_provenance_registry import build_transformation_provenance_registry
from advanced_data_lineage.normalization_lineage_registry import build_normalization_lineage_registry
from advanced_data_lineage.quality_finding_lineage_registry import build_quality_finding_lineage_registry
from advanced_data_lineage.manual_review_lineage_registry import build_manual_review_lineage_registry
from advanced_data_lineage.normalized_output_lineage_registry import build_normalized_output_lineage_registry
from advanced_data_lineage.data_lineage_report_builder import (
    build_transformation_provenance_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    trans_df, trans_sum = build_transformation_provenance_registry(profile)
    norm_df, norm_sum = build_normalization_lineage_registry(profile)
    qf_df, qf_sum = build_quality_finding_lineage_registry(profile)
    rev_df, rev_sum = build_manual_review_lineage_registry(profile)
    out_df, out_sum = build_normalized_output_lineage_registry(profile)

    data_lake.save_transformation_provenance_registry(trans_df, trans_sum)
    data_lake.save_normalization_lineage_registry(norm_df, norm_sum)
    data_lake.save_quality_finding_lineage_registry(qf_df, qf_sum)
    data_lake.save_manual_review_lineage_registry(rev_df, rev_sum)
    data_lake.save_normalized_output_lineage_registry(out_df, out_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    trans_df.to_csv(csv_dir / "transformation_provenance_registry.csv", index=False)
    norm_df.to_csv(csv_dir / "normalization_lineage_registry.csv", index=False)
    qf_df.to_csv(csv_dir / "quality_finding_lineage_registry.csv", index=False)
    rev_df.to_csv(csv_dir / "manual_review_lineage_registry.csv", index=False)
    out_df.to_csv(csv_dir / "normalized_output_lineage_registry.csv", index=False)

    md_trans = build_transformation_provenance_markdown_report(trans_sum, trans_df)
    (md_dir / "transformation_provenance_registry.md").write_text(md_trans, encoding="utf-8")
    (txt_dir / "transformation_provenance_registry.txt").write_text(md_trans, encoding="utf-8")

    print(f"Transformation & output lineage registries built successfully: {len(trans_df)} transformations, {len(norm_df)} normalizations, {len(out_df)} output records.")


if __name__ == "__main__":
    main()
