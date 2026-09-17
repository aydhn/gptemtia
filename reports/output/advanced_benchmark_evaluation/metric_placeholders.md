# Phase 151: Uncalculated Metric Placeholders Report

> [!WARNING]
> **YASAL UYARI VE GÜVENLİK SINIRI:**
> Bu çıktı Phase 151 Benchmark Comparison and Strategy Evaluation Reports raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, benchmark/evaluation/readiness/strategy-evaluation değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/beta/drawdown hesaplama, performans garantisi, strategy approval, capital allocation, portfolio construction, position sizing, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.


## Summary
- **Total Metrics:** 6
- **All Uncalculated:** True
- **Claims Blocked:** True
- **Status:** evaluation_contract_ready

## Metric Placeholders Registry
                  metric_name      category                             formula_spec                       target_role                                                         description  is_calculated actual_value  performance_claim_allowed                    status  non_signal
     total_return_placeholder return_metric        (end_nav - start_nav) / start_nav cumulative_performance_hypothesis               Kümülatif toplam getiri yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True
annualized_return_placeholder return_metric   (1 + total_return) ** (252 / days) - 1 annualized_performance_hypothesis              Yıllıklandırılmış getiri yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True
       volatility_placeholder   risk_metric           std(daily_returns) * sqrt(252)        annualized_risk_hypothesis Yıllıklandırılmış getiri volatilitesi yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True
         drawdown_placeholder   risk_metric min((nav - rolling_peak) / rolling_peak)          drawdown_risk_hypothesis          Zirveden dibe maksimum kayıp yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True
         win_rate_placeholder  trade_metric            winning_trades / total_trades               hit_rate_hypothesis                  Başarılı işlem oranı yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True
    profit_factor_placeholder  trade_metric        gross_profits / abs(gross_losses)    profitability_ratio_hypothesis                     Kâr faktörü oranı yer tutucusu (hesaplanmamış).          False         None                      False evaluation_contract_ready        True