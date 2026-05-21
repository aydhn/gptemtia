from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class RegimeClassificationResult:
    timestamp: str
    regime_label: str
    volatility_state: str
    trend_state: str
    correlation_state: str
    drawdown_state: str
    regime_score: float
    confidence_score: float
    warnings: List[str]

@dataclass
class MacroScenarioDefinition:
    scenario_id: str
    scenario_label: str
    description: str
    shocked_factor: str
    shock_direction: str
    shock_size: float
    affected_symbols: List[str]
    methodology: str
    warnings: List[str]

@dataclass
class BasketStressTestResult:
    basket_id: str
    scenario_id: str
    timeframe: str
    estimated_return_impact: Optional[float]
    estimated_drawdown_impact: Optional[float]
    estimated_volatility_impact: Optional[float]
    stress_severity: str
    methodology: str
    warnings: List[str]

@dataclass
class DrawdownCluster:
    cluster_id: str
    basket_id: str
    start_timestamp: str
    end_timestamp: str
    depth_pct: float
    duration_bars: int
    recovery_bars: Optional[int]
    cluster_label: str
    warnings: List[str]

def build_regime_id(timestamp: str, regime_label: str) -> str:
    return f"{timestamp}_{regime_label}"

def build_scenario_id(scenario_label: str, shock_size: float) -> str:
    return f"{scenario_label}_{shock_size:.4f}"

def build_stress_result_id(basket_id: str, scenario_id: str) -> str:
    return f"{basket_id}_{scenario_id}"

def build_drawdown_cluster_id(basket_id: str, start_timestamp: str, end_timestamp: str) -> str:
    return f"{basket_id}_{start_timestamp}_{end_timestamp}"

def regime_classification_result_to_dict(result: RegimeClassificationResult) -> dict:
    return asdict(result)

def macro_scenario_definition_to_dict(scenario: MacroScenarioDefinition) -> dict:
    return asdict(scenario)

def basket_stress_test_result_to_dict(result: BasketStressTestResult) -> dict:
    return asdict(result)

def drawdown_cluster_to_dict(cluster: DrawdownCluster) -> dict:
    return asdict(cluster)
