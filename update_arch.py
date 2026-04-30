with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

trend_arch = """
### Phase 9 Updates
- **Trend Advanced:** Adds advanced multi-parameter trend indicators (SMA, EMA, WMA, HMA, MACD, ADX, Aroon, Ichimoku) along with derivations like MA distances and slopes.
- **Trend Events:** Produces candidate 0/1 boolean events representing key technical occurrences (e.g. MA cross, MACD shift, ADX strengthening).
- **Trend Feature Set Builder:** Aggregates core trend outputs and derivations into a unified feature set, with configurable "compact" vs "full" profiles.

Extended Pipeline flow:
Processed Data Lake → Trend Indicators → Trend Feature Set → Trend Event Detection → Trend Feature Store → Future Strategy Engine
"""

if "Trend Advanced" not in content:
    content += trend_arch
    with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
        f.write(content)
