with open("commodity_fx_signal_bot/README.md", "a") as f:
    f.write("""

## Teorik Position Sizing Candidate Katmanı

- Bu faz gerçek position sizing motoru değildir.
- theoretical_units gerçek lot/adet/kontrat değildir.
- theoretical_notional gerçek portföy emri değildir.
- sizing_approved_candidate gerçek işlem onayı değildir.
- sizing_rejected_candidate gerçek emir iptali değildir.
- Bu katman ATR, volatilite, risk readiness ve teorik risk bütçesine göre simülasyon amaçlı sizing adayları üretir.
- Gerçek stop-loss, take-profit, leverage, broker emri, paper trade ve canlı işlem yoktur.
- Bu katman ileride backtest ve paper trade simülasyonlarının temel girdilerinden biri olacaktır.

**Komutlar:**
```bash
python -m scripts.run_sizing_candidate_preview --symbol GC=F --timeframe 1d
python -m scripts.run_sizing_batch_build --limit 10 --timeframe 1d
python -m scripts.run_sizing_pool_preview --timeframe 1d --top 20
python -m scripts.run_sizing_status
```
""")
