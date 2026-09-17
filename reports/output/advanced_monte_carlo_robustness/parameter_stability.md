# Phase 149: Parameter Stability and Sensitivity Contracts Report

> **Disclaimer**: Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, bootstrap, resampling, parameter optimization, parameter sweep, optimizer, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Contracts**: `4`
- **All Valid**: `True`
- **Optimizations Disabled**: `True`
- **Status**: `monte_carlo_contract_ready`

## Parameter Stability Matrix

                 parameter_name               strategy_ref                 perturbation_range         sensitivity_metric                                 plateau_detection_rule                                                                               description                                    profile_name  current_phase  optimization_allowed  sweep_allowed                     status                              domain
         lookback_window_length    STRAT_MOMENTUM_TREND_V1 [lookback * 0.80, lookback * 1.20]  Sharpe_Ratio_Variance_Pct Sharpe drop < 15% across +/- 20% lookback neighborhood  Stability contract evaluating lookback window robustness against small parameter shifts. balanced_local_monte_carlo_robustness_contracts            149                 False          False monte_carlo_contract_ready parameter_stability_contract_domain
volatility_stop_loss_multiplier      STRAT_VOL_BREAKOUT_V1   [atr_mult - 0.5, atr_mult + 0.5]  Max_Drawdown_Variance_Pct     Drawdown increase < 20% across ATR multiple shifts Stop-loss parameter stability assessing trade exit resilience across neighborhood values. balanced_local_monte_carlo_robustness_contracts            149                 False          False monte_carlo_contract_ready parameter_stability_contract_domain
        entry_threshold_z_score    STRAT_MEAN_REVERSION_V1   [z_score - 0.25, z_score + 0.25] Win_Rate_Sensitivity_Slope   Win-rate slope |dWR/dz| < 0.10 in local neighborhood                 Mean reversion entry threshold contract verifying broad plateau behavior. balanced_local_monte_carlo_robustness_contracts            149                 False          False monte_carlo_contract_ready parameter_stability_contract_domain
position_sizing_risk_budget_pct STRAT_RISK_PARITY_ALLOC_V1 [risk_pct * 0.85, risk_pct * 1.15]       Tail_Loss_Elasticity                        Elasticity |dCVaR/dRisk| < 1.25               Portfolio risk allocation stability contract examining tail loss linearity. balanced_local_monte_carlo_robustness_contracts            149                 False          False monte_carlo_contract_ready parameter_stability_contract_domain
