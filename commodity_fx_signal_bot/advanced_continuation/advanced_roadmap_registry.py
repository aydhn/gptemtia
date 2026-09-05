import pandas as pd
from .continuation_config import AdvancedContinuationProfile
from .continuation_models import AdvancedRoadmapItem, build_roadmap_id

def build_default_advanced_roadmap_items(profile: AdvancedContinuationProfile) -> list[AdvancedRoadmapItem]:
    return [
        AdvancedRoadmapItem(build_roadmap_id(101, 105, "track_governance_safety"), 101, 105, "track_governance_safety", "MVP sonrası fonksiyonel yeniden açılış", "Phase 101-105", [], ["no scraping", "no live trading"]),
        AdvancedRoadmapItem(build_roadmap_id(106, 115, "track_data_providers"), 106, 115, "track_data_providers", "scraping olmadan veri sağlayıcılar, haber/makro takvim ve veri kalitesi", "Phase 106-115", [], ["no scraping"]),
        AdvancedRoadmapItem(build_roadmap_id(116, 125, "track_feature_engine"), 116, 125, "track_feature_engine", "feature/indicator/factor engine", "Phase 116-125", [], []),
        AdvancedRoadmapItem(build_roadmap_id(126, 135, "track_regime_engine"), 126, 135, "track_regime_engine", "rejim sınıflandırma ve piyasa davranışı", "Phase 126-135", [], []),
        AdvancedRoadmapItem(build_roadmap_id(136, 145, "track_ml_gpu"), 136, 145, "track_ml_gpu", "gelişmiş ML ve GPU hızlandırma", "Phase 136-145", [], []),
        AdvancedRoadmapItem(build_roadmap_id(146, 152, "track_backtest_benchmark"), 146, 152, "track_backtest_benchmark", "backtest, benchmark, stress ve Monte Carlo", "Phase 146-152", [], []),
        AdvancedRoadmapItem(build_roadmap_id(153, 157, "track_portfolio_risk"), 153, 157, "track_portfolio_risk", "portföy optimizasyonu ve risk motoru", "Phase 153-157", [], []),
        AdvancedRoadmapItem(build_roadmap_id(158, 160, "track_final_integration"), 158, 160, "track_final_integration", "full-system integration ve final advanced delivery", "Phase 158-160", [], ["no broker approval"]),
    ]

def build_advanced_roadmap_registry(profile: AdvancedContinuationProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_advanced_roadmap_items(profile)
    df = pd.DataFrame([vars(i) for i in items])
    return df, summarize_advanced_roadmap(df)

def summarize_advanced_roadmap(df: pd.DataFrame) -> dict:
    return {"total_blocks": len(df), "status": "continuation_ready"}
