import pandas as pd
from .continuation_config import AdvancedContinuationProfile
from .continuation_models import PhasePlanItem

def build_default_phase_plan_items(profile: AdvancedContinuationProfile) -> list[PhasePlanItem]:
    plans = [
        (101, "Post-MVP Functional Reopen"), (102, "Core Runtime Consolidation"),
        (103, "Research Engine Interface Layer"), (104, "Advanced Config Profile System"),
        (105, "Functional Gap Closure Report"), (106, "Multi-Provider Data Abstraction"),
        (107, "FX Data Provider Layer"), (108, "Commodities Data Provider Layer"),
        (109, "Macro Data Provider Layer"), (110, "Economic Calendar Integration No Scraping"),
        (111, "News Metadata Integration No Scraping"), (112, "Data Quality Engine"),
        (113, "Data Normalization Layer"), (114, "Data Lineage and Provenance"),
        (115, "Data Provider Benchmark Report"), (116, "Advanced Indicator Registry"),
        (117, "Multi-Timeframe Feature Engine"), (118, "Volatility Feature Pack"),
        (119, "Trend and Momentum Feature Pack"), (120, "Mean Reversion Feature Pack"),
        (121, "Macro-Factor Feature Pack"), (122, "Cross-Asset Correlation Features"),
        (123, "Feature Selection Layer"), (124, "Feature Stability and Drift Monitor"),
        (125, "Feature Store v2 Report"), (126, "Regime Engine v2"),
        (127, "Volatility Regime Classifier"), (128, "Trend Regime Classifier"),
        (129, "Liquidity and Spread Regime Layer"), (130, "Macro Regime Classifier"),
        (131, "Cross-Asset Regime Map"), (132, "Regime Transition Detection"),
        (133, "Regime-Specific Strategy Router"), (134, "Regime Backtest Comparison"),
        (135, "Regime Intelligence Report"), (136, "ML Pipeline v2 Architecture"),
        (137, "GPU Acceleration Readiness Layer"), (138, "Classical ML Model Pack"),
        (139, "Time-Series ML Model Pack"), (140, "Ensemble Signal Model"),
        (141, "Model Calibration Layer"), (142, "Model Drift Detection"),
        (143, "Model Explainability Report"), (144, "GPU Benchmark Report"),
        (145, "ML Governance v2"), (146, "Backtest Engine v2"),
        (147, "Transaction Cost and Slippage Layer"), (148, "Walk-Forward Backtesting"),
        (149, "Strategy Benchmark Framework"), (150, "Stress Testing Engine"),
        (151, "Monte Carlo Robustness Layer"), (152, "Backtest Reliability Report"),
        (153, "Portfolio Construction Engine"), (154, "Position Sizing Layer"),
        (155, "Risk Budgeting Layer"), (156, "Portfolio Optimization Engine"),
        (157, "Portfolio Risk Report"), (158, "Full-System Integration Phase"),
        (159, "Advanced Bot Acceptance Rehearsal"), (160, "Full Advanced Bot Final Delivery")
    ]
    items = []
    for p, title in plans:
        items.append(PhasePlanItem(p, title, title, "track_governance_safety", [], [], ["live trading", "broker execution", "investment advice", "model deployment", "production deployment", "scraping"], False))
    return items

def build_phase_101_160_master_plan(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_phase_plan_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_phase_master_plan(df)

def summarize_phase_master_plan(df: pd.DataFrame) -> dict:
    return {"total_phases": len(df), "status": "continuation_ready"}
