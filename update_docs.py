import re

with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

insert_str = """
## Yönsel Ön Karar / Decision Candidate Katmanı
Bu katman signal candidate havuzundan yönsel bias, conflict, neutral/no-trade ve strategy readiness ayrıştırması yapar.

- Bu faz nihai al/sat stratejisi değildir.
- `long_bias_candidate` gerçek long emri değildir.
- `short_bias_candidate` gerçek short emri değildir.
- `no_trade_candidate` sadece kalite/çelişki nedeniyle adayın strateji motoruna aktarılmamasını gösterir.
- Decision score emir değildir.
- `passed_decision_filters` canlı işlem izni değildir.
- Bu katman ileride strateji motoru, backtest, paper trade ve Telegram raporlama için kullanılacaktır.
- Conflict ve neutral filtreleri düşük kaliteli adayları ayrıştırır.

### Komutlar
```bash
python -m scripts.run_decision_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_decision_batch_build --limit 10 --timeframe 1d
python -m scripts.run_decision_pool_preview --timeframe 1d --top 20
python -m scripts.run_decision_status
```
"""

content = content + "\n" + insert_str

with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

insert_str = """
Signal Candidate Pool
→ DecisionInputLoader
→ Directional Bias Analysis
→ Decision Components
→ Conflict Resolver
→ Neutral / No-Trade Filter
→ DecisionEngine
→ DecisionCandidatePool
→ Future Strategy Engine / Backtest / Paper Trade
"""

content = content + "\n" + insert_str

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
    f.write(content)

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    content = f.read()

insert_str = """
### Phase 20: Yönsel Ön Karar ve Bias Ayrıştırması
- Decision profile sistemi eklendi.
- Decision label registry eklendi.
- Directional bias modülü eklendi.
- Decision input loader eklendi.
- Decision component skorları eklendi.
- Conflict resolver eklendi.
- Neutral/no-trade filter eklendi.
- DecisionCandidate dataclass eklendi.
- DecisionEngine eklendi.
- DecisionCandidatePool eklendi.
- Decision quality report eklendi.
- DecisionPipeline eklendi.
- DataLake decision_candidates/decision_pool desteği aldı.
- Decision preview/batch/status scriptleri eklendi.
- Testler genişletildi.
"""

content = content + "\n" + insert_str

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
    f.write(content)
