with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

trend_section = """
## Phase 9: Trend Feature ve Trend Event Katmanı

Bu faz nihai al/sat stratejisi değildir.
Trend eventleri sadece aday olaylardır (ön sinyal).
SMA, EMA, WMA, HMA, MACD, ADX, DMI, Aroon, Ichimoku gibi trend göstergeleri kullanılır.

**Compact ve Full Trend Feature Set Farkı:**
- **Compact:** Daha az kolonla sadece en kritik trend özelliklerini (SMA 20/50/200, MACD, temel ADX/Aroon vb.) üretir. Backtest ve ML için daha hafiftir.
- **Full:** Belirtilen indikatörlerin birçok farklı parametre setiyle olan kombinasyonlarını ve ek olarak Ichimoku Cloud'u içerir.

**Uyarı:** Ichimoku ve forward-shift içeren yapıların (Chikou Span) leakage (gelecekten bilgi sızdırma) riski vardır; strateji/ML tarafında dikkatle kullanılmalıdır.

Event kolonları (örn. `event_ma_stack_bullish`, `event_macd_hist_positive_shift`) ileride strateji ve backtest motoru tarafından kullanılacaktır. Trend eventleri tek başına işlem kararı değildir.

**Kullanım Komutları:**
```bash
python -m scripts.run_trend_feature_preview --symbol GC=F --timeframe 1d
python -m scripts.run_trend_event_preview --symbol GC=F --timeframe 1d
python -m scripts.run_trend_batch_build --limit 10
python -m scripts.run_trend_status
```
"""

if "Trend Feature ve Trend Event" not in content:
    content += trend_section
    with open("commodity_fx_signal_bot/README.md", "w") as f:
        f.write(content)
