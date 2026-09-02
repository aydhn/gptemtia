
from pathlib import Path
from local_closure.roadmap_backlog import build_future_roadmap_backlog, build_default_roadmap_items
from local_closure.closure_config import get_default_local_closure_profile

def test_roadmap():
    p = get_default_local_closure_profile()
    df, summary = build_future_roadmap_backlog(Path.cwd(), p)
    assert not df.empty
    assert summary["total_items"] > 0
    
    # live_trading is blocked
    live_item = df[df["title"] == "Live Trading Connection"]
    assert not live_item.empty
    assert live_item.iloc[0]["status"] == "roadmap_blocked_by_safety"
