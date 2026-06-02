"""
Master orchestration layer map logic.
"""

import pandas as pd
from typing import Dict, Any

from master_orchestration.master_config import MasterOrchestrationProfile
from master_orchestration.master_models import OrchestrationLayer, build_layer_id

_CORE_LAYERS = [
    ("Data", "data_layer", "Data ingestion and storage", ["data", "storage", "data_lake"], []),
    ("Features", "feature_layer", "Feature engineering and storage", ["features", "feature_store"], ["data_layer"]),
    ("Research", "research_layer", "Research reporting and logic", ["research_reports", "portfolio_research", "portfolio_regime", "synthetic_indices", "factor_research", "meta_research"], ["feature_layer", "data_layer"]),
    ("Validation", "validation_layer", "Backtest and regression validation", ["backtest", "validation", "scenario_regression"], ["research_layer", "feature_layer"]),
    ("ML", "ml_layer", "Machine learning predictions", ["ml", "models", "optimizers"], ["feature_layer"]),
    ("Paper", "paper_layer", "Paper trading logic", ["paper"], ["ml_layer", "validation_layer"]),
    ("Governance", "governance_layer", "Offline governance and planning", ["governance", "experiments", "research_planning"], ["research_layer"]),
    ("Reporting", "reporting_layer", "Reporting outputs", ["reports", "report_exports", "report_summarization"], ["research_layer", "validation_layer", "ml_layer", "paper_layer"]),
    ("Knowledge", "knowledge_layer", "Knowledge base management", ["knowledge_base"], ["reporting_layer"]),
    ("Command Center", "command_center_layer", "Offline command center", ["command_center"], ["knowledge_layer"]),
    ("Quality", "quality_layer", "Quality gates and audits", ["quality_gates"], ["reporting_layer"]),
    ("Performance", "performance_layer", "Performance and bottlenecks", ["performance"], ["quality_layer"]),
    ("Maintenance", "maintenance_layer", "System maintenance", ["maintenance"], ["performance_layer"]),
    ("Documentation", "documentation_layer", "Offline documentation refresh", ["documentation"], ["maintenance_layer", "command_center_layer"]),
    ("Scenarios", "scenario_layer", "Scenarios and demo", ["scenarios"], ["validation_layer"]),
    ("Analyst UX", "analyst_ux_layer", "Local Analyst UX", ["analyst_ux"], ["scenario_layer"]),
    ("Final Review", "final_review_layer", "Final review pipelines", ["final_review"], ["documentation_layer", "quality_layer", "performance_layer"]),
    ("Master Orchestration", "master_orchestration_layer", "Master coordination and dry-runs", ["master_orchestration"], ["final_review_layer"])
]

def build_core_orchestration_layers(profile: MasterOrchestrationProfile) -> list[OrchestrationLayer]:
    layers = []
    for name, ltype, desc, modules, depends in _CORE_LAYERS:
        layer_id = build_layer_id(name, ltype)
        layers.append(OrchestrationLayer(
            layer_id=layer_id,
            layer_name=name,
            layer_type=ltype,
            description=desc,
            modules=modules,
            primary_scripts=[],
            output_roots=[],
            depends_on_layers=depends,
            warnings=[]
        ))
    return layers

def build_orchestration_layer_map(profile: MasterOrchestrationProfile) -> pd.DataFrame:
    layers = build_core_orchestration_layers(profile)
    return pd.DataFrame([vars(l) for l in layers])

def infer_layer_for_module(module_name: str) -> str:
    for name, ltype, desc, modules, depends in _CORE_LAYERS:
        if module_name in modules:
            return ltype
    return "unknown_layer"

def build_layer_dependency_table(layer_df: pd.DataFrame) -> pd.DataFrame:
    records = []
    for _, row in layer_df.iterrows():
        ltype = row["layer_type"]
        depends = row["depends_on_layers"]
        if isinstance(depends, list):
            for dep in depends:
                records.append({
                    "source_layer": ltype,
                    "target_layer": dep
                })
    return pd.DataFrame(records) if records else pd.DataFrame(columns=["source_layer", "target_layer"])

def summarize_layer_map(layer_df: pd.DataFrame) -> dict:
    if layer_df.empty:
        return {"total_layers": 0}
    return {
        "total_layers": len(layer_df),
        "layer_types": layer_df["layer_type"].tolist(),
        "has_master_orchestration": "master_orchestration_layer" in layer_df["layer_type"].values
    }
