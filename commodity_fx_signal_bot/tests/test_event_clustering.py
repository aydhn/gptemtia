import pytest
import pandas as pd
from local_timeline.event_clustering import cluster_events_by_module, cluster_events_by_phase, cluster_events_by_source, build_module_event_cluster_report
from local_timeline.timeline_config import get_default_local_timeline_profile

def test_cluster_events_by_module():
    df = pd.DataFrame([{"module_name": "A"}, {"module_name": "A"}, {"module_name": "B"}])
    profile = get_default_local_timeline_profile()
    clustered, summary = cluster_events_by_module(df, profile)
    assert not clustered.empty
    assert len(clustered) == 2

def test_cluster_events_by_phase():
    df = pd.DataFrame([{"phase_number": 1}, {"phase_number": 2}])
    profile = get_default_local_timeline_profile()
    clustered, summary = cluster_events_by_phase(df, profile)
    assert not clustered.empty
    assert len(clustered) == 2

def test_cluster_events_by_source():
    df = pd.DataFrame([{"source_label": "srcA"}])
    profile = get_default_local_timeline_profile()
    clustered, summary = cluster_events_by_source(df, profile)
    assert not clustered.empty

def test_build_module_event_cluster_report():
    df = pd.DataFrame([{"module_name": "A"}])
    profile = get_default_local_timeline_profile()
    report, summary = build_module_event_cluster_report(df, profile)
    assert not report.empty
    assert summary["total_clusters"] == 1
