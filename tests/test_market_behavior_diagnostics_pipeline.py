from advanced_market_behavior_diagnostics.market_behavior_diagnostics_pipeline import (
    MarketBehaviorDiagnosticsPipeline,
)
from advanced_market_behavior_diagnostics.market_behavior_diagnostics_config import (
    get_default_market_behavior_diagnostics_profile,
)


def test_market_behavior_diagnostics_pipeline():
    profile = get_default_market_behavior_diagnostics_profile()
    pipeline = MarketBehaviorDiagnosticsPipeline(profile=profile)

    status_df, summary = pipeline.build_market_behavior_diagnostics_status(save=False)

    assert not status_df.empty
    assert summary["overall_status"] == "READY"
    assert summary["current_phase"] == 129
    assert summary["next_phase"] == 130
    assert summary["target_final_phase"] == 160
    assert summary["non_signal"] is True
    assert summary["source_preserved"] is True
    assert summary["clustering_executed"] is False
    assert summary["model_training_executed"] is False
