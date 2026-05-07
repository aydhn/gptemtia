import re

with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

section = """
## Teorik Stop/Target Level Candidate Katmanı

Bu faz gerçek stop-loss/take-profit motoru değildir.
theoretical_stop_level gerçek stop-loss emri değildir.
theoretical_target_level gerçek take-profit emri değildir.
invalidation_zone gerçek stop veya pozisyon kapatma talimatı değildir.
reward_risk gerçek trade planı değil simülasyon metriğidir.
Level candidate katmanı ATR, structure, volatility adjustment ve reward/risk hesapları üretir.
Gerçek emir, broker, paper trade, pozisyon açma/kapama yoktur.
Bu katman ileride backtest ve paper trade simülasyonlarının seviye girdilerinden biri olacaktır.

Komutları ekle:
```bash
python -m scripts.run_level_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_reward_risk_preview --symbol GC=F --timeframe 1d
python -m scripts.run_level_batch_build --limit 10 --timeframe 1d
python -m scripts.run_level_status
```
"""

content += "\n" + section

with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(content)
