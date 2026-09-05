# Phase 116-125 Feature Engine Block Dependencies Report

> [!WARNING]
> **YASAL UYARI VE NON-SIGNAL GÜVENCESİ**:
> Bu çıktı Phase 125 Feature/Factor Engine Acceptance Report raporudur. > Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, acceptance score’u trade sinyali olarak kullanma, > strateji üretimi, backtest, optimizer, model training, prediction/target/label üretimi, > production-ready/official approval/broker-ready iddiası, otomatik feature silme/düzeltme, > haber tam metni kullanımı, production deployment, model deployment, scraping veya gerçek provider API çağrısı değildir.


## Summary
- **Total Dependency Edges**: 10
- **All Contracts Satisfied**: True
- **Pipeline Flow**: Phase 116 -> ... -> Phase 126

## Dependency Graph Table
| source_phase | source_module | target_phase | target_module | dependency_type | contract_satisfied | notes | non_signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 116 | advanced_feature_engine | 117 | advanced_technical_indicators | computational_foundation | True | Temel hesaplama arayüzleri ve şemaları indikatör genişlemesine aktarıldı. | True |
| 117 | advanced_technical_indicators | 118 | advanced_feature_grid | indicator_catalog | True | Teknik indikatör katalogları çoklu pencere grid hesaplamalarına bağlandı. | True |
| 118 | advanced_feature_grid | 119 | advanced_cross_asset_alignment | multi_window_features | True | Tek varlık grid serileri çapraz varlık matris hizalamasına aktarıldı. | True |
| 119 | advanced_cross_asset_alignment | 120 | advanced_feature_fusion | aligned_asset_matrix | True | Zaman hizalı çoklu varlık matrisi makro/olay/haber füzyonuna iletildi. | True |
| 120 | advanced_feature_fusion | 121 | advanced_feature_validation | fused_feature_matrix | True | Füzyon serileri no-lookahead ve sızıntı doğrulama motoruna verildi. | True |
| 121 | advanced_feature_validation | 122 | advanced_factor_metadata | validated_features | True | Doğrulanmış ve sızıntısız feature'lar faktör ailelerine girdi sağladı. | True |
| 122 | advanced_factor_metadata | 123 | advanced_feature_quality_drift | factor_families | True | 12 faktör ailesi ve metaverileri kalite/drift tanılarına bağlandı. | True |
| 123 | advanced_feature_quality_drift | 124 | advanced_feature_store_integration | quality_drift_diagnostics | True | Kalite ve drift tanı skorları merkezi feature store metaverisine aktarıldı. | True |
| 124 | advanced_feature_store_integration | 125 | advanced_feature_factor_acceptance | central_feature_store | True | Feature store katalog ve sözleşmeleri blok kabul raporuna bağlandı. | True |
| 125 | advanced_feature_factor_acceptance | 126 | phase_126_handoff | block_acceptance_manifest | True | Kabul edilmiş feature bloğu Phase 126 rejim sınıflandırmasına devredildi. | True |