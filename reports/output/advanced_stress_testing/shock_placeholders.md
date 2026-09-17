# Phase 148: Şok Senaryo Yer Tutucuları Raporu

> [!IMPORTANT]
> **YASAL UYARI VE ARAŞTIRMA BEYANI (PHASE 148)**:
> Bu çıktı Phase 148 Stress Testing and Scenario Simulation raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, stress/readiness/scenario/robustness > değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, > gerçek stress test execution, scenario simulation, optimizer, Monte Carlo, > gerçek model training, model fit/predict/inference, dataset materialization, > target/label/prediction üretimi, gerçek stress PnL/drawdown/VaR/ES hesaplama, > performans garantisi, model deployment, model registry write, model artifact persistence, > scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı > veya gerçek provider API çağrısı değildir.

## Şok Özeti
- **Toplam Şok Yer Tutucu Sayısı**: `0`
- **Gerçek Şok Yürütmesi**: `DEVRE DIŞI`
- **Non-Signal Durumu**: `DOĞRULANDI`

## Şok Yer Tutucuları

| placeholder_name | shock_type | description | magnitude_spec | parameters | real_execution_allowed | non_signal | contains_trading_recommendation | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekend_opening_gap_placeholder | PRICE_DISCONTINUITY | Hafta sonu haber akışından kaynaklanan Pazar akşamı açılış fiyat boşluğu yer tutucusu. | 3x_standard_daily_atr | {'gap_direction': 'BIDIRECTIONAL', 'bypass_stop_loss': True} | False | True | False | True |
| overnight_session_gap_placeholder | OVERNIGHT_GAP | Seans kapanış ile ertesi gün açılışı arasındaki fiyat boşluğu yer tutucusu. | 1.5x_standard_daily_atr | {'gap_direction': 'ADVERSE', 'bypass_stop_loss': True} | False | True | False | True |
| macro_announcement_intraday_gap_placeholder | INTRADAY_JUMP | Veri açıklanma anındaki ardışık çubuksuz dikey fiyat atlaması yer tutucusu. | 2.0x_standard_daily_atr | {'jump_latency_ms': 50, 'liquidity_void': True} | False | True | False | True |
