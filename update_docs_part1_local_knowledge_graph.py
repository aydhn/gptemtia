file_path = "commodity_fx_signal_bot/README.md"
with open(file_path, "r") as f:
    readme_content = f.read()

addition = """
## Local Knowledge Graph and Artifact Relationship Query

- Local knowledge graph external vector DB veya cloud graph DB değildir.
- Semantic index local keyword/TF-IDF tabanlıdır.
- Relationship query komut çalıştırmaz ve yatırım tavsiyesi üretmez.
- Graph centrality yatırım fırsatı veya önem garantisi değildir.
- Graph export local JSON/CSV/GraphML çıktısıdır; cloud upload yapmaz.
- Raw secret/private data graph içine yazılmaz.
- Çıktılar data/lake/local_knowledge_graph ve reports/output/local_knowledge_graph altında oluşur.

### Phase 66 Commands
- `python -m scripts.run_graph_node_edge_registry`: Produces artifact nodes and relationship edges.
- `python -m scripts.run_artifact_relationship_graph`: Builds full artifact relationship graph.
- `python -m scripts.run_semantic_index_report`: Builds local semantic/TF-IDF indices.
- `python -m scripts.run_relationship_query --query "final review hangi evidence dosyalarıyla ilişkili?"`: Queries graph offline.
- `python -m scripts.run_graph_analysis_report`: Runs centrality, orphans, and gap analysis.
- `python -m scripts.run_graph_quality_report`: Validates graph and generates export manifest.
- `python -m scripts.run_graph_status`: Checks graph creation status.
"""

if "Local Knowledge Graph and Artifact Relationship Query" not in readme_content:
    with open(file_path, "a") as f:
        f.write(addition)


file_path2 = "commodity_fx_signal_bot/docs/ARCHITECTURE.md"
with open(file_path2, "r") as f:
    arch_content = f.read()

arch_addition = """
## Local Knowledge Graph Data Flow

Artifact Metadata / Evidence Governance / Report Summaries / Docs / Commands / Scenarios / Regression / DataLake / Reports
→ NodeRegistry
→ EdgeRegistry
→ RelationshipExtractors
→ ArtifactRelationshipGraph
→ ModuleGraph
→ ReportGraph
→ EvidenceGraph
→ CardGraph
→ ScenarioRegressionGraph
→ CommandReportGraph
→ LocalSemanticKeywordIndex
→ LocalTFIDFIndex
→ RelationshipQuery
→ GraphTraversal
→ GraphAnalysis
→ GraphGapDetection
→ GraphExport
→ GraphValidation
→ GraphQuality
→ Local Knowledge Graph Outputs
"""

if "Local Knowledge Graph Data Flow" not in arch_content:
    with open(file_path2, "a") as f:
        f.write(arch_addition)
