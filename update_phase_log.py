import os

if not os.path.exists("commodity_fx_signal_bot/docs/PHASE_LOG.md"):
    with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
        f.write("# Phase Log\n")

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    content = f.read()

phase_log = """
## Phase 9
- Trend advanced modülü eklendi.
- Multi SMA/EMA/WMA/HMA/MACD/ADX/Aroon eklendi.
- Ichimoku full hesaplama eklendi.
- Price-MA distance, MA slope, MA stack ve trend persistence eklendi.
- Trend event detection eklendi.
- TrendFeatureSetBuilder eklendi.
- IndicatorPipeline trend feature desteği aldı.
- DataLake trend/trend_events feature set desteği aldı.
- Trend preview/batch/status scriptleri eklendi.
- Testler genişletildi.
"""

if "Phase 9" not in content:
    content += phase_log
    with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
        f.write(content)
