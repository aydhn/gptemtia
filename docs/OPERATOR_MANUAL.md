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





