# Phase 119: Aligned Feature Matrix Manifest Report

> Bu çıktı Phase 119 Cross-Asset Feature Alignment ve Multi-Domain Feature Matrix Contracts raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, cross-asset hizalanmış feature'ları trade sinyali veya çoklu varlık arbitraj/al-sat kuralı olarak kullanma, strateji üretimi, backtest, optimizer, target/label/prediction üretimi, production deployment, model deployment, scraping, gerçek provider API çağrısı veya official approval sağlamaz.

## Manifest Özeti
- **Toplam Manifest**: 2
- **Non-Signal İlkesi**: `Onaylandı`
- **Durum**: `READY`

## Manifest Detayları

| manifest_id                                  | matrix_name                             | base_domain | aligned_domains                            | row_count | feature_count | join_policy               | source_preserved | non_signal | contains_target_or_prediction | manual_review_required |
| -------------------------------------------- | --------------------------------------- | ----------- | ------------------------------------------ | --------- | ------------- | ------------------------- | ---------------- | ---------- | ----------------------------- | ---------------------- |
| afmm_fx_cross_asset_aligned_matrix_v1        | fx_cross_asset_aligned_matrix_v1        | fx          | ['commodity', 'macro', 'calendar', 'news'] | 1000      | 28            | join_policy_asof_backward | True             | True       | False                         | False                  |
| afmm_commodity_cross_asset_aligned_matrix_v1 | commodity_cross_asset_aligned_matrix_v1 | commodity   | ['fx', 'macro', 'calendar', 'news']        | 1000      | 32            | join_policy_asof_backward | True             | True       | False                         | False                  |
