# Phase 126: Regime Environmental Contexts Report

> **UYARI / DISCLAIMER:** Bu çıktı Phase 126 Regime Classification and Market Behavior Foundation raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, regime state değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, clustering execution, prediction/target üretimi, production-ready/official approval/broker-ready iddiası, haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Özet
- **Bağlam Tipi:** `Event Context`
- **Toplam Kayıt:** `5`
- **Haberler Sadece Metaveri:** `True`
- **Non-Signal:** `True`

## Bağlam Tablosu
| context_id | context_name | regime_family | description | underlying_features | source_phases | non_signal | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| event_ctx_01_pre | pre_event_context | regime_family_event_context | Pre-event window context (e.g. 60-15 minutes prior to scheduled release) characterized by order book thinning | minutes_to_event, pre_event_volatility_dampening | [110, 120, 122] | True | regime_ready |
| event_ctx_02_post | post_event_context | regime_family_event_context | Post-event window context (e.g. 0-60 minutes following announcement) characterized by price re-anchoring | minutes_since_event, post_event_dispersion_ratio | [110, 120, 122] | True | regime_ready |
| event_ctx_03_importance | event_importance_context | regime_family_event_context | High/medium/low event importance tiering filtering non-impacting calendar releases | event_tier_score, historical_market_impact_rank | [110, 120, 122] | True | regime_ready |
| event_ctx_04_delay | release_delay_context | regime_family_event_context | Release reporting latency measuring delta between official release timestamp and market publication | reporting_latency_seconds, embargo_compliance_flag | [110, 120, 122] | True | regime_ready |
| event_ctx_05_window | event_window_context | regime_family_event_context | Combined pre/post boundary envelope active window masking normal technical regime attribution | is_event_window_active, active_event_count | [110, 120, 122] | True | regime_ready |