import json
from pathlib import Path

import pandas as pd

from config.settings import Settings
from governance.artifact_inventory import ArtifactInventoryBuilder
from governance.audit_trail import (
    build_audit_events_from_inventory,
    build_audit_events_from_lineage,
)
from governance.dependency_tracing import ArtifactDependencyTracer
from governance.experiment_lineage_bridge import (
    build_experiment_lineage_table,
)
from governance.freshness_governance import (
    build_freshness_governance_table,
)
from governance.governance_checklist import (
    build_research_governance_checklist,
    evaluate_governance_checklist,
    summarize_governance_checklist,
)
from governance.governance_config import GovernanceProfile, get_default_governance_profile
from governance.governance_quality import build_governance_quality_report
from governance.governance_report_builder import (
    build_artifact_inventory_markdown_report,
    build_audit_trail_markdown_report,
    build_dependency_trace_markdown_report,
    build_lineage_graph_markdown_report,
    build_provenance_markdown_report,
    build_research_governance_markdown_report,
)
from governance.integrity_governance import (
    build_integrity_governance_table,
)
from governance.lineage_graph import build_artifact_lineage_graph
from governance.provenance_registry import build_provenance_records_from_inventory
from governance.source_attribution import (
    build_data_source_attribution_table,
)


class GovernancePipeline:
    def __init__(self, data_lake, settings: Settings, project_root: Path, profile: GovernanceProfile | None = None):
        self.data_lake = data_lake
        self.settings = settings
        self.project_root = project_root
        self.profile = profile or get_default_governance_profile()

        # We need reports_root, using relative to project root usually
        self.reports_root = self.project_root / "reports" / "output"
        self.data_lake_root = self.project_root / "data" / "lake"

    def build_artifact_inventory_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        builder = ArtifactInventoryBuilder(self.project_root, self.data_lake_root, self.reports_root)
        df, summary = builder.scan_artifacts(self.profile)

        if save and hasattr(self.data_lake, "save_artifact_inventory"):
            self.data_lake.save_artifact_inventory(df, summary)

            # also save markdown
            md = build_artifact_inventory_markdown_report(summary, df)
            md_path = self.reports_root / "governance" / "markdown" / "artifact_inventory_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

        return df, summary

    def build_lineage_graph_report(self, save: bool = True) -> tuple[dict[str, pd.DataFrame], dict]:
        df_inv, sum_inv = self.build_artifact_inventory_report(save=False)
        df_prov, _ = build_provenance_records_from_inventory(df_inv)

        graph, meta = build_artifact_lineage_graph(df_inv, df_prov)
        nodes_df = graph.to_node_dataframe()
        edges_df = graph.to_edge_dataframe()

        if save and hasattr(self.data_lake, "save_lineage_nodes"):
            self.data_lake.save_lineage_nodes(nodes_df, meta)
            self.data_lake.save_lineage_edges(edges_df, meta)

            md = build_lineage_graph_markdown_report(meta, nodes_df, edges_df)
            md_path = self.reports_root / "governance" / "markdown" / "lineage_graph_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

        return {"nodes": nodes_df, "edges": edges_df}, meta

    def build_provenance_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df_inv, sum_inv = self.build_artifact_inventory_report(save=False)
        df_prov, summary = build_provenance_records_from_inventory(df_inv)

        if save and hasattr(self.data_lake, "save_provenance_records"):
            self.data_lake.save_provenance_records(df_prov, summary)

            md = build_provenance_markdown_report(summary, df_prov)
            md_path = self.reports_root / "governance" / "markdown" / "provenance_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

        return df_prov, summary

    def build_dependency_trace_report(self, artifact_id_or_node_id: str | None = None, symbol: str | None = None, module_name: str | None = None, direction: str = "upstream", save: bool = True) -> tuple[pd.DataFrame, dict]:
        df_inv, _ = self.build_artifact_inventory_report(save=False)
        df_prov, _ = build_provenance_records_from_inventory(df_inv)
        graph, _ = build_artifact_lineage_graph(df_inv, df_prov)

        tracer = ArtifactDependencyTracer(graph)

        if artifact_id_or_node_id:
            if direction == "upstream":
                df_trace, meta = tracer.trace_upstream(artifact_id_or_node_id, self.profile.lineage_max_depth)
            else:
                df_trace, meta = tracer.trace_downstream(artifact_id_or_node_id, self.profile.lineage_max_depth)
        elif symbol:
            df_trace, meta = tracer.trace_symbol_dependencies(symbol, df_inv, self.profile.lineage_max_depth)
        elif module_name:
            df_trace, meta = tracer.trace_module_dependencies(module_name, df_inv, self.profile.lineage_max_depth)
        else:
            return pd.DataFrame(), {"warnings": ["No target provided for trace"]}

        if save and hasattr(self.data_lake, "save_dependency_trace"):
            trace_name = symbol or module_name or artifact_id_or_node_id or "trace"
            self.data_lake.save_dependency_trace(trace_name, df_trace, meta)

            md = build_dependency_trace_markdown_report(meta, df_trace)
            md_path = self.reports_root / "governance" / "markdown" / "dependency_trace_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

        return df_trace, meta

    def build_audit_trail_report(self, save: bool = True) -> tuple[pd.DataFrame, dict]:
        df_inv, _ = self.build_artifact_inventory_report(save=False)
        df_prov, _ = build_provenance_records_from_inventory(df_inv)
        graph, _ = build_artifact_lineage_graph(df_inv, df_prov)
        nodes_df = graph.to_node_dataframe()
        edges_df = graph.to_edge_dataframe()

        df_audit1, meta1 = build_audit_events_from_inventory(df_inv)
        df_audit2, meta2 = build_audit_events_from_lineage(nodes_df, edges_df)

        df_audit = pd.concat([df_audit1, df_audit2], ignore_index=True)
        summary = {
            "total_events": len(df_audit),
            "event_types": df_audit["event_label"].value_counts().to_dict() if not df_audit.empty else {}
        }

        if save and hasattr(self.data_lake, "save_audit_trail"):
            self.data_lake.save_audit_trail(df_audit, summary)

            md = build_audit_trail_markdown_report(summary, df_audit)
            md_path = self.reports_root / "governance" / "markdown" / "audit_trail_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

        return df_audit, summary

    def build_research_governance_report(self, save: bool = True) -> tuple[dict, dict]:
        # Build all parts
        df_inv, sum_inv = self.build_artifact_inventory_report(save=False)
        df_prov, sum_prov = build_provenance_records_from_inventory(df_inv)
        graph, sum_lin = build_artifact_lineage_graph(df_inv, df_prov)
        nodes_df = graph.to_node_dataframe()
        edges_df = graph.to_edge_dataframe()

        df_audit, sum_audit = self.build_audit_trail_report(save=False)

        df_src = build_data_source_attribution_table(df_inv, df_prov)
        df_fresh = build_freshness_governance_table(df_inv)
        df_int = build_integrity_governance_table(df_inv)

        df_exp, sum_exp = build_experiment_lineage_table(self.data_lake, df_inv)

        base_checklist = build_research_governance_checklist(self.profile)
        eval_checklist = evaluate_governance_checklist(base_checklist, df_inv, sum_lin, sum_audit)

        quality = build_governance_quality_report(
            summary={},
            inventory_df=df_inv,
            provenance_df=df_prov,
            node_df=nodes_df,
            edge_df=edges_df
        )

        full_summary = {
            "inventory": sum_inv,
            "lineage": sum_lin,
            "audit": sum_audit,
            "quality": quality,
            "checklist": summarize_governance_checklist(eval_checklist)
        }

        if save and hasattr(self.data_lake, "save_research_governance_report"):
            # Mock savings of internal parts can be done here, but usually done via orchestrator.
            # Just save the final report

            md = build_research_governance_markdown_report(full_summary, eval_checklist)
            self.data_lake.save_research_governance_report(self.profile.name, full_summary, md)

            md_path = self.reports_root / "governance" / "markdown" / "research_governance_report.md"
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, "w") as f:
                f.write(md)

            json_path = self.reports_root / "governance" / "json" / "research_governance_report.json"
            json_path.parent.mkdir(parents=True, exist_ok=True)
            with open(json_path, "w") as f:
                json.dump(full_summary, f, indent=2)

        return full_summary, full_summary
