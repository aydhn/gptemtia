from pathlib import Path
from config.settings import Settings
from data.storage.data_lake import DataLake
from advanced_data_lineage.data_lineage_config import get_default_data_lineage_profile
from advanced_data_lineage.lineage_findings import build_lineage_finding_registry
from advanced_data_lineage.provenance_scoring import build_provenance_confidence_score_report
from advanced_data_lineage.traceability_scoring import (
    build_dataset_traceability_score_report,
    build_provider_traceability_score_report,
)
from advanced_data_lineage.lineage_graph_placeholder import build_lineage_graph_placeholder
from advanced_data_lineage.cross_domain_provenance_map import build_cross_domain_provenance_map
from advanced_data_lineage.phase_115_handoff import build_phase_115_provider_benchmark_handoff_report
from advanced_data_lineage.data_lineage_report_builder import (
    build_traceability_score_markdown_report,
    build_phase_115_handoff_markdown_report,
)


def main():
    settings = Settings()
    project_root = Path(__file__).resolve().parent.parent
    data_lake = DataLake(base_dir=project_root)
    profile = get_default_data_lineage_profile()

    find_df, find_sum = build_lineage_finding_registry(profile)
    pconf_df, pconf_sum = build_provenance_confidence_score_report(profile)
    dtrace_df, dtrace_sum = build_dataset_traceability_score_report(profile)
    ptrace_df, ptrace_sum = build_provider_traceability_score_report(profile)
    graph_df, graph_sum = build_lineage_graph_placeholder(profile)
    cd_df, cd_sum = build_cross_domain_provenance_map(profile)
    h115_df, h115_sum = build_phase_115_provider_benchmark_handoff_report(profile)

    data_lake.save_lineage_finding_registry(find_df, find_sum)
    data_lake.save_provenance_confidence_score_report(pconf_df, pconf_sum)
    data_lake.save_dataset_traceability_score_report(dtrace_df, dtrace_sum)
    data_lake.save_provider_traceability_score_report(ptrace_df, ptrace_sum)
    data_lake.save_lineage_graph_placeholder(graph_df, graph_sum)
    data_lake.save_cross_domain_provenance_map(cd_df, cd_sum)
    data_lake.save_phase_115_provider_benchmark_handoff_report(h115_df, h115_sum)

    out_dir = project_root / "reports" / "output" / "advanced_data_lineage"
    csv_dir = out_dir / "csv"
    md_dir = out_dir / "markdown"
    txt_dir = out_dir / "txt"

    for d in [csv_dir, md_dir, txt_dir]:
        d.mkdir(parents=True, exist_ok=True)

    find_df.to_csv(csv_dir / "lineage_finding_registry.csv", index=False)
    pconf_df.to_csv(csv_dir / "provenance_confidence_scores.csv", index=False)
    dtrace_df.to_csv(csv_dir / "dataset_traceability_scores.csv", index=False)
    ptrace_df.to_csv(csv_dir / "provider_traceability_scores.csv", index=False)
    graph_df.to_csv(csv_dir / "lineage_graph_placeholder.csv", index=False)
    cd_df.to_csv(csv_dir / "cross_domain_provenance_map.csv", index=False)
    h115_df.to_csv(csv_dir / "phase_115_handoff.csv", index=False)

    md_trace = build_traceability_score_markdown_report(dtrace_sum, dtrace_df)
    (md_dir / "traceability_scoring_report.md").write_text(md_trace, encoding="utf-8")
    (txt_dir / "traceability_scoring_report.txt").write_text(md_trace, encoding="utf-8")

    md_h115 = build_phase_115_handoff_markdown_report(h115_sum, h115_df)
    (md_dir / "phase_115_handoff_report.md").write_text(md_h115, encoding="utf-8")
    (txt_dir / "phase_115_handoff_report.txt").write_text(md_h115, encoding="utf-8")

    print(f"Lineage scoring, graph placeholder and Phase 115 handoff built successfully: Mean traceability score = {dtrace_sum['mean_traceability_score']}, {len(h115_df)} handoff items.")


if __name__ == "__main__":
    main()
