import os

docs = [
    "commodity_fx_signal_bot/docs/OPERATOR_MANUAL.md",
    "commodity_fx_signal_bot/docs/ANALYST_HANDBOOK.md",
    "commodity_fx_signal_bot/docs/CODEX_AGENT_GUIDE.md",
    "commodity_fx_signal_bot/docs/SAFE_USAGE_GUIDE.md"
]

addition = """
## Local Knowledge Graph (Phase 66)
- **Node/Edge Registry**: Lists all extracted artifacts and their relationships. Use to understand how components link together offline.
- **Artifact Relationship Graph**: Maps dependencies without external cloud/DB usage. Does not execute code.
- **Relationship Query**: Use for searching internal linkages (e.g. which report relates to which policy). Cannot generate investment advice or live commands.
- **Semantic Keyword/TF-IDF Index**: Local text index only. External vector DBs are strictly disabled.
- **Graph Centrality**: Purely structural metric. Does not denote investment opportunity or trading significance.
- **Graph Gap/Orphan/Stale Report**: Useful for internal consistency audits. Not an indicator of live market risks.
- **Notice**: No live trading, broker execution, external vector DB, cloud upload, or investment advice is provided by the Knowledge Graph tools.
"""

for doc in docs:
    if os.path.exists(doc):
        with open(doc, "r") as f:
            content = f.read()
        if "Local Knowledge Graph (Phase 66)" not in content:
            with open(doc, "a") as f:
                f.write(addition)

phase_log = "commodity_fx_signal_bot/docs/PHASE_LOG.md"
if os.path.exists(phase_log):
    with open(phase_log, "r") as f:
        content = f.read()
    if "Phase 66" not in content:
        with open(phase_log, "a") as f:
            f.write("""
## Phase 66: Local Knowledge Graph
- Local knowledge graph profile sistemi eklendi.
- Graph label registry eklendi.
- GraphNode, GraphEdge, RelationshipQuery, RelationshipQueryResult ve GraphExportManifest modelleri eklendi.
- Node registry eklendi.
- Edge registry eklendi.
- Relationship extractors eklendi.
- Artifact relationship graph eklendi.
- Module/report/evidence/card/scenario-regression/command-report graph’ları eklendi.
- Local semantic keyword index eklendi.
- Local TF-IDF index manifest eklendi.
- Relationship query layer eklendi.
- Graph traversal ve neighborhood raporları eklendi.
- Graph centrality/orphan/gap/stale relationship analizleri eklendi.
- Graph export eklendi.
- Graph validation ve quality report eklendi.
- LocalKnowledgeGraphPipeline eklendi.
- DataLake local knowledge graph kayıt desteği aldı.
- Local knowledge graph scriptleri eklendi.
- Testler genişletildi.
""")
