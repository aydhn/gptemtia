from research_planning.signal_sources import PlanningSignalCollector
from research_planning.planning_config import get_default_research_planning_profile

class MockDataLake:
    def load_governance_audit_report(self, *args, **kwargs):
        raise Exception("Mock error")

    def load_experiment_tracking_table(self, *args, **kwargs):
        raise Exception("Mock error")

    def load_meta_conflict_report(self, *args, **kwargs):
        raise Exception("Mock error")

def test_collect_all_signals():
    lake = MockDataLake()
    collector = PlanningSignalCollector(lake)
    profile = get_default_research_planning_profile()

    signals, summary = collector.collect_all_signals("1d", profile)
    assert isinstance(signals, list)
    assert len(signals) > 0 # Should have missing report signals

    for sig in signals:
        assert "live trade" not in sig.title.lower()
        assert "alarm" not in sig.title.lower()
