# Phase 150: Backtest Governance Findings Report

> **Disclaimer**: Bu çıktı Phase 150 Backtest Governance and Bias Control raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, backtest/governance/bias-control/readiness değerini trade sinyali veya production-ready/broker-ready/onay olarak kullanma, gerçek backtest execution, benchmark execution, metric calculation, optimizer, model training, model fit/predict/inference, dataset materialization, target/label/prediction üretimi, gerçek Sharpe/win-rate/return/alpha/drawdown hesaplama, performans garantisi, strategy approval, model deployment, model registry write, model artifact persistence, scraping, haber tam metni/article body/raw content/scraped HTML/embedding/vector kullanımı veya gerçek provider API çağrısı değildir.

- **Domain**: `finding_domain`
- **Total Findings**: `4`
- **Critical Count**: `0`
- **High Count**: `0`
- **Manual Review Required Count**: `2`
- **Status**: `governance_contract_ready`

## Findings Registry

                                    finding_id                       finding_type         domain severity_label                                                                                                                         message                                                                                   recommendation  manual_review_required  auto_remediation_allowed                                 profile_name  current_phase  non_signal  local_only
        FINDING_150_CONTRACT_LAYER_MODE_ACTIVE         contract_layer_mode_active finding_domain           INFO Phase 150 operating in contract-only mode. All backtest execution, metric calculations, and performance claims remain disabled. Review governance contracts, bias controls, and claim boundaries before proceeding to Phase 151.                    True                     False balanced_local_backtest_governance_contracts            150        True        True
FINDING_150_OFFLINE_RESEARCH_BOUNDARY_ENFORCED offline_research_boundary_enforced finding_domain           INFO                                  Zero live trading and zero broker connectivity invariants verified across all active profiles.                                                Maintain strict local/offline research perimeter.                   False                     False balanced_local_backtest_governance_contracts            150        True        True
      FINDING_150_BIAS_CONTROL_GUARDS_VERIFIED       bias_control_guards_verified finding_domain           INFO                   Lookahead, survivorship, data snooping, overfitting, multiple testing, and parameter fishing controls active.                        Preserve all guard policies and validation gates in downstream pipelines.                   False                     False balanced_local_backtest_governance_contracts            150        True        True
         FINDING_150_MANUAL_REVIEW_GATES_ARMED          manual_review_gates_armed finding_domain           INFO                      Ten manual review gates armed requiring explicit human operator verification before any phase progression.                             Perform manual review of review items MRQ_150_01 through MRQ_150_10.                    True                     False balanced_local_backtest_governance_contracts            150        True        True
