## Local Continuity Intelligence
- Operator memory book nasıl okunur? -> data/lake/local_continuity_intelligence ve reports altından.
- Lessons-learned codex nasıl yorumlanır? -> Bu sadece local bir prova olup official report değildir.
- Decision rationale capsule neden official decision record değildir? -> Sistem hiçbir recordı official olarak sunamaz, yatırım tavsiyesi veremez, cloud memory kullanamaz.
- Future-reader guide nasıl kullanılır? -> Onboarding map ve reading route ile projeye hizli giriş.
- Continuity binder nasıl okunur? -> Tüm bilgilerin indekslenmiş özetidir.
- Command/output interpretation guides neden komut çalıştırmaz? -> Bu fazda no-go durumundadır ve safe execution kuralları gereği komutlar otomatize edilmez.
- Gerçek memory system, cloud sync, official decision record, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi YOKTUR.

## Local Documentation Export
- **Static site export rehearsal nasıl okunur?** Bu sadece dosya üretimidir, gerçek web server çalıştırmaz.
- **Offline HTML pack neden dashboard/deploy değildir?** Çünkü statiktir ve JS/telemetry barındırmaz.
- **Printable binder nasıl yorumlanır?** Yazdırılabilir bölümlerin index'idir, PDF binary oluşturmaz.
- **PDF-ready layer neden PDF binary üretmez?** Çünkü harici bağımlılıklardan kaçınır, sadece markdown/html oluşturur.
- **Presentation-freeze neden PowerPoint/slides değildir?** PPTX oluşturmak yerine text formatında arşiv narrative sunar.
- **Source/output/route maps nasıl okunur?** Yalnızca lokal rehberdir.
- **Gerçek web server, PDF export, slides generation, cloud hosting, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi OLMADIĞINI UNUTMAYIN.**
\n
## Local Reproducibility Governance
- Reproducibility dossier nasıl okunur? -> Dossier, sistemin nasıl yeniden üretilebileceğini gösterir ancak attestation değildir.
- Environment replay manifest neden install/provisioning talimatı değildir? -> Çünkü sadece offline replay sağlar, kurulum yapmaz.
- Deterministic runbook neden determinism guarantee değildir? -> Deterministik çalışmayı sadece hedefler, garanti etmez.
- Build-free reproduction layer nasıl yorumlanır? -> Gerçek bir build işlemi yapılmadan sistemin okuma katmanıdır.
- Drift/variance/integrity çıktıları nasıl okunur? -> Sadece veri bütünlüğü ve sapmasını gösterir.
- Terminal reproducibility governance binder nasıl yorumlanır? -> Gerçek build, Docker image, CI/CD, dependency install, package publish, deployment, canlı emir, broker execution ve yatırım tavsiyesi olmadığı açık yazılsın.
\n

# Phase 98 Updates
Local completion governance framework appended.


> **UYARI**: Bu proje ve modülleri offline/local terminal closeout ve pre-final handover governance rehearsal çıktısıdır; gerçek project closeout, official governance seal, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir.

## Local Final Closing
- Final master terminal lock rehearsal nasıl okunur?
- Ultimate offline project constitution neden official constitution değildir?
- Final non-production seal rehearsal neden official seal değildir?
- Local-only terminal archive index neden gerçek archive/ZIP değildir?
- Closing governance super-binder nasıl yorumlanır?
- Final closeout readiness score neden approval değildir?
- Phase 100 final katmanının production, live trading, deployment veya yatırım tavsiyesi olmadığı açık yazılsın.
- Gerçek lock, seal, handover, release, build, deployment, canlı emir, broker execution ve yatırım tavsiyesi olmadığı açık yazılsın.



## Phase 105 & 106 Operations
- Phase 105 ile local bot altyapısı tamamlandı.
- Operator olarak Phase 106 veri soyutlama (Data Provider Abstraction) hazırlığı raporlarını `scripts.run_phase_106_data_foundation_handoff` ile kontrol edebilirsiniz.
- Scraping eylemi yasaktır. Harici veri kaynakları için local cache veya user-provided dosyalar kullanın.

## Phase 111 News Metadata Operations
- Haber metadata sağlayıcı katmanı `advanced_news_metadata/` modülü altında çalıştırılır.
- Operatör kesinlikle haber sitelerine yönelik web scraping veya sayfa indirme mekanizması kurmamalıdır.
- İlgili haber kayıtları için yalnızca `news_metadata_schema` ve `news_item_reference_schema` alanları kullanılmalıdır.
- Dry-run testleri için `scripts/run_news_dry_run_fixture.py` çalıştırılır.
- Sağlık denetimi için `scripts/run_news_provider_health_check.py` çıktısı takip edilmelidir.
- Tüm süreç Phase 112 Data Quality Engine için hazır durumdadır.

## Phase 112 Data Quality Engine Operations
- **Kalite Kurallarını Çalıştırma**: `python -m scripts.run_data_quality_rule_registry` ile tüm genel ve alana özgü kalite kuralları test edilir.
- **Manual Review Kuyruğu İnceleme**: `python -m scripts.run_data_quality_provider_checks` sonrasında `reports/output/advanced_data_quality/csv/manual_review_queue.csv` dosyasındaki kayıtlar incelenir. Operatör hiçbir zaman otomatik dosya ezme, silme veya veri tahrifatı yapmamalıdır (`destructive_action_allowed: False`). Düzeltmeler Phase 113 normalizasyon katmanına yönlendirilmelidir.
- **Kalite Skorlarını Yorumlama**: `python -m scripts.run_data_quality_scoring` çıktısı `provider_quality_scores.csv` ve `dataset_quality_scores.csv` tablolarında 0.0 - 1.0 aralığında ceza bazlı teşhis skorları üretir. Bu skorlar kesinlikle resmi sağlayıcı onayı, güvenilirlik sertifikası veya AL/SAT sinyali değildir.
- **Telif ve Scraping Güvenliği**: Haber ve takvim kontrollerinde tam metin indirme veya harici LLM / scraping girişimleri tespit edildiğinde `quality_critical` seviyesinde finding üretilir. Operatör bu kayıtları reddetmelidir.
- **Sistem Sağlığı ve Doğrulama**: `python -m scripts.run_data_quality_health_check` ve `python -m scripts.run_data_quality_validation_report` ile 38 sağlık bileşeni ve güvenlik kuralları doğrulanır.

## Phase 113 Data Normalization Layer Operations
- **Normalizasyon Kurallarını Çalıştırma**: `python -m scripts.run_normalization_rule_registry` ile canonical schema ve 21 kural kataloğu doğrulanır.
- **Sembol ve Gösterge Dönüştürme**: `python -m scripts.run_symbol_normalization_enforcement` ile FX/emtia/makro/takvim girdileri kanonik formatlara (ör. `EUR/USD`, `XAU/USD`, `US_10Y_YIELD`) eşlenir.
- **Zaman, Frekans ve Birim Standartlaştırması**: `python -m scripts.run_time_frequency_unit_normalization` ile ISO 8601 UTC timestamp, periyot sözlüğü (`1d`, `1w`, `1mo`) ve birim kelime hazinesi (`percent`, `usd_per_barrel`) doğrulanır.
- **Non-Destructive Görünümler ve Manifest**: `python -m scripts.run_normalized_output_manifest` ile ayrı normalize edilmiş kopyalar oluşturulur. Operatör hiçbir zaman kaynak veriyi (`raw_df`) silmemeli veya üzerine yazmamalıdır (`source_preserved: True`).
- **Manuel İnceleme Kuyruğu**: Eşleşmeyen sembol veya bozuk tarih tespit edildiğinde kayıt `manual_review_normalization_queue` içine aktarılır. Yıkıcı eylem önerilmez; inceleme Phase 114 soy kütüğüne ve Phase 115 benchmark raporuna havale edilir.
- **Normalizasyon Skorları**: `python -m scripts.run_data_normalization_scoring` ile hesaplanan skorlar iç denetim metriğidir; kesinlikle al/sat sinyali veya resmi onay gibi kullanılamaz.
- **Sağlık ve Doğrulama Kontrolleri**: `python -m scripts.run_data_normalization_health_check` ve `python -m scripts.run_data_normalization_validation_report` çalıştırılarak tüm bileşenlerin ve güvenlik sınırlarının hazır olduğu teyit edilir.

## Phase 114 Data Lineage and Provenance Operations
- **Soy Kütüğü ve Alan Sınıflandırması**: `python -m scripts.run_data_lineage_profile_registry` ile 3 operasyonel profil ve 32 domain sınıfı denetlenir.
- **Kaynak ve Sağlayıcı Kayıt Defterleri**: `python -m scripts.run_provenance_source_registry` ve `python -m scripts.run_provider_dataset_provenance` ile 10 kaynak ve 10 sağlayıcı kaydı izlenir. Tüm referanslarda kimlik bilgisi (`contains_credentials: False`) ve tam metin (`contains_full_text: False`) sızıntısı olmadığı teyit edilir.
- **Dönüşüm ve Normalizasyon İzlenebilirliği**: `python -m scripts.run_transformation_lineage` ile Phase 113 dönüşüm kararları, şema sürümleri ve normalized output manifest bağlantıları kayıt altına alınır. Operatör hiçbir zaman kaynak veriyi silmemeli veya tahrif etmemelidir (`destructive_action_allowed: False`).
- **Alana Özgü İzlenebilirlik**: `python -m scripts.run_domain_lineage_registries` ile FX, Emtia, Makro, Takvim ve Haber soy kütüğü sözleşmeleri teyit edilir.
- **Telif ve Sınır Güvencesi**: `python -m scripts.run_news_provenance_boundary` ile haberlerin strictly metadata-only olduğu, telif sınırlarının korunduğu ve sıfır tam metin kopyalama politikası doğrulandığı teyit edilir.
- **İzlenebilirlik ve Teşhis Skorları**: `python -m scripts.run_lineage_scoring` çalıştırılarak veri seti ve sağlayıcı izlenebilirlik skorları hesaplanır. Operatör bu skorları asla al/sat sinyali, modelleme veya yatırım tavsiyesi olarak değerlendiremez; skorlar yalnızca iç veri kalitesi teşhisidir.
- **Sağlık, Doğrulama ve Güvenlik Denetimi**: `python -m scripts.run_data_lineage_health_check` ve `python -m scripts.run_data_lineage_validation_report` ile 45 sağlık kontrolü ve 32 No-Go / 15 Safe-Go kuralı teyit edilir.
- **Genel Durum**: `python -m scripts.run_data_lineage_status` ile 9 alt sistemin hazır olduğu doğrulanır.

## Phase 115 Data Provider Benchmark Report Operations
- **Profil ve Metrik Defterleri**: `python -m scripts.run_provider_benchmark_profile_registry` ve `python -m scripts.run_provider_benchmark_metrics` ile benchmark profilleri, 10 temel metrik ve alan ağırlıkları denetlenir.
- **Kapsam, Yetenek ve Uyumluluk**: `python -m scripts.run_provider_coverage_capability_benchmark` ile sağlayıcıların evren kapsamı, teknik yetenekleri, açık araştırma lisans sınırları ve katı sıfır-scraping / metadata-only uyumlulukları doğrulanır.
- **Kalite, Normalizasyon ve İzlenebilirlik Konsolidasyonu**: `python -m scripts.run_provider_quality_normalization_lineage_benchmark` ile Phase 112 (veri kalitesi), Phase 113 (normalizasyon) ve Phase 114 (lineage) çıktıları birleştirilir.
- **Alana Özgü ve Çapraz Varlık Karşılaştırmaları**: `python -m scripts.run_domain_provider_benchmarks` ve `python -m scripts.run_cross_domain_provider_benchmark` ile FX, Emtia, Makro, Takvim ve Haber metadata sağlayıcıları değerlendirilir.
- **Skorlama, Araştırma Sıralaması ve Manuel İnceleme**: `python -m scripts.run_provider_benchmark_scoring` ile [0.0, 1.0] aralığında ceza ağırlıklı araştırma skorları ve araştırma sıralama matrisi üretilir. Operatör bu çıktıları kesinlikle al/sat sinyali, resmi sağlayıcı onayı, canlı ticarete uygunluk veya broker uyumluluğu olarak yorumlayamaz (`official_approval: False`, `production_ready: False`, `broker_ready: False`, `destructive_action_allowed: False`).
- **Sağlık, Doğrulama ve Güvenlik Sınırları**: `python -m scripts.run_provider_benchmark_health_check` ve `python -m scripts.run_provider_benchmark_validation_report` ile 45 sağlık kontrolü, yasaklı iddia taraması ve 32 No-Go / 15 Safe-Go kuralı teyit edilir.
- **Genel Durum**: `python -m scripts.run_provider_benchmark_status` ile Phase 115 sistem durumu doğrulanır.

## Phase 116 Advanced Indicator/Feature/Factor Engine Foundation Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_feature_engine_profile_registry` ile 3 operasyonel profil ve 24 feature alanı denetlenir.
- **Kanonik Girdi Kontratları**: `python -m scripts.run_feature_input_contracts` ile FX, emtia, makro, takvim ve haber metadata girdi şemaları doğrulanır.
- **Gösterge Katalogları**: `python -m scripts.run_indicator_catalog_registry` ile fiyat (9), trend (8), momentum (6), volatilite (7) ve ortalamaya dönüş (6) katalogları incelenir. Operatör hiçbir gösterge değerini AL/SAT sinyali olarak kullanamaz (`non_signal: True`).
- **Feature ve Faktör Şemaları**: `python -m scripts.run_feature_schema_registry` ile 17 canonical feature şeması ve 8 kompozit faktör şeması denetlenir.
- **Temel Hesaplama Provası**: `python -m scripts.run_basic_feature_computations` ile 12 saf pandas/numpy matematik dönüşümü test edilir. Girdi dataframe'i mutasyona uğramaz (`df.copy()`); sinyal kolonları üretilmez.
- **Metadata ve Pencere Kontratları**: `python -m scripts.run_feature_metadata_registry` ile standart pencereler ([5, 10, 14, 20, 50, 100, 200]), ısınma satırları ve lookahead koruması denetlenir.
- **Sistem Sağlığı**: `python -m scripts.run_feature_engine_health_check` ile 13 sağlık kontrolünün PASS olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_feature_engine_validation_report` ile yasaklı sinyal kolonları taranır, 38 No-Go ve 15 Safe-Go kuralı doğrulanır.
- **Genel Durum**: `python -m scripts.run_feature_engine_status` ile 23 alt sistemin READY olduğu teyit edilir.

## Phase 117 Technical Indicator Expansion Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_technical_indicator_profile_registry` ile 3 profil (`balanced_local_technical_indicators`, `strict_non_signal_indicator_safety`, `research_offline_indicator_focus`) ve 24 indikatör alanı doğrulanır.
- **Katalog ve Parametre Kontratları**: `python -m scripts.run_technical_indicator_catalogs` ile 12 indikatör ailesi, parametre sınırları, çıktı şemaları ve ısınma NaN politikası denetlenir.
- **Fiyat ve Trend Göstergeleri**: `python -m scripts.run_price_trend_indicator_expansion` ile High/Low, Close/Open, Gap, CLV, Return oranları, SMA/EMA/WMA/DEMA/TEMA, MACD (`macd_smooth`), PPO, Donchian, Aroon, ADX ve Ichimoku göstergeleri incelenir. Operatör bu göstergeleri al/sat sinyali olarak kullanamaz.
- **Momentum ve Osilatör Göstergeleri**: `python -m scripts.run_momentum_oscillator_expansion` ile Momentum, ROC, RSI, CMO, TSI, Stokastik (%K, %D), Williams %R, CCI, Ultimate Oscillator ve MFI çalıştırılır.
- **Volatilite, Aralık ve Kanal Göstergeleri**: `python -m scripts.run_volatility_range_channel_expansion` ile True Range, ATR, Realized Vol, Parkinson Vol, Bollinger Bantları, Bandwidth, %B, Keltner ve Donchian Position denetlenir.
- **Mum Anatomisi, Kote ve Ortalamaya Dönüş**: `python -m scripts.run_candle_quote_mean_reversion_features` ile gövde/fitil oranları, bid-ask spread, rolling z-score ve ortalama mesafeleri hesaplanır.
- **Hesaplama Prova Motoru**: `python -m scripts.run_indicator_computation_rehearsal` ile 62 hesaplama provası sentetik veri üzerinde test edilir; girdi mutasyonsuzluğu (`df.copy()`) ve yasaklı kolon bulunmadığı (`no_forbidden_columns`) teyit edilir.
- **Sağlık Kontrolü**: `python -m scripts.run_technical_indicator_health_check` ile 5 kritik alt sistem kontrolünün PASS olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_technical_indicator_validation_report` ile 18 No-Go ve 9 Safe-Go kuralı teyit edilir; canlı ticaret veya sinyal iddiaları engellenir.
- **Genel Durum**: `python -m scripts.run_technical_indicator_status` ile 15 bileşenin READY olduğu teyit edilir.
## Phase 118 Multi-Window Feature Grid Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_feature_grid_profile_registry` ile 3 profil (`balanced_local_multi_window_feature_grid`, `strict_no_signal_feature_grid_safety`, `dry_run_feature_grid_computation_focus`) ve 27 feature grid domain doğrulanır.
- **Pencere Sözleşmeleri ve Lookahead Guard**: `python -m scripts.run_window_grid_contracts` ile geriye dönük pencere matrisleri, warmup NaN politikası, negatif shift (`shift(-1)`) koruması ve mükerrer feature denetimi incelenir.
- **İndikatör Parametre Gridleri ve İsimlendirme**: `python -m scripts.run_indicator_parameter_grids` ile SMA, EMA, RSI, ATR, Bollinger, Donchian, z-score ve return için parametre gridleri ile standart snake_case isimlendirme (`sma_w20`, `rsi_w14`, `bb_width_w20_std2`) denetlenir.
- **Hareketli Ortalama, Momentum ve Getiri Gridleri**: `python -m scripts.run_moving_average_momentum_grids` ile SMA/EMA/WMA/DEMA/TEMA, RSI/ROC/Momentum/CMO ve getiri varyantları listelenir. Operatör bu çıktıları trade sinyali olarak kullanamaz.
- **Volatilite, Aralık ve Ortalamaya Dönüş Gridleri**: `python -m scripts.run_volatility_range_mean_reversion_grids` ile ATR, standart sapma, Bollinger Bantları, Donchian kanalları ve rolling z-score varyantları incelenir.
- **Hesaplama Prova Motoru**: `python -m scripts.run_feature_grid_computation_rehearsal` ile sentetik veri üzerinde mutasyonsuz (`df.copy()`) ve no-lookahead garantili 7 prova çalıştırılır; tüm provaların PASS olduğu doğrulanır.
- **Metadata ve Bağımlılık Defteri**: `python -m scripts.run_feature_grid_metadata_registry` ile feature grid metadata, girdi bağımlılıkları, validasyon kuralları ve Phase 119 handoff maddeleri incelenir.
- **Sağlık Kontrolü**: `python -m scripts.run_feature_grid_health_check` ile 9 kritik alt sistemin HEALTHY olduğu teyit edilir.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_feature_grid_validation_report` ile 25 validasyon kuralı taranır; 16 No-Go ve 8 Safe-Go güvenlik kuralı teyit edilir.
- **Genel Durum**: `python -m scripts.run_feature_grid_status` ile 16 bileşenin OPERATIONAL olduğu teyit edilir.

## Phase 119 Cross-Asset Feature Alignment and Multi-Domain Feature Matrix Contracts Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_cross_asset_alignment_profile_registry` ile 3 profil (`balanced_local_cross_asset_alignment`, `strict_no_signal_cross_asset_safety`, `dry_run_cross_asset_alignment_focus`) ve 28 alignment domain doğrulanır.
- **Varlık Evreni ve Sembol Eşleme**: `python -m scripts.run_asset_symbol_alignment` ile 5 varlık evreni (EUR/USD, USD/TRY, XAU/USD, WTI, NatGas) ve çoklu kaynak sembol eşlemeleri denetlenir.
- **Zaman ve Seans Hizalaması**: `python -m scripts.run_timestamp_session_alignment` ile ISO 8601 UTC standardı ve seans kovaları (`utc_day`, `utc_hour`, `fx_24_5`, emtia seansları) doğrulanır.
- **Matris Sözleşmeleri ve Join Politikaları**: `python -m scripts.run_feature_matrix_contracts` ile 6 matris sözleşmesi ve 5 birleştirme politikası (asof backward, exact, session bucket, event window, metadata tag) incelenir. Operatör hiçbir birleştirme politikasını ileriye dönük (forward) olarak konfigüre edemez.
- **9 Domain Hizalama Defteri**: `python -m scripts.run_domain_alignment_registries` ile FX-Emtia, FX-Makro, FX-Takvim, FX-Haber, Emtia-Makro, Emtia-Takvim, Emtia-Haber, Makro-Takvim ve Takvim-Haber ilişkileri listelenir. Haber verilerinde tam metin bulunmadığı teyit edilir.
- **Cross-Domain Feature Matrisi ve Manifest**: `python -m scripts.run_cross_domain_feature_matrix` ile mutasyonsuz (`df.copy()`) ve geriye dönük (`safe_asof_join_backward`) feature matrisi ve provenance manifesti oluşturulur.
- **Feature Metadata Defteri**: `python -m scripts.run_cross_asset_alignment_metadata` ile `<domain>__<family>__<source_symbol>__<feature_name>__<window>` ad alanına sahip feature'ların metadata özellikleri ve Phase 120 hazırlığı incelenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_cross_asset_alignment_health_check` ile 39 bileşenin HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_cross_asset_alignment_validation_report` ile 31 No-Go ve 15 Safe-Go güvenlik kuralı, non-signal kısıtları ve Phase 120 devir hazır oluşu teyit edilir.
- **Genel Durum**: `python -m scripts.run_cross_asset_alignment_status` ile 27 tablonun SUCCESS ile üretildiği doğrulanır.

## Phase 120 Macro/Calendar/News Feature Fusion Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_fusion_feature_profile_registry` ile 3 operasyonel profil (`balanced_local_feature_fusion`, `strict_no_lookahead_fusion_safety`, `dry_run_feature_fusion_focus`) ve 35 fusion feature alanı doğrulanır.
- **Fusion Sözleşmeleri**: `python -m scripts.run_fusion_feature_contracts` ile Makro (4), Takvim Olay (5), Release Olay (4) ve Haber Metadata (5) olmak üzere toplam 18 girdi/çıktı kontratı denetlenir.
- **Makro ve Takvim Politika Defterleri**: `python -m scripts.run_macro_calendar_policy_registries` ile makro release lag politikaları (lag >= 0, `release_timestamp <= base_timestamp`), takvim olay penceresi politikaları (pre-event, during-event, post-event) ve zaman damgası hizalama politikaları incelenir.
- **Haber Metadata Fusion Politikaları ve No-Lookahead Guard**: `python -m scripts.run_news_metadata_fusion_policies` ile haberlerin strictly metadata-only (sıfır tam metin, sıfır scraping, sıfır telif kopyası) olduğu, geriye dönük asof join kuralları (`safe_fusion_asof_join_backward`) ve lookahead bias korumaları teyit edilir.
- **Çok Alanlı Fusion Defterleri ve Hesaplama Provaları**: `python -m scripts.run_macro_calendar_news_fusion_registries` ile 17 feature/placeholder dönüşümü ve 4 çapraz alan fusion motoru (Makro-Takvim, Makro-Haber, Takvim-Haber, Çapraz Alan Bağlam) sentetik veri üzerinde mutasyonsuz (`df.copy()`) olarak test edilir.
- **Fusion Feature Matrisi ve Manifest**: `python -m scripts.run_fusion_feature_matrix` ile 6 matris sözleşmesi doğrulanır, multi-domain fusion matrisi oluşturulur ve manifest kayıtları üretilir.
- **Metadata ve Bağımlılık Defteri**: `python -m scripts.run_fusion_feature_metadata_registry` ile `<domain>__<family>__<source_symbol>__<feature_name>__<window>` ad alanına sahip fusion feature'ların metadata özellikleri, girdi bağımlılıkları ve validasyon kuralları incelenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_fusion_feature_health_check` ile 11 kritik alt sistemin HEALTHY olduğu teyit edilir.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_fusion_feature_validation_report` ile 28 No-Go ve 14 Safe-Go güvenlik kuralı, non-signal kısıtları ve Phase 121 devir hazır oluşu teyit edilir.
- **Genel Durum**: `python -m scripts.run_fusion_feature_status` ile 12 operasyonel alt sistemin READY olduğu doğrulanır.

## Phase 121 Feature Validation and No-Lookahead Guard Operations
- **Profil Defteri**: `python -m scripts.run_feature_validation_profile_registry` ile 3 operasyonel profil (`balanced_local_feature_validation`, `strict_no_leakage_feature_validation`, `dry_run_feature_validation_contract_freeze`) ve 27 validasyon alanı doğrulanır.
- **Validasyon Kuralları ve Yasaklı Kolonlar**: `python -m scripts.run_feature_validation_rules` ile 17 deterministik kural, 20 yasaklı kolon terimi (buy, sell, target, prediction, position vb.) ve lookahead korumaları denetlenir.
- **No-Lookahead ve Sızıntı Denetimi**: `python -m scripts.run_no_lookahead_validation` ile negatif shift (`shift(-1)`), ileriye dönük getiri (`future_return`) ve zaman damgası uyumsuzlukları taranır.
- **Feature Matrisi Bütünlüğü**: `python -m scripts.run_feature_matrix_integrity_validation` ile warmup NaNs, duplicate kolonlar, namespace çakışmaları, sayısal outlier ve sonsuz değerler denetlenir.
- **Alan Çıktı Doğrulama**: `python -m scripts.run_domain_feature_output_validation` ile Phase 117 indikatör, Phase 118 grid, Phase 119 cross-asset ve Phase 120 fusion çıktı sözleşmeleri doğrulanır.
- **Bulgular ve Manuel İnceleme Kuyruğu**: `python -m scripts.run_feature_validation_findings` ile tespit edilen anomaliler silinmeden manuel inceleme kuyruğuna alınır (`destructive_action_allowed: False`).
- **Validasyon Skorlama Motoru**: `python -m scripts.run_feature_validation_scoring` ile 0.0 - 1.0 aralığında normalize kalite skoru hesaplanır (bu skor kesinlikle trade sinyali veya onay değildir).
- **Sistem Sağlık ve Güvenlik Sınırları**: `python -m scripts.run_feature_validation_health_check` ile 6 kritik alt sistemin HEALTHY olduğu, 30 No-Go ve 14 Safe-Go kuralının SECURE olduğu teyit edilir.
- **Rapor Üretimi**: `python -m scripts.run_feature_validation_report` ile JSON, Markdown ve Plaintext denetim raporları üretilip `reports/output/advanced_feature_validation/` dizinine kaydedilir.
- **Genel Durum**: `python -m scripts.run_feature_validation_status` ile Phase 121 bileşenlerinin OPERATIONAL olduğu ve Phase 122 Factor Metadata devrinin READY olduğu teyit edilir.

## Phase 122 Factor Metadata and Factor Families Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_factor_metadata_profile_registry` ile 3 operasyonel profil (`balanced_local_factor_metadata`, `strict_metadata_only`, `dry_run`) ve 32 faktör metadata alanı incelenir.
- **Faktör Ailesi Taksonomisi**: `python -m scripts.run_factor_family_registry` ile 12 faktör ailesi (9 hazır, 3 placeholder) listelenir. Operatör bu ailelerin kesinlikle sinyal veya strateji olmadığını teyit eder.
- **Faktör Sözleşmeleri ve Şemaları**: `python -m scripts.run_factor_contracts` ile 12 girdi özellik kümesi, ad alanları (`factor__<family>__<asset_class>__<symbol>__<factor_name>__<window>`) ve çıktı şemaları denetlenir.
- **Faktör Bağımlılık Defteri**: `python -m scripts.run_factor_dependency_registry` ile 17 bağımlılık (14 zorunlu, 9 validasyon, 7 kalite) incelenir. Phase 116-121 girdilerinin eksiksizliği doğrulanır.
- **Teknik ve Fiyat Faktör Aileleri**: `python -m scripts.run_technical_factor_families` ile teknik, trend, momentum, volatilite, ortalamaya dönüş, getiri ve kotasyon mikro-yapı faktör tanımları doğrulanır.
- **Makro, Takvim, Haber ve Çapraz Varlık Faktör Aileleri**: `python -m scripts.run_macro_event_news_factor_families` ile makro bağlam, takvim olay, haber dikkat (strictly metadata-only), çapraz varlık ve rejim hazırlık faktörleri listelenir.
- **Faktör Manifesti ve Yönetişim**: `python -m scripts.run_factor_metadata_manifest` ile 12 manifest girdisi, 6 manuel inceleme maddesi, 5 non-signal politikası, 14 yasaklı desen denetimi ve Phase 123 devir hazırlığı denetlenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_factor_metadata_health_check` ile 10 kontrolün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_factor_metadata_validation_report` ile 6 validasyon kuralı ve 20 NO-GO / 11 SAFE-GO güvenlik sınırının SECURE olduğu teyit edilir.
- **Genel Durum**: `python -m scripts.run_factor_metadata_status` ile tüm Phase 122 bileşenlerinin `factor_ready` veya `factor_placeholder_only` durumunda olduğu teyit edilir.

## Phase 123 Feature Quality and Drift Diagnostics Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_feature_quality_drift_profile_registry` ile 3 operasyonel profil (`balanced_local_feature_quality_drift`, `strict_feature_quality_drift`, `dry_run`) ve 32 tanı alanı incelenir.
- **Metrikler ve Eşikler**: `python -m scripts.run_feature_quality_metric_registry` ile 9 kalite metriği, 10 drift metriği, 6 kalite eşiği ve 5 drift eşiği denetlenir.
- **Feature Kalite Tanı Paketi**: `python -m scripts.run_feature_quality_diagnostics` ile eksik veri, sonsuz değerler (inf/-inf), all-NaN kolonlar, sıfır varyans, yinelenen değerler, dağılım özetleri, donukluk (staleness) ve ad alanı kalitesi test edilir.
- **Feature Drift ve Kararlılık**: `python -m scripts.run_feature_drift_diagnostics` ile baseline vs current dağılım kayması (PSI/KS/Wasserstein/mean-shift) ve yuvarlanan pencere kararlılık skorları denetlenir.
- **Faktör Kalite ve Drift Raporları**: `python -m scripts.run_factor_quality_drift_reports` ile 10 faktör ailesinin kalite, drift, veri mevcudiyeti ve bağımlılık grafiği doğrulanır.
- **Makro, Takvim, Haber ve Çapraz Varlık**: `python -m scripts.run_macro_cross_asset_quality_reports` ile metadata-only sınırı (sıfır tam metin, sıfır kazıma) ve asof birleştirme kalitesi teyit edilir.
- **Bulgular, Manuel İnceleme Kuyruğu ve Manifest**: `python -m scripts.run_feature_quality_drift_findings` ile tespit edilen kusurlar silinmeden kuyruklara aktarılır (`destructive_action_allowed: False`), kalite/drift skorları üretilir ve Phase 124 devir manifestosu hazırlanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_feature_quality_drift_health_check` ile 8 kontrolün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_feature_quality_drift_validation_report` ile 9 validasyon denetimi, yasaklı iddia taraması ve 13 NO-GO / 7 SAFE-GO kuralının SECURE olduğu teyit edilir.
- **Genel Durum**: `python -m scripts.run_feature_quality_drift_status` ile tüm Phase 123 alt sistemlerinin PASS durumunda ve Phase 124 Handoff'un READY olduğu teyit edilir.
## Phase 124 Feature Store Integration Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_feature_store_integration_profile_registry` ile 3 operasyonel profil (`balanced_local_feature_store`, `strict_feature_store`, `dry_run_feature_store`) ve 32 entegrasyon alanı incelenir.
- **Sözleşmeler ve Şemalar**: `python -m scripts.run_feature_store_contracts` ile 7 depo sözleşmesi, 12 kanonik şema, okuma, yazma ve sorgulama sözleşmeleri doğrulanır.
- **Varlık, Feature ve Faktör Katalogları**: `python -m scripts.run_feature_store_catalogs` ile 9 varlık türü, teknik/grid/cross-asset/fusion feature katalogları ve 12 faktör ailesi incelenir.
- **Yönetişim Manifestosu**: `python -m scripts.run_feature_store_metadata_manifest` ile merkezi depo manifestosu ve kaynak koruma değişmezleri (`source_preserved: True`, `non_signal: True`) denetlenir.
- **Kalite ve Drift Katalogları**: `python -m scripts.run_feature_store_quality_drift_catalog` ile feature ve faktör kalite skorları, KS/PSI drift metrikleri ve stabilite skorları incelenir.
- **Validasyon Kataloğu**: `python -m scripts.run_feature_store_validation_catalog` ile doğrulama durumları (`VALIDATION_PASS`, `VALIDATION_WARN`, `VALIDATION_FAIL`) ve inceleme engelleyicileri (`manual_review_blockers`) listelenir.
- **İlkeler ve Politikalar**: `python -m scripts.run_feature_store_policy_registries` ile non-signal, yasaklı kolon, versiyon, bölümleme (partition), soybağı ve kaynak koruma ilkeleri kontrol edilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_feature_store_integration_health_check` ile 10 modül denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_feature_store_integration_validation_report` ile 5 validasyon kuralı ve 15 NO-GO / 8 SAFE-GO güvenlik sınırının SECURE olduğu teyit edilir.
- **Genel Durum**: `python -m scripts.run_feature_store_integration_status` ile tüm Phase 124 alt sistemlerinin PASS durumunda ve Phase 125 Handoff'un READY olduğu teyit edilir.

## Phase 125 Feature/Factor Engine Acceptance Report and Block Finalization Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_feature_factor_acceptance_profile_registry` ile 3 operasyonel profil (`balanced_local_feature_factor_acceptance`, `strict_feature_factor_acceptance`, `dry_run_feature_factor_acceptance`) ve Phase 116-126 arası 11 kabul alanı incelenir.
- **Blok Envanteri ve Bağımlılıklar**: `python -m scripts.run_feature_engine_block_inventory` ile 10 modül (Phase 116-125), 93 operasyonel betik, 193 test dosyası ve 10 bağımlılık kenarı denetlenir.
- **Kabul Geçitleri ve Skorlama**: `python -m scripts.run_feature_engine_block_acceptance_gates` ile 16 kabul geçidi (tümü GEÇTİ), ağırlıklı kabul skoru (1.0 - EXCELLENT_READINESS) ve tahribatsız manuel inceleme kuyruğu doğrulanır.
- **Uyumluluk Denetimi**: `python -m scripts.run_feature_engine_block_compliance` ile 6 yönlü uyumluluk (non-signal, no-lookahead, yasaklı kolon blokajı, haber sadece-metaveri, kaynak koruma ve feature store hazır olma) doğrulanır.
- **Sözleşmeler Denetimi**: `python -m scripts.run_feature_engine_block_contracts` ile 9 dokümantasyon sözleşmesi, 20 temsilci betik sözleşmesi ve 10 temsilci test sözleşmesi denetlenir.
- **Kabul Manifestosu ve Devir**: `python -m scripts.run_phase_116_125_acceptance_manifest` ile Phase 116-125 blok kabul manifestosu ve Phase 126 (Regime Classification and Market Behavior Foundation) 12 devir kalemi doğrulanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_feature_factor_acceptance_health_check` ile 15 modül ve dizin kontrolünün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_feature_factor_acceptance_validation_report` ile 5 validasyon kuralı ve 15 NO-GO / 7 SAFE-GO güvenlik sınırının SECURE olduğu teyit edilir.
- **Genel Durum**: `python -m scripts.run_feature_factor_acceptance_status` ile tüm Phase 125 alt sistemlerinin ACCEPTANCE_PASS durumunda ve Phase 126 Regime Handoff'un READY olduğu teyit edilir.

## Phase 126 Regime Classification and Market Behavior Foundation Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_regime_foundation_profile_registry` ile 3 operasyonel profil (`balanced_local_regime_foundation`, `strict_non_signal_regime_foundation`, `dry_run_regime_foundation`) ve 22 rejim etki alanı incelenir.
- **Piyasa Davranış Taksonomisi ve Rejim Durumları**: `python -m scripts.run_market_behavior_taxonomy` ile 12 piyasa davranış biçimi (9 hazır, 3 placeholder) ve 11 rejim durumu (`regime_state_*`) incelenir. Sinyal, buy, sell, target, prediction bulunmadığı teyit edilir.
- **Rejim Aileleri Defteri**: `python -m scripts.run_regime_family_registry` ile 9 rejim ailesi, volatilite/trend/yatay/likidite alt aileleri ve durumları incelenir. Model eğitimi veya kümeleme çalıştırılmadığı doğrulanır.
- **Çevresel Bağlam Defterleri**: `python -m scripts.run_regime_context_registries` ile makro bağlam, takvim olay bağlamı, haber metadata bağlamı (tam metin yok, kazıma yok) ve çapraz varlık bağlamı kontrol edilir.
- **Sözleşmeler ve Bağımlılıklar**: `python -m scripts.run_regime_contracts_dependencies` ile 9 rejim girdi sözleşmesi, 15 faktör bağımlılığı, 8 validasyon kuralı, 7 kalite metriği, 8 ad alanı ve çıktı şeması denetlenir.
- **Manifesto ve Phase 127 Devir**: `python -m scripts.run_regime_foundation_manifest` ile merkezi rejim manifestosu, 12 devir kalemi ve Phase 127 (Regime Feature Matrix and State Dataset Contracts) devir şartnamesi doğrulanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_foundation_health_check` ile 11 alt sistemin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırları**: `python -m scripts.run_regime_foundation_validation_report` ile 6 validasyon kuralı, yasaklı iddia taraması ve 15 NO-GO / 8 SAFE-GO güvenlik sınırının SECURE olduğu teyit edilir.
- **Genel Durum**: `python -m scripts.run_regime_foundation_status` ile tüm Phase 126 bileşenlerinin OPERATIONAL/READY durumunda olduğu teyit edilir.

## Phase 127 Regime Feature Matrix and State Dataset Contracts Operations
- **Profil, Alan ve Varlık Defterleri**: `python -m scripts.run_regime_matrix_profile_registry` ile 3 profil (`balanced_local_regime_matrix`, `strict_non_signal_regime_matrix_safety`, `dry_run_regime_matrix`), 6 etki alanı ve 9 kanonik varlık incelenir.
- **Feature Matrix Sözleşmeleri ve Şema**: `python -m scripts.run_regime_feature_matrix_contracts` ile 7 matrix sözleşmesi, `regime_matrix__` ad alanı ve 16 standart sütunlu şema doğrulanır.
- **State Dataset Sözleşmeleri ve Aday Bağlamlar**: `python -m scripts.run_regime_state_dataset_contracts` ile 5 durum veri kümesi sözleşmesi, 11 standart alan ve 10 aday bağlam incelenir. Aday bağlamların kesinlikle hedef etiket olmadığı teyit edilir.
- **Girdi Bileşenleri ve Bağımlılıklar**: `python -m scripts.run_regime_matrix_input_registries` ile teknik, faktör, çevresel bağlam ve kalite girdileri denetlenir.
- **Zaman Hizalaması ve No-Lookahead Güvenliği**: `python -m scripts.run_regime_matrix_alignment_guards` ile UTC zaman damgası, backward-only asof join, no-lookahead guard ve yasaklı sütun kuralları test edilir.
- **Bütünlük Manifestosu ve Manuel İnceleme**: `python -m scripts.run_regime_matrix_integrity_manifest` ile 8 bütünlük kuralı, MANIFEST_VALID durumu ve 8 inceleme maddesi incelenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_matrix_health_check` ile 12 alt sistemin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon, Güvenlik ve Phase 128 Devir**: `python -m scripts.run_regime_matrix_validation_report` ile validasyon kuralları, yasaklı iddialar, 15 NO-GO / 7 SAFE-GO kuralı ve Phase 128 (Regime Rule-Free Labeling Contracts and Unsupervised Prep) 12 devir maddesi doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_matrix_status` ile Phase 127 durumunun OPERATIONAL/READY olduğu teyit edilir.

## Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_regime_rule_free_profile_registry` ile 3 profil (`balanced_local_regime_rule_free_prep`, `strict_non_signal_rule_free_safety`, `dry_run_unsupervised_prep_contract_focus`) ve 31 fonksiyonel alan incelenir.
- **Kural-Bağımsız Etiketleme Sözleşmeleri ve Politikaları**: `python -m scripts.run_rule_free_labeling_contracts` ile 8 aday durum sözleşmesi (`volatility`, `trend`, `range`, `macro_event`, `news_attention`, `cross_asset`, `transition`, `uncertain`) ve 8 atama politikası yer tutucusu denetlenir. Kesinlikle hedef/tahmin üretilmez.
- **Aday Durum ve Pseudo-Durum Şemaları**: `python -m scripts.run_candidate_state_schemas` ile 12 standart sütunlu aday durum şeması, 8 non-signal pseudo-state şeması ve `candidate_state_` ad alanı kuralları doğrulanır.
- **Denetimsiz Hazırlık Sözleşmeleri ve Algoritma Yer Tutucuları**: `python -m scripts.run_unsupervised_prep_contracts` ile 6 hazırlık sözleşmesi, 5 kümeleme girdi sözleşmesi, 6 algoritma yer tutucusu (KMeans, DBSCAN, GMM, vb.), 5 mesafe metriği (Euclidean, Cosine, vb.) ve 4 boyut indirgeme yer tutucusu incelenir. Algoritmalar asla çalıştırılmaz (zero-execution).
- **Girdi Bileşenleri ve Aday Özellik Kümeleri**: `python -m scripts.run_candidate_state_input_registries` ile 7 aday özellik kümesi (33 feature), 8 araştırma bağlamı ve 8 metaveri kaydı incelenir.
- **Bütünlük Manifestosu ve Manuel İnceleme**: `python -m scripts.run_candidate_state_integrity_manifest` ile 8 bütünlük kuralı, MANIFEST_VALID durumu, zaman damgası politikaları, no-lookahead guard ve 9 maddelik tahribatsız manuel inceleme kuyruğu doğrulanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_rule_free_health_check` ile 12 alt sistem kontrolünün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon, Güvenlik ve Phase 129 Devir**: `python -m scripts.run_regime_rule_free_validation_report` ile 6 validasyon kuralı (VALIDATION_PASS), olumsuzlama duyarlı yasaklı iddia taraması, 16 NO-GO / 8 SAFE-GO güvenlik kuralı ve Phase 129 (Market Behavior Diagnostics and Regime Quality) 12 devir maddesi doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_rule_free_status` ile Phase 128 durumunun READY olduğu teyit edilir.

## Phase 129 Market Behavior Diagnostics and Regime Quality Operations
- **Profil, Alan ve Taksonomi Defterleri**: `python -m scripts.run_market_behavior_diagnostics_profile_registry` ile 3 profil (`balanced_local_market_behavior_diagnostics`, `strict_non_signal_behavior_quality_safety`, `dry_run_behavior_diagnostics_focus`) ve 12 davranış taksonomi bağlamı incelenir.
- **Kalite ve Tanı Metrik Registries**: `python -m scripts.run_behavior_quality_metric_registry` ile 10 kalite metriği (`candidate_state_coverage_ratio`, `candidate_state_consistency_score` vb.), 10 davranış tanı metriği ve 12 kalite eşiği denetlenir.
- **Aday Durum Kalite Raporları**: `python -m scripts.run_candidate_state_quality_reports` ile 8 aday durum kalite denetimi, 8 non-signal pseudo-state denetimi ve coverage/consistency/ambiguity/stability/missingness/namespace raporları üretilir. Kesinlikle auto-imputation veya auto-drop yapılmaz.
- **Rejim Ailesi Kalite Raporları**: `python -m scripts.run_regime_family_quality_reports` ile 9 rejim ailesi kalite denetimi, rejim ailesi kapsama oranları ve tutarlılık skorları incelenir.
- **Davranış Tanı Raporları**: `python -m scripts.run_behavior_diagnostics_reports` ile volatilite, trend, yatay/kanal, makro-olay, haber metaverisi (sıfır tam metin, sıfır scraping, sıfır NLP) ve çapraz varlık davranış tanı raporları üretilir. Ayrıca geçiş ve kararlılık hazırlık raporları ile Phase 121/123/124/127/128 bağımlılık doğrulaması yapılır.
- **Bulgular, Manuel İnceleme ve Kalite Skoru**: `python -m scripts.run_behavior_quality_findings` ile davranış anomali bulguları, 3 maddelik tahribatsız manuel inceleme kuyruğu ve ceza bazlı iç teşhis kalite skoru ([0.0, 1.0] aralığı) üretilir. Bu skor sinyal değildir.
- **Tanı Manifestosu ve Phase 130 Devir**: `python -m scripts.run_behavior_diagnostics_manifest` ile davranış tanı manifestosu (MANIFEST_VALID), 12 Phase 130 devir maddesi ve Phase 130 (Regime Transition and Stability Analysis) için hazırlık şartnamesi denetlenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_market_behavior_diagnostics_health_check` ile 12 alt sistemin tümünün (Phase 121-128 bağımlılıkları dahil) HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_market_behavior_diagnostics_validation_report` ile validasyon kuralları, yasaklı iddia taraması, 16 NO-GO / 8 SAFE-GO güvenlik sınırı (SECURE) doğrulanır.
- **Genel Durum**: `python -m scripts.run_market_behavior_diagnostics_status` ile Phase 129 durumunun READY olduğu teyit edilir.

## Phase 130 Regime Transition and Stability Analysis Operations
- **Profil, Alan ve Metrik Defterleri**: `python -m scripts.run_regime_transition_profile_registry` ile 3 profil (`balanced_local_regime_transition`, `strict_non_signal_regime_transition`, `dry_run_regime_transition`), 28 fonksiyonel geçiş alanı, geçiş ve kararlılık metrikleri incelenir.
- **Aday ve Pseudo Durum Sekans Sözleşmeleri**: `python -m scripts.run_regime_state_sequence_contracts` ile aday durum sekans sözleşmeleri, pseudo-durum sözleşmeleri, şemalar, zaman damgası politikaları ve no-lookahead korumaları denetlenir.
- **Geçiş ve Kararlılık Metrikleri**: `python -m scripts.run_regime_transition_metrics` ile geçiş sıklığı, geçiş oranı, geçiş belirsizliği, durum kalıcılığı ve geçiş kararlılığı metrikleri incelenir.
- **Durum Geçiş Tanı Raporları**: `python -m scripts.run_state_transition_diagnostics` ile durum kalıcılığı run-length tahminleri, ampirik geçiş sıklığı, Markov-fit içermeyen matris yer tutucuları, geçiş belirsizliği, sekans sürekliliği ve genel kararlılık tanı raporları üretilir.
- **Bağlamsal Geçiş Raporları**: `python -m scripts.run_transition_context_reports` ile volatilite, trend, range, makro olay ve haber metaverisi geçiş bağlamları ile çapraz varlık geçiş hazırlık raporu incelenir.
- **Kalite Bulguları, Manuel İnceleme ve Skorlama**: `python -m scripts.run_transition_quality_findings` ile tespit edilen geçiş kusurları silinmeden kuyruklara aktarılır (`destructive_action_allowed: False`, `auto_fix_forbidden: True`), 3 maddelik manuel inceleme kuyruğu ve kararlılık skoru üretilir.
- **Tanı Manifestosu**: `python -m scripts.run_transition_diagnostics_manifest` ile geçiş tanı manifestosu (MANIFEST_VALID) ve kaynak koruma garantileri denetlenir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_transition_health_check` ile 12 alt sistemin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon, Güvenlik ve Phase 131 Devri**: `python -m scripts.run_regime_transition_validation_report` ile 5 validasyon kuralı (VALIDATION_PASS), yasaklı terim taraması, 18 NO-GO / 8 SAFE-GO güvenlik sınırı (SECURE) ve Phase 131 (Cross-Asset Regime Context and Dynamic Behavior Interplay) için 9 devir maddesi doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_transition_status` ile Phase 130 durumunun READY olduğu teyit edilir.

## Phase 131 Cross-Asset Regime Context Expansion Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_cross_asset_regime_profile_registry` ile 3 profil (`balanced_local_cross_asset_regime_context`, `strict_non_signal_cross_asset_regime_safety`, `dry_run_cross_asset_context_focus`) ve 34 fonksiyonel çapraz varlık alanı denetlenir.
- **Varlıklar, Çiftler ve Taksonomi**: `python -m scripts.run_cross_asset_regime_entities` ile 27 varlık, 12 kanonik çift ve 13 ilişki tipi taksonomisi incelenir.
- **Çapraz Varlık Rejim Bağlamları**: `python -m scripts.run_cross_asset_regime_contexts` ile FX-Emtia, FX-Makro, Emtia-Makro, Makro-Takvim ve Takvim-Haber (sıfır tam metin, sıfır scraping, sıfır NLP duygu analizi) bağlamları üretilir.
- **Bağlantı ve Tanı Raporları**: `python -m scripts.run_cross_asset_regime_linkage_reports` ile geçiş uyumu, volatilite bağlantısı, trend bağlantısı, range bağlantısı, ıraksama ve yakınsama tanıları ile korelasyon ve öncü/gecikmeli yer tutucuları incelenir. Kesinlikle trade sinyali veya pairs trading üretilmez.
- **Sözleşmeler ve Lookahead Korumaları**: `python -m scripts.run_cross_asset_regime_alignment_guards` ile 6 bağlam sözleşmesi, geriye dönük zaman damgası politikaları, strictly backward asof join politikaları (`direction='backward'`) ve no-lookahead korumaları (`context_timestamp <= base_timestamp`, `.shift(-1)` yasağı) denetlenir.
- **Bulgular, Manifest ve Phase 132 Devri**: `python -m scripts.run_cross_asset_regime_findings_manifest` ile 2 tanı bulgusu, 7 maddelik manuel inceleme kuyruğu, 0.86 bağlam skoru, MANIFEST_VALID manifestosu ve Phase 132 için 10 maddelik devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_cross_asset_regime_health_check` ile 15 alt sistemin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_cross_asset_regime_validation_report` ile 8 kuralın tümünün PASS olduğu ve 18 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_cross_asset_regime_status` ile tüm Phase 131 alt sistemlerinin yeşil ve Phase 132 için hazır olduğu teyit edilir.

## Phase 132 Macro/Event/News Regime Context Expansion Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_macro_event_news_regime_profile_registry` ile 3 profil (`balanced_local_macro_event_news_regime_context`, `strict_metadata_only_news_regime_safety`, `dry_run_macro_event_context_focus`) ve 43 makro, olay ve haber alanı doğrulanır.
- **Varlıklar ve Taksonomiler**: `python -m scripts.run_macro_event_news_regime_entities` ile 10 makro varlık, 10 takvim olay varlığı, 11 haber metaveri varlığı ve 26 taksonomi kuralı denetlenir.
- **Makro Gösterge ve Yayın Bağlamları**: `python -m scripts.run_macro_regime_contexts` ile göstergeler, resmi yayın takvimleri, revizyon döngüleri ve deskriptif sürpriz yer tutucuları incelenir.
- **Takvim Olayı ve Olay Pencereleri**: `python -m scripts.run_event_regime_contexts` ile FOMC, CPI, NFP, ECB olay pencereleri, pre-event ve post-event tampon süreleri, önem dereceleri, yayın gecikmesi ve planlanan vs. gerçekleşen yayın zamanlaması denetlenir.
- **Haber Metaveri Katmanı (Yalnızca Metaveri)**: `python -m scripts.run_news_metadata_regime_contexts` ile haber konuları, varlık etiketleri, makro tematik etiketler, olay bağlantıları, tazelik yarı-ömrü ve 14 yasaklı alan için sınır kuralları doğrulanır (tam metin, HTML, duygu modelleri ve embeddingler kesinlikle yasaktır).
- **Çapraz Varlık, Sözleşmeler ve No-Lookahead Korumaları**: `python -m scripts.run_macro_event_news_alignment_guards` ile 7 duyarlılık kanalı, 6 geçiş bağlamı, 3 bağlam sözleşmesi, geriye dönük zaman damgası ve asof birleştirme kuralları (`direction='backward'`) ve negatif shift yasakları denetlenir.
- **Bulgular, Manifest ve Phase 133 Devri**: `python -m scripts.run_macro_event_news_findings_manifest` ile 3 tanı bulgusu, 8 maddelik tahribatsız manuel inceleme kuyruğu, 1.0 bağlam skoru, MANIFEST_VALID manifestosu ve Phase 133 için 13 maddelik devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_macro_event_news_regime_health_check` ile 16 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_macro_event_news_regime_validation_report` ile 5 kuralın VALIDATION_PASS olduğu ve 20 NO-GO / 9 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_macro_event_news_regime_status` ile tüm Phase 132 alt sistemlerinin yeşil ve Phase 133 için hazır olduğu teyit edilir.

## Phase 133 Regime Validation and No-Lookahead Acceptance Operations
- **Profil ve Kabul Alan Defterleri**: `python -m scripts.run_regime_validation_acceptance_profile_registry` ile 3 operasyonel profil (`balanced_local_regime_validation_acceptance`, `strict_no_lookahead_regime_safety`, `dry_run_regime_acceptance_focus`) ve 44 fonksiyonel kabul alanı doğrulanır.
- **19 Kanonik Kabul Geçidi**: `python -m scripts.run_regime_validation_gates` ile 19 kabul geçidi (no-lookahead, backward asof, monotonic UTC timestamps, yasaklı kolon karantinası, haber metaveri sınır koruması, kaynak koruma, non-signal teminatı, hedef/etiket yokluğu, model eğitilmeme güvencesi, 6 bileşen kabulü, 2 bağımlılık kabulü, manuel inceleme ve skor eşiği) denetlenir.
- **No-Lookahead ve Zaman Damgası Kabulü**: `python -m scripts.run_regime_no_lookahead_acceptance` ile `context_ts <= base_ts`, kesin artan UTC zaman damgası sıralaması, backward-only asof join ve negatif shift yasağı doğrulanır.
- **Metadata-Only Haber Kabulü**: `python -m scripts.run_regime_metadata_only_acceptance` ile haber girdilerinde haber tam metni, makale gövdesi, ham içerik, kazınmış HTML, NLP duygu modeli çıktıları ve embedding/vektör veri tabanı bulunmadığı teyit edilir.
- **Bileşen Kabul Raporları**: `python -m scripts.run_regime_component_acceptance_reports` ile Phase 127 rejim matrisi, Phase 128 aday durum ve pseudo-durum, Phase 130 geçiş, Phase 131 çapraz varlık ve Phase 132 makro/olay/haber bileşenlerinin kabul raporları üretilir.
- **Bulgular, Manuel İnceleme ve Skorlama**: `python -m scripts.run_regime_validation_findings` ile 3 tanı bulgusu, 8 maddelik tahribatsız manuel inceleme kuyruğu ve 1.0 kabul skoru (`high_acceptance_integrity`) doğrulanır.
- **Kabul Manifestosu ve Phase 134 Devri**: `python -m scripts.run_regime_validation_acceptance_manifest` ile master kabul manifestosu (MANIFEST_VALID) ve Phase 134 (Regime FeatureStore Integration) için 14 devir maddesi onaylanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_validation_acceptance_health_check` ile 20 alt sistem kontrolünün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_regime_validation_acceptance_validation_report` ile 6 validasyon kuralının VALIDATION_PASS olduğu ve 22 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_validation_acceptance_status` ile tüm Phase 133 alt sistemlerinin yeşil ve Phase 134 için hazır olduğu teyit edilir.

## Phase 134 Regime FeatureStore Integration Operations
- **Profil ve Depolama Alan Defterleri**: `python -m scripts.run_regime_featurestore_profile_registry` ile 3 profil (`balanced_local_regime_featurestore_integration`, `strict_metadata_only_featurestore`, `dry_run_featurestore_focus`) ve 33 fonksiyonel depolama alanı doğrulanır.
- **Sözleşmeler ve Varlıklar**: `python -m scripts.run_regime_featurestore_contracts` ile 10 FeatureStore sözleşmesi, 10 kanonik varlık, sürüm ve bölümleme politikaları denetlenir.
- **Şema, İsim Alanı ve Okuma/Yazma/Sorgu**: `python -m scripts.run_regime_featurestore_schema_catalogs` ile 16 alanlık minimum çekirdek şema, `regime_store_` ad alanı, 2 okuma, 2 yazma ve 8 sorgu kuralı incelenir.
- **8 Bileşen Deposu Kataloğu**: `python -m scripts.run_regime_component_store_catalogs` ile Taxonomy (Phase 126), Matrix (Phase 127), Candidate States (Phase 128), Pseudo States (Phase 128), Transition (Phase 130), Cross-Asset (Phase 131), Macro/Event/News (Phase 132) ve Validation Acceptance (Phase 133) katalogları üretilir (toplam 25 kayıt).
- **Kabul Edilmiş Referanslar ve Bağımlılıklar**: `python -m scripts.run_regime_accepted_reference_registries` ile 21 kabul edilmiş referans (no-lookahead, metadata-only news, source preservation, non-signal), 6 kalite bağımlılığı, 6 doğrulama bağımlılığı ve 9 soykütüğü adımı denetlenir.
- **Politikalar, Manifest ve Phase 135 Devri**: `python -m scripts.run_regime_featurestore_policies_manifest` ile 9 engelleyici denetimi, 23 yasaklı kolon, 14 yasaklı iddia, 7 yasaklı eylem, master manifest (`readiness_score: 1.0`) ve Phase 135 (Regime Classification Acceptance Report) için 14 devir maddesi onaylanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_featurestore_health_check` ile 16 alt sistem kontrolünün tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_regime_featurestore_validation_report` ile 6 validasyon denetiminin VALIDATION_PASS olduğu ve 21 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_featurestore_status` ile tüm Phase 134 bileşenlerinin `regime_store_ready` durumunda olduğu ve Phase 135 devrine hazır olduğu teyit edilir.

## Phase 135 Regime Classification Acceptance Report and Block Finalization Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_regime_acceptance_profile_registry` ile 3 operasyonel profil (`balanced_local_regime_acceptance`, `strict_non_signal_regime_block_acceptance`, `dry_run_regime_manifest_focus`) ve Phase 126-136 arasındaki 11 fonksiyonel kabul alanı doğrulanır.
- **Blok Envanteri ve Bağımlılık Çizgesi**: `python -m scripts.run_regime_block_inventory` ile 10 fazlık rejim bloğunun (Phase 126-135) modül envanteri (10 modül, 92 runner betiği, 185 test dosyası) ve ardışık bağımlılık DAG'ı (126 -> 127 -> ... -> 135 -> 136) denetlenir.
- **17 Kanonik Kabul Geçidi**: `python -m scripts.run_regime_block_acceptance_gates` ile blok kabulü için 17 kabul geçidi (10 fazın tamamlanması, no-lookahead uyumu, metadata-only haber doğrulaması, kaynak veri korunumu, non-signal teminatı, FeatureStore entegrasyonu, 1.0 skor vb.) çalıştırılır ve 17/17 PASS olduğu doğrulanır.
- **6 Boyutlu Uyumluluk Denetimi**: `python -m scripts.run_regime_block_compliance` ile non-signal, no-lookahead, metadata-only haber, yasaklı kolon karantinası, kaynak veri dokunulmazlığı ve FeatureStore hazırlık uyumluluk raporları üretilir.
- **Bileşen Kabul Matrisi**: `python -m scripts.run_regime_block_component_acceptance` ile Phase 126'dan 135'e kadar 10 bileşenin tamamının kabul edildiği (`component_accepted: True`) teyit edilir.
- **Sözleşmeler Denetimi**: `python -m scripts.run_regime_block_contracts` ile 9 dokümantasyon sözleşmesi, 20 temsilci runner betik sözleşmesi ve 10 temsilci test paketi sözleşmesi denetlenir.
- **Blok Kabul Manifestosu ve Phase 136 Devri**: `python -m scripts.run_phase_126_135_acceptance_manifest` ile imzalı master blok kabul manifestosu (MANIFEST_VALID), 1.0 kompozit skor (`HIGH_INTEGRITY`) ve Phase 136 (GPU Acceleration and Advanced ML Runtime Foundation) için 14 devir önkoşulu doğrulanır.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_regime_acceptance_health_check` ile 15 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik**: `python -m scripts.run_regime_acceptance_validation_report` ile 6 validasyon kuralının VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 19 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_regime_acceptance_status` ile Phase 126-135 rejim bloğu genel kabul durumunun `acceptance_pass` olduğu ve Phase 136 devrine hazır olduğu teyit edilir.

## Phase 136 GPU Acceleration and Advanced ML Runtime Foundation Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_gpu_ml_runtime_profile_registry` ile 3 temel profil (`balanced_local_gpu_ml_runtime_foundation`, `strict_no_training_gpu_runtime_safety`, `dry_run_ml_capability_discovery_focus`) ve 23 çalışma zamanı alanı doğrulanır.
- **Yerel Donanım ve Hızlandırıcı Keşfi**: `python -m scripts.run_local_hardware_discovery` ile OS, CPU mimarisi, çekirdek sayısı, RAM, takas alanı, NVIDIA GPU varlığı, CUDA desteği ve çalışma ortamı anlık görüntüsü güvenli biçimde çıkarılır.
- **ML Bağımlılık İncelemesi**: `python -m scripts.run_ml_dependency_capability_reports` ile PyTorch, Scikit-Learn, NumPy, Pandas ve 11 opsiyonel ML kütüphanesi (XGBoost, LightGBM, CatBoost, Optuna, SHAP, ONNX vb.) model fit edilmeden ve tensor tahsis edilmeden incelenir.
- **Güvenlik Sözleşmeleri ve İzin Politikaları**: `python -m scripts.run_ml_runtime_safety_contracts` ile 12 uygulanabilir güvenlik sözleşmesi, izinli keşifler, engellenmiş model eğitimi/çıkarımı/etiket üretimi ve yönetişim yer tutucuları denetlenir.
- **Girdi Sözleşmeleri**: `python -m scripts.run_ml_input_contracts` ile Phase 126-135 rejim metadata, FeatureStore katalogları, no-lookahead (kronolojik asof), metadata-only haber ve kaynak koruma sözleşmeleri doğrulanır.
- **Bulgular, Puanlama ve Manifest**: `python -m scripts.run_gpu_ml_runtime_findings_manifest` ile ortam bulguları, manuel inceleme kuyruğu, hazırlık skoru (0.0-1.0), master manifest ve Phase 137 devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_gpu_ml_runtime_health_check` ile 11 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırı**: `python -m scripts.run_gpu_ml_runtime_validation_report` ile 6 validasyon kuralının tümünün geçtiği ve 20 NO-GO / 11 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_gpu_ml_runtime_status` ile tam pipeline çalıştırılarak tüm Phase 136 bileşenlerinin READY olduğu ve Phase 137 devrine hazır olduğu teyit edilir.

## Phase 137 Advanced ML Dataset Contracts and Experiment Registry Operations
- **Profil ve Alan Defterleri**: python -m scripts.run_advanced_ml_dataset_profile_registry ile 3 operasyonel profil (alanced_local_ml_dataset_contracts, strict_no_materialization_no_training_dataset_safety, dry_run_experiment_registry_focus) ve 42 fonksiyonel yönetişim alanı doğrulanır.
- **Veri Kümesi Sözleşmeleri ve Kaynak Kataloğu**: python -m scripts.run_ml_dataset_contracts ile 9 ana ML veri kümesi ailesi sözleşmesi ve 21 salt-metadata kaynak referansı doğrulanır. Fiziksel veri materyalleştirmesi ve model eğitimi engellidir.
- **Şemalar, İsim Alanları ve Bölümleme Politikaları**: python -m scripts.run_ml_dataset_schema_policies ile 9 şema sözleşmesi, 8 özellik ad alanı (ml_feature_ öneki zorunlu), 3 versiyon, 3 partition, 3 zaman indeksi, 4 zaman serisi bölme, 3 walk-forward ve 2 arındırılmış (purged) bölme politikası denetlenir.
- **Güvenlik Korumaları (Guards)**: python -m scripts.run_ml_dataset_guards ile 4 sızıntı önleme kuralı, 4 no-lookahead kuralı, haber metaveri kısıtları, kaynak koruma ilkeleri, 20 yasaklı kolon ve 5 hedef/etiket engelleme politikası çalıştırılır.
- **Deney Kaydı ve Eğitimsiz Yönetişim**: python -m scripts.run_ml_experiment_registry ile 6 deney tanımı, 6 şablon, 14 izin, 4 yürütme planı yer tutucusu, 10 model ailesi yer tutucusu, 7 metrik yer tutucusu ve 3 eğitim/çıkarım/artifact engelleme sözleşmesi denetlenir.
- **Bulgular, Manifest ve Devir**: python -m scripts.run_ml_dataset_findings_manifest ile 4 yönetişim bulgusu, 9 maddelik manuel inceleme kuyruğu, hazırlık skoru (0.0-1.0), master Phase 137 manifestosu ve Phase 138 devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: python -m scripts.run_advanced_ml_dataset_health_check ile 13 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırı**: python -m scripts.run_advanced_ml_dataset_validation_report ile 8 validasyon kuralının tümünün geçtiği ve 22 NO-GO / 12 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: python -m scripts.run_advanced_ml_dataset_status ile tam pipeline çalıştırılarak tüm Phase 137 bileşenlerinin OPERATIONAL olduğu ve Phase 138 devrine hazır olduğu teyit edilir.

## Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness Operations
- **Profil ve Alan Defterleri**: python -m scripts.run_baseline_ml_model_profile_registry ile 3 profil (alanced_local_baseline_ml_contracts, strict_no_real_training_baseline_safety, dry_run_harness_contract_focus), 37 operasyonel alan ve 10 model algoritma ailesi doğrulanır.
- **Model, Girdi ve Çıktı Sözleşmeleri**: python -m scripts.run_baseline_model_contracts ile 10 model sözleşmesi, 3 girdi sözleşmesi şablonu (Emtia/FX, Makro Olay, Çapraz Varlık Rejim), 10 çıktı sözleşmesi ve 10 dry-run eğitim planı denetlenir. Gerçek eğitim, model uyumu, tahmin ve sinyal üretimi kesinlikle engellenir.
- **Dry-Run Training Harness ve Trainer Stub'lar**: python -m scripts.run_dry_run_training_harness_contracts ile 5 harness sözleşmesi, 15 harness arayüzü (6 izinli, 9 yasaklı), 10 dry-run trainer stub'ı ve 6 zorunlu eğitim politikası (alidate_dry_run_training_request) çalıştırılır.
- **Devre Dışı Yürütme Güvenlik Raporları**: python -m scripts.run_baseline_model_safety_reports ile 5 bağımsız devre dışı yürütme denetimi (gerçek eğitim engelli, tahmin engelli, etiket/hedef üretimi engelli, model artifact kaydı engelli, model registry yazımı engelli) ve 24 NO-GO / 9 SAFE-GO güvenlik sınırı denetlenir.
- **Girdiler, Bağımlılıklar ve Güvenlik Muhafızları**: python -m scripts.run_baseline_model_dependencies_inputs ile 8 metrik yer tutucusu, 7 değerlendirme yer tutucusu, upstream doğrulama ve kalite bağımlılıkları, 5 aşamalı soykütük, FeatureStore/Rejim girdi katalogları, no-lookahead korumaları, yalnızca metadata haber korumaları, kaynak koruma ilkeleri, 23 yasaklı kolon ve 4 deney bağlantı şablonu denetlenir.
- **Bulgular, Manifest ve Phase 139 Devri**: python -m scripts.run_baseline_model_findings_manifest ile 0 kritik bulgulu temiz kayıt defteri, 5 maddelik manuel denetçi inceleme kuyruğu, 1.0 hazırlık skoru (READY_FOR_LOCAL_DRY_RUN_HARNESS), master Phase 138 manifestosu ve Phase 139 devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: python -m scripts.run_baseline_ml_model_health_check ile 11 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Yasaklı İddia Taraması**: python -m scripts.run_baseline_ml_model_validation_report ile 5 validasyon kuralının VALIDATION_PASS olduğu ve sıfır yasaklı iddia tespit edildiği doğrulanır.
- **Genel Durum**: python -m scripts.run_baseline_ml_model_status ile tam pipeline çalıştırılarak 18 bileşenin tümünün READY/VALID/SECURE olduğu ve Phase 139 devrine hazır olduğu teyit edilir.

## Phase 139 GPU-Accelerated Training Harness and Resource Governance Operations
- **Profil ve Alan Defterleri**: python -m scripts.run_gpu_training_governance_profile_registry ile 3 profil (alanced_local_gpu_training_governance, strict_no_training_resource_governance_safety, dry_run_gpu_resource_contract_focus) ve 40 operasyonel alan doğrulanır.
- **Kaynak Yönetişimi ve Yürütme Politikaları**: python -m scripts.run_gpu_training_resource_policies ile 4 kaynak politikası, deterministik cihaz seçimi, bellek bütçesi (%80 ceiling, 2048 MB reserved), CPU fallback politikaları, zaman aşımı politikaları (300s/1800s/3600s), batch size (16/32/64) ve sıralı/walk-forward dataloader yer tutucuları denetlenir.
- **Eğitim Döngüsü Stub Sözleşmeleri ve Harness Arayüzleri**: python -m scripts.run_gpu_training_harness_contracts ile 5 eğitim döngüsü stub sözleşmesi, 8 harness arayüzü ve 3 harness stub'ı çalıştırılır. 10 yasaklı yöntem (it, 	rain, predict, inference, 	ransform, ackward, optimizer_step, save_model, write_model_registry, generate_signal) kilitlenir.
- **Dry-Run Kaynak ve Yürütme Muhafızları**: python -m scripts.run_gpu_training_dry_run_guards ile donanım kullanılabilirlik denetimi, cihaz seçim simülasyonu, bellek istek sınaması, zaman aşımı sınaması ve 17 yasaklı yürütme anahtar kelimesi taraması gerçekleştirilir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: python -m scripts.run_gpu_training_disabled_execution_reports ile gerçek model eğitimi, model tahmini/çıkarımı, hedef/etiket üretimi, model ağırlığı kalıcılığı ve model registry yazımının engellendiğini belgeleyen 5 bağımsız denetim raporu üretilir.
- **Girdiler, Bağımlılıklar ve Güvenlik Muhafızları**: python -m scripts.run_gpu_training_dependencies_inputs ile Phase 136-138 bağımlılıkları, FeatureStore girdileri, no-lookahead kuralları, yalnızca-metadata haber kuralları, kaynak koruma ilkeleri, 23 yasaklı kolon ve kaynak/deney denetim yer tutucuları denetlenir.
- **Bulgular, Manifest ve Phase 140 Devri**: python -m scripts.run_gpu_training_findings_manifest ile 3 yönetişim bulgusu, 8 maddelik manuel inceleme kuyruğu, 1.0 hazırlık skoru (READY_FOR_GPU_RESOURCE_GOVERNANCE_DRY_RUN), master Phase 139 manifestosu ve Phase 140 devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: python -m scripts.run_gpu_training_governance_health_check ile 12 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırı**: python -m scripts.run_gpu_training_governance_validation_report ile 5 validasyon kuralının VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 24 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: python -m scripts.run_gpu_training_governance_status ile tam pipeline çalıştırılarak 20 bileşenin tümünün READY/VALID/SECURE olduğu ve Phase 140 devrine hazır olduğu teyit edilir.

## Phase 140 Ensemble Model Contracts and Candidate Model Registry Operations
- **Profil ve Alan Defterleri**: python -m scripts.run_ensemble_model_profile_registry ile 3 profil (alanced_local_ensemble_model_registry, strict_no_ensemble_execution_safety, candidate_registry_contract_focus) ve 40 operasyonel alan doğrulanır.
- **Aday Model Sözleşmeleri ve Aileler**: python -m scripts.run_candidate_model_contracts ile 5 aday model ailesi, 5 aday model sözleşmesi (
eal_training_allowed=False, model_fit_allowed=False, model_predict_allowed=False, rtifact_persistence_allowed=False, model_registry_write_allowed=False), 3 girdi sözleşmesi ve 5 çıktı sözleşmesi denetlenir.
- **Aday Model Uygunluk Kapıları ve Uyumluluk**: python -m scripts.run_candidate_model_eligibility_compatibility ile 12 aday model uygunluk kapısı ve 10 aday model uyumluluk sözleşmesi çalıştırılır. Uyumluluk skorları kesinlikle sinyal ve performans iddiası içermez.
- **Ensemble Strateji Sözleşmeleri ve Yer Tutucuları**: python -m scripts.run_ensemble_strategy_contracts ile 4 ensemble strateji sözleşmesi, 3 voting yer tutucusu, 2 blending yer tutucusu, 2 stacking yer tutucusu, 2 ağırlıklandırma politikası ve 2 meta-model yer tutucusu denetlenir (execution_blocked=True).
- **Devre Dışı Bırakılmış Yürütme Raporları**: python -m scripts.run_ensemble_disabled_execution_reports ile ensemble yürütmesi, aday model eğitimi, aday model tahmini/çıkarımı, hedef/etiket üretimi, model ağırlığı kalıcılığı ve model registry yazımının engellendiğini belgeleyen 6 bağımsız denetim raporu üretilir.
- **Bağımlılıklar, Muhafızlar ve Girdiler**: python -m scripts.run_ensemble_dependencies_inputs ile Phase 136-139 bağımlılıkları, metrik yer tutucuları, değerlendirme yer tutucuları, soykütük, no-lookahead kuralları, yalnızca-metadata haber kuralları, kaynak koruma ilkeleri, 24 yasaklı kolon ve deney bağlantı şablonları denetlenir.
- **Bulgular, Manifest ve Phase 141 Devri**: python -m scripts.run_ensemble_findings_manifest ile 3 yönetişim bulgusu, 10 maddelik manuel inceleme kuyruğu, 1.0 hazırlık skoru (READY_FOR_ENSEMBLE_CANDIDATE_REGISTRY_DRY_RUN), master Phase 140 manifestosu ve Phase 141 devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: python -m scripts.run_ensemble_model_health_check ile 12 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırı**: python -m scripts.run_ensemble_model_validation_report ile 5 validasyon kuralının VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 25 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: python -m scripts.run_ensemble_model_status ile tam pipeline çalıştırılarak 22 bileşenin tümünün READY/VALID/SECURE olduğu ve Phase 141 devrine hazır olduğu teyit edilir.

## Phase 141 Probability Calibration and Uncertainty Estimation Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_calibration_uncertainty_profile_registry` ile 3 kalibrasyon/belirsizlik profili (`balanced_local_calibration_uncertainty_contracts`, `strict_non_executing_calibration_safety`, `dry_run_uncertainty_governance_focus`) ve 49 operasyonel alan doğrulanır.
- **Olasılık Kalibrasyonu Sözleşmeleri ve Yöntemler**: `python -m scripts.run_probability_calibration_contracts` ile 7 kalibrasyon sözleşmesi, 7 yöntem yer tutucusu, girdi/çıktı sözleşmeleri ve 9 kalite kapısı denetlenir. Olasılık üretimi ve model uyumu kesinlikle kilitlidir (`all_zero_prediction=True`).
- **Belirsizlik Tahmini Sözleşmeleri ve Yöntemler**: `python -m scripts.run_uncertainty_estimation_contracts` ile 8 belirsizlik sözleşmesi, 8 yöntem yer tutucusu, girdi/çıktı sözleşmeleri ve 8 kalite kapısı denetlenir. Aralık hesaplaması ve çıkarım engellidir (`all_zero_uncertainty=True`).
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_calibration_uncertainty_disabled_reports` ile kalibrasyon yürütmesi, kalibrasyon uyumu, kalibrasyon dönüşümü, olasılık tahmini ve belirsizlik yürütmesinin engellendiğini belgeleyen 5 bağımsız denetim raporu üretilir.
- **Yer Tutucular ve Metrikler**: `python -m scripts.run_calibration_uncertainty_placeholders` ile güven puanı (3), güven aralığı (3), tahmin aralığı (3), kuantil (5), konformal tahmin (3), metrikler (ECE, Brier, Sharpness) ve değerlendirme şablonları denetlenir (`all_uncalculated=True`, `all_unexecuted=True`).
- **Bağımlılıklar, Muhafızlar ve Girdiler**: `python -m scripts.run_calibration_uncertainty_dependencies_inputs` ile Phase 136-140 bağımlılıkları, soykütüğü (lineage), deney bağlantıları, no-lookahead kuralları, yalnızca-metadata haber muhafızları, kaynak koruma ilkeleri ve yasaklı kolon politikaları denetlenir.
- **Bulgular, Manifest ve Phase 142 Devri**: `python -m scripts.run_calibration_uncertainty_findings_manifest` ile 3 yönetişim bulgusu, 7 maddelik manuel inceleme kuyruğu, 1.0 hazırlık skoru (`READY_FOR_PHASE_142_DRIFT_MONITORING_HANDOFF`) ve master Phase 141 manifestosu üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_calibration_uncertainty_health_check` ile 12 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Sınırı**: `python -m scripts.run_calibration_uncertainty_validation_report` ile 12 validasyon kuralının VALID olduğu, sıfır yasaklı iddia tespit edildiği ve 25 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_calibration_uncertainty_status` ile tam pipeline çalıştırılarak konsolide JSON ve Markdown raporları üretilir, Phase 142 devrine hazır olduğu teyit edilir.

## Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_model_drift_profile_registry` ile 3 drift profili (`balanced_local_model_drift_contracts`, `strict_non_executing_drift_safety`, `dry_run_linkage_governance_focus`) ve 59 operasyonel domain doğrulanır (`all_non_executing=True`, `all_zero_calculation=True`).
- **İzleme Sözleşmeleri**: `python -m scripts.run_drift_monitoring_contracts` ile 6 model drift sözleşmesi, 6 veri drift sözleşmesi, 6 öznitelik drift sözleşmesi, 3 kalibrasyon drift sözleşmesi, 3 belirsizlik drift sözleşmesi ve 3 tahmin dağılımı drift yer tutucusu denetlenir.
- **Bağlantı Sözleşmeleri (Linkages)**: `python -m scripts.run_drift_linkage_contracts` ile Phase 123 öznitelik kalite, Phase 124 FeatureStore ve Phase 126-135 rejim drift bağlantı sözleşmeleri doğrulanır.
- **Pencere ve Eşik Değer Politikaları**: `python -m scripts.run_drift_window_threshold_policies` ile referans, güncel ve kayan pencere politikaları ile PSI, KS, JS, Wasserstein eşik değer yer tutucuları denetlenir.
- **Metrik Yer Tutucuları (10 Kategori)**: `python -m scripts.run_drift_metric_placeholders` ile 10 kategoride hesaplanmamış drift metrik yer tutucuları kataloglanır (`all_uncalculated=True`).
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_drift_disabled_execution_reports` ile drift yürütmesi, drift metrik hesabı, canlı izleme/uyarı, yeniden eğitim tetikleyicisi, model değiştirme ve tahmin engellerini belgeleyen 6 bağımsız denetim raporu üretilir.
- **Bağımlılıklar, Girdiler ve Muhafızlar**: `python -m scripts.run_drift_dependencies_inputs` ile Phase 136-141 bağımlılıkları, girdi/çıktı sözleşmeleri, soykütüğü (lineage), deney bağlantıları, no-lookahead korumaları, yalnızca-metadata haber kuralları, kaynak koruma ilkeleri ve 24 yasaklı kolon denetlenir.
- **Bulgular, Manifest ve Phase 143 Devri**: `python -m scripts.run_drift_findings_manifest` ile 5 yönetişim bulgusu, 3 maddelik operatör inceleme kuyruğu, 100.0 hazırlık skoru (`READY_FOR_PHASE_143_EXPLAINABILITY_HANDOFF`), master Phase 142 manifestosu ve Phase 143 devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_model_drift_health_check` ile 12 bileşenli sağlık denetimi (12/12 HEALTHY) doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_model_drift_validation_report` ile 12 validasyon kuralının VALID olduğu, sıfır yasaklı iddia tespit edildiği ve 25 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum**: `python -m scripts.run_model_drift_status` ile tam pipeline çalıştırılarak konsolide JSON ve Markdown raporları üretilir, Phase 143 devrine hazır olduğu teyit edilir.

## Phase 143 Explainability and Feature Attribution Reports Operations
- **Ana Açıklanabilirlik Pipeline**: `python -m scripts.run_explainability_pipeline` ile tüm sözleşmeler, rapor şablonları, yer tutucular, engelleme raporları ve handoff paketi uçtan uca yürütülür (`contract_only_dry_run` modunda).
- **Öznitelik Atıf Sözleşmeleri**: `python -m scripts.run_feature_attribution_contracts` ile 8 atıf sözleşmesi (SHAP, LIME, Permütasyon, Integrated Gradients, PDP, ICE, Vekil Model, Neden Kodları) denetlenir.
- **SHAP Yer Tutucuları**: `python -m scripts.run_shap_placeholders` ile TreeSHAP ve KernelSHAP sözleşmeleri, arka plan örnekleme engelleri ve hesaplanmamış yer tutucular denetlenir.
- **LIME Yer Tutucuları**: `python -m scripts.run_lime_placeholders` ile LIME Tabular yer tutucuları ve sıfır pertürbasyon garantisi denetlenir.
- **Permütasyon Önem Derecesi Yer Tutucuları**: `python -m scripts.run_permutation_importance_placeholders` ile özellik karıştırma (shuffle) engelleri ve hesaplanmamış permütasyon yer tutucuları denetlenir.
- **PDP ve ICE Yer Tutucuları**: `python -m scripts.run_pdp_ice_placeholders` ile kısmi bağımlılık ve bireysel koşullu beklenti ızgara hesaplama engelleri denetlenir.
- **Vekil Model Yer Tutucuları**: `python -m scripts.run_surrogate_model_placeholders` ile karar ağacı vekil modellerinin sıfır eğitim ve sıfır çıkarım güvenceleri denetlenir.
- **Karşıgözlemsel Senaryo Yer Tutucuları**: `python -m scripts.run_counterfactual_placeholders` ile karşıgözlemsel optimizasyon ve arama engelleri denetlenir.
- **Drift Bağlantısı**: `python -m scripts.run_attribution_drift_linkage` ile Phase 142 drift izleme sözleşmeleri ile atıf kayması arasındaki izleme şablonları doğrulanır.
- **Phase 144 Devir Paketi**: `python -m scripts.run_phase_144_handoff` ile 8 maddelik devir önkoşulları doğrulanır, 1.0 hazırlık skoru ve Phase 144 devir sözleşmesi üretilir.

## Phase 144 Model Governance, Model Cards and Audit Trail Operations
- **Profil ve Alan Kayıtları**: `python -m scripts.run_model_governance_profile_registry` ile 3 model governance profili (`balanced_local_model_governance_contracts`, `strict_non_production_governance_safety`, `dry_run_model_cards_audit_focus`) ve 62 operasyonel domain doğrulanır.
- **Model Yönetişim Sözleşmeleri**: `python -m scripts.run_model_governance_contracts` ile 7 model sözleşmesi, 8 doğrulama kanıtı, 12 risk kaydı ve 12 kontrol kontrol listesi denetlenir.
- **Model Kartları ve Şablonları**: `python -m scripts.run_model_card_contracts` ile 7 model kartı sözleşmesi, 7 şablon, 12 standart bölüm, kısıtlamalar, amaçlanan ve yasaklı kullanımlar, risk açıklamaları ve 4 katmanlı bağımlılıklar incelenir.
- **Yönetişim Sınırları ve İnceleme Kapıları**: `python -m scripts.run_governance_boundaries` ile onay sınırları, yayınlama sınırları, üretim-dışı çalışma sınırları ve 9 insan inceleme kapısı denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_governance_disabled_execution_reports` ile 10 politikanın (model kayıt yazımı, model saklama, dağıtım, üretim onayı, broker hazır durumu, canlı işlem, tahmin, eğitim, sinyal, performans iddiası) engellendiği doğrulanır.
- **Bağımlılıklar, Muhafızlar ve Köken**: `python -m scripts.run_governance_dependencies_guards` ile 7 faz bağımlılığı, geleceğe bakış muhafızları, salt-metadata haber kuralları, kaynak koruma ilkeleri, 37 yasaklı kolon ve soykütüğü (lineage) denetlenir.
- **Denetim İzi Yer Tutucuları**: `python -m scripts.run_governance_audit_trail` ile denetim izi, karar logları, değişiklik logları, sahip sorumlulukları, yaşam döngüsü ve sürüm geçmişi sözleşmeleri doğrulanır.
- **Bulgular, Puanlama ve Manifest**: `python -m scripts.run_governance_findings_manifest` ile 4 yönetişim bulgusu, 10 manuel inceleme maddesi, 1.0 hazırlık skoru ve ModelGovernanceManifest üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_model_governance_health_check` ile 17 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon Raporu**: `python -m scripts.run_model_governance_validation_report` ile validasyon kurallarının VALID olduğu ve temiz iddialar içerdiği teyit edilir.
- **Genel Durum ve Phase 145 Devri**: `python -m scripts.run_model_governance_status` ile tam pipeline çalıştırılarak 10 bileşenin durumu listelenir ve Phase 145 (Advanced ML Acceptance Report) devir statüsü (`READY_FOR_PHASE_145`) teyit edilir.

## Phase 145 Advanced ML Acceptance Report and Consolidated Acceptance Layer Operations
- **Profil ve Alan Kayıtları**: `python -m scripts.run_advanced_ml_acceptance_profile_registry` ile 3 kabul profili (`balanced_local_advanced_ml_acceptance`, `strict_safety_governance_acceptance`, `dry_run_audit_acceptance`), 30 domain tanımı ve 16 kapsam maddesi denetlenir.
- **Bileşen Kabul ve Kontrol Noktaları**: `python -m scripts.run_advanced_ml_component_acceptance` ile bloktaki 10 bileşen (`Phase136` - `Phase145`) ve 10 kontrol noktası denetimi gerçekleştirilir.
- **Konsolide Faz Kabul Denetimi (Phases 136-144)**: `python -m scripts.run_advanced_ml_phase_acceptance` ile Phase 136'dan Phase 144'e kadar olan 9 fazın her biri için 8 kabul kuralı (toplam 72 kural) doğrulanır (%100 PASSED).
- **Bağımlılıklar, Kanıtlar ve Sınırlar**: `python -m scripts.run_advanced_ml_dependency_evidence` ile 14 faz bağımlılığı, 12 doğrulama kanıtı ve 11 güvenlik sınırı denetlenir.
- **Sınırlar, Kapılar, Engeller, Boşluklar ve Bulgular**: `python -m scripts.run_advanced_ml_boundaries_findings` ile 7 üretim-dışı çalışma kuralı, 10 operatör manuel inceleme kapısı, 15 Go/No-Go kuralı, 0 blocker, 2 gap, 7 uyarı ve 3 bulgu denetlenir.
- **Kabul Manifestosu ve Phase 146 Devri**: `python -m scripts.run_advanced_ml_acceptance_manifest` ile 1.00 hazırlık skoru (`advanced_ml_contract_acceptance_ready_non_production`), master kabul manifestosu ve Phase 146 (Realistic Backtest, Transaction Cost and Slippage Modeling) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_advanced_ml_acceptance_health_check` ile 18 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_advanced_ml_acceptance_validation_report` ile 18 kuralın VALID olduğu, sıfır yasaklı iddia tespit edildiği ve 34 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_advanced_ml_acceptance_status` ile tam pipeline çalıştırılarak 44 rapor ve çıktı dosyası üretilir, Phase 146 devir hazırlığı (`READY_FOR_PHASE_146`) teyit edilir.

## Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling Operations
- **Profil ve Alan Defterleri**: `python -m scripts.run_realistic_backtest_profile_registry` ile 3 operasyonel profil (`balanced_local_realistic_backtest`, `strict_non_executing_backtest_safety`, `dry_run_backtest_contracts_focus`), 68 etki alanı, 18 kapsam öğesi ve 12 gerçekçi varsayım denetlenir.
- **Backtest Motor Sözleşmeleri**: `python -m scripts.run_backtest_engine_contracts` ile 6 motor sözleşmesi (event-driven, vectorized, portfolio arayüzleri ve veri/özellik/sinyal girdi/çıktı sözleşmeleri) doğrulanır.
- **İşlem Maliyeti ve Kayma Modelleri**: `python -m scripts.run_backtest_execution_cost_models` ile emir simülasyonu (8 emir türü), fill modelleri (8 kural), komisyon modelleri (5 model), borsa ücret modelleri (6 model), spread modelleri (6 model), kayma modelleri (6 model) ve 6 gerçekçilik yer tutucusu denetlenir.
- **Muhasebe ve Yaşam Döngüsü**: `python -m scripts.run_backtest_accounting_lifecycle` ile PnL muhasebesi, nakit/pozisyon takibi, kaldıraç/teminat, işlem ve pozisyon durum makineleri, kurumsal eylemler, döviz dönüşümü ve 12 metrik yer tutucusu doğrulanır.
- **Bias ve Geleceğe Bakış Muhafızları**: `python -m scripts.run_backtest_bias_guards` ile zaman dilimi hizalaması (UTC/DST), no-lookahead koruması (`direction='backward'`), hayatta kalma yanlılığı, veri gözetleme, aşırı uyum, salt-metadata haber kuralları, kaynak koruma ilkeleri ve 40 yasaklı kolon karantinası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_backtest_disabled_execution_reports` ile 9 engelleme politikasının (motor yürütme, optimizasyon, walk-forward, benchmark, canlı işlem, aracı kurum iletimi, model eğitimi, model tahmini, performans iddiaları) engellendiğini belgeleyen denetim raporları üretilir.
- **Bulgular, Manifest ve Phase 147 Devri**: `python -m scripts.run_backtest_findings_manifest` ile 12 yukarı akış bağımlılığı, 10 doğrulama kanıtı, 8 manuel inceleme maddesi, 3 bulgu, 1.00 hazırlık skoru (`READY_FOR_PHASE_147_WALK_FORWARD_HANDOFF`), master bütünlük manifestosu ve Phase 147 devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_realistic_backtest_health_check` ile 18 alt sistem denetiminin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_realistic_backtest_validation_report` ile 18 kuralın VALID olduğu, sıfır yasaklı iddia tespit edildiği ve 35 NO-GO / 10 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_realistic_backtest_status` ile 11 aşamalı master pipeline çalıştırılarak 50+ rapor ve veri seti üretilir, Phase 147 devir hazırlığı (`READY_FOR_PHASE_147`) teyit edilir.

## Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking Operations
- **Profil ve Kapsam Kayıtları**: `python -m scripts.run_walk_forward_profile_registry` ile 3 operasyonel doğrulama profili (`balanced_local_walk_forward_validation_contracts`, `strict_safety_walk_forward_contracts`, `dry_run_oos_benchmark_contracts`), 35 etki alanı ve 18 kapsam öğesi doğrulanır.
- **Walk-Forward ve Split Sözleşmeleri**: `python -m scripts.run_walk_forward_split_contracts` ile rolling, expanding, anchored, purged walk-forward sözleşmeleri, purge/embargo politikaları, train/val/test/OOS sınırları, mühürlü holdout dönemleri, rejim duyarlı ve çapraz varlık test sözleşmeleri doğrulanır.
- **Out-of-Sample Benchmark Sözleşmeleri**: `python -m scripts.run_oos_benchmark_contracts` ile Emtia ve FX benchmark evrenleri, Buy & Hold, nakit (SOFR), eşit ağırlıklı sepet (1/N), rejim geçişli ve maliyet duyarlı 5 referans strateji yer tutucusu denetlenir.
- **Doğrulama ve Benchmark Metrik Yer Tutucuları**: `python -m scripts.run_validation_metric_placeholders` ile Alpha, Beta, IR, Tracking Error, Return, MaxDD, Sharpe, Sortino, Calmar, Win Rate ve fold stabilite metrik yer tutucuları ve çıktı sözleşmeleri doğrulanır (`all_uncalculated=True`).
- **Yanlılık ve Sızıntı Muhafızları**: `python -m scripts.run_validation_bias_guards` ile no-lookahead zaman/kolon muhafızı, purge/embargo muhafızları, data snooping bias, aşırı uyum (overfitting), hayatta kalma yanlılığı, çoklu hipotez testi, salt-metadata haber kuralları, kaynak dokunulmazlığı ve 34 yasaklı kolon karantinası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_validation_disabled_execution_reports` ile walk-forward simülasyonu, benchmark simülasyonu, metrik hesaplama, optimizasyon, model eğitimi, model tahmini, canlı işlem, broker iletimi ve getiri iddialarının engellendiğini belgeleyen 9 resmi denetim raporu üretilir.
- **Bulgular, Manifest ve Hazırlık Skoru**: `python -m scripts.run_walk_forward_findings_manifest` ile 9 doğrulama kanıtı, 7 operatör manuel inceleme maddesi, 3 yönetişim bulgusu, 1.00 hazırlık skoru (`walk_forward_oos_contract_ready_non_production`), master Phase 147 manifestosu ve Phase 148 devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_walk_forward_health_check` ile 9 alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon Raporu**: `python -m scripts.run_walk_forward_validation_report` ile 6 validasyon kuralının VALID/PASS olduğu ve sıfır yasaklı iddia tespit edildiği doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_walk_forward_status` ile 8 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 148 (Stress Testing and Scenario Simulation) devir hazırlığı (`phase_148_handoff_ready=True`) teyit edilir.

## Phase 148 Stress Testing and Scenario Simulation Operations
- **Profil ve Kapsam Kayıtları**: `python -m scripts.run_stress_testing_profile_registry` ile 3 operasyonel stres testi profili (`balanced_local_stress_testing_contracts`, `strict_safety_stress_contracts`, `dry_run_scenario_simulation_contracts`), 35 etki alanı ve 18 kapsam öğesi doğrulanır.
- **Senaryo Sözleşmeleri ve Kütüphanesi**: `python -m scripts.run_stress_scenario_contracts` ile Tarihsel Kriz Senaryoları (2008 GFC, 2020 COVID, 2022 Emtia/Enflasyon Şoku), Hipotetik Senaryolar, Ters Stres Testi (Reverse Stress Testing) ve Rejim Geçiş Şoku sözleşmeleri incelenir.
- **Şok Yer Tutucuları ve Taksonomisi**: `python -m scripts.run_stress_shock_placeholders` ile Piyasa Şoku, Volatilite Şoku, Likidite Şoku, Spread Genişlemesi, Gap/Kopuş Riski ve Korelasyon Çöküşü yer tutucuları denetlenir (`all_uncalculated=True`).
- **Stres Metrik Yer Tutucuları**: `python -m scripts.run_stress_metric_placeholders` ile Stressed PnL, Stressed VaR (%95/%99), Expected Shortfall (CVaR), Max Drawdown, Toparlanma Süresi ve Stressed Sharpe yer tutucuları ve formül sözleşmeleri incelenir (`execution_blocked=True`).
- **Bağımlılıklar, Girdiler ve Muhafızlar**: `python -m scripts.run_stress_dependencies_guards` ile Phase 146 ve 147 bağımlılıkları, no-lookahead zaman muhafızı, senaryo sızıntı koruması, veri gözetleme muhafızı, hayatta kalma yanlılığı denetleyicisi, salt-metadata haber kuralları, kaynak dokunulmazlığı ve 36 yasaklı kolon karantinası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_stress_disabled_execution_reports` ile stres testi simülasyonu, senaryo yürütmesi, Monte Carlo yürütmesi, optimizasyon, model eğitimi, model tahmini, canlı işlem, broker iletimi ve getiri iddialarının engellendiğini belgeleyen 9 resmi denetim raporu üretilir.
- **Bulgular, Manifest ve Phase 149 Devri**: `python -m scripts.run_stress_findings_manifest` ile 9 doğrulama kanıtı, 7 operatör manuel inceleme maddesi, 3 yönetişim bulgusu, 1.00 hazırlık skoru (`stress_testing_contract_ready_non_production`), master Phase 148 manifestosu ve Phase 149 (Monte Carlo Robustness and Parameter Stability) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_stress_testing_health_check` ile 10 alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_stress_testing_validation_report` ile 8 validasyon kuralının VALID/PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 14 NO-GO / 7 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_stress_testing_status` ile 8 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 149 devir hazırlığı (`phase_149_handoff_ready=True`) teyit edilir.

## Phase 149 Monte Carlo Robustness and Parameter Stability Operations
- **Profil ve Kapsam Kayıtları**: `python -m scripts.run_monte_carlo_profile_registry` ile 3 operasyonel Monte Carlo profili (`balanced_local_monte_carlo_robustness_contracts`, `conservative_local_monte_carlo_robustness_contracts`, `institutional_local_monte_carlo_robustness_contracts`), 10 etki alanı ve 5 kapsam öğesi doğrulanır.
- **Sağlamlık ve Bootstrap Sözleşmeleri**: `python -m scripts.run_monte_carlo_contracts` ile Standart IID bootstrap, otokorelasyon koruyucu blok bootstrap, durağan geometrik blok bootstrap, getiri yolu yeniden örnekleme ve işlem sırası permütasyon sözleşmeleri doğrulanır.
- **Yeniden Örnekleme ve Pertürbasyon Yer Tutucuları**: `python -m scripts.run_monte_carlo_resampling_placeholders` ile artık yeniden örnekleme, gürültü enjeksiyonu ve yol pertürbasyon yer tutucuları denetlenir (`all_unexecuted=True`).
- **Parametre Stabilitesi ve Duyarlılık Sözleşmeleri**: `python -m scripts.run_parameter_stability_contracts` ile strateji parametre tedirginlik aralıkları, duyarlılık esneklikleri, grid stabilite yer tutucuları, parametre yüzey / plato analizleri ve kırılganlık tespit sözleşmeleri denetlenir (`all_optimizations_disabled=True`).
- **Zarf ve Metrik Yer Tutucuları**: `python -m scripts.run_monte_carlo_metric_placeholders` ile üst/alt zarf sınırları, stabilite bantları, %90/%95/%99 güven aralıkları, azami drawdown, getiri ve kuyruk riski (VaR, Beklenen Kayıp) yer tutucuları doğrulanır (`all_uncalculated=True`).
- **Bağımlılıklar ve Muhafızlar**: `python -m scripts.run_monte_carlo_dependencies_guards` ile Phase 146-148 bağlantıları, no-lookahead muhafızı, yeniden örnekleme sızıntı koruması, veri gözetleme muhafızı, aşırı uyum denetleyicisi, salt-metadata haber kuralları, kaynak dokunulmazlığı ve 34 yasaklı kolon karantinası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_monte_carlo_disabled_execution_reports` ile Monte Carlo simülasyonu, bootstrap, parametre optimizasyonu, parametre taraması, metrik hesaplama, model eğitimi, model tahmini, canlı işlem, broker iletimi ve getiri iddialarının engellendiğini belgeleyen 10 resmi denetim raporu üretilir.
- **Bulgular, Manifest ve Phase 150 Devri**: `python -m scripts.run_monte_carlo_findings_manifest` ile 7 operatör manuel inceleme maddesi, 3 yönetişim bulgusu, 1.00 hazırlık skoru (`monte_carlo_robustness_contract_ready_non_production`), master Phase 149 manifestosu ve Phase 150 (Backtest Governance and Bias Control) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_monte_carlo_health_check` ile 8 alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_monte_carlo_validation_report` ile 5 validasyon kuralının VALID/PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 14 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
## Phase 150 Backtest Governance and Bias Control Operations
- **Profil ve Kapsam Kayıtları**: `python -m scripts.run_backtest_governance_profile_registry` ile 3 operasyonel yönetişim profili (`balanced_local_backtest_governance`, `conservative_local_backtest_governance`, `institutional_local_backtest_governance`), 27 etki alanı ve 16 kapsam unsuru doğrulanır.
- **Yönetişim Sözleşmeleri**: `python -m scripts.run_backtest_governance_contracts` ile Phase 146-149 çıktılarını bağlayan 7 çekirdek yönetişim sözleşmesi (`CONTRACT_DEFINITIONS`) doğrulanır.
- **Yanlılık Kontrolleri**: `python -m scripts.run_backtest_bias_controls` ile 11 yanlılık kontrol sözleşmesi (Lookahead, Survivorship, Data Snooping, Overfitting, Multiple Testing, Parameter Fishing, Benchmark Selection, Regime Coverage, Sample Coverage, Transaction Cost Realism, Slippage Realism) denetlenir.
- **Sonuç ve Metrik İddia Sınırları**: `python -m scripts.run_backtest_result_boundaries` ile metrik iddia engelleme sınırları, performans iddia engelleme sınırları, 6 zorunlu rapor açıklama bölümü ve sonuç yayınlama kısıtları doğrulanır.
- **Gerçekçilik ve Doğrulama Bölümleme Yönetişimi**: `python -m scripts.run_backtest_realism_governance` ile komisyon/ücret gerçekçiliği, kayma ve piyasa etkisi, fill modeli ve kuyruk önceliği, likidite ve ADV kısıtları, zaman damgası monotonik bütünlüğü, kronolojik bölme, walk-forward OOS kilitleri, stres ve Monte Carlo yönetişim bağlantıları doğrulanır.
- **Politikalar, Kapılar ve Veri Muhafızları**: `python -m scripts.run_backtest_governance_guards` ile denetim politikaları, kanıt politikaları, 10 insan onay kapısı, Go/No-Go sınırları, zorunlu feragatnameler, kaynak dokunulmazlığı muhafızı, metadata-only haber muhafızı ve 40 yasaklı kolon politikası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_backtest_governance_disabled_execution_reports` ile backtest yürütme, sonuç iddiaları, metrik hesaplama, optimizasyon, model eğitimi, tahmin üretimi, canlı işlem, broker iletimi ve üretim dağıtımının engellendiğini belgeleyen 9 resmi denetim raporu üretilir.
- **Bulgular, Manifest ve Phase 151 Devri**: `python -m scripts.run_backtest_governance_findings_manifest` ile 5 doğrulama kanıtı, 8 operatör inceleme maddesi, 3 yönetişim bulgusu, 1.00 hazırlık skoru (`backtest_governance_contract_ready_non_production`), master Phase 150 manifestosu ve Phase 151 (Benchmark Comparison and Strategy Evaluation Contracts) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_backtest_governance_health_check` ile 8 alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_backtest_governance_validation_report` ile 5 validasyon kuralının PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 10 NO-GO / 3 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_backtest_governance_status` ile 11 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 151 devir hazırlığı (`phase_151_handoff_ready=True`) teyit edilir.

## Phase 151 Benchmark Comparison and Strategy Evaluation Reports Operations
- **Profil ve Kapsam Kayıtları**: `python -m scripts.run_benchmark_evaluation_profile_registry` ile 3 operasyonel değerlendirme profili (`balanced_local_benchmark_evaluation_contracts`, `conservative_local_benchmark_evaluation_contracts`, `institutional_local_benchmark_evaluation_contracts`), 36 etki alanı ve 16 araştırma kapsamı doğrulanır.
- **Benchmark Rapor Sözleşmeleri**: `python -m scripts.run_benchmark_report_contracts` ile benchmark karşılaştırma, referans evren ve baseline (Buy & Hold, Nakit Risksiz Faiz, Sepet) sözleşmeleri incelenir.
- **Strateji Değerlendirme Sözleşmeleri**: `python -m scripts.run_strategy_evaluation_report_contracts` ile strateji değerlendirme, göreli karşılaştırma, maliyet/kayma düzeltmeli, rejim duyarlı, walk-forward, OOS, stres, Monte Carlo, stabilite, yönetişim, yanlılık ve açıklama sözleşmeleri incelenir.
- **Değerlendirme Özet Yer Tutucuları**: `python -m scripts.run_evaluation_summary_placeholders` ile 11 hesaplanmamış özet şablonu ve yasal feragatnameler denetlenir.
- **Metrik Yer Tutucuları**: `python -m scripts.run_evaluation_metric_placeholders` ile strateji, benchmark, göreli, risk düzeltmeli, maliyet düzeltmeli ve sağlamlık metrik yer tutucuları doğrulanır (`all_uncalculated=True`, `actual_value=None`).
- **Bağımlılıklar, Veri Girişleri ve Muhafızlar**: `python -m scripts.run_evaluation_dependencies_guards` ile Phase 146-150 bağımlılıkları, veri giriş sözleşmeleri, no-lookahead, sonuç/performans iddia engelleme, strateji onayı engelleme, yanlılık muhafızları ve 40 yasaklı kolon politikası denetlenir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_evaluation_disabled_execution_reports` ile 11 resmi devre dışı yürütme raporu (benchmark simülasyonu, strateji değerlendirmesi, metrik hesaplama, sonuç iddiaları, strateji onayı, optimizasyon, model eğitimi, tahmin üretimi, canlı işlem, broker emir iletimi ve dağıtım) incelenir.
- **Bulgular, Manifest ve Phase 152 Devri**: `python -m scripts.run_benchmark_evaluation_findings_manifest` ile 10 operatör manuel inceleme maddesi, 3 teşhis bulgusu, 1.00 hazırlık skoru (`benchmark_evaluation_contract_ready_non_production`), master Phase 151 manifestosu ve Phase 152 (Backtest Acceptance Report) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_benchmark_evaluation_health_check` ile 11 alt sistem bileşeninin tümünün HEALTHY olduğu teyit edilir.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_benchmark_evaluation_validation_report` ile tüm validasyon kontrollerinin PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 15 NO-GO / 7 SAFE-GO kuralının SECURE durumda olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_benchmark_evaluation_status` ile 9 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 152 devir hazırlığı (`phase_152_handoff_ready=True`) teyit edilir.

## Phase 152 Backtest Acceptance Report Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_backtest_acceptance_profile_registry` ile 3 operasyonel kabul profili (`balanced_local_backtest_acceptance_contracts`, `strict_non_production_backtest_acceptance_safety`, `dry_run_phase_146_152_acceptance_focus`), 27 etki alanı ve 10 araştırma kapsamı doğrulanır.
- **Bileşenler ve Kontrol Noktaları**: `python -m scripts.run_backtest_acceptance_component_checkpoints` ile 7 bileşen (Phase 146-152) ve 7 kabul kontrol noktası denetlenir.
- **Faz Düzeyi Kabul Tescilleri**: `python -m scripts.run_backtest_phase_acceptance` ile Phase 146 (Realistic Backtest), Phase 147 (Walk-Forward), Phase 148 (Stress Testing), Phase 149 (Monte Carlo), Phase 150 (Backtest Governance) ve Phase 151 (Benchmark Evaluation) için 60 kontrolün tümü doğrulanır (60/60 PASS).
- **Bağımlılıklar, Kanıtlar ve Güvenlik Sınırları**: `python -m scripts.run_backtest_acceptance_dependencies_evidence` ile 11 yukarı akış bağımlılığı, 8 doğrulama kanıtı ve 12 güvenlik sınırı incelenir.
- **Sınırlar, Kapılar ve Bulgular**: `python -m scripts.run_backtest_acceptance_boundaries_findings` ile 5 non-production kuralı, 7 manuel inceleme kapısı, 22 Go/No-Go kuralı (4 Go, 18 No-Go), 0 engel, 0 boşluk, 8 uyarı ve 1 konsolide bulgu kayıt altına alınır.
- **Manifesto ve Hazırlık Skoru**: `python -m scripts.run_backtest_acceptance_manifest` ile 1.0000 hazırlık skoru (`backtest_acceptance_contract_ready_non_production`), master kabul manifestosu ve Phase 153 (Portfolio Construction, Position Sizing and Risk Budgeting) devir raporu üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_backtest_acceptance_health_check` ile 18 bileşenin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_backtest_acceptance_validation_report` ile 6 kontrolün VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 20 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_backtest_acceptance_status` ile genel kabul durumu konsolide edilir ve Phase 153 devir hazırlığı (`phase_153_handoff_ready=True`) teyit edilir.

## Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_portfolio_construction_profile_registry` ile 3 operasyonel portföy inşa profili (`balanced_local_portfolio_construction_contracts`, `conservative_portfolio_risk_budgeting_safety`, `institutional_governed_allocation_contracts`), 36 etki alanı ve 16 araştırma kapsamı doğrulanır.
- **Portföy, Evren ve Giriş Sözleşmeleri**: `python -m scripts.run_portfolio_construction_contracts` ile 12 portföy sözleşmesi, 10 Emtia-Döviz varlığı evreni, 6 varlık uygunluk kuralı, 5 sinyal giriş ve 5 risk girdi spesifikasyonu denetlenir.
- **Pozisyon Boyutlandırma Şablonları ve Yer Tutucuları**: `python -m scripts.run_position_sizing_contracts` ile 9 pozisyon boyutlandırma şablonu (Fixed Fractional, Volatility Targeting, Risk Parity, Drawdown-Aware, Confidence-Aware, Regime-Aware, Correlation-Aware, Liquidity-Aware, Cost/Slippage Aware) ve yer tutucu çıktıları doğrulanır (`is_placeholder=True`, gerçek lot/boyut hesaplanmaz).
- **Risk Bütçeleme Şablonları ve Yer Tutucuları**: `python -m scripts.run_risk_budget_contracts` ile 9 risk bütçeleme şablonu (Varlık, Strateji, Rejim, Portföy, Drawdown, Volatilite, Exposure) ve yer tutucu çıktıları denetlenir (`is_placeholder=True`, gerçek bütçe tahsis edilmez).
- **Limitler ve Kısıt Yer Tutucuları**: `python -m scripts.run_portfolio_limits_placeholders` ile 10 limit modülü (Konsantrasyon, Brüt/Net Exposure, Kaldıraç, Marjin, Nominal Değer, Para Birimi, Çapraz Varlık, Sektör, Korelasyon, Likidite) ve yer tutucu metrikleri doğrulanır (`actual_weight=None`).
- **Bağımlılıklar, Kanıtlar ve Muhafızlar**: `python -m scripts.run_portfolio_dependencies_guards` ile 5 yukarı akış bağımlılığı (Phase 152, 151, 145, 140, 130), 8 doğrulama kanıtı ve 11 muhafız kontrolü tescil edilir.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_portfolio_disabled_execution_reports` ile 11 resmi yürütme yasağı raporu (portföy inşası, boyutlandırma, bütçeleme, optimizasyon, metrik hesaplama, canlı işlem, broker iletimi vb.) üretilir.
- **Bulgular, Manifest ve Phase 154 Devri**: `python -m scripts.run_portfolio_findings_manifest` ile 10 operatör manuel inceleme maddesi, 3 teşhis bulgusu, 1.0000 hazırlık skoru (`portfolio_construction_contract_ready_non_production`), master portföy bütünlük manifestosu ve Phase 154 (Portfolio Optimization Contracts) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_portfolio_construction_health_check` ile 18 bileşenin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_portfolio_construction_validation_report` ile 6 kontrolün VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 20 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_portfolio_construction_status` ile 9 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 154 devir hazırlığı (`phase_154_handoff_ready=True`) teyit edilir.

## Phase 154 Portfolio Optimization and Allocation Constraints Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_portfolio_optimization_profile_registry` ile 3 operasyonel portföy optimizasyon profili (`balanced_local_portfolio_optimization_contracts`, `strict_non_production_portfolio_optimization_safety`, `dry_run_phase_154_optimization_contracts_focus`), 26 etki alanı ve 4 araştırma kapsamı doğrulanır.
- **Portföy Optimizasyon Sözleşmeleri**: `python -m scripts.run_portfolio_optimization_contracts` ile 11 optimizasyon sözleşmesi (Mean-Variance, Min-Variance, Max-Sharpe, Risk-Parity, CVaR, Drawdown, Turnover, Cost, Slippage, Regime, Robust) incelenir.
- **Optimizasyon Amaç Fonksiyonu Sözleşmeleri ve Yer Tutucuları**: `python -m scripts.run_optimization_objective_contracts` ile 11 amaç fonksiyonu formül ve şema metaverileri doğrulanır (`is_placeholder=True`, gerçek optimizasyon hesabı yapılmaz).
- **Tahsisat Kısıt Sözleşmeleri ve Yer Tutucuları**: `python -m scripts.run_allocation_constraint_contracts` ile 22 tahsisat kısıt sözleşmesi ve yer tutucusu (Long-only, Ağırlıklar, Gruplar, Yoğunlaşma, Maruziyetler, Korelasyon, Likidite, Turnover, Maliyet, Risk Bütçesi, Volatilite, Drawdown, Kaldıraç, Teminat, Rebalance) denetlenir (`is_enforced_live=False`).
- **Çözücüler ve Etkin Sınır Yer Tutucuları**: `python -m scripts.run_optimization_solver_placeholders` ile konveks ve sezgisel çözücü yer tutucuları, grid search yasağı ve etkin sınır yer tutucusu denetlenir (`zero_solvers_executed=True`).
- **Çıktılar ve Metrik Yer Tutucuları**: `python -m scripts.run_optimization_outputs_metrics` ile optimizasyon sonuç, sermaye tahsisat, yeniden dengeleme çıktı sözleşmeleri ve 8 metrik yer tutucusu incelenir (`contains_actual_weights=False`).
- **Bağımlılıklar, Muhafızlar ve Politikalar**: `python -m scripts.run_optimization_dependencies_guards` ile 6 yukarı akış bağımlılığı (Phase 153, 152, 151, 145, 135, 134), 12 muhafız kontrolü ve 52 yasaklı kolon karantina politikası doğrulanır.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_optimization_disabled_execution_reports` ile 10 resmi yürütme yasağı raporu (optimizasyon, ağırlık üretimi, tahsisat üretimi, yeniden dengeleme, metrik hesaplama, model eğitimi, tahmin, canlı trading, broker iletimi, dağıtım) incelenir.
- **Bulgular, Manifest ve Phase 155 Devri**: `python -m scripts.run_portfolio_optimization_findings_manifest` ile 3 teşhis bulgusu, 1.0000 hazırlık skoru (`portfolio_optimization_contract_ready_non_production`), master portföy optimizasyon manifestosu ve Phase 155 (Portfolio Risk Monitoring, Exposure Attribution and Limit Enforcement Contracts) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_portfolio_optimization_health_check` ile 19 bileşenin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_portfolio_optimization_validation_report` ile 7 kontrolün VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 18 NO-GO / 8 SAFE-GO kuralının SECURE durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_portfolio_optimization_status` ile 9 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 155 devir hazırlığı (`phase_155_handoff_ready=True`) teyit edilir.

## Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_risk_reporting_profile_registry` ile 4 operasyonel risk raporlama profili (`balanced_local_risk_reporting_contracts`, `conservative_risk_reporting_contracts`, `institutional_risk_reporting_contracts`, `audit_risk_reporting_contracts`), 28 etki alanı ve 15 araştırma kapsamı doğrulanır.
- **Risk Rapor Sözleşmeleri**: `python -m scripts.run_risk_report_contracts` ile 9 risk rapor sözleşmesi ve özetleri (günlük risk, çapraz varlık exposure, emtia-döviz limitleri, düşüş, volatilite, VaR/ES, yoğunlaşma, likidite-kaldıraç, maliyet) incelenir (`is_placeholder=True`, gerçek rapor yürütmesi yapılmaz).
- **Exposure Attribution Sözleşmeleri**: `python -m scripts.run_exposure_attribution_contracts` ile 10 exposure sözleşmesi ve 13 yer tutucu (brüt, net, long/short, döviz, çapraz varlık, yoğunlaşma, likidite, kaldıraç, marjin, nominal, rejim, strateji, varlık) doğrulanır (`actual_exposure_calculated=None`).
- **Limit İzleme Sözleşmeleri**: `python -m scripts.run_limit_monitoring_contracts` ile limit tanım sözleşmesi ve 9 limit izleme sözleşmesi (exposure, yoğunlaşma, kaldıraç, marjin, likidite, düşüş, volatilite, turnover, risk bütçesi) denetlenir (`is_enforced_live=False`).
- **Risk İzleme ve Katkı Yer Tutucuları**: `python -m scripts.run_risk_monitor_placeholders` ile 3 risk katkı ve 7 risk izleme yer tutucusu (Drawdown, Volatilite, VaR, ES, Turnover, Maliyet, Slippage) formül metaverileriyle incelenir.
- **Çıktılar ve Metrik Yer Tutucuları**: `python -m scripts.run_risk_reporting_outputs_metrics` ile risk rapor, exposure attribution, limit izleme çıktı sözleşmeleri ve 4 metrik yer tutucusu denetlenir.
- **Bağımlılıklar, Muhafızlar ve Politikalar**: `python -m scripts.run_risk_reporting_dependencies_guards` ile 13 yukarı akış bağımlılığı (Phase 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 135, 134), 12 muhafız kontrolü ve 48 yasaklı kolon karantina politikası doğrulanır.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_risk_reporting_disabled_execution_reports` ile 12 resmi yürütme yasağı raporu (risk raporu yürütmesi, exposure attribution yürütmesi, limit izleme yürütmesi, metrik hesaplama, limit alarmları, dashboard üretimi, portföy düzeltmesi/rebalance, model eğitimi, tahmin, canlı trading, broker iletimi, dağıtım) incelenir.
- **Bulgular, Manifest ve Phase 156 Devri**: `python -m scripts.run_risk_reporting_findings_manifest` ile 3 teşhis bulgusu, 4 operatör manuel inceleme maddesi, 1.0000 hazırlık skoru (`risk_reporting_contract_ready_non_production`), master risk rapor bütünlük manifestosu ve Phase 156 (Portfolio Scenario Testing and Drawdown Control) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_risk_reporting_health_check` ile 21 bileşenin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_risk_reporting_validation_report` ile 5 kontrolün VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 25 NO-GO / 21 SAFE-GO kuralının ACTIVE durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_risk_reporting_status` ile 10 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 156 devir hazırlığı (`phase_156_handoff_ready=True`) teyit edilir.

## Phase 156 Portfolio Scenario Testing and Drawdown Control Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_portfolio_scenario_control_profile_registry` ile 4 operasyonel profil (`balanced_local_portfolio_scenario_control_contracts`, `conservative_portfolio_scenario_control_contracts`, `institutional_portfolio_scenario_control_contracts`, `audit_portfolio_scenario_control_contracts`), 30 etki alanı ve 18 araştırma kapsamı doğrulanır.
- **Portföy Senaryo Testi Sözleşmeleri ve Şok Kütüphanesi**: `python -m scripts.run_portfolio_scenario_testing_contracts` ile tarihsel krizler (2008 GFC, 2020 COVID, 2022 Emtia), hipotetik şoklar, rejim geçişleri, volatilite sıçraması, likidite daralması, korelasyon çöküşü, kur şoku, spread, maliyet ve slippage şok sözleşmeleri incelenir (`is_placeholder=True`, gerçek simülasyon yapılmaz).
- **Drawdown Kontrol ve Kurtarma Sözleşmeleri**: `python -m scripts.run_drawdown_control_contracts` ile drawdown eşik sözleşmeleri, uyarı yer tutucuları, ihlal yer tutucuları, toparlanma planları ve kontrol politikaları denetlenir (`is_enforced_live=False`).
- **Portföy Kontrol Aksiyon Yer Tutucuları**: `python -m scripts.run_portfolio_control_placeholders` ile 7 portföy kontrol aksiyon yer tutucusu (exposure azaltma, de-risking, hedge, rebalance, stop, dondurma, sürdürme) incelenir (`actual_action_taken=False`).
- **Çıktılar ve Metrik Yer Tutucuları**: `python -m scripts.run_scenario_control_outputs_metrics` ile senaryo çıktı, drawdown çıktı, dayanıklılık çıktı sözleşmeleri ve 5 metrik yer tutucusu denetlenir.
- **Bağımlılıklar, Muhafızlar ve Politikalar**: `python -m scripts.run_scenario_control_dependencies_guards` ile 10 yukarı akış bağımlılığı (Phase 155, 154, 153, 152, 148, 149, 145, 144, 135, 134), 14 muhafız kontrolü ve 52 yasaklı kolon karantina politikası doğrulanır.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_scenario_control_disabled_execution_reports` ile 14 resmi yürütme yasağı raporu (senaryo testi, drawdown kontrol, portföy aksiyon, hedge/de-risk, rebalance, metrik hesaplama, alarmlar, dashboard, model eğitimi, tahmin, canlı trading, broker iletimi, dağıtım) incelenir.
- **Bulgular, Manifest ve Phase 157 Devri**: `python -m scripts.run_portfolio_scenario_findings_manifest` ile 3 teşhis bulgusu, 5 operatör manuel inceleme maddesi, 1.0000 hazırlık skoru (`portfolio_scenario_control_contract_ready_non_production`), master senaryo kontrol bütünlük manifestosu ve Phase 157 (Portfolio Acceptance Report) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_portfolio_scenario_control_health_check` ile 24 bileşenin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_portfolio_scenario_control_validation_report` ile 5 kontrolün VALIDATION_PASS olduğu, sıfır yasaklı iddia tespit edildiği ve 28 NO-GO / 24 SAFE-GO kuralının ACTIVE durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_portfolio_scenario_control_status` ile 10 aşamalı master pipeline çalıştırılarak tüm raporlar üretilir ve Phase 157 devir hazırlığı (`phase_157_handoff_ready=True`) teyit edilir.

## Phase 157 Portfolio Acceptance Report Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_portfolio_acceptance_profile_registry` ile 3 operasyonel portföy kabul profili (`balanced_local_portfolio_acceptance_contracts`, `conservative_portfolio_acceptance_contracts`, `institutional_portfolio_acceptance_contracts`), 25 etki alanı ve 14 operasyonel araştırma kapsamı doğrulanır.
- **Bileşen Kayıt ve Kontrol Noktaları**: `python -m scripts.run_portfolio_acceptance_component_checkpoints` ile Phase 153-157 arası 5 bileşenin modül, script, test, manifest, validasyon raporu ve güvenlik sınırları denetlenir (`contract_only=True`, `non_production=True`).
- **Faz Düzeyi Kabul Tescilleri**: `python -m scripts.run_portfolio_phase_acceptance` ile Phase 153 (Portfolio Construction), Phase 154 (Portfolio Optimization), Phase 155 (Risk Reporting) ve Phase 156 (Portfolio Scenario Testing and Drawdown Control) fazlarının 40 kabul kriteri eksiksiz denetlenir ve onaylanır.
- **Bağımlılık, Kanıt ve Güvenlik Kayıtları**: `python -m scripts.run_portfolio_acceptance_dependencies_evidence` ile 16 yukarı akış bağımlılığı, 8 doğrulama kanıtı ve 12 güvenlik kuralı doğrulanır.
- **Üretim Dışı Sınırlar, İnceleme Kapıları, Karar Ağacı ve Bulgular**: `python -m scripts.run_portfolio_acceptance_boundaries_findings` ile 7 üretim dışı değişmezi, 5 operatör manuel inceleme kapısı, 4 GO kuralı, 26 NO-GO kuralı, 25 potansiyel engel (0 aktif), 7 potansiyel boşluk (0 açık), 13 yönetişim uyarısı ve 2 kabul bulgusu denetlenir.
- **Hazırlık Skoru, Ana Manifesto ve Phase 158 Devir Raporu**: `python -m scripts.run_portfolio_acceptance_manifest` ile 0.9500 hazırlık skoru (`portfolio_acceptance_contract_ready_non_production`), master portföy kabul manifestosu, konsolide Markdown raporu ve Phase 158 (Full-System Integration and Advanced Acceptance Rehearsal) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_portfolio_acceptance_health_check` ile 20 alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_portfolio_acceptance_validation_report` ile 5 kuralın VALIDATION_PASS olduğu, sıfır yasaklı iddia bulunduğu ve 29 NO-GO / 8 SAFE-GO kuralının SAFETY_BOUNDARY_ENFORCED durumda olduğu teyit edilir.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_portfolio_acceptance_status` ile 9 aşamalı master pipeline çalıştırılarak tüm kabul raporları üretilir ve Phase 158 devir hazırlığı (`phase_158_handoff_ready=True`) teyit edilir.

## Phase 158 Full-System Integration and Advanced Acceptance Rehearsal Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_full_system_integration_profile_registry` ile 3 operasyonel tam sistem kabul profili (`balanced_local_full_system_integration_contracts`, `strict_non_production_system_integration_safety`, `dry_run_acceptance_rehearsal_focus`), 34 etki alanı ve 20 araştırma kapsamı doğrulanır.
- **Sistem Bileşenleri ve Bağımlılık Haritası**: `python -m scripts.run_system_component_registry` ile tüm mimariyi kapsayan 36 bileşen (`CMP-001` - `CMP-036`), 32 yönlü mimari bağımlılık ilişkisi (`DEP-001` - `DEP-032`) ve 13 kontrol noktası (`CHK-001` - `CHK-013`) denetlenir.
- **Sözleşme, Manifesto ve Kanıt Entegrasyonu**: `python -m scripts.run_system_contract_integration` ile 11 sözleşme grubu (`CNT-001` - `CNT-011`), 13 entegre alt sistem manifestosu (`MNF-INT-001` - `MNF-INT-013`) ve 8 sistem doğrulama kanıtı incelenir.
- **İleri Düzey Kabul Provası**: `python -m scripts.run_advanced_acceptance_rehearsal` ile 11 kabul provası maddesi (`REH-158-001` - `REH-158-011`) ve 8 prova kontrol noktası canlı yürütme olmadan tüm alt sistemlerin yapılandırma, import güvenliği ve manifesto bütünlüğünü doğrular (%100 REHEARSED & PASSED).
- **Sistem Sınırları ve Manuel İnceleme Kapıları**: `python -m scripts.run_system_boundaries` ile 18 güvenlik kuralı, 6 non-production kuralı, 5 dry-run kuralı, 10 operatör manuel inceleme kapısı ve 52 yasaklı kolon politikası doğrulanır.
- **Devre Dışı Bırakılmış Yürütme Raporları**: `python -m scripts.run_system_disabled_execution_reports` ile 13 resmi yürütme yasağı raporu (tam sistem yürütmesi, canlı trading, broker yürütmesi, üretim dağıtımı, model eğitimi, model tahmini, backtest, portföy, risk, senaryo, emir üretimi, sinyal üretimi ve yatırım tavsiyesi) incelenir.
- **Bulgular, Hazırlık Skoru, Master Manifesto ve Phase 159 Devri**: `python -m scripts.run_system_integration_findings_manifest` ile 20 potansiyel engel (0 aktif), 1.0000 hazırlık skoru (`full_system_integration_contract_ready_non_production`), `FSI-MANIFEST-PHASE-158` master manifestosu ve Phase 159 (Final Hardening, Operator Runbook and Release Candidate) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_full_system_integration_health_check` ile 34 alt sistem modülü ve dizininin tümünün HEALTHY olduğu doğrulanır.
- **Genel Durum Konsolidasyonu**: `python -m scripts.run_full_system_integration_status` ile 9 aşamalı master pipeline çalıştırılarak tüm kabul raporları üretilir ve Phase 159 devir hazırlığı (`handoff_ready=True`, `status=ACCEPTED`) teyit edilir.

## Phase 159 Final Hardening, Operator Runbook and Release Candidate Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_final_hardening_profile_registry` ile 3 operasyonel sertleştirme profili (`balanced_local_final_hardening_contracts`, `strict_non_production_hardening_safety`, `dry_run_release_candidate_focus`), 34 etki alanı ve 20 araştırma kapsamı doğrulanır.
- **Sertleştirme ve Sözleşme Tescili**: `python -m scripts.run_final_hardening_contracts` ile 9 sertleştirme sözleşmesi, 10 operatör çalıştırma sözleşmesi ve 5 release candidate sözleşmesi doğrulanır.
- **Operatör Kılavuzları (Runbooks)**: `python -m scripts.run_operator_runbook_contracts` ile başlatma (`system_startup_verification`), kapatma (`graceful_offline_shutdown`), konfigürasyon (`offline_configuration_audit`), veri (`local_data_integrity_check`), rapor (`offline_report_inspection`), sağlık (`subsystem_health_audit`), teşhis (`diagnostic_and_troubleshooting`), kurtarma (`safe_state_recovery`), NO-GO protokolü (`no_go_violation_handling`), manuel inceleme (`manual_review_sign_off`) ve güvenli kullanım (`safe_offline_usage_rules`) prosedürleri denetlenir.
- **Release Candidate Kontrol Listeleri**: `python -m scripts.run_release_candidate_checklists` ile 16 doğrulama kontrol listesi (`RC-CHK-01` - `RC-CHK-16`), bileşen, bağımlılık, validasyon, güvenlik ve dokümantasyon kontrolleri çalıştırılır (%100 READY).
- **Dondurma ve Konfigürasyon Denetimleri**: `python -m scripts.run_final_freeze_audits` ile konfigürasyon, dokümantasyon, güvenlik, doğrulama, bağımlılık, manifesto ve rapor dondurma sözleşmeleri ile ayar, ortam şablonu ve dizin denetimleri incelenir.
- **Sistem Envanterleri**: `python -m scripts.run_final_inventory_reports` ile betik, test, doküman, rapor, depolama, bileşen, engellenmiş işlem, güvenlik sınırı ve inceleme kapısı envanterleri çıkarılır.
- **Sınırlar ve Kurallar**: `python -m scripts.run_release_candidate_boundaries` ile 16 NO-GO kuralı ve 16 SAFE-GO kuralının tam olarak uygulandığı teyit edilir.
- **Bulgular, Hazırlık Skoru, Master Manifesto ve Phase 160 Devri**: `python -m scripts.run_release_candidate_findings_manifest` ile 0 aktif engel, 0 açık boşluk, onaylanmış uyarılar, 0.9500 hazırlık skoru, `MNF-159-RELEASE-CANDIDATE-001` manifestosu ve Phase 160 (Full Advanced Bot Final Delivery) devir paketi üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_final_hardening_health_check` ile 24 fiziksel alt sistem bileşeninin tümünün HEALTHY olduğu doğrulanır.
- **Validasyon ve Güvenlik Raporu**: `python -m scripts.run_final_hardening_validation_report` ile 6 validasyon kontrolünün VALIDATION_PASS olduğu ve 32 NO-GO kuralının SAFETY_BOUNDARY_ENFORCED durumda olduğu teyit edilir.
- **Konsolide Release Candidate Durumu**: `python -m scripts.run_release_candidate_status` ile master pipeline çalıştırılarak konsolide release candidate durumu (`release_candidate_contract_ready`) ve Phase 160 devir hazırlığı (`phase_160_handoff_ready=True`) teyit edilir.

## Phase 160 Full Advanced Bot Final Delivery and Plan Closure Operations
- **Profil, Alan ve Kapsam Kayıtları**: `python -m scripts.run_final_delivery_profile_registry` ile 3 teslimat profili (`balanced_local_final_delivery_package`, `strict_non_production_final_delivery_package`, `dry_run_audit_delivery_package`), 12 etki alanı ve 5 araştırma kapsamı doğrulanır.
- **Teslimat Paketi Sözleşmeleri**: `python -m scripts.run_final_delivery_package_contracts` ile 4 teslimat sözleşmesi (`FDC-CONTRACT-001` - `FDC-CONTRACT-004`) ve 20+ sistem bileşeni doğrulanır.
- **Sistem Envanterleri**: `python -m scripts.run_final_delivery_inventory` ile modül (50+), script (12), test (55+), dokümantasyon (15+), rapor (12+), DataLake (20+) ve FeatureStore (15+) envanterleri derlenir.
- **Kabul ve Kanıt Kayıtları**: `python -m scripts.run_final_delivery_evidence` ile kabul, manifest, doğrulama, güvenlik, kısıtlı çalıştırma, manuel gözden geçirme, runbook ve release candidate kanıtları doğrulanır.
- **160 Faz Haritası ve Blok Özetleri**: `python -m scripts.run_final_delivery_phase_summaries` ile 1-160 Faz Haritası, MVP 1-100 özeti, Advanced 101-160 özeti, Backtest, Portfolio ve Full-System blok özetleri ile nihai devir paketi üretilir.
- **Güvenlik Sınırları ve No-Go Denetimi**: `python -m scripts.run_final_delivery_boundaries` ile 16 No-Go kuralı, 16 Go kuralı, genel güvenlik sınırları ve yasaklı kolon politikaları doğrulanır.
- **Engellenmiş İşlem Raporları**: `python -m scripts.run_final_delivery_disabled_execution_reports` ile 14 resmi devre dışı bırakılmış işlem raporu incelenir.
- **Bulgular, Hazırlık Skoru ve Master Manifest**: `python -m scripts.run_final_delivery_findings_manifest` ile 0 blocker, 0 gap, 100.0/100.0 hazırlık skoru ve `FDM-MANIFEST-PHASE-160` master teslimat manifestosu üretilir.
- **Sistem Sağlık Kontrolü**: `python -m scripts.run_final_delivery_health_check` ile tüm alt sistem bileşenlerinin ve dizinlerinin HEALTHY olduğu doğrulanır.
- **Validasyon Raporu**: `python -m scripts.run_final_delivery_validation_report` ile tüm doğrulama kurallarının VALIDATION_PASS olduğu teyit edilir.
- **Nihai Teslimat Durumu Panosu**: `python -m scripts.run_final_delivery_status` ile konsolide teslimat durumu (`FULL_ADVANCED_BOT_FINAL_DELIVERY_READY`) görüntülenir.
- **Resmi 160-Faz Kapanış Raporu**: `python -m scripts.run_final_160_phase_completion_report` ile 160 fazlık planın resmi kapanış beyanı (`final_plan_closed=True`, `next_phase=None`) üretilir.
