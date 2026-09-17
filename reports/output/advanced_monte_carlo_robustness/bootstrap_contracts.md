# Phase 149: Bootstrap Simulation Contracts Report

> **Disclaimer**: Bu çıktı Phase 149 Monte Carlo Robustness and Parameter Stability raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, Monte-Carlo/readiness/robustness/parameter-stability değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek Monte Carlo execution, bootstrap, resampling, parameter optimization, parameter sweep, optimizer, gerçek model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek VaR/ES/distribution/robustness metric hesaplama, performans garantisi, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Total Methods**: `4`
- **All Unexecuted**: `True`
- **Status**: `monte_carlo_contract_ready`

## Bootstrap Specifications

                   method_name           resampling_type  preserves_autocorrelation       resampling_block_size_formula  requires_iid_assumption                                                                                      description                                    profile_name  current_phase  simulation_executed  sample_generated                     status                    domain
        standard_iid_bootstrap       uniform_replacement                      False          b = 1 (single observation)                     True    Standard Efron IID bootstrap drawing returns with replacement, destroying serial correlation. balanced_local_monte_carlo_robustness_contracts            149                False             False monte_carlo_contract_ready bootstrap_contract_domain
      circular_block_bootstrap wrapped_block_replacement                       True                   b = ceil(T^(1/3))                    False  Circular block bootstrap wrapping ends of the series to ensure uniform observation probability. balanced_local_monte_carlo_robustness_contracts            149                False             False monte_carlo_contract_ready bootstrap_contract_domain
wild_bootstrap_heteroskedastic       residual_multiplier                      False v ~ Rademacher distribution {-1, 1}                    False             Wild bootstrap preserving conditional heteroskedasticity in time series innovations. balanced_local_monte_carlo_robustness_contracts            149                False             False monte_carlo_contract_ready bootstrap_contract_domain
         studentized_bootstrap    t_statistic_resampling                      False         t* = (theta* - theta) / se*                     True Second-order accurate bootstrap for confidence interval estimation without normal approximation. balanced_local_monte_carlo_robustness_contracts            149                False             False monte_carlo_contract_ready bootstrap_contract_domain
