from dataclasses import dataclass
from typing import Optional, List, Dict
import hashlib

@dataclass
class GraphNode:
    node_id: str
    node_type: str
    label: str
    module_name: Optional[str]
    relative_path: Optional[str]
    title: str
    summary: str
    metadata: Dict
    warnings: List[str]

@dataclass
class GraphEdge:
    edge_id: str
    source_node_id: str
    target_node_id: str
    edge_type: str
    relationship_strength: str
    evidence: str
    weight: float
    metadata: Dict
    warnings: List[str]

@dataclass
class RelationshipQuery:
    query_id: str
    query_text: str
    query_intent: str
    matched_terms: List[str]
    filters: Dict
    warnings: List[str]

@dataclass
class RelationshipQueryResult:
    result_id: str
    query_id: str
    node_id: Optional[str]
    edge_id: Optional[str]
    rank: int
    score: float
    explanation: str
    warnings: List[str]

@dataclass
class GraphExportManifest:
    export_id: str
    profile_name: str
    created_at_utc: str
    node_count: int
    edge_count: int
    export_formats: List[str]
    local_only: bool
    warnings: List[str]

def build_graph_node_id(node_type: str, label: str, relative_path: Optional[str] = None) -> str:
    seed = f"{node_type}_{label}_{relative_path or ''}".encode('utf-8')
    return "node_" + hashlib.sha256(seed).hexdigest()[:12]

def build_graph_edge_id(source_node_id: str, target_node_id: str, edge_type: str) -> str:
    seed = f"{source_node_id}_{target_node_id}_{edge_type}".encode('utf-8')
    return "edge_" + hashlib.sha256(seed).hexdigest()[:12]

def build_relationship_query_id(query_text: str) -> str:
    return "query_" + hashlib.sha256(query_text.encode('utf-8')).hexdigest()[:12]

def build_relationship_query_result_id(query_id: str, rank: int) -> str:
    return f"{query_id}_res_{rank}"

def build_graph_export_id(profile_name: str, created_at_utc: str) -> str:
    seed = f"{profile_name}_{created_at_utc}".encode('utf-8')
    return "export_" + hashlib.sha256(seed).hexdigest()[:12]

def graph_node_to_dict(node: GraphNode) -> dict:
    return {
        "node_id": node.node_id,
        "node_type": node.node_type,
        "label": node.label,
        "module_name": node.module_name,
        "relative_path": node.relative_path,
        "title": node.title,
        "summary": node.summary,
        "metadata": node.metadata,
        "warnings": node.warnings
    }

def graph_edge_to_dict(edge: GraphEdge) -> dict:
    return {
        "edge_id": edge.edge_id,
        "source_node_id": edge.source_node_id,
        "target_node_id": edge.target_node_id,
        "edge_type": edge.edge_type,
        "relationship_strength": edge.relationship_strength,
        "evidence": edge.evidence,
        "weight": edge.weight,
        "metadata": edge.metadata,
        "warnings": edge.warnings
    }

def relationship_query_to_dict(query: RelationshipQuery) -> dict:
    return {
        "query_id": query.query_id,
        "query_text": query.query_text,
        "query_intent": query.query_intent,
        "matched_terms": query.matched_terms,
        "filters": query.filters,
        "warnings": query.warnings
    }

def relationship_query_result_to_dict(result: RelationshipQueryResult) -> dict:
    return {
        "result_id": result.result_id,
        "query_id": result.query_id,
        "node_id": result.node_id,
        "edge_id": result.edge_id,
        "rank": result.rank,
        "score": result.score,
        "explanation": result.explanation,
        "warnings": result.warnings
    }

def graph_export_manifest_to_dict(manifest: GraphExportManifest) -> dict:
    return {
        "export_id": manifest.export_id,
        "profile_name": manifest.profile_name,
        "created_at_utc": manifest.created_at_utc,
        "node_count": manifest.node_count,
        "edge_count": manifest.edge_count,
        "export_formats": manifest.export_formats,
        "local_only": manifest.local_only,
        "warnings": manifest.warnings
    }
