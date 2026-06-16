import re

file_path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(file_path, "r") as f:
    content = f.read()

addition = """
# Phase 66: Local Knowledge Graph
def build_graph_disclaimer() -> str:
    return "Bu çıktı offline/local knowledge graph ve artifact relationship raporudur. Canlı emir, broker talimatı, gerçek pozisyon, external vector DB, cloud graph DB, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir."

def build_graph_node_edge_registry_text_report(summary: dict, node_df: pd.DataFrame | None = None, edge_df: pd.DataFrame | None = None) -> str:
    lines = ["# GRAPH NODE AND EDGE REGISTRY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if node_df is not None:
        lines.append("\\n## NODES\\n" + node_df.head(100).to_string())
    if edge_df is not None:
        lines.append("\\n## EDGES\\n" + edge_df.head(100).to_string())
    return "\\n".join(lines)

def build_artifact_relationship_graph_text_report(summary: dict, graph_df: pd.DataFrame | None = None) -> str:
    lines = ["# ARTIFACT RELATIONSHIP GRAPH REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if graph_df is not None:
        lines.append("\\n## GRAPH\\n" + graph_df.head(100).to_string())
    return "\\n".join(lines)

def build_semantic_index_text_report(summary: dict, keyword_df: pd.DataFrame | None = None) -> str:
    lines = ["# LOCAL SEMANTIC KEYWORD INDEX REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if keyword_df is not None:
        lines.append("\\n## INDEX\\n" + keyword_df.head(100).to_string())
    return "\\n".join(lines)

def build_relationship_query_text_report(summary: dict, results_df: pd.DataFrame | None = None) -> str:
    lines = ["# RELATIONSHIP QUERY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if results_df is not None:
        lines.append("\\n## RESULTS\\n" + results_df.head(100).to_string())
    return "\\n".join(lines)

def build_graph_analysis_text_report(summary: dict, centrality_df: pd.DataFrame | None = None, gap_df: pd.DataFrame | None = None) -> str:
    lines = ["# GRAPH ANALYSIS REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if centrality_df is not None:
        lines.append("\\n## CENTRALITY\\n" + centrality_df.head(100).to_string())
    if gap_df is not None:
        lines.append("\\n## GAPS\\n" + gap_df.head(100).to_string())
    return "\\n".join(lines)

def build_graph_quality_text_report(summary: dict, quality: dict | None = None) -> str:
    lines = ["# GRAPH QUALITY REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    if quality is not None:
        lines.append("\\n## QUALITY\\n")
        for k, v in quality.items():
            lines.append(f"{k}: {v}")
    return "\\n".join(lines)

def build_graph_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = ["# GRAPH STATUS REPORT", build_graph_disclaimer()]
    for k, v in summary.items():
        lines.append(f"{k}: {v}")
    lines.append("\\n## STATUS\\n" + status_df.to_string())
    return "\\n".join(lines)

"""

if "build_graph_disclaimer" not in content:
    content = content + "\n\n" + addition

with open(file_path, "w") as f:
    f.write(content)
