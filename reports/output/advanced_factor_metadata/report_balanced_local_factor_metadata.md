# Phase 122: Factor Metadata Profile Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Profile Summary
- **Active Profile**: `balanced_local_factor_metadata`
- **Total Profiles**: 3
- **Current Phase**: 122
- **Target Final Phase**: 160
- **Next Phase**: 123
- **Dry Run Default**: True
- **Non-Signal Mandate**: True
- **Status**: `factor_ready`

## Registered Profiles
| profile_id | profile_name | current_phase | target_final_phase | next_phase | local_only | non_production | research_only | dry_run | non_signal | status_label | warnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| prof_balanced_local_factor_metadata_0f253983 | balanced_local_factor_metadata | 122 | 160 | 123 | True | True | True | True | True | factor_ready | [] |
| prof_strict_non_signal_factor_metadata_496b53c8 | strict_non_signal_factor_metadata | 122 | 160 | 123 | True | True | True | True | True | factor_ready | [] |
| prof_dry_run_factor_contract_focus_97d2ab41 | dry_run_factor_contract_focus | 122 | 160 | 123 | True | True | True | True | True | factor_ready | [] |


---

# Phase 122: Factor Family Taxonomy Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Family Taxonomy Overview
- **Active Profile**: `balanced_local_factor_metadata`
- **Total Families**: 12
- **Ready Families**: 9
- **Placeholder Families**: 3
- **Non-Signal Mandate**: True
- **Status**: `factor_ready`

## Family Specifications
| family_id | family_label | family_name | description | source_feature_families | expected_inputs | non_signal_usage_note | status_label | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fam_factor_family_trend_1a0c7209 | factor_family_trend | Trend Factor Family | Directional persistence and slope metrics derived from moving averages and channel breakouts. | ['moving_average_grid', 'donchian_grid', 'macd_features'] | ['sma_grid', 'ema_grid', 'donchian_high', 'donchian_low'] | Research grouping for trend slope and channel context. Strictly non-signal. | factor_ready | False |
| fam_factor_family_momentum_096d6131 | factor_family_momentum | Momentum Factor Family | Velocity and rate of price changes derived from oscillators and multi-window ROC. | ['rsi_grid', 'roc_grid', 'stochastic_grid'] | ['rsi_14', 'roc_10', 'roc_20', 'stoch_k'] | Research grouping for momentum magnitude. Not an overbought/oversold signal. | factor_ready | False |
| fam_factor_family_volatility_48ba9b71 | factor_family_volatility | Volatility Factor Family | Dispersion, range, and realized variance metrics across parameterized observation windows. | ['atr_grid', 'realized_vol_grid', 'bollinger_bandwidth'] | ['atr_14', 'rolling_std_20', 'realized_vol_20', 'bb_width_20'] | Risk and dispersion context. Zero directional claim or position sizing. | factor_ready | False |
| fam_factor_family_mean_reversion_db973651 | factor_family_mean_reversion | Mean Reversion Factor Family | Distance-to-mean, standard score (z-score), and oscillation boundary metrics. | ['zscore_grid', 'distance_to_ma_grid', 'percentile_rank'] | ['zscore_20', 'dist_sma_50', 'percentile_100'] | Distributional distance context. Not an entry or counter-trend signal. | factor_ready | False |
| fam_factor_family_return_49116008 | factor_family_return | Return Factor Family | Multi-horizon trailing returns and cumulative log return representations. | ['return_grid', 'log_return_grid'] | ['ret_1d', 'ret_5d', 'ret_20d', 'log_ret_1d'] | Trailing historical return observations. Zero forward or lookahead returns. | factor_ready | False |
| fam_factor_family_quote_microstructure_d03ff5dc | factor_family_quote_microstructure | Quote Microstructure Factor Placeholder | Bid-ask spread widths, mid-quote changes, and order staleness contextual indicators. | ['quote_spread_grid', 'bid_ask_ratio_grid'] | ['spread_bps', 'mid_change_1m', 'staleness_sec'] | Execution liquidity hygiene context. Placeholder only. | factor_placeholder_only | True |
| fam_factor_family_macro_context_b52adbb3 | factor_family_macro_context | Macro Context Factor Family | Point-in-time macroeconomic levels, surprise metrics, and revision indicators. | ['macro_fusion', 'macro_revision_flags'] | ['inflation_rate', 'policy_rate', 'gdp_growth', 'macro_surprise'] | Macroeconomic backdrop classification. No directional economic bets. | factor_ready | False |
| fam_factor_family_calendar_event_f74a0753 | factor_family_calendar_event | Calendar Event Factor Family | Scheduled economic releases, window proximity indicators, and release delay flags. | ['calendar_event_windows', 'release_delay_features'] | ['event_pre_window', 'event_post_window', 'event_importance_weight'] | Event risk awareness and blackout intervals. Not an event-trading strategy. | factor_ready | False |
| fam_factor_family_news_attention_1e3109f1 | factor_family_news_attention | News Attention Factor Family | Headline entity counts, topic frequency, and metadata attention intensity. | ['news_topic_fusion', 'news_asset_tag_fusion'] | ['topic_attention_count', 'asset_tag_count', 'macro_tag_count'] | Metadata-only count aggregation. Zero article text, NLP sentiment, or scraping. | factor_ready | False |
| fam_factor_family_cross_asset_context_0bfcc608 | factor_family_cross_asset_context | Cross-Asset Context Factor Family | Aligned multi-domain feature context across FX, commodities, and macro variables. | ['cross_domain_fusion', 'aligned_cross_asset_matrix'] | ['fx_commodity_corr', 'gold_rate_spread', 'oil_usd_context'] | Cross-domain aligned observation matrix. No multi-asset arbitrage trading. | factor_ready | False |
| fam_factor_family_regime_prep_1656bd38 | factor_family_regime_prep | Regime Prep Factor Placeholder | Candidate feature aggregates structured as inputs for Phase 126+ Regime Classification. | ['volatility_grid', 'macro_fusion', 'trend_grid'] | ['regime_vol_input', 'regime_trend_input'] | Preparation contracts for Phase 126+. Does not perform regime classification. | factor_placeholder_only | True |
| fam_factor_family_composite_975d187b | factor_family_composite | Composite Factor Placeholder | Multi-family feature aggregation containers for cross-disciplinary research grouping. | ['trend_grid', 'macro_fusion', 'cross_domain_matrix'] | ['comp_tech_input', 'comp_macro_input'] | Multi-feature grouping placeholder. Not an execution strategy or rule engine. | factor_placeholder_only | True |


---

# Phase 122: Factor Contract Registry Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Contract Summary
- **Total Contracts**: 12
- **Valid Contracts**: 12
- **All Contracts Valid**: True
- **Current Phase**: 122
- **Non-Signal**: True

## Active Contracts
| contract_id | factor_name | factor_family | required_feature_sets | optional_feature_sets | validation_dependencies | quality_dependencies | namespace | output_schema_ref | non_signal | manual_review_required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cntr_factor_trend_multi_window_context_b9319376 | factor_trend_multi_window_context | factor_family_trend | ['fset_moving_average_grid', 'fset_donchian_grid'] | ['fset_macd_grid'] | ['val_no_lookahead', 'val_monotonic_timestamp', 'val_no_forbidden_columns'] | ['qual_missingness_under_threshold', 'qual_finite_values_only'] | factor_trend_multi_window_context | schema_factor_trend_float64 | True | False |
| cntr_factor_momentum_rsi_roc_context_531156a5 | factor_momentum_rsi_roc_context | factor_family_momentum | ['fset_rsi_grid', 'fset_roc_grid'] | ['fset_stochastic_grid'] | ['val_no_lookahead', 'val_numeric_sanity'] | ['qual_missingness_under_threshold', 'qual_drift_baseline_ready'] | factor_momentum_rsi_roc_context | schema_factor_momentum_float64 | True | False |
| cntr_factor_volatility_atr_realized_context_22b85429 | factor_volatility_atr_realized_context | factor_family_volatility | ['fset_atr_grid', 'fset_realized_vol_grid'] | ['fset_bollinger_bandwidth_grid'] | ['val_no_lookahead', 'val_positive_values_only'] | ['qual_missingness_under_threshold', 'qual_no_infinite_values'] | factor_volatility_atr_realized_context | schema_factor_volatility_float64 | True | False |
| cntr_factor_mean_reversion_zscore_context_a501027b | factor_mean_reversion_zscore_context | factor_family_mean_reversion | ['fset_zscore_grid', 'fset_distance_to_ma_grid'] | ['fset_percentile_rank_grid'] | ['val_no_lookahead', 'val_warmup_nan_preserved'] | ['qual_finite_values_only', 'qual_missingness_under_threshold'] | factor_mean_reversion_zscore_context | schema_factor_mean_reversion_float64 | True | False |
| cntr_factor_return_multi_horizon_context_a5d1d292 | factor_return_multi_horizon_context | factor_family_return | ['fset_return_grid'] | ['fset_log_return_grid'] | ['val_no_lookahead', 'val_no_forward_returns'] | ['qual_no_infinite_values'] | factor_return_multi_horizon_context | schema_factor_return_float64 | True | False |
| cntr_factor_quote_spread_context_placeholder_4c333715 | factor_quote_spread_context_placeholder | factor_family_quote_microstructure | ['fset_quote_spread_grid'] | ['fset_bid_ask_ratio_grid'] | ['val_monotonic_timestamp'] | ['qual_liquidity_data_present'] | factor_quote_spread_context_placeholder | schema_factor_quote_float64 | True | True |
| cntr_factor_macro_inflation_rate_context_73e16b8c | factor_macro_inflation_rate_context | factor_family_macro_context | ['fset_macro_fusion'] | ['fset_macro_revision_flags'] | ['val_macro_release_lag', 'val_backward_asof_join'] | ['qual_point_in_time_guaranteed'] | factor_macro_inflation_rate_context | schema_factor_macro_float64 | True | False |
| cntr_factor_event_release_context_1dbb154c | factor_event_release_context | factor_family_calendar_event | ['fset_calendar_event_windows'] | ['fset_release_delay_features'] | ['val_event_window_temporal_integrity'] | ['qual_event_timestamps_verified'] | factor_event_release_context | schema_factor_event_float64 | True | False |
| cntr_factor_news_attention_context_ca4587ae | factor_news_attention_context | factor_family_news_attention | ['fset_news_topic_fusion', 'fset_news_tag_fusion'] | ['fset_news_event_linkage'] | ['val_news_metadata_only', 'val_no_full_text_or_scraping'] | ['qual_metadata_frequency_sanity'] | factor_news_attention_context | schema_factor_news_float64 | True | False |
| cntr_factor_cross_asset_context_b941eae3 | factor_cross_asset_context | factor_family_cross_asset_context | ['fset_cross_domain_matrix'] | ['fset_aligned_universe_features'] | ['val_backward_asof_join', 'val_no_lookahead'] | ['qual_cross_asset_alignment_verified'] | factor_cross_asset_context | schema_factor_cross_asset_float64 | True | False |
| cntr_factor_regime_prep_placeholder_2fcceaef | factor_regime_prep_placeholder | factor_family_regime_prep | ['fset_volatility_grid', 'fset_trend_grid'] | ['fset_macro_fusion'] | ['val_no_lookahead', 'val_numeric_sanity'] | ['qual_phase_126_readiness'] | factor_regime_prep_placeholder | schema_factor_regime_prep_float64 | True | True |
| cntr_factor_composite_context_placeholder_9a6bf660 | factor_composite_context_placeholder | factor_family_composite | ['fset_moving_average_grid', 'fset_macro_fusion'] | ['fset_cross_domain_matrix'] | ['val_no_lookahead', 'val_no_forbidden_columns'] | ['qual_composite_stability'] | factor_composite_context_placeholder | schema_factor_composite_float64 | True | True |


---

# Phase 122: Factor Validation Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Validation Summary
- **Overall Status**: `factor_ready`
- **All Non-Signal Verified**: True
- **Zero Forbidden Claims**: True
- **Zero Lookahead Guarantees**: True
- **Source Preserved**: True

## Validation Results
| check_name | is_valid | error_count | errors | status | non_signal |
| --- | --- | --- | --- | --- | --- |
| profile_registry_validation | True | 0 | None | PASS | True |
| family_registry_validation | True | 0 | None | PASS | True |
| contract_registry_validation | True | 0 | None | PASS | True |
| namespace_registry_validation | True | 0 | None | PASS | True |
| output_schema_validation | True | 0 | None | PASS | True |
| manifest_validation | True | 0 | None | PASS | True |


---

# Phase 122: Factor Metadata Health Check Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Health Check Summary
- **Overall Health**: `HEALTHY`
- **Total Checks**: 10
- **Passed Checks**: 10
- **Failed Checks**: 0
- **Prerequisites Ready**: True

## Health Check Items
| check_id | component | description | path | status | passed | non_signal |
| --- | --- | --- | --- | --- | --- | --- |
| health_phase_116_engine | advanced_feature_engine | Phase 116 Feature Engine Foundation availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_feature_engine | PASS | True | True |
| health_phase_117_indicators | advanced_technical_indicators | Phase 117 Technical Indicators Expansion availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_technical_indicators | PASS | True | True |
| health_phase_118_grid | advanced_feature_grid | Phase 118 Multi-Window Feature Grid availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_feature_grid | PASS | True | True |
| health_phase_119_alignment | advanced_cross_asset_alignment | Phase 119 Cross-Asset Feature Alignment availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_cross_asset_alignment | PASS | True | True |
| health_phase_120_fusion | advanced_feature_fusion | Phase 120 Macro/Calendar/News Feature Fusion availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_feature_fusion | PASS | True | True |
| health_phase_121_validation | advanced_feature_validation | Phase 121 Feature Validation and Lookahead Guard availability. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_feature_validation | PASS | True | True |
| health_phase_122_metadata | advanced_factor_metadata | Phase 122 Factor Metadata and Factor Families package. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\advanced_factor_metadata | PASS | True | True |
| health_phase_122_scripts | scripts.run_factor_metadata_status | Phase 122 Operational CLI scripts. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\scripts\run_factor_metadata_status.py | PASS | True | True |
| health_phase_122_tests | tests.test_factor_metadata_config | Phase 122 Unit and Contract Tests. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\tests\test_factor_metadata_config.py | PASS | True | True |
| health_phase_122_docs | docs.ARCHITECTURE | Documentation architecture ledger. | C:\Users\immor\OneDrive\Belgeler\Projelerim\gptemtia\docs\ARCHITECTURE.md | PASS | True | True |


---

# Phase 122: Factor Safety Boundary Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Safety Boundary Summary
- **Safety Status**: `SECURE`
- **NO-GO Conditions Enforced**: 20
- **SAFE-GO Principles Active**: 11
- **Destructive Action Allowed**: False
- **Non-Signal Mandate**: True

## Safety Rules Matrix
| rule_id | rule_type | name | description | enforcement | non_signal |
| --- | --- | --- | --- | --- | --- |
| NG-122-01 | NO_GO | No Live Trading | Strictly no execution of live market orders or connections. | STRICT_BARRIER | True |
| NG-122-02 | NO_GO | No Broker Integration | Zero integration with broker APIs or accounts. | STRICT_BARRIER | True |
| NG-122-03 | NO_GO | No Real Orders | Never route real capital or simulated live positions. | STRICT_BARRIER | True |
| NG-122-04 | NO_GO | No Investment Advice | Factors never constitute financial or trading recommendations. | STRICT_BARRIER | True |
| NG-122-05 | NO_GO | No Factor as Signal | Factor values must not be presented or used as buy/sell signals. | STRICT_BARRIER | True |
| NG-122-06 | NO_GO | No Directional Claims | No claims that high/low factor scores ensure directional movement. | STRICT_BARRIER | True |
| NG-122-07 | NO_GO | No Strategy Rule Generation | No automated compilation of strategy execution rules. | STRICT_BARRIER | True |
| NG-122-08 | NO_GO | No Backtest Execution | Backtesting of factor strategies is prohibited in Phase 122. | STRICT_BARRIER | True |
| NG-122-09 | NO_GO | No Optimizer Execution | No portfolio optimization or parameter curve fitting. | STRICT_BARRIER | True |
| NG-122-10 | NO_GO | No Model Training | Zero ML model training or weight fitting in this phase. | STRICT_BARRIER | True |
| NG-122-11 | NO_GO | No Target or Label Generation | Zero forward returns, labels, or prediction target synthesis. | STRICT_BARRIER | True |
| NG-122-12 | NO_GO | No Sentiment Model Output | No NLP sentiment classification outputs or vector embeddings. | STRICT_BARRIER | True |
| NG-122-13 | NO_GO | No Full Article Usage | Zero ingestion or storage of copyrighted raw article texts. | STRICT_BARRIER | True |
| NG-122-14 | NO_GO | No Web Scraping | Zero web scraping, HTML parsing, or browser automation. | STRICT_BARRIER | True |
| NG-122-15 | NO_GO | No Paywall/Rate Limit Bypass | Strict prohibition of rate abuse or reverse engineering. | STRICT_BARRIER | True |
| NG-122-16 | NO_GO | No Credential Output | Never print, write, or export API keys or credentials. | STRICT_BARRIER | True |
| NG-122-17 | NO_GO | No Source Overwrite | Never overwrite or destructively mutate original data sources. | STRICT_BARRIER | True |
| NG-122-18 | NO_GO | No Destructive Cleaning | Never silently delete or drop anomalous records. | STRICT_BARRIER | True |
| NG-122-19 | NO_GO | No Production Approval Claim | Zero claims of production readiness or official compliance signoff. | STRICT_BARRIER | True |
| NG-122-20 | NO_GO | No Deployment | Zero cloud publishing, docker pushes, or git release tags. | STRICT_BARRIER | True |
| SG-122-01 | SAFE_GO | Local Research Metadata | Compile structured offline factor metadata and descriptions. | MANDATORY_PRACTICE | True |
| SG-122-02 | SAFE_GO | Factor Family Taxonomy | Classify factors into trend, momentum, volatility, macro, event, news, cross-asset. | MANDATORY_PRACTICE | True |
| SG-122-03 | SAFE_GO | Factor Contracts | Establish formal contract schemas linking required features and validations. | MANDATORY_PRACTICE | True |
| SG-122-04 | SAFE_GO | Namespace Registry | Enforce lowercase snake_case standard with mandatory factor_ prefix. | MANDATORY_PRACTICE | True |
| SG-122-05 | SAFE_GO | Dependency Tracking | Map upstream indicator, grid, alignment, and fusion dependencies. | MANDATORY_PRACTICE | True |
| SG-122-06 | SAFE_GO | Validation Dependency Mapping | Require no-lookahead, forbidden column, and causality check prerequisites. | MANDATORY_PRACTICE | True |
| SG-122-07 | SAFE_GO | Quality Dependency Mapping | Require missingness, infinite value, and drift readiness prerequisites. | MANDATORY_PRACTICE | True |
| SG-122-08 | SAFE_GO | Metadata-Only News Factors | Use solely frequency counts, tags, and category metadata for news. | MANDATORY_PRACTICE | True |
| SG-122-09 | SAFE_GO | Regime Prep Placeholders | Structure candidate feature groups as research inputs for Phase 126+. | MANDATORY_PRACTICE | True |
| SG-122-10 | SAFE_GO | Non-Destructive Manual Review | Queue anomalies and placeholders for human review without data loss. | MANDATORY_PRACTICE | True |
| SG-122-11 | SAFE_GO | Phase 123 Drift Handoff | Provide complete factor inventory ready for drift and quality diagnostics. | MANDATORY_PRACTICE | True |


---

# Phase 122 to Phase 123: Feature Quality & Drift Handoff Report

> **Yasal Uyarı**: Bu çıktı Phase 122 Factor Metadata and Factor Families raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, factor değerini trade sinyali olarak kullanma, strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, sentiment model output, haber tam metni kullanımı, production-ready/official approval iddiası, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.

## Handoff Summary
- **Source Phase**: 122 (Factor Metadata and Factor Families)
- **Target Phase**: 123 (Feature Quality and Drift Diagnostics)
- **Target Final Phase**: 160
- **Total Handoff Items**: 11
- **Ready Items**: 11
- **Handoff Status**: `READY`
- **Non-Signal**: True

## Handoff Specifications
| handoff_id | topic | description | status | downstream_consumer |
| --- | --- | --- | --- | --- |
| HO-123-01 | factor_level_missingness_diagnostics_prerequisites | Baseline feature missingness thresholds (<= 35%) mapped to each factor family. | READY | Phase 123 Missingness Diagnostics |
| HO-123-02 | factor_level_infinite_value_diagnostics_prerequisites | Zero +inf/-inf invariant rules mapped to all numerical factor contracts. | READY | Phase 123 Infinite Value Diagnostics |
| HO-123-03 | factor_level_duplicate_namespace_diagnostics_prerequisites | Namespace uniqueness standards established with factor_ prefix and snake_case. | READY | Phase 123 Namespace Diagnostics |
| HO-123-04 | factor_level_stability_diagnostics_prerequisites | Rolling window lookback lengths defined for statistical stability assessments. | READY | Phase 123 Factor Stability Engine |
| HO-123-05 | factor_level_drift_diagnostics_prerequisites | Distributional reference windows configured for KS-test and Wasserstein drift tests. | READY | Phase 123 Distributional Drift Monitor |
| HO-123-06 | feature_availability_by_factor_family | Dependency coverage matrix verifying all required inputs from Phases 116-121. | READY | Phase 123 Availability Checker |
| HO-123-07 | validation_blockers_by_factor_family | Validation dependency gates preventing unverified features from entering drift evaluation. | READY | Phase 123 Validation Gatekeeper |
| HO-123-08 | quality_dependencies_by_factor_family | Quality criteria thresholds formalized in factor quality dependency registry. | READY | Phase 123 Quality Scorer |
| HO-123-09 | macro_calendar_news_metadata_only_quality_checks | Strict verification that news factors remain frequency-based and text-free. | READY | Phase 123 Metadata Hygiene Auditor |
| HO-123-10 | cross_asset_context_quality_dependencies | Backward-asof timestamp alignment verification across multi-asset calendars. | READY | Phase 123 Cross-Asset Alignment Quality |
| HO-123-11 | manual_review_blockers_before_quality_drift_diagnostics | Review queue integration ensuring placeholder factors require sign-off before drift monitoring. | READY | Phase 123 Governance Blocker Interface |
