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


## Advanced Config Profile System (Phase 104)
- Research mode nasıl seçilir? research_mode_presets üzerinden seçilir.
- Universe profile ne işe yarar? Hangi varlıkların taranacağını belirler.
- Timeframe profile nasıl yorumlanır? Sinyallerin zaman aralığını simüle eder.
- Risk preference neden gerçek risk yönetimi değildir? Sadece simülasyon ve araştırma amaçlıdır.
- ML profile neden deployment değildir? Offline çalışır.
- Portfolio profile neden gerçek portföy emri değildir? Broker emri üretmez.
- Safety profile neden zorunludur? Canlı işlemi ve scraping'i önlemek içindir. Scraping kesinlikle yapılmaz.


## Phase 106 Configuration
- Phase 106 provider tercihleri config profillerine nasıl bağlanır? Phase 104 profile registry üzerinden.
- No-scraping provider preference nasıl yorumlanır? Sadece allowed pattern'lar (API, manual file, cache) desteklenir.
- Manual file import, local cache, official API adapter ve licensed provider adapter farkları tanımlanmıştır.
- Provider credential'larının output'a yazılmaması esastır.
- Provider profile'ın gerçek veri indirme izni olmadığı garanti edilmiştir.



## Phase 106 Provider Configuration
- Provider type nasıl seçilir? (provider_registry içinden)
- dry_run_fixture_provider ne işe yarar? (Gerçek API çağırmadan sahte veri üretir)
- manual_file_provider placeholder nasıl yorumlanır? (Dosya silmez/taşımaz, sadece placeholder)
- local_cache_provider placeholder nasıl yorumlanır? (Sadece cache simülasyonu)
- official_api_provider_placeholder neden gerçek API çağrısı değildir? (Sadece placeholder, network call yapmaz)
- licensed_provider_placeholder neden credential istemez? (Credential policy gereği sadece manual review önerir)
- no-scraping provider preference nasıl uygulanır? (Preference resolver ile)
- credential output neden yasaktır? (Güvenlik sınırları gereği)



## Phase 107 FX Configuration
- FX provider profile nasıl seçilir? `DEFAULT_FX_PROVIDER_PROFILE` env vars ile seçilir.
- FX pair universe nasıl yorumlanır? Major, minor, exotic olarak ayrılır. Sinyal değildir.
- major/minor/exotic pair farkları: İşlem hacmi ve likiditeye göre.
- FX symbol normalization nasıl çalışır? Broker/Provider sembollerini `XXX/YYY` canonical formuna getirir.
- FX quote/OHLCV schema ne işe yarar? Çekilecek veri sözleşmesini tanımlar.
- Cross-rate requirements neden kesin fiyat üretmez? Spread ve slippage içerir.
- FX dry-run fixture provider ne işe yarar? Gerçek API çağırmadan sahte veriyle testi sağlar.
- FX official API placeholder neden gerçek API çağrısı değildir? Yalnızca contract ve adapter arayüzü sunar.
- FX licensed provider placeholder neden credential istemez? Çünkü no-scraping ve offline test boundary altındadır.
- no-scraping FX provider preference nasıl uygulanır? Profil özellikleriyle varsayılan yapılır.
- credential output neden yasaktır? Güvenlik (secrets hygiene) gereği.


### Phase 108 Commodities Configuration
- Commodity provider profile nasıl seçilir? `settings.py` içinden `default_commodity_provider_profile` ile.
- Commodity universe nasıl yorumlanır? Emtia evreni sinyal değil, tanım listesidir.
- Precious metals / energy / industrial metals / agriculture farkları `CommodityCategory` ile ayrılır.
- XAU/XAG neden FX currency değil commodity olarak tutulur? Çakışmaları önlemek için.
- Commodity symbol normalization nasıl çalışır? Provider-spesifik semboller canonical form'a (`XAU/USD` vs) döner.
- Commodity spot/OHLCV schema ne işe yarar? Çıktı standartlarını belirler.
- Futures contract metadata neden execution değildir? Yalnızca tanımlayıcıdır.
- Continuous contract requirements neden gerçek continuous seri üretmez? Sadece kuralları tanımlar (Phase 113 için).
- Roll-adjustment requirements neden sinyal değildir? Fiyat uyarlamasını tanımlar.
- Commodity dry-run fixture provider ne işe yarar? Gerçek API çağırmadan sistemi test etmeyi sağlar.
- Commodity official API placeholder neden gerçek API çağrısı değildir? Offline geliştirme içindir.
- Commodity licensed provider placeholder neden credential istemez? Güvenlik (no credential output) kuralı gereği.
- no-scraping commodity provider preference nasıl uygulanır? Provider resolver üzerinden uygulanır.
- credential output neden yasaktır? Secrets hygiene kuralı.

Phase 109 Macro Provider Configuration
## Phase 110 Calendar Provider Config
- `advanced_economic_calendar_enabled=true`
- `default_calendar_provider_profile="balanced_no_scraping_calendar_provider"`
- `calendar_provider_allow_web_scraping=false`

## Phase 111 News Metadata Provider Config
- `advanced_news_metadata_enabled=true`
- `default_news_provider_profile="balanced_no_scraping_news_metadata_provider"`
- `news_provider_current_phase=111`
- `news_provider_next_phase=112`
- `news_provider_target_final_phase=160`
- `news_provider_dry_run_default=true`
- `news_provider_local_only=true`
- `news_provider_non_production=true`
- `news_provider_research_only=true`
- `news_provider_allow_web_scraping=false`
- `news_provider_allow_news_page_scraping=false`
- `news_provider_allow_html_scraping=false`
- `news_provider_allow_full_article_download=false`
- `news_provider_allow_copyrighted_article_copy=false`
- `news_provider_allow_sentiment_as_signal=false`
- `news_provider_allow_live_trading=false`
- `news_provider_allow_broker_integration=false`

## Phase 112 Data Quality Engine Configuration
- `advanced_data_quality_enabled=true`: Phase 112 veri kalite kontrol motorunu etkinleştirir.
- `default_data_quality_profile="balanced_local_data_quality"`: Varsayılan veri kalitesi profilini belirler (seçenekler: `balanced_local_data_quality`, `strict_data_quality_safety`, `dry_run_quality_contract_focus`).
- `data_quality_current_phase=112`: Mevcut faz numarası.
- `data_quality_next_phase=113`: Normalizasyon katmanı için bir sonraki faz.
- `data_quality_target_final_phase=160`: Nihai hedef faz.
- `data_quality_dry_run_default=true`: Gerçek disk ezmesi olmadan kuru çalıştırma modu.
- `data_quality_local_only=true`: Yalnızca yerel çalışma kısıtı.
- `data_quality_non_production=true`: Üretim dışı geliştirme/araştırma koruması.
- `data_quality_research_only=true`: Araştırma ve doğrulama kısıtı.
- `data_quality_allow_live_trading=false`: Canlı emir iletimi kesinlikle kapalı.
- `data_quality_allow_broker_integration=false`: Broker entegrasyonu kapalı.
- `data_quality_allow_auto_overwrite_cleaning=false`: Otomatik veri silme/ezme kesinlikle kapalı.
- `data_quality_allow_credential_output=false`: Credential loglama/çıktılama kapalı.
- `data_quality_allow_web_scraping=false`: Web scraping kesinlikle yasak.
- `data_quality_enable_schema_compliance_rules=true`: Şema uygunluk kurallarını etkinleştirir.
- `data_quality_enable_missing_data_rules=true`: Eksik veri kurallarını etkinleştirir.
- `data_quality_enable_stale_data_rules=true`: Bayat/gecikmiş veri kurallarını etkinleştirir.
- `data_quality_enable_duplicate_data_rules=true`: Mükerrer kayıt kurallarını etkinleştirir.
- `data_quality_enable_outlier_placeholder_rules=true`: İstatiksel aykırı değer kurallarını etkinleştirir.
- `data_quality_enable_timestamp_integrity_rules=true`: Zaman damgası kurallarını etkinleştirir.
- `data_quality_enable_frequency_unit_rules=true`: Frekans ve birim uyumluluk kurallarını etkinleştirir.
- `data_quality_enable_news_copyright_rules=true`: Telif hakkı ve tam metin sınır kurallarını etkinleştirir.

## Phase 113 Data Normalization Layer Configuration

### 1. Data Normalization Profili Nasıl Seçilir?
- `ADVANCED_DATA_NORMALIZATION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_DATA_NORMALIZATION_PROFILE="balanced_non_destructive_normalization"`: Varsayılan dengeli kural seti.
- Seçenekler:
  - `balanced_non_destructive_normalization`: Tüm dönüştürme ve kanonik kural setlerini dengeli çalıştırır.
  - `strict_non_destructive_normalization_safety`: Güvenlik ve kaynak koruma eşiklerini daha sıkı denetler (`min_score=0.65`).
  - `dry_run_normalization_contract_focus`: Sentetik ve sözleşme dataframe'leri üzerinde şema uygunluk testlerine odaklanır.

### 2. Non-Destructive Normalization Ne Anlama Gelir?
- Normalizasyon işlemleri asla kaynak veriyi (`raw_df`) in-place değiştirmez, silmez veya üzerine yazmaz.
- Tüm operasyonlar `df.copy()` üzerinden yürütülür ve dönüştürülmüş değerler `normalized_<field>` olarak yeni sütunlara yazılır.
- Orijinal sütunlar (örneğin `pair`, `timestamp`, `unit`) veri kaybını önlemek için korunur.

### 3. Normalized View/Copy/Report Kaynak Veriden Nasıl Ayrılır?
- Orijinal veri `data/raw/` veya sağlayıcı kaynak dizininde dokunulmadan kalır.
- Normalize edilmiş görünümler `data/lake/advanced_data_normalization/normalized_views/` altına ayrı dosya olarak yazılır.
- `NormalizedViewManifest` tablosu kaynak dosya URI'si (`original_ref`) ile normalize edilmiş dosya URI'si (`normalized_ref`) arasındaki bağlantıyı açıkça kaydeder.

### 4. Canonical Schema Registry Nasıl Kullanılır?
- FX quote/OHLCV, emtia spot/OHLCV/futures metadata, makro zaman serisi, ekonomik takvim ve haber metadata için 12 merkezi şema tanımlanmıştır.
- Her şemanın birincil anahtarları (`primary_key_fields`), zaman alanı (`timestamp_field`) ve sağlayıcı alanı (`provider_field`) sabittir.

### 5. Symbol/Indicator/Event/Tag Normalization Nasıl Çalışır?
- **FX**: `EURUSD` veya `EUR_USD` girdilerini ISO standart `EUR/USD` slash formatına çevirir.
- **Commodity**: `GOLD` girdisini `XAU/USD`'ye, `CL` girdisini `WTI_CRUDE_CONTINUOUS_PLACEHOLDER`'a eşler.
- **Macro**: `US10Y` -> `US_10Y_YIELD`, `FEDFUNDS` -> `FED_POLICY_RATE`.
- **Calendar**: `FOMC` -> `FOMC_RATE_DECISION`, `NFP` -> `US_NONFARM_PAYROLLS_RELEASE`.
- **News**: `central bank` -> `CENTRAL_BANK`, `crude oil` -> `CRUDE_OIL`.
- Eşleşmeyen veya şüpheli semboller manual review gerektiren bulgu olarak işaretlenir.

### 6. Timestamp/Timezone Normalization Neden UTC Canonical Kullanır?
- Farklı veri sağlayıcılarının farklı saat dilimlerini (EST, GMT, UTC, Europe/Istanbul) tekilleştirmek için ISO 8601 UTC kanonik depolama standardı kullanılır.
- Orijinal zaman damgası korunurken, `normalized_timestamp` alanında UTC formatı saklanır.

### 7. Frequency/Unit Normalization Neden Değer Dönüşümü Garantisi Değildir?
- Bu fazda veri değerleri birim çarpanıyla (ör. barrel'den tona) dönüştürülmez; yalnızca birim kelime hazinesi (`unit vocabulary`) standartlaştırılır (`USD/barrel` -> `usd_per_barrel`, `%` -> `percent`).
- Değer dönüşümleri ve revizyon politikaları Phase 114 lineage ve Phase 115 benchmark sonrasına bırakılmıştır.

### 8. Duplicate Key Normalization Neden Kayıt Silmez?
- Kayıt silme (`deduplication`) yıkıcı (`destructive`) bir işlemdir.
- Phase 113'te yalnızca bileşik kanonik anahtar (`canonical_duplicate_key`) üretilir ve mükerrer kayıtlar etiketlenerek Phase 114 ve Phase 115'e raporlanır.

### 9. Manual Review Normalization Queue Nasıl Kullanılır?
- Standart sözlüğe uymayan veya otomatik dönüştürülemeyen anomaliler `manual_review_normalization_queue`'ya eklenir.
- Her kuyruk kaydı `destructive_action_allowed: False` ve `source_preserved: True` garantisi taşır.

### 10. Normalization Score Neden Sinyal veya Official Approval Değildir?
- Normalization score (0.0 - 1.0) ceza bazlı iç teşhis metriğidir.
- Kesinlikle al/sat sinyali, finansal tavsiye veya sistemin canlıya uygun olduğuna dair resmi onay değildir.

### 11. Phase 114 Lineage/Provenance Handoff Nasıl Kullanılır?
- Phase 113'te gerçekleşen her alan düzeyindeki dönüştürme kuralı, kaynak sütun ve hedef kanonik sütun ilişkisi `Phase 114 Handoff` raporuna kaydedilir.
- Phase 114 Data Lineage katmanı bu raporu okuyarak uçtan uca veri soy kütüğü grafiğini inşa eder.

## Phase 114 Data Lineage and Provenance Configuration

### 1. Data Lineage Profili Nasıl Seçilir?
- `ADVANCED_DATA_LINEAGE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_DATA_LINEAGE_PROFILE="balanced_local_lineage_provenance"`: Varsayılan dengeli soy kütüğü profili.
- Seçenekler:
  - `balanced_local_lineage_provenance`: Tüm kaynak, sağlayıcı, veri seti ve dönüşüm soy kütüğünü yerel ve dengeli olarak izler.
  - `strict_lineage_provenance_safety`: Güvenlik, telif ve izlenebilirlik eşiklerini daha sıkı denetler (`min_score=0.65`).
  - `dry_run_lineage_contract_focus`: Sentetik ve sözleşme fikstürleri üzerinde soy kütüğü sözleşmelerine odaklanır.

### 2. Source-to-Normalized Lineage Nasıl Çalışır?
- Orijinal ham veri referansı (`SourceReference`) ile Phase 113 tarafından üretilen normalize görünüm (`NormalizedOutputLineage`) arasında birebir bağlantı kurulur.
- Hiçbir kaynak dosya üzerine yazılmaz veya silinmez (`source_preserved: True`, `destructive_action_allowed: False`).

### 3. Provider Provenance Registry Nasıl Yapılandırılır?
- Phase 106-111 arasındaki sağlayıcılar (`advanced_data_providers`, `advanced_fx_providers`, `advanced_commodity_providers`, `advanced_macro_providers`, `advanced_economic_calendar`, `advanced_news_metadata`) kayıt defterinde listelenir.
- Her sağlayıcının yetenekleri, lisans notları ve veri modları izlenir.

### 4. License ve Copyright Boundary Provenance Neden Önemlidir?
- Haber metadata kayıtlarında telif hakları korunarak tam metin indirme kesin olarak engellenir (`contains_full_text: False`, `metadata_only: True`).
- Sağlayıcı referanslarında hiçbir zaman API anahtarı veya şifre loglanmaz (`contains_credentials: False`).

### 5. Audit Trail Event Registry Nasıl Çalışır?
- Veri kayıt, şema uyumlama, alan dönüştürme ve manuel inceleme kararları değişmez denetim izi olayları olarak saklanır.
- Yıkıcı eylemlere izin verilmez (`destructive_action_allowed: False`).

### 6. Traceability ve Provenance Skorları Nasıl Yorumlanır?
- 0.0 - 1.0 aralığında üretilen skorlar tamamen sistem içi veri kalitesi ve izlenebilirlik teşhisidir.
- Kesinlikle al/sat sinyali, yatırım tavsiyesi veya resmi onay değildir.

### 7. Lineage Graph Placeholder Nedir?
- Harici bir grafik veya vektör veritabanı (Neo4j, Chroma vb.) kurulmaz.
- Soy kütüğü düğümleri ve kenarları bellek içi pandas tabloları olarak modellenir.

### 8. Phase 115 Provider Benchmark Handoff Nasıl Kullanılır?
- Phase 114, sağlayıcı ve veri seti izlenebilirlik ve kalite metriklerini konsolide ederek Phase 115 Data Provider Benchmark raporuna devir girdisi olarak aktarır.

## Phase 115 Data Provider Benchmark Report Configuration

### 1. Data Provider Benchmark Profili Nasıl Seçilir?
- `ADVANCED_PROVIDER_BENCHMARK_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_PROVIDER_BENCHMARK_PROFILE="balanced_local_provider_benchmark"`: Varsayılan dengeli benchmark profili.
- Seçenekler:
  - `balanced_local_provider_benchmark`: FX, emtia, makro, takvim ve haber sağlayıcılarını dengeli ağırlıklarla karşılaştırır.
  - `strict_provider_benchmark_safety`: Güvenlik, telif ve sıfır-scraping eşiklerini daha sıkı denetler (`min_benchmark_score=0.65`).
  - `dry_run_provider_benchmark_focus`: Sözleşme fikstürleri ve yerel çıktılar üzerinde dry-run testlerine odaklanır.

### 2. Benchmark Metrikleri ve Ağırlıkları Nasıl Yapılandırılır?
- 10 temel metrik kullanılır: `metric_coverage`, `metric_capability`, `metric_quality`, `metric_normalization`, `metric_traceability`, `metric_license_provenance`, `metric_no_scraping_compliance`, `metric_metadata_only_compliance`, `metric_manual_review_load`, `metric_cross_domain_consistency`.
- Her domain için toplam ağırlık 1.0 olacak şekilde dengelenmiştir (`provider_benchmark_weight_registry.py`).

### 3. Provider Benchmark Score Neden Sinyal veya Resmi Onay Değildir?
- Skorlar [0.0, 1.0] aralığında ceza ağırlıklı araştırma metriğidir.
- Kesinlikle trade/alım-satım sinyali, yatırım tavsiyesi, resmi akreditasyon veya production/broker hazır olma iddiası değildir (`official_approval: False`, `production_ready: False`, `broker_ready: False`).

### 4. Non-Scraping ve Metadata-Only İlkeleri Nasıl Denetlenir?
- `provider_no_scraping_compliance.py` ve `provider_metadata_only_compliance.py` modülleri ile sıfır scraping ve sıfır haber tam metni kuralı %100 oranında denetlenir.

### 5. Phase 116 Feature/Factor Engine Handoff Nasıl Kullanılır?
- Phase 115, Phase 116 gösterge ve faktör motoruna veri hazırlık gereksinimlerini aktarır (`phase_116_handoff.py`). Gösterge veya sinyal üretmez.

## Phase 116 Advanced Indicator/Feature/Factor Engine Configuration

### 1. Feature Engine Profili Nasıl Seçilir?
- `ADVANCED_FEATURE_ENGINE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FEATURE_ENGINE_PROFILE="balanced_local_feature_engine"`: Varsayılan dengeli feature motoru profili.
- Seçenekler:
  - `balanced_local_feature_engine`: Fiyat, trend, momentum, volatilite ve ortalamaya dönüş göstergelerini dengeli hesaplama bütçesiyle çalıştırır.
  - `strict_non_signal_feature_engine_safety`: Non-signal ve lookahead bias sınırlarını en katı biçimde denetler (`strict_safety: True`).
  - `dry_run_feature_contract_focus`: Kanonik girdi sözleşmeleri ve şema doğrulama odaklı offline test profili.

### 2. Güvenlik ve Non-Signal Ayarları
- `FEATURE_ENGINE_ALLOW_FEATURE_AS_SIGNAL=false`: Hiçbir gösterge değeri al/sat sinyali veya trade kararı olarak kullanılamaz.
- `FEATURE_ENGINE_ALLOW_INDICATOR_DIRECTIONAL_CLAIM=false`: "RSI düşük -> al" gibi yönlü kurallar kesinlikle yasaktır.
- `FEATURE_ENGINE_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `FEATURE_ENGINE_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılmaz.
- `FEATURE_ENGINE_ALLOW_OPTIMIZER_EXECUTION=false`: Parametre optimizasyonu engellenir.
- `FEATURE_ENGINE_ALLOW_LIVE_TRADING=false`: Canlı emir ve broker API çağrıları kesinlikle kapalıdır.

### 3. Yasaklı Kolon Adı Doğrulaması
- `FEATURE_ENGINE_FORBIDDEN_SIGNAL_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation"`: Bu kolon adlarının feature DataFrame'lerinde yer alması validasyon hatası fırlatır.

### 4. Standart Rolling Pencereler ve Isınma (Warmup) Politikası
- Standart pencereler: `[5, 10, 14, 20, 50, 100, 200]`.
- Isınma periyodundaki ilk `window - 1` satırdaki NaN değerler maskelenir; sentetik dolgu veya tahmin yapılmaz.

### 5. Phase 117 Handoff
- Phase 116, Phase 117 Technical Indicator Expansion katmanına 8 devir başlığı ile temiz temel sağlar (`phase_117_handoff.py`).

## Phase 117 Technical Indicator Expansion Configuration

### 1. Technical Indicator Profili Nasıl Seçilir?
- `ADVANCED_TECHNICAL_INDICATORS_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_TECHNICAL_INDICATORS_PROFILE="balanced_local_technical_indicators"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_technical_indicators`: 12 indikatör ailesini standart pencerelerle dengeli hesaplar.
  - `strict_non_signal_indicator_safety`: Sıkı kolon adı ve lookahead denetimiyle güvenliği önceliklendirir.
  - `research_offline_indicator_focus`: Gelişmiş osilatör, oynaklık ve ortalamaya dönüş araştırmalarına odaklanır.

### 2. Güvenlik ve Non-Signal Ayarları
- `TECHNICAL_INDICATORS_ALLOW_INDICATOR_AS_SIGNAL=false`: İndikatör çıktılarının sinyal olarak kullanılması kesinlikle yasaktır.
- `TECHNICAL_INDICATORS_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü tahmin veya getiri beklentisi yasaktır.
- `TECHNICAL_INDICATORS_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `TECHNICAL_INDICATORS_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılmaz.
- `TECHNICAL_INDICATORS_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılmaz.
- `TECHNICAL_INDICATORS_ALLOW_LIVE_TRADING=false`: Canlı emir ve broker entegrasyonu yasaktır.

### 3. Yasaklı Kolon Adları
- `TECHNICAL_INDICATORS_FORBIDDEN_SIGNAL_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return"`: Bu kolonların üretimi anında hata fırlatır.
- MACD yumuşatma çizgisi için zorunlu isim: `macd_smooth`.

### 4. Isınma NaN Politikası ve TA-Lib Bağımsızlığı
- `TECHNICAL_INDICATORS_PRESERVE_WARMUP_NANS=true`: Başlangıç pencerelerindeki NaN değerler doldurulmaz veya silinmez.
- `TECHNICAL_INDICATORS_PURE_PYTHON_NUMPY=true`: Hesaplamalar TA-Lib gerektirmeyen saf Python/pandas/numpy matematik katmanıyla yürütülür.

### 5. Phase 118 Handoff
- Phase 117, Phase 118 Multi-Window Feature Grid katmanına parametrik kontratlar ve devir maddeleri sağlar (`phase_118_handoff.py`).

## Phase 118 Multi-Window Feature Grid Configuration

### 1. Multi-Window Feature Grid Profili Nasıl Seçilir?
- `ADVANCED_FEATURE_GRID_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FEATURE_GRID_PROFILE="balanced_local_multi_window_feature_grid"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_multi_window_feature_grid`: Tüm gösterge aileleri için standart kısa/orta/uzun pencere matrisini dengeli uygular.
  - `strict_no_signal_feature_grid_safety`: Sıkı kolon adı, negatif shift yasağı ve duplicate kontrolünü önceliklendirir.
  - `dry_run_feature_grid_computation_focus`: Sentetik prova ve hızlı bellek bütçeli grid hesaplamalarına odaklanır.

### 2. Güvenlik, Non-Signal ve Sınır Ayarları
- `FEATURE_GRID_CURRENT_PHASE=118`: Mevcut operasyon fazı.
- `FEATURE_GRID_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_GRID_NEXT_PHASE=119`: Sıradaki faz (Cross-Asset Feature Alignment).
- `FEATURE_GRID_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_GRID_LOCAL_ONLY=true`: Yalnızca yerel ortamda çalışma zorunluluğu.
- `FEATURE_GRID_RESEARCH_ONLY=true`: Yalnızca araştırma modu; canlı ticaret kesinlikle yasaktır.
- `FEATURE_GRID_ALLOW_FEATURE_GRID_AS_SIGNAL=false`: Grid değerlerinin al/sat sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_GRID_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü tahmin veya getiri iddiası yasaktır.
- `FEATURE_GRID_ALLOW_STRATEGY_GENERATION=false`: Ticaret stratejisi üretimi yasaktır.
- `FEATURE_GRID_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılamaz.
- `FEATURE_GRID_ALLOW_OPTIMIZER_EXECUTION=false`: Grid optimizasyonu çalıştırılamaz.
- `FEATURE_GRID_ALLOW_TARGET_LABEL_GENERATION=false`: Makine öğrenmesi target/label kolonları üretilemez.
- `FEATURE_GRID_ALLOW_PREDICTION_GENERATION=false`: Model tahmin kolonları üretilemez.
- `FEATURE_GRID_ALLOW_WEB_SCRAPING=false`: Web scraping ve HTML kazıma kesinlikle yasaktır.
- `FEATURE_GRID_ALLOW_CREDENTIAL_OUTPUT=false`: Gizli anahtar loglaması yasaktır.
- `FEATURE_GRID_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez.
- `FEATURE_GRID_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Veri silme veya otomatik temizlik yasaktır.

### 3. İsimlendirme, Lookahead ve Warmup NaN Ayarları
- `FEATURE_GRID_FORBIDDEN_SIGNAL_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return"`: Üretilen kolonlarda bu kelimelerin bulunması anında validasyon hatası fırlatır.
- `FEATURE_GRID_NAMING_STANDARD="lowercase_snake_case"`: Kolon adları `sma_w20`, `rsi_w14`, `bb_width_w20_std2` standardına uyar.
- `FEATURE_GRID_PRESERVE_WARMUP_NANS=true`: Büyük pencere ısınma NaN değerleri doldurulmaz veya silinmez.
- `FEATURE_GRID_NO_LOOKAHEAD_ENFORCED=true`: `shift(-1)` veya geleceğe dönük zaman kaydırmaları kesinlikle engellenir.

## Phase 119 Cross-Asset Feature Alignment Configuration

### 1. Cross-Asset Alignment Profili Nasıl Seçilir?
- `ADVANCED_CROSS_ASSET_ALIGNMENT_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_CROSS_ASSET_ALIGNMENT_PROFILE="balanced_local_cross_asset_alignment"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_cross_asset_alignment`: FX, emtia, makro, takvim ve haber metadata etki alanları arasında dengeli asof ve kova hizalaması uygular.
  - `strict_no_signal_cross_asset_safety`: Sıkı no-lookahead guard (`direction="backward"` zorunlu), yasaklı kolon denetimi ve sıfır hedef/tahmin kontrolünü önceliklendirir.
  - `dry_run_cross_asset_alignment_focus`: Hızlı bellek bütçeli sentetik veri ile etki alanları arası matris hizalama provasına odaklanır.

### 2. Güvenlik, Non-Signal ve Sınır Ayarları
- `CROSS_ASSET_ALIGNMENT_CURRENT_PHASE=119`: Mevcut operasyon fazı.
- `CROSS_ASSET_ALIGNMENT_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `CROSS_ASSET_ALIGNMENT_NEXT_PHASE=120`: Sıradaki faz (Macro/Calendar/News Feature Fusion & Composite Factor Engineering).
- `CROSS_ASSET_ALIGNMENT_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `CROSS_ASSET_ALIGNMENT_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma zorunluluğu.
- `CROSS_ASSET_ALIGNMENT_RESEARCH_ONLY=true`: Yalnızca araştırma modu; canlı işlem kesinlikle yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_ALIGNMENT_AS_SIGNAL=false`: Hizalama çıktılarının al/sat veya arbitraj sinyali olarak kullanımı kesinlikle yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_PAIRS_ARBITRAGE_SIGNALS=false`: İkili varlık (pairs trading) veya istatistiksel arbitraj sinyali üretimi yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü tahmin veya getiri iddiası yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_STRATEGY_GENERATION=false`: Ticaret stratejisi üretimi yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılamaz.
- `CROSS_ASSET_ALIGNMENT_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizatörler çalıştırılamaz.
- `CROSS_ASSET_ALIGNMENT_ALLOW_TARGET_LABEL_GENERATION=false`: Makine öğrenmesi target/label kolonları üretilemez.
- `CROSS_ASSET_ALIGNMENT_ALLOW_PREDICTION_GENERATION=false`: Model tahmin kolonları üretilemez.
- `CROSS_ASSET_ALIGNMENT_ALLOW_LIVE_TRADING=false`: Canlı emir iletimi kesinlikle yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_BROKER_SOCKET=false`: Aracı kurum soket veya canlı API bağlantısı yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi veya yönlendirmesi yapılamaz.
- `CROSS_ASSET_ALIGNMENT_ALLOW_WEB_SCRAPING=false`: Web scraping ve HTML kazıma kesinlikle yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_NEWS_FULL_TEXT=false`: Haber tam metin işleme yasaktır (`metadata_only: True`).
- `CROSS_ASSET_ALIGNMENT_ALLOW_CREDENTIAL_OUTPUT=false`: Gizli anahtar loglaması yasaktır.
- `CROSS_ASSET_ALIGNMENT_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez.
- `CROSS_ASSET_ALIGNMENT_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Veri silme veya otomatik temizlik yasaktır.

### 3. Namespace, Asof Join ve Zaman Damgası Standartları
- `CROSS_ASSET_ALIGNMENT_NAMESPACE_STANDARD="<domain>__<family>__<source_symbol>__<feature_name>__<window>"`: Çapraz etki alanı standart ad alanı biçimi (örn. `fx__momentum__eurusd__rsi__w14`, `commodity__trend__xauusd__sma__w20`).
- `CROSS_ASSET_ALIGNMENT_TIMESTAMP_STANDARD="ISO_8601_UTC"`: Bütün zaman damgaları UTC saat diliminde ve ISO 8601 standardında normalize edilir (`timestamp_utc`).
- `CROSS_ASSET_ALIGNMENT_DEFAULT_JOIN_POLICY="asof_backward"`: Zamansal birleştirmeler yalnızca geriye dönük (`direction="backward"`) olarak gerçekleştirilir; ileriye veya en yakın yönde birleştirme kesinlikle yasaktır.
- `CROSS_ASSET_ALIGNMENT_FORBIDDEN_SIGNAL_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return,spread_trade,arbitrage"`: Üretilen kolonlarda bu kelimelerin bulunması anında validasyon hatası fırlatır.
- `CROSS_ASSET_ALIGNMENT_NON_MUTATION_ENFORCED=true`: Veri setleri üzerinde in-place değişiklik yapılmaz; her adımda `df.copy()` güvencesi işletilir.
- `CROSS_ASSET_ALIGNMENT_NO_LOOKAHEAD_ENFORCED=true`: `shift(-1)` veya geleceğe dönük zaman kaydırmaları `no_lookahead_alignment_guard.py` ile kesin olarak engellenir.

### 4. Phase 120 Handoff
- Phase 119, Phase 120 Macro/Calendar/News Feature Fusion & Composite Factor Engineering katmanına çok alanlı hizalanmış özellik matrisi sözleşmelerini ve devir maddelerini devir eder (`phase_120_handoff.py`).

## Phase 120 Macro/Calendar/News Feature Fusion Configuration

### 1. Feature Fusion Profili Nasıl Seçilir?
- `ADVANCED_FEATURE_FUSION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FEATURE_FUSION_PROFILE="balanced_local_feature_fusion"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_feature_fusion`: Makro, takvim ve haber metadata alanlarını dengeli gecikme ve olay penceresi politikalarıyla birleştirir.
  - `strict_no_lookahead_fusion_safety`: Sıkı makro release lag (`release_timestamp <= base_timestamp`), geriye dönük asof birleştirme ve sıfır hedef/tahmin denetimini zorunlu kılar.
  - `dry_run_feature_fusion_focus`: Sentetik prova verileri üzerinde hızlı fusion hesaplaması ve sözleşme doğrulaması yapar.

### 2. Güvenlik, Non-Signal ve Sınır Ayarları
- `FEATURE_FUSION_CURRENT_PHASE=120`: Mevcut operasyon fazı.
- `FEATURE_FUSION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_FUSION_NEXT_PHASE=121`: Sıradaki faz (Advanced Statistical/Econometric Feature Engine).
- `FEATURE_FUSION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_FUSION_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma zorunluluğu.
- `FEATURE_FUSION_RESEARCH_ONLY=true`: Yalnızca araştırma modu; canlı işlem kesinlikle yasaktır.
- `FEATURE_FUSION_ALLOW_FUSION_AS_SIGNAL=false`: Fusion çıktılarının al/sat sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_FUSION_ALLOW_MACRO_TRADE_SIGNALS=false`: Makro ekonomik göstergelerden trade sinyali üretimi yasaktır.
- `FEATURE_FUSION_ALLOW_CALENDAR_EVENT_SIGNALS=false`: Takvim olay duyurularından alım-satım sinyali üretimi yasaktır.
- `FEATURE_FUSION_ALLOW_NEWS_SENTIMENT_SIGNALS=false`: Haber duygu veya başlıklarından yönlü sinyal üretimi yasaktır.
- `FEATURE_FUSION_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü tahmin veya getiri iddiası yasaktır.
- `FEATURE_FUSION_ALLOW_STRATEGY_GENERATION=false`: Ticaret stratejisi üretimi yasaktır.
- `FEATURE_FUSION_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılamaz.
- `FEATURE_FUSION_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizatörler çalıştırılamaz.
- `FEATURE_FUSION_ALLOW_TARGET_LABEL_GENERATION=false`: Makine öğrenmesi target/label kolonları üretilemez.
- `FEATURE_FUSION_ALLOW_PREDICTION_GENERATION=false`: Model tahmin kolonları üretilemez.
- `FEATURE_FUSION_ALLOW_LIVE_TRADING=false`: Canlı emir iletimi kesinlikle yasaktır.
- `FEATURE_FUSION_ALLOW_BROKER_SOCKET=false`: Aracı kurum soket veya canlı API bağlantısı yasaktır.
- `FEATURE_FUSION_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi veya yönlendirmesi yapılamaz.
- `FEATURE_FUSION_ALLOW_WEB_SCRAPING=false`: Web scraping ve HTML kazıma kesinlikle yasaktır.
- `FEATURE_FUSION_ALLOW_NEWS_FULL_TEXT=false`: Haber tam metin işleme yasaktır (`metadata_only: True`).
- `FEATURE_FUSION_ALLOW_CREDENTIAL_OUTPUT=false`: Gizli anahtar loglaması yasaktır.
- `FEATURE_FUSION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez.
- `FEATURE_FUSION_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Veri silme veya otomatik temizlik yasaktır.

### 3. Namespace, Asof Join ve No-Lookahead Standartları
- `FEATURE_FUSION_NAMESPACE_STANDARD="<domain>__<family>__<source_symbol>__<feature_name>__<window>"`: Standart ad alanı biçimi.
- `FEATURE_FUSION_TIMESTAMP_STANDARD="ISO_8601_UTC"`: UTC ISO 8601 zaman damgası standardı.
- `FEATURE_FUSION_DEFAULT_JOIN_POLICY="asof_backward"`: Yalnızca geriye dönük (`direction="backward"`) birleştirme politikası.
- `FEATURE_FUSION_FORBIDDEN_SIGNAL_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return,trade_action"`: Yasaklı kolon ve terim filtresi.
- `FEATURE_FUSION_NON_MUTATION_ENFORCED=true`: `df.copy()` ile mutasyonsuz veri işleme garantisi.
- `FEATURE_FUSION_NO_LOOKAHEAD_ENFORCED=true`: Negatif shift ve yayın öncesi makro kullanımı yasağı.

### 4. Phase 121 Handoff
- Phase 120, Phase 121 Feature Validation and No-Lookahead Guard katmanına çok alanlı fusion feature matrislerini, manifestlerini ve devir maddelerini aktarır (`phase_121_handoff.py`).

## Phase 121 Feature Validation and No-Lookahead Guard Configuration

### 1. Feature Validation Profili Nasıl Seçilir?
- `ADVANCED_FEATURE_VALIDATION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FEATURE_VALIDATION_PROFILE="balanced_local_feature_validation"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_feature_validation`: Yerel araştırma, çoklu alan validasyonu ve kalite skorlaması için varsayılan dengeli profil.
  - `strict_no_leakage_feature_validation`: Sıfır toleranslı sızıntı denetimi, negatif shift engeli ve sıkı yasaklı kolon karantinası.
  - `dry_run_feature_validation_contract_freeze`: Sentetik veri ve kontrat şemaları üzerinde dry-run test odaklı profil.

### 2. Güvenlik, Non-Signal ve Sınır Ayarları
- `FEATURE_VALIDATION_CURRENT_PHASE=121`: Mevcut operasyonel faz.
- `FEATURE_VALIDATION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_VALIDATION_NEXT_PHASE=122`: Sıradaki faz (Factor Metadata and Factor Families).
- `FEATURE_VALIDATION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_VALIDATION_LOCAL_ONLY=true`: Yalnızca yerel ortamda çalışma zorunluluğu.
- `FEATURE_VALIDATION_RESEARCH_ONLY=true`: Yalnızca araştırma modu; canlı işlem kesinlikle yasaktır.
- `FEATURE_VALIDATION_ALLOW_VALIDATION_AS_SIGNAL=false`: Doğrulama skoru veya sonuçlarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_VALIDATION_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü getiri tahmini veya piyasa iddiası yasaktır.
- `FEATURE_VALIDATION_ALLOW_STRATEGY_GENERATION=false`: Ticaret stratejisi üretimi yasaktır.
- `FEATURE_VALIDATION_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılamaz.
- `FEATURE_VALIDATION_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `FEATURE_VALIDATION_ALLOW_TARGET_LABEL_GENERATION=false`: Makine öğrenmesi target/label kolonları üretilemez.
- `FEATURE_VALIDATION_ALLOW_PREDICTION_GENERATION=false`: Model tahmin kolonları üretilemez.
- `FEATURE_VALIDATION_ALLOW_LIVE_TRADING=false`: Canlı emir iletimi kesinlikle yasaktır.
- `FEATURE_VALIDATION_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `FEATURE_VALIDATION_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi veya yönlendirmesi yapılamaz.
- `FEATURE_VALIDATION_ALLOW_WEB_SCRAPING=false`: Web scraping ve HTML kazıma kesinlikle yasaktır.
- `FEATURE_VALIDATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metin kullanımı yasaktır (`metadata_only: True`).
- `FEATURE_VALIDATION_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay veya akreditasyon iddiası yasaktır.
- `FEATURE_VALIDATION_ALLOW_PRODUCTION_READY_CLAIM=false`: Canlıya/üretime hazır olma iddiası yasaktır.
- `FEATURE_VALIDATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez.
- `FEATURE_VALIDATION_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Veri silme veya yıkıcı temizlik yasaktır (`destructive_action_allowed: False`).

### 3. Yasaklı Kolonlar, Kurallar ve Doğrulama Eşikleri
- `FEATURE_VALIDATION_FORBIDDEN_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return,trade_action,entry_price,exit_price,take_profit,stop_loss,order_type,leverage"`: 20 yasaklı kolon ve terim deseni.
- `FEATURE_VALIDATION_MAX_MISSINGNESS_RATIO=0.50`: Eksik veri uyarı eşiği.
- `FEATURE_VALIDATION_MAX_NUMERIC_MAGNITUDE=1e12`: Sayısal değer büyüklük tavanı.
- `FEATURE_VALIDATION_MIN_SCORE=0.45`: Minimum kabul edilebilir kalite puanı eşiği.
- `FEATURE_VALIDATION_SAFE_ASOF_DIRECTION="backward"`: Asof birleştirmelerinde yalnızca backward yönü zorunludur.

### 4. Phase 122 Handoff
- Phase 121, doğrulanmış feature matrislerini, manifest kayıtlarını ve kalite skorlarını Phase 122 Factor Metadata and Factor Families katmanına devreder (`phase_122_handoff.py`).

## Phase 122 Factor Metadata and Factor Families Configuration

### 1. Factor Metadata Profili Nasıl Seçilir?
- `ADVANCED_FACTOR_METADATA_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FACTOR_METADATA_PROFILE="balanced_local_factor_metadata"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_factor_metadata`: Yerel araştırma, 12 faktör ailesi taksonomisi ve sözleşme doğrulaması için varsayılan dengeli profil.
  - `strict_metadata_only`: Sıkı metadata-only haber ve sıfır-tahmin denetimini en üst seviyede tutan profil.
  - `dry_run`: Sözleşme dondurma ve sentetik fikstür provalarına odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sınır Ayarları
- `FACTOR_METADATA_CURRENT_PHASE=122`: Mevcut operasyonel faz.
- `FACTOR_METADATA_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FACTOR_METADATA_NEXT_PHASE=123`: Sıradaki faz (Feature Quality and Drift Diagnostics).
- `FACTOR_METADATA_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FACTOR_METADATA_LOCAL_ONLY=true`: Yalnızca yerel ortamda çalışma zorunluluğu.
- `FACTOR_METADATA_RESEARCH_ONLY=true`: Yalnızca araştırma modu; canlı işlem kesinlikle yasaktır.
- `FACTOR_METADATA_ALLOW_FACTOR_AS_SIGNAL=false`: Faktör değerlerinin trade sinyali olarak kullanımı kesinlikle yasaktır.
- `FACTOR_METADATA_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü getiri tahmini veya piyasa iddiası yasaktır.
- `FACTOR_METADATA_ALLOW_STRATEGY_GENERATION=false`: Ticaret stratejisi üretimi yasaktır.
- `FACTOR_METADATA_ALLOW_BACKTEST_EXECUTION=false`: Backtest simülasyonu çalıştırılamaz.
- `FACTOR_METADATA_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `FACTOR_METADATA_ALLOW_TARGET_LABEL_GENERATION=false`: Makine öğrenmesi target/label kolonları üretilemez.
- `FACTOR_METADATA_ALLOW_PREDICTION_GENERATION=false`: Model tahmin kolonları üretilemez.
- `FACTOR_METADATA_ALLOW_LIVE_TRADING=false`: Canlı emir iletimi kesinlikle yasaktır.
- `FACTOR_METADATA_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `FACTOR_METADATA_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi veya yönlendirmesi yapılamaz.
- `FACTOR_METADATA_ALLOW_WEB_SCRAPING=false`: Web scraping ve HTML kazıma kesinlikle yasaktır.
- `FACTOR_METADATA_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metin kullanımı yasaktır (`metadata_only: True`).
- `FACTOR_METADATA_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay veya akreditasyon iddiası yasaktır.
- `FACTOR_METADATA_ALLOW_PRODUCTION_READY_CLAIM=false`: Canlıya/üretime hazır olma iddiası yasaktır.
- `FACTOR_METADATA_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez.
- `FACTOR_METADATA_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Veri silme veya yıkıcı temizlik yasaktır (`destructive_action_allowed: False`).

### 3. Faktör Ad Alanı, Sözleşmeler ve Bağımlılıklar
- `FACTOR_METADATA_NAMESPACE_STANDARD="factor__<family>__<asset_class>__<symbol>__<factor_name>__<window>"`: Standart faktör ad alanı şablonu.
- `FACTOR_METADATA_MAX_MISSINGNESS_RATIO=0.50`: Eksik veri tolerans eşiği.
- `FACTOR_METADATA_MIN_SCORE=0.45`: Minimum kalite onay puanı eşiği.

### 4. Phase 123 Handoff
- Phase 122, 12 faktör ailesi taksonomisini, sözleşmelerini, manifestlerini ve devir şartnamesini Phase 123 Feature Quality and Drift Diagnostics katmanına devreder (`phase_123_handoff.py`).

## Phase 123 Feature Quality and Drift Diagnostics Configuration

### 1. Feature Quality and Drift Profili Nasıl Seçilir?
- `ADVANCED_FEATURE_QUALITY_DRIFT_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_FEATURE_QUALITY_DRIFT_PROFILE="balanced_local_feature_quality_drift"`: Varsayılan dengeli profil.
- Seçenekler:
  - `balanced_local_feature_quality_drift`: Dengeli yerel araştırma, 9 kalite ve 10 drift metriği denetimi.
  - `strict_feature_quality_drift`: Sıkı eşikler ve sıfır-tolerans kontrolleri içeren profil.
  - `dry_run`: Sentetik fikstürler ve sözleşme doğrulaması odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Non-Destructive Ayarları
- `FEATURE_QUALITY_DRIFT_CURRENT_PHASE=123`: Mevcut operasyonel faz.
- `FEATURE_QUALITY_DRIFT_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_QUALITY_DRIFT_NEXT_PHASE=124`: Sıradaki faz (Feature Store Integration).
- `FEATURE_QUALITY_DRIFT_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_QUALITY_DRIFT_LOCAL_ONLY=true`: Yalnızca yerel ortamda çalışma kısıtı.
- `FEATURE_QUALITY_DRIFT_RESEARCH_ONLY=true`: Araştırma ve tanı amaçlı çalışma.
- `FEATURE_QUALITY_DRIFT_ALLOW_QUALITY_DRIFT_AS_SIGNAL=false`: Kalite veya drift skorlarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `FEATURE_QUALITY_DRIFT_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `FEATURE_QUALITY_DRIFT_ALLOW_TARGET_LABEL_GENERATION=false`: Target/label kolonları üretilemez.
- `FEATURE_QUALITY_DRIFT_ALLOW_PREDICTION_GENERATION=false`: Model tahminleri üretilemez.
- `FEATURE_QUALITY_DRIFT_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_WEB_SCRAPING=false`: Web kazıma kesinlikle yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `FEATURE_QUALITY_DRIFT_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_SOURCE_OVERWRITE=false`: Kaynak dosyalar ezilemez (`source_preserved: True`).
- `FEATURE_QUALITY_DRIFT_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `FEATURE_QUALITY_DRIFT_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `FEATURE_QUALITY_DRIFT_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik kolon silme yasaktır (`auto_drop_allowed: False`).

### 3. Tanı Eşikleri ve Parametreleri
- `FEATURE_QUALITY_DRIFT_WARNING_MISSINGNESS_THRESHOLD=0.25`: Eksik veri uyarı eşiği (%25).
- `FEATURE_QUALITY_DRIFT_CRITICAL_MISSINGNESS_THRESHOLD=0.50`: Eksik veri kritik eşiği (%50).
- `FEATURE_QUALITY_DRIFT_WARNING_DUPLICATE_RATIO_THRESHOLD=0.90`: Mükerrer değer uyarı eşiği.
- `FEATURE_QUALITY_DRIFT_CRITICAL_DUPLICATE_RATIO_THRESHOLD=0.98`: Mükerrer değer kritik eşiği.
- `FEATURE_QUALITY_DRIFT_WARNING_STALE_BARS_THRESHOLD=30`: Donukluk uyarı bar eşiği.
- `FEATURE_QUALITY_DRIFT_CRITICAL_STALE_BARS_THRESHOLD=60`: Donukluk kritik bar eşiği.
- `FEATURE_QUALITY_DRIFT_WARNING_PSI_THRESHOLD=0.10`: Dağılım kayması (PSI) uyarı eşiği.
- `FEATURE_QUALITY_DRIFT_CRITICAL_PSI_THRESHOLD=0.25`: Dağılım kayması (PSI) kritik eşiği.
- `FEATURE_QUALITY_DRIFT_MIN_QUALITY_SCORE=0.70`: Minimum kabul edilebilir genel kalite skoru.
- `FEATURE_QUALITY_DRIFT_MIN_DRIFT_SCORE=0.60`: Minimum kabul edilebilir genel kararlılık skoru.

### 4. Phase 124 Handoff
- Phase 123, 10 faktör ailesinin kalite, drift, veri mevcudiyeti ve kararlılık tanılarını, yönetişim manifestolarını ve Phase 124 Feature Store Entegrasyonu devir şartnamesini teslim eder (`phase_124_handoff.py`).
## Phase 124 Feature Store Integration Configuration
### 1. Çalışma Profilleri
- `FEATURE_STORE_INTEGRATION_PROFILE`: Çalışma profilini belirler (`balanced_local_feature_store`, `strict_feature_store`, `dry_run_feature_store`).
  - `balanced_local_feature_store`: Dengeli yerel araştırma profili.
  - `strict_feature_store`: Sıkı doğrulama, sıfır tolerans ve tüm kontrollerin zorunlu olduğu profil.
  - `dry_run_feature_store`: Fikstürler üzerinden sözleşme doğrulama odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Kaynak Koruma Ayarları
- `FEATURE_STORE_INTEGRATION_CURRENT_PHASE=124`: Mevcut operasyonel faz.
- `FEATURE_STORE_INTEGRATION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_STORE_INTEGRATION_NEXT_PHASE=125`: Sıradaki faz (Feature/Factor Engine Acceptance Report).
- `FEATURE_STORE_INTEGRATION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_STORE_INTEGRATION_LOCAL_ONLY=true`: Yalnızca yerel ortamda çalışma kısıtı.
- `FEATURE_STORE_INTEGRATION_RESEARCH_ONLY=true`: Araştırma ve depolama amaçlı çalışma.
- `FEATURE_STORE_INTEGRATION_ALLOW_STORE_AS_SIGNAL=false`: Depo çıktılarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `FEATURE_STORE_INTEGRATION_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `FEATURE_STORE_INTEGRATION_ALLOW_TARGET_LABEL_GENERATION=false`: Target/label kolonları üretilemez.
- `FEATURE_STORE_INTEGRATION_ALLOW_PREDICTION_GENERATION=false`: Model tahminleri üretilemez.
- `FEATURE_STORE_INTEGRATION_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_WEB_SCRAPING=false`: Web kazıma kesinlikle yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `FEATURE_STORE_INTEGRATION_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak dosyalar ezilemez (`source_preserved: True`).
- `FEATURE_STORE_INTEGRATION_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `FEATURE_STORE_INTEGRATION_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `FEATURE_STORE_INTEGRATION_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik kolon silme yasaktır (`auto_drop_allowed: False`).

### 3. Depolama ve Bölümleme Parametreleri
- `FEATURE_STORE_INTEGRATION_ENABLE_PARQUET_COMPRESSION=true`: Parquet snappy sıkıştırma etkinliği.
- `FEATURE_STORE_INTEGRATION_PARTITION_BY_UTC_DAY=true`: UTC gün bazlı bölümleme.
- `FEATURE_STORE_INTEGRATION_ENFORCE_LINEAGE_TRACKING=true`: Soybağı takibi zorunluluğu.
- `FEATURE_STORE_INTEGRATION_BLOCK_ON_MANUAL_REVIEW=true`: Kritik inceleme bekleyen kolonların blokajı.

### 4. Phase 125 Handoff
- Phase 124, 7 merkezi depo sözleşmesini, 9 varlık şemasını, 12 kanonik şemayı, kalite/drift metaverilerini ve Phase 125 Blok Kapanışı devir şartnamesini teslim eder (`phase_125_handoff.py`).

## Phase 125 Feature/Factor Engine Acceptance Report and Block Finalization Configuration
### 1. Çalışma Profilleri
- `FEATURE_FACTOR_ACCEPTANCE_PROFILE`: Çalışma profilini belirler (`balanced_local_feature_factor_acceptance`, `strict_feature_factor_acceptance`, `dry_run_feature_factor_acceptance`).
  - `balanced_local_feature_factor_acceptance`: Dengeli yerel blok kabul ve sentez profili.
  - `strict_feature_factor_acceptance`: Sıkı kabul geçitleri, sıfır tolerans ve tüm uyumluluk kontrollerinin zorunlu olduğu profil.
  - `dry_run_feature_factor_acceptance`: Sentetik fikstürler üzerinden sözleşme ve geçit kontrolü odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Kabul Sınır Ayarları
- `ADVANCED_FEATURE_FACTOR_ACCEPTANCE_ENABLED=true`: Phase 125 katmanının aktifliği.
- `FEATURE_FACTOR_ACCEPTANCE_CURRENT_PHASE=125`: Mevcut operasyonel faz.
- `FEATURE_FACTOR_ACCEPTANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `FEATURE_FACTOR_ACCEPTANCE_NEXT_PHASE=126`: Sıradaki faz (Regime Classification and Market Behavior Foundation).
- `FEATURE_FACTOR_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `FEATURE_FACTOR_ACCEPTANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `FEATURE_FACTOR_ACCEPTANCE_RESEARCH_ONLY=true`: Yalnızca araştırma ve blok kabul amaçlı çalışma.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_ACCEPTANCE_AS_SIGNAL=false`: Kabul raporu veya skorunun trade sinyali olarak kullanımı kesinlikle yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_TARGET_LABEL_GENERATION=false`: Target/label kolonları üretilemez.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_PREDICTION_GENERATION=false`: Model tahminleri üretilemez.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_WEB_SCRAPING=false`: Web kazıma kesinlikle yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak dosyalar ezilemez (`source_preserved: True`).
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır (`auto_fix_allowed: False`).
- `FEATURE_FACTOR_ACCEPTANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik kolon silme yasaktır (`auto_drop_allowed: False`).

### 3. Kabul Geçitleri ve Eşik Parametreleri
- `FEATURE_FACTOR_ACCEPTANCE_MIN_ACCEPTANCE_SCORE=0.80`: Minimum kabul edilebilir genel blok skoru.
- `FEATURE_FACTOR_ACCEPTANCE_REQUIRE_ALL_GATES_PASS=true`: Tüm 16 kabul geçidinin başarıyla geçme zorunluluğu.
- `FEATURE_FACTOR_ACCEPTANCE_ENFORCE_MANUAL_REVIEW_EMPTY=false`: Manuel inceleme kuyruğundaki bekleyen maddelerin blok kabulüne engel olup olmayacağını belirler.

### 4. Phase 126 Regime Handoff
- Phase 125, Phase 116-125 bloğunu kabul manifestosu (`phase_116_125_acceptance_manifest`) ile kilitler ve Phase 126 (Regime Classification and Market Behavior Foundation) için 12 yapılandırılmış girdi öğesini devreder (`phase_126_handoff.py`).

## Phase 126 Regime Classification and Market Behavior Foundation Configuration
### 1. Çalışma Profilleri
- `REGIME_FOUNDATION_PROFILE`: Çalışma profilini belirler (`balanced_local_regime_foundation`, `strict_non_signal_regime_foundation`, `dry_run_regime_foundation`).
  - `balanced_local_regime_foundation`: Dengeli yerel araştırma profili. 9 rejim ailesi, 12 piyasa davranışı ve sözleşme doğrulaması.
  - `strict_non_signal_regime_foundation`: Sıkı non-signal ve sıfır-tahmin denetimini en üst seviyede tutan profil.
  - `dry_run_regime_foundation`: Fikstürler ve sentetik şemalar üzerinden sözleşme dondurma odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Model Eğitimi Yasağı Ayarları
- `ADVANCED_REGIME_FOUNDATION_ENABLED=true`: Phase 126 katmanının aktifliği.
- `REGIME_FOUNDATION_CURRENT_PHASE=126`: Mevcut operasyonel faz.
- `REGIME_FOUNDATION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_FOUNDATION_NEXT_PHASE=127`: Sıradaki faz (Regime Feature Matrix and State Dataset Contracts).
- `REGIME_FOUNDATION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_FOUNDATION_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REGIME_FOUNDATION_RESEARCH_ONLY=true`: Yalnızca araştırma ve rejim sınıflandırma temeli amaçlı çalışma.
- `REGIME_FOUNDATION_ALLOW_REGIME_AS_SIGNAL=false`: Rejim çıktılarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `REGIME_FOUNDATION_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `REGIME_FOUNDATION_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `REGIME_FOUNDATION_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `REGIME_FOUNDATION_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `REGIME_FOUNDATION_ALLOW_MODEL_TRAINING=false`: HMM, GMM veya ML model eğitimi kesinlikle engellenir.
- `REGIME_FOUNDATION_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `REGIME_FOUNDATION_ALLOW_TARGET_LABEL_GENERATION=false`: Target/label kolonları üretilemez.
- `REGIME_FOUNDATION_ALLOW_PREDICTION_GENERATION=false`: Model tahminleri üretilemez.
- `REGIME_FOUNDATION_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `REGIME_FOUNDATION_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `REGIME_FOUNDATION_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `REGIME_FOUNDATION_ALLOW_WEB_SCRAPING=false`: Web kazıma kesinlikle yasaktır.
- `REGIME_FOUNDATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_FOUNDATION_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `REGIME_FOUNDATION_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `REGIME_FOUNDATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak dosyalar ezilemez (`source_preserved: True`).
- `REGIME_FOUNDATION_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `REGIME_FOUNDATION_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır (`auto_fix_allowed: False`).
- `REGIME_FOUNDATION_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik kolon silme yasaktır (`auto_drop_allowed: False`).

### 3. Rejim Durum Adlandırma ve Şema Parametreleri
- `REGIME_FOUNDATION_STATE_PREFIX="regime_state_"`: Zorunlu rejim durumu öneki.
- `REGIME_FOUNDATION_FORBIDDEN_COLUMNS="signal,buy,sell,long,short,position,target,label,prediction,recommendation,future_return,forward_return,next_return,trade_action"`: Yasaklı kolon ve terim filtresi.
- `REGIME_FOUNDATION_MIN_SCORE=0.70`: Minimum kabul edilebilir genel rejim sağlık/doğrulama skoru.

### 4. Phase 127 Handoff
- Phase 126, 9 rejim ailesi taksonomisini, 12 piyasa davranışını, 11 rejim durumunu, çevresel bağlam defterlerini ve Phase 127 (Regime Feature Matrix and State Dataset Contracts) devir şartnamesini teslim eder (`phase_127_handoff.py`).

## Phase 127 Regime Feature Matrix and State Dataset Contracts Configuration

### 1. Operasyonel Profiller
- `DEFAULT_REGIME_MATRIX_PROFILE="balanced_local_regime_matrix"`: Varsayılan dengeli yerel rejim matrisi profili.
- Desteklenen profiller:
  - `balanced_local_regime_matrix`: 7 feature matrix ve 5 state dataset sözleşmesini dengeli yerel kısıtlarla çalıştıran profil.
  - `strict_non_signal_regime_matrix_safety`: En yüksek seviyede non-signal ve no-lookahead denetimi uygulayan profil.
  - `dry_run_regime_matrix`: Sentetik şemalar ve fikstürler üzerinden sözleşme dondurma odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Kaynak Koruma Ayarları
- `ADVANCED_REGIME_MATRIX_ENABLED=true`: Phase 127 katmanının aktifliği.
- `REGIME_MATRIX_CURRENT_PHASE=127`: Mevcut operasyonel faz.
- `REGIME_MATRIX_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_MATRIX_NEXT_PHASE=128`: Sıradaki faz (Regime Rule-Free Labeling Contracts and Unsupervised Prep).
- `REGIME_MATRIX_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_MATRIX_LOCAL_ONLY=true`: Yerel çevrimdışı çalışma kısıtı.
- `REGIME_MATRIX_RESEARCH_ONLY=true`: Araştırma ve sözleşme dondurma amaçlı çalışma.
- `REGIME_MATRIX_ALLOW_REGIME_AS_SIGNAL=false`: Matris veya durum çıktılarının trade sinyali olarak kullanımı yasaktır.
- `REGIME_MATRIX_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü getiri iddiası yasaktır.
- `REGIME_MATRIX_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `REGIME_MATRIX_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `REGIME_MATRIX_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `REGIME_MATRIX_ALLOW_MODEL_TRAINING=false`: HMM, GMM veya ML model eğitimi yasaktır.
- `REGIME_MATRIX_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `REGIME_MATRIX_ALLOW_TARGET_LABEL_GENERATION=false`: Target/label üretimi yasaktır.
- `REGIME_MATRIX_ALLOW_PREDICTION_GENERATION=false`: Model tahmini üretimi yasaktır.
- `REGIME_MATRIX_ALLOW_LIVE_TRADING=false`: Canlı ticaret yasaktır.
- `REGIME_MATRIX_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `REGIME_MATRIX_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `REGIME_MATRIX_ALLOW_WEB_SCRAPING=false`: Web kazıma yasaktır.
- `REGIME_MATRIX_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_MATRIX_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `REGIME_MATRIX_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `REGIME_MATRIX_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `REGIME_MATRIX_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `REGIME_MATRIX_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `REGIME_MATRIX_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik kolon silme yasaktır.
- `REGIME_MATRIX_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REGIME_MATRIX_ALLOW_FUTURE_SHIFT=false`: Negatif shift (`shift(-1)`) yasaktır.
- `REGIME_MATRIX_ALLOW_FORWARD_RETURNS=false`: İleriye dönük getiri hesabı yasaktır.

### 3. Ad Alanı ve Şema Parametreleri
- `REGIME_MATRIX_NAMESPACE_PREFIX="regime_matrix__"`: Zorunlu feature matris öneki.
- `REGIME_MATRIX_ASOF_DIRECTION="backward"`: Zorunlu geriye-dönük asof join yönü.
- `REGIME_MATRIX_TIMEZONE="UTC"`: Standart zaman dilimi.
- `REGIME_MATRIX_MIN_READINESS_SCORE=0.70`: Minimum kabul skoru.

### 4. Phase 128 Handoff
- Phase 127, 7 feature matrix sözleşmesini, 5 state dataset sözleşmesini, 10 aday bağlam tanımını, zaman damgası ve guard kurallarını Phase 128 (Regime Rule-Free Labeling Contracts and Unsupervised Prep) fazına devir şartnamesi ile teslim eder (`phase_128_handoff.py`).

## Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep Configuration

### 1. Operasyonel Profiller
- `DEFAULT_REGIME_RULE_FREE_PROFILE="balanced_local_regime_rule_free_prep"`: Varsayılan dengeli yerel kural-bağımsız hazırlık profili.
- Desteklenen profiller:
  - `balanced_local_regime_rule_free_prep`: 8 aday durum sözleşmesi, 8 pseudo-state şeması ve 6 denetimsiz hazırlık sözleşmesini dengeli yerel kısıtlarla çalıştıran profil.
  - `strict_non_signal_rule_free_safety`: En yüksek seviyede non-signal ve zero-execution denetimi uygulayan profil.
  - `dry_run_unsupervised_prep_contract_focus`: Sentetik şemalar ve sözleşme dondurma odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sıfır Yürütme (Zero-Execution) Ayarları
- `ADVANCED_REGIME_RULE_FREE_ENABLED=true`: Phase 128 katmanının aktifliği.
- `REGIME_RULE_FREE_CURRENT_PHASE=128`: Mevcut operasyonel faz.
- `REGIME_RULE_FREE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_RULE_FREE_NEXT_PHASE=129`: Sıradaki faz (Market Behavior Diagnostics and Regime Quality).
- `REGIME_RULE_FREE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_RULE_FREE_LOCAL_ONLY=true`: Yerel çevrimdışı çalışma kısıtı.
- `REGIME_RULE_FREE_RESEARCH_ONLY=true`: Araştırma ve hazırlık amaçlı çalışma.
- `REGIME_RULE_FREE_ALLOW_REGIME_AS_SIGNAL=false`: Aday durumların veya pseudo-state çıktılarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `REGIME_RULE_FREE_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `REGIME_RULE_FREE_ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `REGIME_RULE_FREE_ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `REGIME_RULE_FREE_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `REGIME_RULE_FREE_ALLOW_CLUSTERING_EXECUTION=false`: KMeans, DBSCAN, GMM, HDBSCAN, SOM gibi kümeleme algoritmaları kesinlikle çalıştırılamaz.
- `REGIME_RULE_FREE_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fitting yasaktır.
- `REGIME_RULE_FREE_ALLOW_MODEL_PREDICT=false`: Model inference veya transform yasaktır.
- `REGIME_RULE_FREE_ALLOW_DIMENSIONALITY_REDUCTION=false`: PCA, UMAP, t-SNE çalıştırılamaz.
- `REGIME_RULE_FREE_ALLOW_TARGET_LABEL_GENERATION=false`: Gözetimli öğrenme hedef değişkeni (`target`) üretimi yasaktır.
- `REGIME_RULE_FREE_ALLOW_PREDICTION_GENERATION=false`: Model tahmini üretimi yasaktır.
- `REGIME_RULE_FREE_ALLOW_LIVE_TRADING=false`: Canlı ticaret yasaktır.
- `REGIME_RULE_FREE_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `REGIME_RULE_FREE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `REGIME_RULE_FREE_ALLOW_WEB_SCRAPING=false`: Web kazıma yasaktır.
- `REGIME_RULE_FREE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_RULE_FREE_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `REGIME_RULE_FREE_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `REGIME_RULE_FREE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `REGIME_RULE_FREE_ALLOW_AUTO_DESTRUCTIVE_CLEANING=false`: Otomatik dosya silme yasaktır (`destructive_action_allowed: False`).
- `REGIME_RULE_FREE_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `REGIME_RULE_FREE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.
- `REGIME_RULE_FREE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REGIME_RULE_FREE_ALLOW_FUTURE_SHIFT=false`: Negatif shift (`shift(-1)`) yasaktır.

### 3. Ad Alanı ve Şema Parametreleri
- `REGIME_RULE_FREE_NAMESPACE_PREFIX="candidate_state_"`: Standart aday durum öneki.
- `REGIME_RULE_FREE_TIMEZONE="UTC"`: Standart zaman dilimi.
- `REGIME_RULE_FREE_MIN_READINESS_SCORE=0.70`: Minimum kabul skoru.

### 4. Phase 129 Handoff
- Phase 128, 8 aday durum sözleşmesini, 8 pseudo-durum şemasını, 6 denetimsiz hazırlık sözleşmesini, 15 algoritma/mesafe yer tutucusunu ve no-lookahead guard kurallarını Phase 129 (Market Behavior Diagnostics and Regime Quality) fazına devir şartnamesi ile teslim eder (`phase_129_handoff.py`).

## Phase 129 Market Behavior Diagnostics and Regime Quality Configuration

### 1. Operasyonel Profiller
- `DEFAULT_MARKET_BEHAVIOR_DIAGNOSTICS_PROFILE="balanced_local_market_behavior_diagnostics"`: Varsayılan dengeli yerel piyasa davranış tanı profili.
- Desteklenen profiller:
  - `balanced_local_market_behavior_diagnostics`: 8 aday durum ailesi, 9 rejim ailesi, 6 davranış bağlamı tanısını dengeli yerel kısıtlarla çalıştıran profil.
  - `strict_non_signal_behavior_quality_safety`: En yüksek seviyede non-signal ve davranış kalitesi güvenlik denetimi uygulayan profil.
  - `dry_run_behavior_diagnostics_focus`: Tanı kalitesi raporu ve sözleşme bütünlüğü odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Teşhis Ayarları
- `ADVANCED_MARKET_BEHAVIOR_DIAGNOSTICS_ENABLED=true`: Phase 129 katmanının aktifliği.
- `MARKET_BEHAVIOR_DIAGNOSTICS_CURRENT_PHASE=129`: Mevcut operasyonel faz.
- `MARKET_BEHAVIOR_DIAGNOSTICS_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `MARKET_BEHAVIOR_DIAGNOSTICS_NEXT_PHASE=130`: Sıradaki faz (Regime Transition and Stability Analysis).
- `BEHAVIOR_DIAGNOSTICS_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `BEHAVIOR_DIAGNOSTICS_LOCAL_ONLY=true`: Yerel çevrimdışı çalışma kısıtı.
- `BEHAVIOR_DIAGNOSTICS_RESEARCH_ONLY=true`: Araştırma ve tanı amaçlı çalışma.
- `ALLOW_QUALITY_AS_SIGNAL=false`: Davranış kalitesinin trade sinyali olarak kullanımı kesinlikle yasaktır.
- `ALLOW_BEHAVIOR_AS_SIGNAL=false`: Davranış tanı raporunun AL/SAT yönü olarak kullanımı yasaktır.
- `ALLOW_CANDIDATE_STATE_AS_SIGNAL=false`: Aday durum kalite sonuçlarının sinyal sayılması yasaktır.
- `ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `ALLOW_CLUSTERING_EXECUTION=false`: KMeans, DBSCAN, GMM, HDBSCAN, SOM kümeleme algoritmaları kesinlikle çalıştırılamaz.
- `ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fitting yasaktır.
- `ALLOW_MODEL_PREDICT=false`: Model inference veya transform yasaktır.
- `ALLOW_DIMENSIONALITY_REDUCTION=false`: PCA, UMAP, t-SNE çalıştırılamaz.
- `ALLOW_TARGET_LABEL_GENERATION=false`: Gözetimli öğrenme hedef değişkeni üretimi yasaktır.
- `ALLOW_PREDICTION_GENERATION=false`: Model tahmini üretimi yasaktır.
- `ALLOW_LIVE_TRADING=false`: Canlı ticaret yasaktır.
- `ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `ALLOW_WEB_SCRAPING=false`: Web kazıma yasaktır.
- `ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modeli veya embedding yasaktır.
- `ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.
- `ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ALLOW_FUTURE_SHIFT=false`: Negatif shift (`shift(-1)`) yasaktır.
- `DESTRUCTIVE_ACTION_ALLOWED=false`: Yıkıcı temizlik eylemi yasaktır.

### 3. Kalite Eşiği ve Metrik Parametreleri
- `BEHAVIOR_QUALITY_MIN_COVERAGE_RATIO=0.70`: Minimum aday durum kapsama oranı eşiği.
- `BEHAVIOR_QUALITY_MIN_CONSISTENCY_SCORE=0.70`: Minimum aday durum tutarlılık skoru eşiği.
- `BEHAVIOR_QUALITY_MIN_STABILITY_SCORE=0.60`: Minimum zamansal kararlılık skoru eşiği.
- `BEHAVIOR_QUALITY_GRADE_READY_THRESHOLD=0.70`: `READY` kalite derecesi için minimum genel skor.
- `BEHAVIOR_QUALITY_GRADE_WARNING_THRESHOLD=0.50`: `READY_WITH_WARNINGS` için minimum skor.
- `BEHAVIOR_DIAGNOSTICS_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 130 Handoff
- Phase 129, 8 aday durum ailesi kalite raporlarını, 9 rejim ailesi tanı raporlarını, 6 davranış bağlamı tanı raporunu, geçiş/kararlılık hazırlık raporlarını, 3 maddelik manuel inceleme kuyruğunu, davranış anomali bulgularını, MANIFEST_VALID bütünlük belgesini ve Phase 130 (Regime Transition and Stability Analysis) için doğrulanmış 12 devir maddesini teslim eder (`phase_130_handoff.py`).

## Phase 130 Regime Transition and Stability Analysis Configuration
### 1. Çalışma Profilleri
- `REGIME_TRANSITION_PROFILE`: Çalışma profilini belirler (`balanced_local_regime_transition`, `strict_non_signal_regime_transition`, `dry_run_regime_transition`).
  - `balanced_local_regime_transition`: Varsayılan dengeli yerel araştırma profili. 28 alt etki alanı, aday durum sekans sözleşmeleri, ampirik geçiş sıklığı, geçiş matris yer tutucuları ve geçiş kararlılığı tanıları.
  - `strict_non_signal_regime_transition`: Sıkı no-lookahead (`context_timestamp <= base_timestamp`), sıfır-Markov-fit ve sıfır-tahmin denetimini en üst seviyede tutan güvenlik profili.
  - `dry_run_regime_transition`: Sentetik sekanslar ve sözleşme doğrulaması odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_REGIME_TRANSITION_ENABLED=true`: Phase 130 katmanının aktifliği.
- `REGIME_TRANSITION_CURRENT_PHASE=130`: Mevcut operasyonel faz.
- `REGIME_TRANSITION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_TRANSITION_NEXT_PHASE=131`: Sıradaki faz (Cross-Asset Regime Context and Dynamic Behavior Interplay).
- `REGIME_TRANSITION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_TRANSITION_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REGIME_TRANSITION_RESEARCH_ONLY=true`: Yalnızca araştırma ve rejim geçiş tanı amaçlı çalışma.
- `ALLOW_TRANSITION_AS_SIGNAL=false`: Geçiş sıklığı veya metriklerinin trade sinyali olarak kullanımı kesinlikle yasaktır.
- `ALLOW_STABILITY_AS_SIGNAL=false`: Kararlılık skorlarının trade sinyali olarak kullanımı kesinlikle yasaktır.
- `ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `ALLOW_MARKOV_CHAIN_FIT=false`: Markov zinciri uydurma veya olasılık tahmini kesinlikle çalıştırılamaz.
- `ALLOW_FORWARD_PROBABILITY_GENERATION=false`: İleriye dönük rejim olasılık projeksiyonu yasaktır.
- `ALLOW_CLUSTERING_EXECUTION=false`: KMeans, DBSCAN, GMM, HDBSCAN, SOM kümeleme algoritmaları kesinlikle çalıştırılamaz.
- `ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fitting yasaktır.
- `ALLOW_MODEL_PREDICT=false`: Model inference veya transform yasaktır.
- `ALLOW_TARGET_LABEL_GENERATION=false`: Gözetimli öğrenme hedef değişkeni üretimi yasaktır.
- `ALLOW_PREDICTION_GENERATION=false`: Model tahmini üretimi yasaktır.
- `ALLOW_LIVE_TRADING=false`: Canlı ticaret yasaktır.
- `ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `ALLOW_WEB_SCRAPING=false`: Web kazıma yasaktır.
- `ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modeli veya embedding yasaktır.
- `ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.
- `ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ALLOW_FUTURE_SHIFT=false`: Negatif shift (`shift(-1)`) yasaktır.
- `DESTRUCTIVE_ACTION_ALLOWED=false`: Yıkıcı temizlik eylemi yasaktır.

### 3. Tanı Eşikleri ve Geçiş Parametreleri
- `REGIME_TRANSITION_MIN_PERSISTENCE_SCORE=0.50`: Minimum kabul edilebilir kalıcılık skoru eşiği.
- `REGIME_TRANSITION_MAX_TRANSITION_AMBIGUITY=0.50`: Maksimum tolere edilebilir geçiş belirsizliği eşiği.
- `REGIME_TRANSITION_MIN_CONTINUITY_RATIO=0.50`: Minimum kabul edilebilir sekans sürekliliği eşiği.
- `REGIME_TRANSITION_MIN_STABILITY_SCORE=0.45`: Minimum kabul edilebilir geçiş kararlılık skoru eşiği.
- `REGIME_TRANSITION_MISSINGNESS_WARNING_THRESHOLD=0.25`: Eksik veri uyarı eşiği (%25).
- `REGIME_TRANSITION_MISSINGNESS_CRITICAL_THRESHOLD=0.50`: Eksik veri kritik eşiği (%50).
- `REGIME_TRANSITION_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 131 Handoff
- Phase 130, 28 alt etki alanı kayıt defterini, aday durum sekans sözleşmelerini, ampirik geçiş sıklığı ve matris yer tutucu raporlarını, geçiş belirsizliği ve süreklilik tanılarını, volatilite/trend/range/makro/haber geçiş bağlamlarını, çapraz varlık geçiş hazırlık raporunu, kalite bulguları ve manuel inceleme kuyruğunu, MANIFEST_VALID bütünlük belgesini ve Phase 131 (Cross-Asset Regime Context and Dynamic Behavior Interplay) için doğrulanmış 9 devir maddesini teslim eder (`phase_131_handoff.py`).

## Phase 131 Cross-Asset Regime Context Expansion Configuration
### 1. Çalışma Profilleri
- `CROSS_ASSET_REGIME_PROFILE`: Çalışma profilini belirler (`balanced_local_cross_asset_regime_context`, `strict_non_signal_cross_asset_regime_context`, `dry_run_cross_asset_regime_context`).
  - `balanced_local_cross_asset_regime_context`: Varsayılan dengeli yerel araştırma profili. FX, emtia, makro, takvim, haber metadata etki alanları arası rejim bağlamı, co-movement, ayrışma/yakınsama, volatilite/trend/range bağlantıları ve makro duyarlılık tanıları.
  - `strict_non_signal_cross_asset_regime_context`: Sıkı no-lookahead (`context_timestamp <= base_timestamp`), sıfır pairs trading, sıfır model eğitimi ve sıfır tahmin denetimini en üst seviyede tutan güvenlik profili.
  - `dry_run_cross_asset_regime_context`: Sentetik şemalar ve sözleşme doğrulaması odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_CROSS_ASSET_REGIME_CONTEXT_ENABLED=true`: Phase 131 katmanının aktifliği.
- `CROSS_ASSET_REGIME_CURRENT_PHASE=131`: Mevcut operasyonel faz.
- `CROSS_ASSET_REGIME_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `CROSS_ASSET_REGIME_NEXT_PHASE=132`: Sıradaki faz (Multi-Asset Regime Synchronization and Macro Driver Attribution).
- `CROSS_ASSET_REGIME_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `CROSS_ASSET_REGIME_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `CROSS_ASSET_REGIME_RESEARCH_ONLY=true`: Yalnızca araştırma ve çapraz varlık rejim bağlamı amaçlı çalışma.
- `ALLOW_CONTEXT_AS_SIGNAL=false`: Rejim bağlam metriklerinin trade sinyali olarak kullanımı kesinlikle yasaktır.
- `ALLOW_PAIRS_TRADING_SIGNALS=false`: İkili işlem (pairs trading) veya arbitraj sinyali üretimi kesinlikle yasaktır.
- `ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `ALLOW_STRATEGY_GENERATION=false`: Strateji üretimi yasaktır.
- `ALLOW_BACKTEST_EXECUTION=false`: Backtest çalıştırılamaz.
- `ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon çalıştırılamaz.
- `ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları kesinlikle çalıştırılamaz.
- `ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fitting yasaktır.
- `ALLOW_MODEL_PREDICT=false`: Model inference veya transform yasaktır.
- `ALLOW_TARGET_LABEL_GENERATION=false`: Gözetimli öğrenme hedef değişkeni üretimi yasaktır.
- `ALLOW_PREDICTION_GENERATION=false`: Model tahmini üretimi yasaktır.
- `ALLOW_LIVE_TRADING=false`: Canlı ticaret yasaktır.
- `ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu yasaktır.
- `ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `ALLOW_WEB_SCRAPING=false`: Web kazıma yasaktır.
- `ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modeli veya embedding yasaktır.
- `ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.
- `ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ALLOW_FUTURE_SHIFT=false`: Negatif shift (`shift(-1)`) yasaktır.
- `DESTRUCTIVE_ACTION_ALLOWED=false`: Yıkıcı temizlik eylemi yasaktır.

### 3. Tanı Eşikleri ve Bağlam Parametreleri
- `CROSS_ASSET_REGIME_MIN_ALIGNMENT_SCORE=0.50`: Minimum kabul edilebilir geçiş uyum skoru eşiği.
- `CROSS_ASSET_REGIME_MAX_DIVERGENCE_THRESHOLD=0.50`: Maksimum tolere edilebilir ayrışma eşiği.
- `CROSS_ASSET_REGIME_MIN_CO_MOVEMENT_SCORE=0.40`: Minimum kabul edilebilir birlikte hareket skoru eşiği.
- `CROSS_ASSET_REGIME_MIN_LINKAGE_SCORE=0.45`: Minimum kabul edilebilir bağlantı skoru eşiği.
- `CROSS_ASSET_REGIME_MISSINGNESS_WARNING_THRESHOLD=0.25`: Eksik veri uyarı eşiği (%25).
- `CROSS_ASSET_REGIME_MISSINGNESS_CRITICAL_THRESHOLD=0.50`: Eksik veri kritik eşiği (%50).
- `CROSS_ASSET_REGIME_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 132 Handoff
- Phase 131, varlık ve profil kayıt defterlerini, sözleşmeleri, FX-Emtia rejim bağlantı raporunu, co-movement, ayrışma/yakınsama, geçiş uyumu, volatilite/trend/range bağlantılarını, makro duyarlılık ve haber metadata bağlamlarını, kalite bulguları ve manuel inceleme kuyruğunu, MANIFEST_VALID bütünlük belgesini ve Phase 132 (Macro, Event & News Regime Context Expansion) için doğrulanmış 10 devir maddesini teslim eder (`phase_132_handoff.py`).

## Phase 132 Macro/Event/News Regime Context Expansion Configuration
### 1. Çalışma Profilleri
- `DEFAULT_MACRO_EVENT_NEWS_REGIME_PROFILE`: Çalışma profilini belirler (`balanced_local_macro_event_news_regime_context`, `strict_metadata_only_news_regime_safety`, `dry_run_macro_event_context_focus`).
  - `balanced_local_macro_event_news_regime_context`: Varsayılan dengeli yerel araştırma profili. Makro göstergeler, revizyonlar, ekonomik takvim pencereleri, yalnızca metaveri haber etiketleri ve çapraz varlık duyarlılık kanalları.
  - `strict_metadata_only_news_regime_safety`: Sıkı metaveri-yalnızca haber güvenliği, tam metin/HTML/duygu modeli/vektör blokajı, sıfır lookahead ve sıfır sinyal denetimini en üst seviyede tutan güvenlik profili.
  - `dry_run_macro_event_context_focus`: Sentetik şemalar, yer tutucular ve sözleşme doğrulaması odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_MACRO_EVENT_NEWS_REGIME_ENABLED=true`: Phase 132 katmanının aktifliği.
- `MACRO_EVENT_NEWS_REGIME_CURRENT_PHASE=132`: Mevcut operasyonel faz.
- `MACRO_EVENT_NEWS_REGIME_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `MACRO_EVENT_NEWS_REGIME_NEXT_PHASE=133`: Sıradaki faz (Regime Validation and No-Lookahead Acceptance).
- `MACRO_EVENT_NEWS_REGIME_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `MACRO_EVENT_NEWS_REGIME_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `MACRO_EVENT_NEWS_REGIME_RESEARCH_ONLY=true`: Yalnızca araştırma ve rejim bağlamı amaçlı çalışma.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_CONTEXT_AS_SIGNAL=false`: Rejim bağlam değerlerinin trade sinyali olarak kullanımı yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni veya makale gövdesi kullanımı yasaktır (`strictly_metadata_only: True`).
- `MACRO_EVENT_NEWS_REGIME_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri veya embedding kullanımı yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `MACRO_EVENT_NEWS_REGIME_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `MACRO_EVENT_NEWS_REGIME_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Tanı Eşikleri ve Bağlam Parametreleri
- `MACRO_EVENT_NEWS_REGIME_MIN_CONTEXT_SCORE=0.45`: Minimum kabul edilebilir bağlam bütünlüğü skoru.
- `MACRO_EVENT_NEWS_REGIME_MAX_RELEASE_LAG_DAYS=60`: Maksimum tolere edilebilir makro yayın gecikmesi.
- `MACRO_EVENT_NEWS_REGIME_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 133 Handoff
- Phase 132, 42 kayıt defteri ve veri seti, makro ve takvim olay pencereleri, yalnızca metaveri haber etiketleri, çapraz varlık duyarlılığı, no-lookahead korumaları, MANIFEST_VALID bütünlük manifestosu ve Phase 133 (Regime Validation and No-Lookahead Acceptance) için doğrulanmış 13 devir maddesini teslim eder (`phase_133_handoff.py`).

## Phase 133 Regime Validation and No-Lookahead Acceptance Configuration
### 1. Çalışma Profilleri
- `DEFAULT_REGIME_VALIDATION_ACCEPTANCE_PROFILE`: Çalışma profilini belirler (`balanced_local_regime_validation_acceptance`, `strict_no_lookahead_regime_safety`, `dry_run_regime_acceptance_focus`).
  - `balanced_local_regime_validation_acceptance`: Varsayılan dengeli yerel araştırma profili. 19 kanonik kabul geçidi, no-lookahead ve zaman damgası doğrulaması, yalnızca metaveri haber denetimi, 6 bileşen kabulü ve 1.0 bileşik kabul skoru.
  - `strict_no_lookahead_regime_safety`: Sıkı no-lookahead, sıfır tolerans, geriye dönük asof birleştirme (`direction='backward'`), yasaklı kolon karantinası ve sıfır-sinyal öncelikli güvenlik profili.
  - `dry_run_regime_acceptance_focus`: Sentetik şemalar, fikstürler ve sözleşme doğrulaması odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_REGIME_VALIDATION_ACCEPTANCE_ENABLED=true`: Phase 133 katmanının aktifliği.
- `REGIME_VALIDATION_ACCEPTANCE_CURRENT_PHASE=133`: Mevcut operasyonel faz.
- `REGIME_VALIDATION_ACCEPTANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_VALIDATION_ACCEPTANCE_NEXT_PHASE=134`: Sıradaki faz (Regime FeatureStore Integration).
- `REGIME_VALIDATION_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_VALIDATION_ACCEPTANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REGIME_VALIDATION_ACCEPTANCE_RESEARCH_ONLY=true`: Yalnızca araştırma ve rejim kabul amaçlı çalışma.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_ACCEPTANCE_AS_SIGNAL=false`: Kabul sonuçlarının trade sinyali olarak kullanımı yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `REGIME_VALIDATION_ACCEPTANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Kabul Eşikleri ve Parametreleri
- `REGIME_VALIDATION_ACCEPTANCE_MIN_SCORE=0.80`: Minimum kabul edilebilir genel blok skoru.
- `REGIME_VALIDATION_ACCEPTANCE_REQUIRE_ALL_GATES_PASS=true`: Tüm 19 kabul geçidinin başarıyla geçme zorunluluğu.
- `REGIME_VALIDATION_ACCEPTANCE_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 134 Handoff
- Phase 133, 19 kanonik kabul geçidini, no-lookahead ve geriye dönük asof doğrulamalarını, haber metaveri sınır belgelerini, bileşen kabul raporlarını, MANIFEST_VALID bütünlük manifestosunu ve Phase 134 (Regime FeatureStore Integration) için doğrulanmış 14 devir maddesini teslim eder (`phase_134_handoff.py`).

## Phase 134 Regime FeatureStore Integration Configuration
### 1. Çalışma Profilleri
- `DEFAULT_REGIME_FEATURESTORE_PROFILE`: Çalışma profilini belirler (`balanced_local_regime_featurestore_integration`, `strict_metadata_only_featurestore`, `dry_run_featurestore_focus`).
  - `balanced_local_regime_featurestore_integration`: Varsayılan dengeli yerel FeatureStore profili. 10 kanonik sözleşme, 10 varlık, 16 alanlık şema, 8 bileşen kataloğu, 21 kabul edilmiş referans ve 1.0 hazır bulunuşluk skoru.
  - `strict_metadata_only_featurestore`: Sıkı metaveri odaklı, sıfır-tam-metin, sıfır-duygu-modeli ve sıfır-vektör güvenlik profili.
  - `dry_run_featurestore_focus`: Kuru koşum ve sözleşme bütünlüğü odaklı profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_REGIME_FEATURESTORE_INTEGRATION_ENABLED=true`: Phase 134 katmanının aktifliği.
- `REGIME_FEATURESTORE_CURRENT_PHASE=134`: Mevcut operasyonel faz.
- `REGIME_FEATURESTORE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_FEATURESTORE_NEXT_PHASE=135`: Sıradaki faz (Regime Classification Acceptance Report).
- `REGIME_FEATURESTORE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_FEATURESTORE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REGIME_FEATURESTORE_RESEARCH_ONLY=true`: Yalnızca araştırma ve rejim depolama amaçlı çalışma.
- `REGIME_FEATURESTORE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `REGIME_FEATURESTORE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `REGIME_FEATURESTORE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `REGIME_FEATURESTORE_ALLOW_STORE_AS_SIGNAL=false`: FeatureStore kayıtlarının trade sinyali olarak kullanımı yasaktır.
- `REGIME_FEATURESTORE_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `REGIME_FEATURESTORE_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `REGIME_FEATURESTORE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_FEATURESTORE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `REGIME_FEATURESTORE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REGIME_FEATURESTORE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `REGIME_FEATURESTORE_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `REGIME_FEATURESTORE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Depolama ve Sorgu Parametreleri
- `REGIME_FEATURESTORE_READINESS_MIN_SCORE=0.80`: Minimum kabul edilebilir hazır bulunuşluk skoru.
- `REGIME_FEATURESTORE_TIMEZONE="UTC"`: Standart zaman dilimi.
- `REGIME_FEATURESTORE_ENFORCE_NON_SIGNAL=true`: Tüm kayıt ve sözleşmelerde non-signal zorunluluğu.
- `REGIME_FEATURESTORE_ENFORCE_SOURCE_PRESERVATION=true`: Kaynak dokunulmazlığı zorunluluğu.

### 4. Phase 135 Handoff
- Phase 134, 10 kanonik FeatureStore sözleşmesini, 10 varlığı, 16 alanlık şemayı, 8 bileşen kataloğunu, 21 kabul edilmiş referansı, 12 bağımlılığı, 9 soykütüğü adımını, 0 aktif engelleyiciyi, MANIFEST_VALID manifestosunu ve Phase 135 (Regime Classification Acceptance Report) için doğrulanmış 14 devir maddesini teslim eder (`phase_135_handoff.py`).

## Phase 135 Regime Classification Acceptance Report Configuration
### 1. Çalışma Profilleri
- `DEFAULT_REGIME_ACCEPTANCE_PROFILE`: Çalışma profilini belirler (`balanced_local_regime_acceptance`, `strict_non_signal_regime_block_acceptance`, `dry_run_regime_manifest_focus`).
  - `balanced_local_regime_acceptance`: Varsayılan dengeli yerel blok kabul profili. 17 kanonik kabul geçidi, 10 bileşen envanteri, 6 uyumluluk denetimi, 10 inceleme kuyruğu ve 1.0 kompozit skor.
  - `strict_non_signal_regime_block_acceptance`: Sıkı non-signal ve model eğitilmeme denetimlerini en üst düzeyde tutan profil.
  - `dry_run_regime_manifest_focus`: Kuru koşum ve imzalı blok manifestosu odaklı profil.

### 2. Güvenlik, Non-Signal ve Blok Kabul Ayarları
- `ADVANCED_REGIME_ACCEPTANCE_ENABLED=true`: Phase 135 katmanının aktifliği.
- `REGIME_ACCEPTANCE_CURRENT_PHASE=135`: Mevcut operasyonel faz.
- `REGIME_ACCEPTANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REGIME_ACCEPTANCE_NEXT_PHASE=136`: Sıradaki faz (GPU Acceleration and Advanced ML Runtime Foundation).
- `REGIME_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `REGIME_ACCEPTANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REGIME_ACCEPTANCE_RESEARCH_ONLY=true`: Yalnızca araştırma ve blok kabul amaçlı çalışma.
- `REGIME_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_ACCEPTANCE_AS_SIGNAL=false`: Kabul çıktılarının veya skorlarının trade sinyali olarak kullanımı yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `REGIME_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REGIME_ACCEPTANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `REGIME_ACCEPTANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `REGIME_ACCEPTANCE_ALLOW_PRODUCTION_READY_CLAIM=false`: Canlıya/üretime hazır olma iddiası yasaktır.

### 3. Kabul ve Eşik Parametreleri
- `REGIME_ACCEPTANCE_MIN_COMPOSITE_SCORE=0.85`: Minimum kabul edilebilir bileşik skor eşiği.
- `REGIME_ACCEPTANCE_REQUIRE_ALL_GATES_PASS=true`: Tüm 17 kabul geçidinin başarıyla geçme zorunluluğu.
- `REGIME_ACCEPTANCE_TIMEZONE="UTC"`: Standart zaman dilimi.
- `REGIME_ACCEPTANCE_ENFORCE_NON_SIGNAL=true`: Tüm rapor ve manifestolarda non-signal zorunluluğu.
- `REGIME_ACCEPTANCE_ENFORCE_SOURCE_PRESERVATION=true`: Kaynak dokunulmazlığı zorunluluğu.

### 4. Phase 136 Handoff
- Phase 135, Phase 126-135 rejim ve piyasa davranışı bloğunu nihai kabul raporuna ve imzalı manifestoya bağlar, 17 kabul geçidini, 10 bileşen kabulünü, 6 uyumluluk raporunu ve Phase 136 (GPU Acceleration and Advanced ML Runtime Foundation) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_136_handoff.py`).

## Phase 136 GPU Acceleration and Advanced ML Runtime Foundation Configuration
### 1. Çalışma Profilleri
- `DEFAULT_GPU_ML_RUNTIME_PROFILE`: Çalışma profilini belirler (`cpu_only_safe_baseline`, `balanced_local_ml_runtime`, `gpu_accelerated_research_ready`).
  - `cpu_only_safe_baseline`: CPU tabanlı güvenli temel profil. GPU hızlandırıcı kullanılmaz veya mevcut değilse güvenli geri çekilme sağlar.
  - `balanced_local_ml_runtime`: Varsayılan dengeli yerel ML runtime profili. CPU/GPU donanım keşfi, Torch/Sklearn/Numpy bağımlılık denetimleri, 12 güvenlik sözleşmesi ve 1.0 hazır bulunuşluk skoru.
  - `gpu_accelerated_research_ready`: GPU yeteneklerinin aktif olarak incelendiği ve doğrulanmış donanım hızlandırma önkoşullarının araştırıldığı profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_GPU_ML_RUNTIME_ENABLED=true`: Phase 136 katmanının aktifliği.
- `GPU_ML_RUNTIME_CURRENT_PHASE=136`: Mevcut operasyonel faz.
- `GPU_ML_RUNTIME_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `GPU_ML_RUNTIME_NEXT_PHASE=137`: Sıradaki faz (Advanced Feature Transformation, Normalization & Scaling for ML).
- `GPU_ML_RUNTIME_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `GPU_ML_RUNTIME_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `GPU_ML_RUNTIME_RESEARCH_ONLY=true`: Yalnızca araştırma ve ML altyapı hazırlığı amaçlı çalışma.
- `GPU_ML_RUNTIME_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `GPU_ML_RUNTIME_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `GPU_ML_RUNTIME_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `GPU_ML_RUNTIME_ALLOW_RUNTIME_AS_SIGNAL=false`: Donanım ve runtime çıktılarının trade sinyali olarak kullanımı yasaktır.
- `GPU_ML_RUNTIME_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `GPU_ML_RUNTIME_ALLOW_INFERENCE_EXECUTION=false`: Model tahmini veya predict operasyonu yasaktır.
- `GPU_ML_RUNTIME_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef etiket türetimi yasaktır.
- `GPU_ML_RUNTIME_ALLOW_CLUSTERING_EXECUTION=false`: Kümeleme algoritmaları çalıştırılamaz.
- `GPU_ML_RUNTIME_ALLOW_ENSEMBLE_EXECUTION=false`: Ansambl modeller çalıştırılamaz.
- `GPU_ML_RUNTIME_ALLOW_CALIBRATION_EXECUTION=false`: Olasılık kalibrasyonu çalıştırılamaz.
- `GPU_ML_RUNTIME_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `GPU_ML_RUNTIME_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `GPU_ML_RUNTIME_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `GPU_ML_RUNTIME_ALLOW_SOURCE_OVERWRITE=false`: Kaynak tablolar ezilemez (`source_preserved: True`).
- `GPU_ML_RUNTIME_ALLOW_AUTO_IMPUTATION=false`: Otomatik veri doldurma yasaktır.
- `GPU_ML_RUNTIME_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Donanım ve Hızlandırıcı Eşik Parametreleri
- `GPU_ML_RUNTIME_PREFER_GPU=true`: GPU mevcut olduğunda hızlandırma profili tercih edilir.
- `GPU_ML_RUNTIME_FALLBACK_TO_CPU=true`: GPU yoksa sorunsuz CPU geri çekilmesi sağlanır.
- `GPU_ML_RUNTIME_MIN_GPU_VRAM_GB=4.0`: Araştırma GPU'su için önerilen asgari VRAM.
- `GPU_ML_RUNTIME_MIN_CPU_CORES=2`: Asgari CPU çekirdek sayısı.
- `GPU_ML_RUNTIME_MIN_RAM_GB=8.0`: Asgari sistem RAM boyutu.
- `GPU_ML_RUNTIME_MIN_READINESS_SCORE=0.85`: Minimum kabul edilebilir hazır bulunuşluk skoru.
- `GPU_ML_RUNTIME_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 137 Handoff
- Phase 136, yerel donanım ve hızlandırıcı keşfini, PyTorch/CUDA ve Scikit-learn/Numpy yeteneklerini, 12 ML güvenlik sözleşmesini, rejim/FeatureStore/no-lookahead girdi sözleşmelerini, MANIFEST_VALID manifestosunu ve Phase 137 (Advanced ML Dataset Contracts and Experiment Registry) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_137_handoff.py`).

## Phase 137 Advanced ML Dataset Contracts and Experiment Registry Configuration
### 1. Çalışma Profilleri
- `DEFAULT_ADVANCED_ML_DATASET_PROFILE`: Çalışma profilini belirler (`balanced_local_ml_dataset_contracts`, `strict_no_materialization_no_training_dataset_safety`, `dry_run_experiment_registry_focus`).
  - `balanced_local_ml_dataset_contracts`: Varsayılan dengeli yerel profil. 9 veri kümesi sözleşmesi, şema politikaları, sızıntı korumaları, eğitimsiz deney kaydı ve Phase 138 devir hazırlığı.
  - `strict_no_materialization_no_training_dataset_safety`: Sıfır materyalleştirme, sıfır eğitim ve sıfır çıkarım odaklı sıkı güvenlik profili.
  - `dry_run_experiment_registry_focus`: Deney şablonları, izin matrisi ve yürütme planı yer tutucularına odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_ML_DATASET_REGISTRY_ENABLED=true`: Phase 137 katmanının aktifliği.
- `ML_DATASET_REGISTRY_CURRENT_PHASE=137`: Mevcut operasyonel faz.
- `ML_DATASET_REGISTRY_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `ML_DATASET_REGISTRY_NEXT_PHASE=138`: Sıradaki faz (Baseline ML Model Contracts and Training Harness Governance).
- `ML_DATASET_REGISTRY_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu.
- `ML_DATASET_REGISTRY_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `ML_DATASET_REGISTRY_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `ML_DATASET_REGISTRY_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_DATASET_AS_SIGNAL=false`: Veri kümesi veya deney çıktılarının trade sinyali olarak kullanımı yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_DATASET_MATERIALIZATION=false`: Fiziksel veri kümesi materyalleştirmesi yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_FEATURE_SNAPSHOT_MATERIALIZATION=false`: Fiziksel özellik anlık görüntüsü materyalleştirmesi yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_MODEL_TRAINING=false`: Model eğitimi veya fit operasyonu yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_MODEL_PREDICT=false`: Model tahmini veya predict operasyonu yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef ve etiket kolonları türetimi yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ML_DATASET_REGISTRY_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `ML_DATASET_REGISTRY_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `ML_DATASET_REGISTRY_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Eşik Parametreleri
- `ML_DATASET_REGISTRY_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `ML_DATASET_REGISTRY_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 138 Handoff
- Phase 137, 9 ML veri kümesi ailesi sözleşmesini, 21 kaynak referansını, şema ve sızıntı korumalarını, eğitimsiz deney kaydını, 10 model ve 7 metrik yer tutucusunu ve Phase 138 (Baseline ML Model Contracts and Training Harness Governance) için 13 doğrulanmış devir önkoşulunu teslim eder (`phase_138_handoff.py`).

## Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness Configuration
### 1. Çalışma Profilleri
- `DEFAULT_BASELINE_ML_MODEL_PROFILE`: Çalışma profilini belirler (`balanced_local_baseline_ml_contracts`, `strict_no_real_training_baseline_safety`, `dry_run_harness_contract_focus`).
  - `balanced_local_baseline_ml_contracts`: Varsayılan dengeli yerel profil. 10 model sözleşmesi, girdi/çıktı sözleşmeleri, dry-run harness, stubs, devre dışı bırakılmış yürütme kontrolleri ve Phase 139 devir hazırlığı.
  - `strict_no_real_training_baseline_safety`: Sıfır gerçek eğitim, sıfır tahmin, sıfır hedef/etiket ve sıfır artifact kalıcılığı odaklı sıkı güvenlik profili.
  - `dry_run_harness_contract_focus`: Simüle edilmiş dry-run harness sözleşmeleri, trainer stub'ları ve politikalarına odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ADVANCED_BASELINE_ML_MODELS_ENABLED=true`: Phase 138 katmanının aktifliği.
- `BASELINE_ML_MODEL_CURRENT_PHASE=138`: Mevcut operasyonel faz.
- `BASELINE_ML_MODEL_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `BASELINE_ML_MODEL_NEXT_PHASE=139`: Sıradaki faz (GPU-Accelerated Training Harness and Resource Governance).
- `BASELINE_ML_MODEL_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`would_run=False`, `blocked_by_policy=True`).
- `BASELINE_ML_MODEL_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `BASELINE_ML_MODEL_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `BASELINE_ML_MODEL_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `BASELINE_ML_MODEL_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `BASELINE_ML_MODEL_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `BASELINE_ML_MODEL_ALLOW_MODEL_AS_SIGNAL=false`: Model veya çıktı sözleşmelerinin trade sinyali olarak kullanımı yasaktır.
- `BASELINE_ML_MODEL_ALLOW_REAL_MODEL_TRAINING=false`: Gerçek model eğitimi veya parametre optimizasyonu yasaktır.
- `BASELINE_ML_MODEL_ALLOW_MODEL_FIT=false`: Model `.fit()` operasyonu yasaktır.
- `BASELINE_ML_MODEL_ALLOW_MODEL_PREDICT=false`: Model `.predict()` operasyonu yasaktır.
- `BASELINE_ML_MODEL_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef (`target`) ve etiket (`label`) kolonları türetimi yasaktır.
- `BASELINE_ML_MODEL_ALLOW_ARTIFACT_PERSISTENCE=false`: Model yapay nesnelerinin diske kaydı yasaktır.
- `BASELINE_ML_MODEL_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine veya MLflow'a yazım yasaktır.
- `BASELINE_ML_MODEL_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `BASELINE_ML_MODEL_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `BASELINE_ML_MODEL_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `BASELINE_ML_MODEL_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `BASELINE_ML_MODEL_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `BASELINE_ML_MODEL_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `BASELINE_ML_MODEL_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Eşik Parametreleri
- `BASELINE_ML_MODEL_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `BASELINE_ML_MODEL_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 139 Handoff
- Phase 138, 10 temel model ailesi sözleşmesini, dry-run training harness'ını, 15 harness arayüz spesifikasyonunu, 10 trainer stub'ını, devre dışı bırakılmış yürütme raporlarını, metrik/değerlendirme yer tutucularını ve Phase 139 (GPU-Accelerated Training Harness and Resource Governance) için 12 doğrulanmış devir önkoşulunu teslim eder (`phase_139_handoff.py`).

## Phase 139 GPU-Accelerated Training Harness and Resource Governance Configuration

### 1. GPU Training Governance Profili Nasıl Seçilir?
- `ADVANCED_GPU_TRAINING_GOVERNANCE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_GPU_TRAINING_GOVERNANCE_PROFILE="balanced_local_gpu_training_governance"`: Varsayılan dengeli profil.
- Seçenekler:
  - `balanced_local_gpu_training_governance`: Standart dengeli yerel profil, GPU eğitim kaynak yönetişimi ve kontrollü kuru koşum (dry-run) harness'ı.
  - `strict_no_training_resource_governance_safety`: Sıfır gerçek eğitim, engellenmiş yürütme stub'ları ve muhafazakar bellek sınırlarına odaklanan sıkı güvenlik profili.
  - `dry_run_gpu_resource_contract_focus`: Kuru koşum GPU kaynak politikaları, cihaz seçim doğrulaması ve Phase 140 aday model kayıt defteri hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `GPU_TRAINING_GOVERNANCE_CURRENT_PHASE=139`: Mevcut operasyonel faz.
- `GPU_TRAINING_GOVERNANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `GPU_TRAINING_GOVERNANCE_NEXT_PHASE=140`: Sıradaki faz (Ensemble Model Contracts and Candidate Model Registry).
- `GPU_TRAINING_GOVERNANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`would_run=False`, `blocked_by_policy=True`).
- `GPU_TRAINING_GOVERNANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `GPU_TRAINING_GOVERNANCE_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `GPU_TRAINING_GOVERNANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_SIGNAL_GENERATION=false`: Model veya kaynak yönetişim sözleşmelerinin trade sinyali olarak kullanımı yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_REAL_MODEL_TRAINING=false`: Gerçek model eğitimi veya parametre optimizasyonu yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_MODEL_FIT=false`: Model `.fit()` operasyonu yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_MODEL_PREDICT=false`: Model `.predict()` operasyonu yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef (`target`) ve etiket (`label`) kolonları türetimi yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_ARTIFACT_PERSISTENCE=false`: Model yapay nesnelerinin diske kaydı yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine veya MLflow'a yazım yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `GPU_TRAINING_GOVERNANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `GPU_TRAINING_GOVERNANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `GPU_TRAINING_GOVERNANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Kaynak ve Eşik Parametreleri
- `GPU_TRAINING_GOVERNANCE_MAX_MEMORY_FRACTION_LIMIT=0.80`: Maksimum GPU bellek fraksiyon limiti (%80).
- `GPU_TRAINING_GOVERNANCE_MAX_TIMEOUT_SECONDS_LIMIT=3600`: Maksimum yürütme zaman aşımı tavanı (saniye).
- `GPU_TRAINING_GOVERNANCE_DEFAULT_BATCH_SIZE_PLACEHOLDER=32`: Varsayılan batch size yer tutucusu.
- `GPU_TRAINING_GOVERNANCE_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.

### 4. Phase 140 Handoff
- Phase 139, GPU/CPU kaynak yönetişimi kurallarını, cihaz seçim ve CPU fallback politikalarını, bellek bütçesi ve zaman aşımı korumalarını, 15 harness arayüz spesifikasyonunu, 10 trainer stub'ını, 5 devre dışı bırakılmış yürütme raporunu ve Phase 140 (Ensemble Model Contracts and Candidate Model Registry) için 12 doğrulanmış devir önkoşulunu teslim eder (`phase_140_handoff.py`).

## Phase 140 Ensemble Model Contracts and Candidate Model Registry Configuration

### 1. Ensemble Model Registry Profili Nasıl Seçilir?
- `ADVANCED_ENSEMBLE_MODEL_REGISTRY_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_ENSEMBLE_MODEL_PROFILE="balanced_local_ensemble_model_registry"`: Varsayılan dengeli profil.
- Seçenekler:
  - `balanced_local_ensemble_model_registry`: Standart dengeli yerel profil, topluluk model sözleşmeleri, aday model kayıt defteri ve yürütmesiz ensemble katmanı.
  - `strict_no_ensemble_execution_safety`: Sıfır ensemble yürütmesi, engellenmiş aday eğitimi/çıkarımı ve katı güvenlik sınırlarına odaklanan profil.
  - `candidate_registry_contract_focus`: Aday model sözleşmeleri, uyumluluk matrisi ve Phase 141 olasılık kalibrasyonu hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `ENSEMBLE_MODEL_CURRENT_PHASE=140`: Mevcut operasyonel faz.
- `ENSEMBLE_MODEL_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `ENSEMBLE_MODEL_NEXT_PHASE=141`: Sıradaki faz (Probability Calibration and Uncertainty Estimation).
- `ENSEMBLE_MODEL_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `ENSEMBLE_MODEL_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `ENSEMBLE_MODEL_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `ENSEMBLE_MODEL_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `ENSEMBLE_MODEL_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `ENSEMBLE_MODEL_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `ENSEMBLE_MODEL_ALLOW_SIGNAL_GENERATION=false`: Ensemble sözleşmelerinin trade sinyali olarak kullanımı yasaktır.
- `ENSEMBLE_MODEL_ALLOW_REAL_MODEL_TRAINING=false`: Aday modellerin gerçek eğitimi yasaktır.
- `ENSEMBLE_MODEL_ALLOW_MODEL_FIT=false`: Model `.fit()` operasyonu yasaktır.
- `ENSEMBLE_MODEL_ALLOW_MODEL_PREDICT=false`: Model `.predict()` operasyonu yasaktır.
- `ENSEMBLE_MODEL_ALLOW_ENSEMBLE_EXECUTION=false`: Ensemble stratejilerinin (Voting, Blending, Stacking, Dynamic Weighting) yürütülmesi yasaktır.
- `ENSEMBLE_MODEL_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef (`target`) ve etiket (`label`) kolonları türetimi yasaktır.
- `ENSEMBLE_MODEL_ALLOW_ARTIFACT_PERSISTENCE=false`: Model yapay nesnelerinin diske kaydı yasaktır.
- `ENSEMBLE_MODEL_ALLOW_MODEL_REGISTRY_WRITE=false`: Harici/dahili model kayıt defterlerine veya MLflow'a yazım yasaktır.
- `ENSEMBLE_MODEL_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ENSEMBLE_MODEL_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `ENSEMBLE_MODEL_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `ENSEMBLE_MODEL_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ENSEMBLE_MODEL_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `ENSEMBLE_MODEL_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `ENSEMBLE_MODEL_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Kaynak ve Eşik Parametreleri
- `ENSEMBLE_MODEL_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `ENSEMBLE_MODEL_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 141 Handoff
- Phase 140, 5 aday model ailesi sözleşmesini, 12 uygunluk kapısını, 10 uyumluluk matrisi sözleşmesini, 4 ensemble strateji sözleşmesini, 6 devre dışı bırakılmış yürütme raporunu, metrik/değerlendirme yer tutucularını ve Phase 141 (Probability Calibration and Uncertainty Estimation) için 12 doğrulanmış devir önkoşulunu teslim eder (`phase_141_handoff.py`).

## Phase 141 Probability Calibration and Uncertainty Estimation Configuration

### 1. Calibration and Uncertainty Profili Nasıl Seçilir?
- `ADVANCED_CALIBRATION_UNCERTAINTY_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_CALIBRATION_UNCERTAINTY_PROFILE="balanced_local_calibration_uncertainty_contracts"`: Varsayılan dengeli profil.
- Seçenekler:
  - `balanced_local_calibration_uncertainty_contracts`: Standart dengeli yerel profil, kalibrasyon ve belirsizlik sözleşmeleri, yer tutucular ve kalite kapıları.
  - `strict_non_executing_calibration_safety`: Sıfır kalibrasyon yürütmesi, sıfır belirsizlik kestirimi ve katı güvenlik sınırlarına odaklanan profil.
  - `dry_run_uncertainty_governance_focus`: Belirsizlik yöntem sözleşmeleri, aralık yer tutucuları ve Phase 142 drift izleme hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `CALIBRATION_UNCERTAINTY_CURRENT_PHASE=141`: Mevcut operasyonel faz.
- `CALIBRATION_UNCERTAINTY_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `CALIBRATION_UNCERTAINTY_NEXT_PHASE=142`: Sıradaki faz (Model Drift Monitoring and Data/Feature Drift Linkage).
- `CALIBRATION_UNCERTAINTY_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `CALIBRATION_UNCERTAINTY_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `CALIBRATION_UNCERTAINTY_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `CALIBRATION_UNCERTAINTY_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_SIGNAL_GENERATION=false`: Kalibrasyon/belirsizlik çıktılarının trade sinyali olarak kullanımı yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_MODEL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_PROBABILITY_PREDICTION=false`: Olasılık tahmini (`predict_proba`) üretimi yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_CALIBRATION_EXECUTION=false`: Kalibrasyon algoritmalarının yürütülmesi yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_UNCERTAINTY_ESTIMATION=false`: Belirsizlik kestirim algoritmalarının yürütülmesi yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef (`target`) ve etiket (`label`) kolonları türetimi yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_ARTIFACT_PERSISTENCE=false`: Kalibratör nesnelerinin diske kaydı yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `CALIBRATION_UNCERTAINTY_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `CALIBRATION_UNCERTAINTY_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `CALIBRATION_UNCERTAINTY_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Kaynak ve Eşik Parametreleri
- `CALIBRATION_UNCERTAINTY_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `CALIBRATION_UNCERTAINTY_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 142 Handoff
- Phase 141, 7 olasılık kalibrasyon sözleşmesini, 8 belirsizlik tahmin sözleşmesini, 5 devre dışı bırakılmış yürütme raporunu, güven puanı/aralık/metrik yer tutucularını, muhafızları ve Phase 142 (Model Drift Monitoring and Data/Feature Drift Linkage) için 8 doğrulanmış devir önkoşulunu teslim eder (`phase_142_handoff.py`).

## Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Configuration

### 1. Model Drift Profili Nasıl Seçilir?
- `ADVANCED_MODEL_DRIFT_MONITORING_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_MODEL_DRIFT_PROFILE="balanced_local_model_drift_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_model_drift_contracts`: 59 domain, 24 izleme sözleşmesi, 10 metrik yer tutucu kategorisi ve tam bağlantı doğrulaması için varsayılan dengeli yerel profil.
  - `strict_non_executing_drift_safety`: Sıfır drift hesabı, sıfır canlı izleme, sıfır uyarı ve katı güvenlik sınırlarına odaklanan profil.
  - `dry_run_linkage_governance_focus`: Phase 123, 124, 126-135 bağlantıları, pencere politikaları ve Phase 143 devir hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `MODEL_DRIFT_CURRENT_PHASE=142`: Mevcut operasyonel faz.
- `MODEL_DRIFT_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `MODEL_DRIFT_NEXT_PHASE=143`: Sıradaki faz (Explainability and Feature Attribution Reports).
- `MODEL_DRIFT_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `MODEL_DRIFT_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `MODEL_DRIFT_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `MODEL_DRIFT_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `MODEL_DRIFT_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `MODEL_DRIFT_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `MODEL_DRIFT_ALLOW_SIGNAL_GENERATION=false`: Drift çıktılarının trade sinyali olarak kullanımı yasaktır.
- `MODEL_DRIFT_ALLOW_MODEL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `MODEL_DRIFT_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `MODEL_DRIFT_ALLOW_DRIFT_CALCULATION=false`: Canlı veride gerçek drift metriği hesaplanması yasaktır.
- `MODEL_DRIFT_ALLOW_DRIFT_ALERTING=false`: Otomatik alarm ve bildirim üretimi yasaktır.
- `MODEL_DRIFT_ALLOW_RETRAINING_TRIGGER=false`: Drift kaynaklı otomatik yeniden eğitim tetiklemesi yasaktır.
- `MODEL_DRIFT_ALLOW_MODEL_ACTION=false`: Model değiştirme veya yayından kaldırma aksiyonları yasaktır.
- `MODEL_DRIFT_ALLOW_DATASET_MATERIALIZATION=false`: Veri kümesi materyalizasyonu yasaktır.
- `MODEL_DRIFT_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `MODEL_DRIFT_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `MODEL_DRIFT_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `MODEL_DRIFT_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `MODEL_DRIFT_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `MODEL_DRIFT_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `MODEL_DRIFT_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `MODEL_DRIFT_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Drift Eşikleri ve Parametreleri
- `MODEL_DRIFT_WARNING_PSI_THRESHOLD=0.10`: PSI uyarı eşiği.
- `MODEL_DRIFT_CRITICAL_PSI_THRESHOLD=0.25`: PSI kritik eşiği.
- `MODEL_DRIFT_WARNING_KS_PVALUE_THRESHOLD=0.05`: KS p-değeri uyarı eşiği.
- `MODEL_DRIFT_CRITICAL_KS_PVALUE_THRESHOLD=0.01`: KS p-değeri kritik eşiği.
- `MODEL_DRIFT_WARNING_WASSERSTEIN_THRESHOLD=0.15`: Wasserstein uyarı eşiği.
- `MODEL_DRIFT_CRITICAL_WASSERSTEIN_THRESHOLD=0.30`: Wasserstein kritik eşiği.
- `MODEL_DRIFT_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `MODEL_DRIFT_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 143 Handoff
- Phase 142, 24 izleme sözleşmesini, 4 bağlantı sözleşme grubunu, pencere ve eşik politikalarını, 10 metrik yer tutucu kategorisini, 6 devre dışı bırakılmış yürütme raporunu, muhafızları ve Phase 143 (Explainability and Feature Attribution Reports) için 8 doğrulanmış devir önkoşulunu teslim eder (`phase_143_handoff.py`).

## Phase 143 Explainability and Feature Attribution Reports Configuration

### 1. Açıklanabilirlik Profili Nasıl Seçilir?
- `ADVANCED_EXPLAINABILITY_ATTRIBUTION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_EXPLAINABILITY_PROFILE="balanced_local_explainability_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_explainability_contracts`: 31 domain, 7 rapor sözleşmesi, 8 atıf sözleşmesi, 8 yöntem politikası, 4 kapsam politikası ve tam bağlantı doğrulaması için varsayılan dengeli yerel profil.
  - `strict_non_executing_xai_safety`: Sıfır XAI hesabı, sıfır SHAP/LIME, sıfır permütasyon/PDP, sıfır vekil model, sıfır model aksiyonu ve katı güvenlik sınırlarına odaklanan profil.
  - `dry_run_attribution_report_governance_focus`: FeatureStore, Rejim, Drift, Kalibrasyon bağlantıları ve Phase 144 devir hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `EXPLAINABILITY_CURRENT_PHASE=143`: Mevcut operasyonel faz.
- `EXPLAINABILITY_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `EXPLAINABILITY_NEXT_PHASE=144`: Sıradaki faz (Model Governance, Model Cards and Audit Trail).
- `EXPLAINABILITY_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `EXPLAINABILITY_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `EXPLAINABILITY_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `EXPLAINABILITY_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `EXPLAINABILITY_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `EXPLAINABILITY_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `EXPLAINABILITY_ALLOW_SIGNAL_GENERATION=false`: Açıklanabilirlik çıktılarının trade sinyali olarak kullanımı yasaktır.
- `EXPLAINABILITY_ALLOW_MODEL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `EXPLAINABILITY_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `EXPLAINABILITY_ALLOW_XAI_CALCULATION=false`: Canlı veride gerçek açıklanabilirlik hesaplanması yasaktır.
- `EXPLAINABILITY_ALLOW_SHAP_EXECUTION=false`: SHAP kütüphanesi çağrımı ve hesaplaması yasaktır.
- `EXPLAINABILITY_ALLOW_LIME_EXECUTION=false`: LIME pertürbasyon örneklemesi ve hesaplaması yasaktır.
- `EXPLAINABILITY_ALLOW_PERMUTATION_IMPORTANCE=false`: Permütasyon önem derecesi hesaplaması yasaktır.
- `EXPLAINABILITY_ALLOW_PDP_ICE_EXECUTION=false`: Kısmi bağımlılık ve ICE ızgara eğrisi hesaplaması yasaktır.
- `EXPLAINABILITY_ALLOW_SURROGATE_MODEL=false`: Karar ağacı vekil modelleri eğitimi yasaktır.
- `EXPLAINABILITY_ALLOW_COUNTERFACTUAL_GENERATION=false`: Karşıgözlemsel optimizasyon ve arama yasaktır.
- `EXPLAINABILITY_ALLOW_MODEL_ACTION=false`: Açıklamaya dayalı model budama, silme veya değiştirme aksiyonları yasaktır.
- `EXPLAINABILITY_ALLOW_DATASET_MATERIALIZATION=false`: Veri kümesi materyalizasyonu yasaktır.
- `EXPLAINABILITY_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `EXPLAINABILITY_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `EXPLAINABILITY_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `EXPLAINABILITY_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `EXPLAINABILITY_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `EXPLAINABILITY_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `EXPLAINABILITY_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `EXPLAINABILITY_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Açıklanabilirlik Parametreleri ve Eşikleri
- `EXPLAINABILITY_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `EXPLAINABILITY_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 144 Handoff
- Phase 143, 7 rapor sözleşmesini, 8 atıf sözleşmesini, 8 yöntem politikasını, 4 kapsam politikasını, 9 devre dışı bırakılmış yürütme raporunu, muhafızları ve Phase 144 (Model Governance, Model Cards and Audit Trail) için 8 doğrulanmış devir önkoşulunu teslim eder (`phase_144_handoff.py`).







## Phase 144 Model Governance, Model Cards and Audit Trail Configuration

### 1. Model Governance Profili Nasıl Seçilir?
- `ADVANCED_MODEL_GOVERNANCE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_MODEL_GOVERNANCE_PROFILE="balanced_local_model_governance_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_model_governance_contracts`: 62 domain, model card şablonları, sınır kayıt defterleri, devre dışı yürütme raporları ve yerel denetim izi yer tutucuları için varsayılan dengeli yerel profil.
  - `strict_non_production_governance_safety`: Sıfır canlı onay, sıfır dağıtım yetkilendirmesi, sıfır model eğitimi/çıkarımı, sıfır registry yazımı ve katı güvenlik sınırlarına odaklanan profil.
  - `dry_run_model_governance_manifest_focus`: Sınır denetimleri, doğrulama manifestoları ve Phase 145 devir hazırlığına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `MODEL_GOVERNANCE_CURRENT_PHASE=144`: Mevcut operasyonel faz.
- `MODEL_GOVERNANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `MODEL_GOVERNANCE_NEXT_PHASE=145`: Sıradaki faz (Advanced ML Acceptance Report and Candidate Finalization).
- `MODEL_GOVERNANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `MODEL_GOVERNANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `MODEL_GOVERNANCE_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `MODEL_GOVERNANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `MODEL_GOVERNANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `MODEL_GOVERNANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `MODEL_GOVERNANCE_ALLOW_SIGNAL_GENERATION=false`: Model yönetişimi çıktılarının trade sinyali olarak kullanımı yasaktır.
- `MODEL_GOVERNANCE_ALLOW_MODEL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `MODEL_GOVERNANCE_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `MODEL_GOVERNANCE_ALLOW_PRODUCTION_APPROVAL=false`: Gerçek production veya canlıya geçiş onayı yasaktır.
- `MODEL_GOVERNANCE_ALLOW_DEPLOYMENT=false`: Dağıtım veya servis etme işlemleri yasaktır.
- `MODEL_GOVERNANCE_ALLOW_BROKER_READY_CLAIM=false`: Broker-ready veya canlı işlem onay iddiaları yasaktır.
- `MODEL_GOVERNANCE_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine (MLflow/S3 vb.) yazım yasaktır.
- `MODEL_GOVERNANCE_ALLOW_REAL_AUDIT_LOG=false`: Gerçek SIEM veya harici denetim loglaması yasaktır (`mock_offline_audit_placeholder`).
- `MODEL_GOVERNANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `MODEL_GOVERNANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `MODEL_GOVERNANCE_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `MODEL_GOVERNANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `MODEL_GOVERNANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `MODEL_GOVERNANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `MODEL_GOVERNANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Model Governance Parametreleri ve Eşikleri
- `MODEL_GOVERNANCE_MIN_READINESS_SCORE=0.45`: Minimum kabul edilebilir hazırlık skoru.
- `MODEL_GOVERNANCE_TIMEZONE="UTC"`: Standart zaman dilimi.

### 4. Phase 145 Handoff
- Phase 144, 48 çekirdek modülü, model kart sözleşmelerini, sınır kayıt defterlerini, devre dışı bırakılmış yürütme raporlarını, bağımlılık muhafızlarını ve Phase 145 (Advanced ML Acceptance Report and Candidate Finalization) için 8 doğrulanmış devir önkoşulunu teslim eder (`phase_145_handoff.py`).

## Phase 145 Advanced ML Acceptance Report Configuration

### 1. Advanced ML Acceptance Profili Nasıl Seçilir?
- `ADVANCED_ML_ACCEPTANCE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_ADVANCED_ML_ACCEPTANCE_PROFILE="balanced_local_advanced_ml_acceptance"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_advanced_ml_acceptance`: 30 domain, bileşen kayıt defteri, konsolide faz kabul denetimleri (Phases 136-144), bağımlılık/kanıt kontrolü ve Phase 146 devir hazırlığı için dengeli yerel profil.
  - `strict_safety_governance_acceptance`: Sıfır canlı işlem, sıfır broker entegrasyonu, sıfır model eğitimi/tahmini, sıfır registry yazımı ve 34 No-Go güvenlik sınırına odaklanan profil.
  - `dry_run_audit_acceptance`: Yalnızca denetim, sağlık kontrolü ve doğrulama raporlarına odaklanan profil.

### 2. Güvenlik, Non-Signal ve Kabul Sözleşmesi Ayarları
- `ADVANCED_ML_ACCEPTANCE_CURRENT_PHASE=145`: Mevcut operasyonel faz.
- `ADVANCED_ML_ACCEPTANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `ADVANCED_ML_ACCEPTANCE_NEXT_PHASE=146`: Sıradaki faz (Realistic Backtest, Transaction Cost and Slippage Modeling).
- `ADVANCED_ML_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `ADVANCED_ML_ACCEPTANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `ADVANCED_ML_ACCEPTANCE_RESEARCH_ONLY=true`: Yalnızca araştırma amaçlı çalışma.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_SIGNAL_GENERATION=false`: Kabul çıktılarının sinyal olarak kullanımı yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_PRODUCTION_APPROVAL=false`: Gerçek production veya canlıya geçiş onayı yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_BROKER_READY_APPROVAL=false`: Broker-ready onay iddiaları yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `ADVANCED_ML_ACCEPTANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `ADVANCED_ML_ACCEPTANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `ADVANCED_ML_ACCEPTANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Kabul Parametreleri ve Eşikleri
- `ADVANCED_ML_ACCEPTANCE_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `ADVANCED_ML_ACCEPTANCE_SAVE_REPORTS=true`: Kabul raporlarının diske kaydedilmesi ayarı.

### 4. Phase 146 Handoff
- Phase 145, Advanced ML bloğu (Phases 136-145) kapanış kabulünü, 10 bileşen kaydını, 72 faz kabul kontrolünü, 14 bağımlılık kabulünü, 12 doğrulama kanıtını, güvenlik sınırlarını ve Phase 146 (Realistic Backtest, Transaction Cost and Slippage Modeling) için 13 doğrulanmış devir önkoşulunu teslim eder (`phase_146_handoff.py`).

## Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling Configuration

### 1. Realistic Backtest Profili Nasıl Seçilir?
- `ADVANCED_REALISTIC_BACKTEST_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_REALISTIC_BACKTEST_PROFILE="balanced_local_realistic_backtest"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_realistic_backtest`: 68 domain, motor sözleşmeleri, maliyet modelleri, muhasebe sözleşmeleri, muhafızlar ve Phase 147 devir hazırlığı için dengeli yerel profil.
  - `strict_non_executing_backtest_safety`: Sıfır canlı işlem, sıfır broker entegrasyonu, sıfır backtest/optimizasyon yürütmesi ve 35 No-Go kuralına odaklanan sıkı güvenlik profili.
  - `dry_run_backtest_contracts_focus`: Yalnızca sözleşme doğrulaması, sağlık kontrolleri ve manifest üretimine odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `REALISTIC_BACKTEST_CURRENT_PHASE=146`: Mevcut operasyonel faz.
- `REALISTIC_BACKTEST_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `REALISTIC_BACKTEST_NEXT_PHASE=147`: Sıradaki faz (Walk-Forward Validation and Out-of-Sample Testing).
- `REALISTIC_BACKTEST_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `REALISTIC_BACKTEST_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `REALISTIC_BACKTEST_RESEARCH_ONLY=true`: Yalnızca araştırma ve modelleme amaçlı çalışma.
- `REALISTIC_BACKTEST_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `REALISTIC_BACKTEST_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `REALISTIC_BACKTEST_ALLOW_BROKER_EXECUTION=false`: Broker emir iletimi kesinlikle yasaktır.
- `REALISTIC_BACKTEST_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `REALISTIC_BACKTEST_ALLOW_SIGNAL_GENERATION=false`: Backtest çıktılarının canlı sinyal olarak kullanımı yasaktır.
- `REALISTIC_BACKTEST_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `REALISTIC_BACKTEST_ALLOW_BACKTEST_EXECUTION=false`: Canlı backtest motoru yürütmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_OPTIMIZER_EXECUTION=false`: Parametre optimizasyon yürütmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_WALK_FORWARD_EXECUTION=false`: Walk-forward simülasyonu yürütmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_BENCHMARK_EXECUTION=false`: Benchmark karşılaştırma yürütmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_STRESS_TEST_EXECUTION=false`: Stres testi / Monte Carlo yürütmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_PRODUCTION_APPROVAL=false`: Üretim onay iddiaları yasaktır.
- `REALISTIC_BACKTEST_ALLOW_BROKER_READY_APPROVAL=false`: Broker-ready onay iddiaları yasaktır.
- `REALISTIC_BACKTEST_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `REALISTIC_BACKTEST_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `REALISTIC_BACKTEST_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `REALISTIC_BACKTEST_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `REALISTIC_BACKTEST_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `REALISTIC_BACKTEST_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `REALISTIC_BACKTEST_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `REALISTIC_BACKTEST_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `REALISTIC_BACKTEST_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `REALISTIC_BACKTEST_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `REALISTIC_BACKTEST_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `REALISTIC_BACKTEST_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `REALISTIC_BACKTEST_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Backtest ve Maliyet Parametreleri
- `REALISTIC_BACKTEST_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `REALISTIC_BACKTEST_INITIAL_CASH=100000.0`: Varsayılan başlangıç nakit sermayesi.
- `REALISTIC_BACKTEST_DEFAULT_CURRENCY="USD"`: Varsayılan baz para birimi.
- `REALISTIC_BACKTEST_MAX_LEVERAGE=1.0`: Varsayılan maksimum kaldıraç oranı (1.0 = kaldıraçsız).
- `REALISTIC_BACKTEST_DEFAULT_LATENCY_MS=50`: Varsayılan simüle edilmiş gecikme (ms).
- `REALISTIC_BACKTEST_MAX_VOLUME_PARTICIPATION=0.05`: Varsayılan maksimum hacim katılım oranı (%5).
- `REALISTIC_BACKTEST_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 147 Handoff
- Phase 146, gerçekçi backtest motor sözleşmelerini, işlem maliyeti ve kayma modellerini, muhasebe ve yaşam döngüsü kurallarını, bias muhafızlarını, 9 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 147 (Walk-Forward Validation and Out-of-Sample Testing) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_147_handoff.py`).

## Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking Configuration

### 1. Walk-Forward Validation Profili Nasıl Seçilir?
- `ADVANCED_WALK_FORWARD_VALIDATION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_WALK_FORWARD_PROFILE="balanced_local_walk_forward_validation"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_walk_forward_validation`: 68 domain, split sözleşmeleri, OOS benchmark sözleşmeleri, metrik yer tutucuları, muhafızlar ve Phase 148 devir hazırlığı için dengeli yerel profil.
  - `strict_non_executing_validation_safety`: Sıfır canlı işlem, sıfır broker entegrasyonu, sıfır walk-forward/benchmark yürütmesi ve 35 No-Go kuralına odaklanan sıkı güvenlik profili.
  - `dry_run_walk_forward_contracts_focus`: Yalnızca sözleşme doğrulaması, sağlık kontrolleri ve manifest üretimine odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `WALK_FORWARD_CURRENT_PHASE=147`: Mevcut operasyonel faz.
- `WALK_FORWARD_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `WALK_FORWARD_NEXT_PHASE=148`: Sıradaki faz (Stress Testing, Scenario Simulation and Robustness).
- `WALK_FORWARD_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `WALK_FORWARD_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `WALK_FORWARD_RESEARCH_ONLY=true`: Yalnızca araştırma ve doğrulama modelleme amaçlı çalışma.
- `WALK_FORWARD_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `WALK_FORWARD_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `WALK_FORWARD_ALLOW_BROKER_EXECUTION=false`: Broker emir iletimi kesinlikle yasaktır.
- `WALK_FORWARD_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `WALK_FORWARD_ALLOW_SIGNAL_GENERATION=false`: Doğrulama çıktılarının canlı sinyal olarak kullanımı yasaktır.
- `WALK_FORWARD_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `WALK_FORWARD_ALLOW_WALK_FORWARD_EXECUTION=false`: Canlı walk-forward yürütmesi yasaktır.
- `WALK_FORWARD_ALLOW_OPTIMIZER_EXECUTION=false`: Parametre optimizasyon yürütmesi yasaktır.
- `WALK_FORWARD_ALLOW_BENCHMARK_EXECUTION=false`: Benchmark karşılaştırma yürütmesi yasaktır.
- `WALK_FORWARD_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama koşturulması yasaktır.
- `WALK_FORWARD_ALLOW_STRESS_TEST_EXECUTION=false`: Stres testi / Monte Carlo yürütmesi yasaktır.
- `WALK_FORWARD_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `WALK_FORWARD_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `WALK_FORWARD_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `WALK_FORWARD_ALLOW_PRODUCTION_APPROVAL=false`: Üretim onay iddiaları yasaktır.
- `WALK_FORWARD_ALLOW_BROKER_READY_APPROVAL=false`: Broker-ready onay iddiaları yasaktır.
- `WALK_FORWARD_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `WALK_FORWARD_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `WALK_FORWARD_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `WALK_FORWARD_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `WALK_FORWARD_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `WALK_FORWARD_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `WALK_FORWARD_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `WALK_FORWARD_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `WALK_FORWARD_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `WALK_FORWARD_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `WALK_FORWARD_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `WALK_FORWARD_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `WALK_FORWARD_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Walk-Forward ve Doğrulama Parametreleri
- `WALK_FORWARD_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `WALK_FORWARD_DEFAULT_SPLIT_MODE="rolling_window"`: Varsayılan pencere bölme modu (`rolling_window`, `expanding_window`, `anchored_walk_forward`).
- `WALK_FORWARD_DEFAULT_EMBARGO_PERIODS=5`: Varsayılan sızıntı önleme ambargo bar periyodu.
- `WALK_FORWARD_DEFAULT_PURGE_PERIODS=2`: Varsayılan etiket örtüşmesi temizleme (purge) bar periyodu.
- `WALK_FORWARD_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 148 Handoff
- Phase 147, walk-forward split sözleşmelerini, out-of-sample benchmark sözleşmelerini, metrik yer tutucularını, bias muhafızlarını, 9 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 148 (Stress Testing, Scenario Simulation and Robustness) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_148_handoff.py`).

## Phase 148 Stress Testing and Scenario Simulation Configuration

### 1. Stress Testing Profili Nasıl Seçilir?
- `ADVANCED_STRESS_TESTING_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_STRESS_TESTING_PROFILE="balanced_local_stress_testing_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_stress_testing_contracts`: 35 domain, tarihsel/hipotetik/rejim senaryo sözleşmeleri, şok yer tutucuları, stres metrik formülleri, muhafızlar ve Phase 149 devir hazırlığı için dengeli yerel profil.
  - `strict_safety_stress_contracts`: Sıfır canlı işlem, sıfır broker entegrasyonu, sıfır stres simülasyonu yürütmesi ve 14 No-Go kuralına odaklanan sıkı güvenlik profili.
  - `dry_run_scenario_simulation_contracts`: Yalnızca sözleşme doğrulaması, sağlık kontrolleri ve manifest üretimine odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `STRESS_TESTING_CURRENT_PHASE=148`: Mevcut operasyonel faz.
- `STRESS_TESTING_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `STRESS_TESTING_NEXT_PHASE=149`: Sıradaki faz (Monte Carlo Robustness and Parameter Stability).
- `STRESS_TESTING_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `STRESS_TESTING_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `STRESS_TESTING_RESEARCH_ONLY=true`: Yalnızca araştırma ve senaryo modelleme amaçlı çalışma.
- `STRESS_TESTING_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `STRESS_TESTING_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `STRESS_TESTING_ALLOW_BROKER_EXECUTION=false`: Broker emir iletimi kesinlikle yasaktır.
- `STRESS_TESTING_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `STRESS_TESTING_ALLOW_SIGNAL_GENERATION=false`: Stres çıktılarının canlı sinyal olarak kullanımı yasaktır.
- `STRESS_TESTING_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `STRESS_TESTING_ALLOW_STRESS_TEST_EXECUTION=false`: Canlı stres testi yürütmesi yasaktır.
- `STRESS_TESTING_ALLOW_SCENARIO_SIMULATION=false`: Gerçek senaryo simülasyonu yürütmesi yasaktır.
- `STRESS_TESTING_ALLOW_MONTE_CARLO_EXECUTION=false`: Monte Carlo simülasyonu yürütmesi yasaktır.
- `STRESS_TESTING_ALLOW_OPTIMIZER_EXECUTION=false`: Parametre optimizasyon yürütmesi yasaktır.
- `STRESS_TESTING_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama koşturulması yasaktır.
- `STRESS_TESTING_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `STRESS_TESTING_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `STRESS_TESTING_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `STRESS_TESTING_ALLOW_PRODUCTION_APPROVAL=false`: Üretim onay iddiaları yasaktır.
- `STRESS_TESTING_ALLOW_BROKER_READY_APPROVAL=false`: Broker-ready onay iddiaları yasaktır.
- `STRESS_TESTING_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `STRESS_TESTING_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `STRESS_TESTING_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `STRESS_TESTING_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `STRESS_TESTING_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `STRESS_TESTING_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `STRESS_TESTING_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `STRESS_TESTING_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `STRESS_TESTING_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `STRESS_TESTING_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `STRESS_TESTING_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `STRESS_TESTING_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `STRESS_TESTING_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Senaryo ve Şok Parametreleri
- `STRESS_TESTING_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `STRESS_TESTING_DEFAULT_MARKET_SHOCK_PCT=-0.20`: Varsayılan piyasa şok büyüklüğü (-%20).
- `STRESS_TESTING_DEFAULT_VOLATILITY_SHOCK_PCT=1.00`: Varsayılan volatilite şoku (+%100 artış).
- `STRESS_TESTING_DEFAULT_SPREAD_WIDENING_MULT=3.0`: Varsayılan spread genişleme katsayısı (3x).
- `STRESS_TESTING_DEFAULT_LIQUIDITY_DROP_PCT=0.50`: Varsayılan likidite düşüş oranı (-%50).
- `STRESS_TESTING_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 149 Handoff
- Phase 148, senaryo sözleşmelerini, şok taksonomisini ve yer tutucularını, stres metrik sözleşmelerini, bias ve senaryo sızıntı muhafızlarını, 9 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 149 (Monte Carlo Robustness and Parameter Stability) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_149_handoff.py`).

## Phase 149 Monte Carlo Robustness and Parameter Stability Configuration

### 1. Monte Carlo Robustness Profili Nasıl Seçilir?
- `ADVANCED_MONTE_CARLO_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_MONTE_CARLO_PROFILE="balanced_local_monte_carlo_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_monte_carlo_contracts`: Bootstrap simülasyon yer tutucuları, getiri yolu yeniden örnekleme, işlem sırası karıştırma, parametre pertürbasyon/duyarlılık sözleşmeleri, dayanıklılık zarfı, stabilite bantları, kırılganlık bayrakları ve Phase 150 devir hazırlığı için dengeli yerel profil.
  - `strict_safety_monte_carlo_contracts`: Sıfır canlı işlem, sıfır broker entegrasyonu, sıfır Monte Carlo simülasyonu yürütmesi, sıfır parametre optimizasyonu ve 14 No-Go kuralına odaklanan sıkı güvenlik profili.
  - `dry_run_resampling_simulation_contracts`: Yalnızca sözleşme doğrulaması, sağlık kontrolleri ve manifest üretimine odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `MONTE_CARLO_CURRENT_PHASE=149`: Mevcut operasyonel faz.
- `MONTE_CARLO_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `MONTE_CARLO_NEXT_PHASE=150`: Sıradaki faz (Backtest Governance, Bias Control and Overfitting Safeguards).
- `MONTE_CARLO_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `MONTE_CARLO_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `MONTE_CARLO_RESEARCH_ONLY=true`: Yalnızca araştırma ve dayanıklılık modelleme amaçlı çalışma.
- `MONTE_CARLO_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `MONTE_CARLO_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `MONTE_CARLO_ALLOW_BROKER_EXECUTION=false`: Broker emir iletimi kesinlikle yasaktır.
- `MONTE_CARLO_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `MONTE_CARLO_ALLOW_SIGNAL_GENERATION=false`: Dayanıklılık çıktılarının canlı sinyal olarak kullanımı yasaktır.
- `MONTE_CARLO_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `MONTE_CARLO_ALLOW_MONTE_CARLO_EXECUTION=false`: Canlı Monte Carlo yürütmesi yasaktır.
- `MONTE_CARLO_ALLOW_BOOTSTRAP_SAMPLING=false`: Gerçek bootstrap örnekleme yürütmesi yasaktır.
- `MONTE_CARLO_ALLOW_PARAMETER_OPTIMIZATION=false`: Parametre optimizasyon yürütmesi yasaktır.
- `MONTE_CARLO_ALLOW_PARAMETER_GRID_SWEEP=false`: Parametre ızgara taraması yürütmesi yasaktır.
- `MONTE_CARLO_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama koşturulması yasaktır.
- `MONTE_CARLO_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `MONTE_CARLO_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `MONTE_CARLO_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `MONTE_CARLO_ALLOW_PRODUCTION_APPROVAL=false`: Üretim onay iddiaları yasaktır.
- `MONTE_CARLO_ALLOW_BROKER_READY_APPROVAL=false`: Broker-ready onay iddiaları yasaktır.
- `MONTE_CARLO_ALLOW_OFFICIAL_APPROVAL_CLAIM=false`: Resmi onay iddiası yasaktır.
- `MONTE_CARLO_ALLOW_PRODUCTION_READY_CLAIM=false`: Üretime hazır iddiası yasaktır.
- `MONTE_CARLO_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `MONTE_CARLO_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `MONTE_CARLO_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `MONTE_CARLO_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `MONTE_CARLO_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `MONTE_CARLO_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `MONTE_CARLO_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `MONTE_CARLO_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `MONTE_CARLO_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `MONTE_CARLO_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `MONTE_CARLO_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Simülasyon, Pertürbasyon ve Dayanıklılık Parametreleri
- `MONTE_CARLO_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `MONTE_CARLO_DEFAULT_BOOTSTRAP_REPLICATIONS=1000`: Varsayılan bootstrap tekrar sayısı sözleşme metaverisi.
- `MONTE_CARLO_DEFAULT_CONFIDENCE_INTERVAL=0.95`: Varsayılan güven aralığı metaverisi.
- `MONTE_CARLO_DEFAULT_BLOCK_SIZE=10`: Varsayılan blok büyüklüğü (Block Bootstrap).
- `MONTE_CARLO_DEFAULT_PERTURBATION_PCT=0.10`: Varsayılan parametre pertürbasyon yüzdesi (%10).
- `MONTE_CARLO_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 150 Handoff
- Phase 149, Monte Carlo simülasyon sözleşmelerini, bootstrap ve yeniden örnekleme yer tutucularını, parametre kararlılık sözleşmelerini, dayanıklılık zarfı şablonlarını, bias ve sızıntı muhafızlarını, 9 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 150 (Backtest Governance, Bias Control and Overfitting Safeguards) için 10 doğrulanmış devir önkoşulunu teslim eder (`phase_150_handoff.py`).

## Phase 150 Backtest Governance and Bias Control Configuration

### 1. Backtest Governance Profili Nasıl Seçilir?
- `ADVANCED_BACKTEST_GOVERNANCE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_BACKTEST_GOVERNANCE_PROFILE="balanced_local_backtest_governance"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_backtest_governance`: 53 domain, 9 yanlılık kontrol sözleşmesi, sonuç iddia sınırları, gerçekçilik yönetişim sözleşmeleri, manuel inceleme kapıları ve Phase 151 devir hazırlığı için dengeli yerel profil.
  - `strict_bias_control_governance`: Sıfır toleranslı yanlılık denetimi, katı p-değeri ayarlamaları, sıfır sonuç iddiası ve 10 No-Go kuralına odaklanan sıkı güvenlik profili.
  - `dry_run_governance_contracts_focus`: Yalnızca yönetişim sözleşmesi doğrulaması, sağlık kontrolleri ve manifest üretimine odaklanan kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `BACKTEST_GOVERNANCE_CURRENT_PHASE=150`: Mevcut operasyonel faz.
- `BACKTEST_GOVERNANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `BACKTEST_GOVERNANCE_NEXT_PHASE=151`: Sıradaki faz (Backtest Performance Diagnostics, Deflated Sharpe and Haircut Metrics).
- `BACKTEST_GOVERNANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `BACKTEST_GOVERNANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `BACKTEST_GOVERNANCE_RESEARCH_ONLY=true`: Yalnızca araştırma ve yönetişim modelleme amaçlı çalışma.
- `BACKTEST_GOVERNANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_BROKER_EXECUTION=false`: Broker emir iletimi kesinlikle yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi kesinlikle yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_SIGNAL_GENERATION=false`: Yönetişim çıktılarının canlı sinyal olarak kullanımı yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_DIRECTIONAL_CLAIM=false`: Yönlü piyasa iddiası yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_BACKTEST_EXECUTION=false`: Canlı backtest motoru yürütmesi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_SIMULATION_EXECUTION=false`: Gerçek simülasyon yürütmesi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_OPTIMIZER_EXECUTION=false`: Parametre optimizasyon yürütmesi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama koşturulması yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_RESULT_CLAIM=false`: Backtest sonuç iddiası yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_APPROVAL_CLAIM=false`: Üretim veya resmi onay iddiaları yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_MODEL_REGISTRY_WRITE=false`: Model kayıt defterlerine yazım yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_ARTIFACT_PERSISTENCE=false`: Model ağırlıklarının diske kaydedilmesi yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_DATASET_MATERIALIZATION=false`: Veri seti materyalizasyonu yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `BACKTEST_GOVERNANCE_ALLOW_NLP_SENTIMENT_MODEL=false`: NLP duygu modelleri kullanımı yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_NEGATIVE_SHIFT=false`: Negatif zaman damgası kaydırması (`shift(-1)`) yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_LOOKAHEAD=false`: Geleceğe bakış sızıntısı yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).
- `BACKTEST_GOVERNANCE_ALLOW_AUTO_IMPUTATION=false`: Otomatik eksik veri doldurma yasaktır.
- `BACKTEST_GOVERNANCE_ALLOW_AUTO_FEATURE_DROP=false`: Otomatik özellik silme yasaktır.

### 3. Yönetişim ve Yanlılık Kontrol Parametreleri
- `BACKTEST_GOVERNANCE_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `BACKTEST_GOVERNANCE_AUDIT_TRAIL_RETENTION_DAYS=365`: Denetim izi saklama süresi (gün).
- `BACKTEST_GOVERNANCE_LOOKAHEAD_GUARD_STRICTNESS="strict"`: Geleceğe bakış muhafızı katılık seviyesi (`strict`, `moderate`).
- `BACKTEST_GOVERNANCE_SNOOPING_PENALTY_RATE=0.25`: Veri gözetleme cezalandırma katsayısı (%25).
- `BACKTEST_GOVERNANCE_MAX_ALLOWABLE_MULTIPLE_TESTS=50`: İzin verilen maksimum çoklu hipotez testi sayısı.
- `BACKTEST_GOVERNANCE_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 151 Handoff
- Phase 150, backtest yönetişim profillerini, 9 yanlılık kontrol sözleşmesini, sonuç ve metrik iddia sınırlarını, gerçekçilik ve bölme yönetişimini, 9 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 151 (Benchmark Comparison and Strategy Evaluation Reports) için 10 doğrulanmış devir önkoşulunu teslim eder (`phase_151_handoff.py`).

## Phase 151 Benchmark Comparison and Strategy Evaluation Reports Configuration

### 1. Benchmark Evaluation Profili Nasıl Seçilir?
- `ADVANCED_BENCHMARK_EVALUATION_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_BENCHMARK_EVALUATION_PROFILE="balanced_local_benchmark_evaluation_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_benchmark_evaluation_contracts`: 36 etki alanı, 16 rapor sözleşmesi, 11 özet şablonu, 6 metrik yer tutucusu ve Phase 152 devir hazırlığı için dengeli yerel araştırma profili.
  - `conservative_local_benchmark_evaluation_contracts`: Yüksek güvenlik, sıkı yanlılık kontrolleri ve sıfır toleranslı kısıtlamalara odaklanan muhafazakâr profil.
  - `institutional_local_benchmark_evaluation_contracts`: Kurumsal denetim izi, risk açıklamaları ve çoklu rejim kapsamına odaklanan kurumsal profil.

### 2. Güvenlik, Non-Signal ve Sözleşme Ayarları
- `BENCHMARK_EVALUATION_CURRENT_PHASE=151`: Mevcut operasyonel faz.
- `BENCHMARK_EVALUATION_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `BENCHMARK_EVALUATION_NEXT_PHASE=152`: Sıradaki faz (Backtest Acceptance Report).
- `BENCHMARK_EVALUATION_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `BENCHMARK_EVALUATION_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `BENCHMARK_EVALUATION_RESEARCH_ONLY=true`: Yalnızca araştırma ve değerlendirme sözleşme modellemesi amaçlı çalışma.
- `BENCHMARK_EVALUATION_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_BACKTEST_EXECUTION=false`: Canlı backtest motoru yürütmesi yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_BENCHMARK_EXECUTION=false`: Gerçek benchmark simülasyonu yürütmesi yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama koşturulması yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_RESULT_CLAIM=false`: Backtest veya benchmark sonuç iddiası yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_PERFORMANCE_CLAIM=false`: Performans veya kârlılık iddiaları yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_STRATEGY_APPROVAL=false`: Strateji onayı veya sermaye tahsisatı yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_REAL_TRAINING=false`: Gerçek model eğitimi yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_MODEL_PREDICTION=false`: Model tahmini üretimi yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef / etiket kolon türetimi yasaktır.
- `BENCHMARK_EVALUATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `BENCHMARK_EVALUATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Değerlendirme Parametreleri ve Eşikleri
- `BENCHMARK_EVALUATION_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `BENCHMARK_EVALUATION_BENCHMARK_SELECTION_BIAS_TOLERANCE=0.05`: Benchmark seçim yanlılığı toleransı.
- `BENCHMARK_EVALUATION_SNOOPING_PENALTY_RATIO=0.25`: Veri gözetleme cezalandırma katsayısı (%25).
- `BENCHMARK_EVALUATION_MAX_MULTIPLE_TESTS=50`: İzin verilen maksimum çoklu test sayısı.
- `BENCHMARK_EVALUATION_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 152 Handoff
- Phase 151, 16 rapor sözleşmesini, 11 özet şablonunu, 6 metrik yer tutucusunu, 11 muhafızı, 11 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 152 (Backtest Acceptance Report) için 10 doğrulanmış devir önkoşulunu teslim eder (`phase_152_handoff.py`).

## Phase 152 Backtest Acceptance Report Configuration

### 1. Backtest Acceptance Profili Nasıl Seçilir?
- `ADVANCED_BACKTEST_ACCEPTANCE_ENABLED=true` ile katman aktif edilir.
- `DEFAULT_BACKTEST_ACCEPTANCE_PROFILE="balanced_local_backtest_acceptance_contracts"`: Varsayılan profil.
- Seçenekler:
  - `balanced_local_backtest_acceptance_contracts`: 27 etki alanı, 7 bileşen, Phase 146-151 konsolide kabulü ve Phase 153 devir hazırlığı için dengeli yerel kabul profili.
  - `strict_non_production_backtest_acceptance_safety`: Sıkı güvenlik sınırları, sıfır-backtest yürütme ve sıfır-canlı ticaret denetimini en üst seviyede tutan profil.
  - `dry_run_phase_146_152_acceptance_focus`: Dry-run uyumlu sözleşme doğrulama ve Phase 153 devir odaklı kuru koşum profili.

### 2. Güvenlik, Non-Signal ve Kabul Ayarları
- `BACKTEST_ACCEPTANCE_CURRENT_PHASE=152`: Mevcut operasyonel faz.
- `BACKTEST_ACCEPTANCE_TARGET_FINAL_PHASE=160`: Nihai mimari hedefi.
- `BACKTEST_ACCEPTANCE_NEXT_PHASE=153`: Sıradaki faz (Portfolio Construction, Position Sizing and Risk Budgeting).
- `BACKTEST_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan kuru koşum modu (`execution_blocked=True`).
- `BACKTEST_ACCEPTANCE_LOCAL_ONLY=true`: Yalnızca yerel çevrimdışı ortamda çalışma kısıtı.
- `BACKTEST_ACCEPTANCE_NON_PRODUCTION=true`: Non-production araştırma kabul modu.
- `BACKTEST_ACCEPTANCE_RESEARCH_ONLY=true`: Araştırma ve sözleşme kabulü amaçlı çalışma.
- `BACKTEST_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı ticaret kesinlikle yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker entegrasyonu kesinlikle yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_REAL_ORDER=false`: Gerçek emir gönderimi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_SIGNAL_GENERATION=false`: Sinyal üretimi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_BACKTEST_EXECUTION=false`: Gerçek backtest yürütmesi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_BENCHMARK_EXECUTION=false`: Gerçek benchmark simülasyonu yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesaplama yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_RESULT_CLAIM=false`: Sonuç iddiası yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_PERFORMANCE_CLAIM=false`: Performans iddiası yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_STRATEGY_APPROVAL=false`: Strateji onayı yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_CAPITAL_ALLOCATION=false`: Sermaye tahsisi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_PORTFOLIO_CONSTRUCTION=false`: Portföy oluşturma yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_POSITION_SIZING=false`: Pozisyon büyüklüğü üretimi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_OPTIMIZER_EXECUTION=false`: Optimizasyon yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_MODEL_TRAINING=false`: Model eğitimi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_MODEL_PREDICT=false`: Model tahmini yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_TARGET_LABEL_GENERATION=false`: Hedef etiket türetimi yasaktır.
- `BACKTEST_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `BACKTEST_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Kabul Parametreleri ve Eşikleri
- `BACKTEST_ACCEPTANCE_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `BACKTEST_ACCEPTANCE_ENABLE_COMPONENT_CHECKPOINTS=true`: Bileşen kontrol noktaları etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_PHASE_ACCEPTANCE=true`: Faz kabul tescilleri etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_DEPENDENCY_EVIDENCE=true`: Bağımlılık ve kanıt tescilleri etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_BOUNDARIES=true`: Güvenlik ve Go/No-Go sınırları etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_FINDINGS=true`: Bulgular tescili etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_MANIFEST=true`: Kabul manifestosu etkinliği.
- `BACKTEST_ACCEPTANCE_ENABLE_PHASE_153_HANDOFF=true`: Phase 153 devri etkinliği.
- `BACKTEST_ACCEPTANCE_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 153 Handoff
- Phase 152, 7 bileşenin kabul tescillerini, 60 faz düzeyi kontrolünü, 11 bağımlılığı, 8 doğrulama kanıtını, 12 güvenlik sınırını, 7 inceleme kapısını, 22 Go/No-Go kuralını, master kabul manifestosunu ve Phase 153 (Portfolio Construction, Position Sizing and Risk Budgeting) için 13 doğrulanmış devir önkoşulunu teslim eder (`phase_153_handoff.py`).

## Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting Configuration

### 1. Portföy İnşa ve Risk Bütçeleme Profilleri
- `PORTFOLIO_CONSTRUCTION_PROFILE="balanced"`: Varsayılan portföy inşa profili (`balanced`, `conservative`, `institutional`).
  - `balanced_local_portfolio_construction_contracts`: 36 etki alanı, 12 portföy sözleşmesi, 10 evren varlığı, 9 pozisyon boyutlandırma şablonu, 9 risk bütçeleme şablonu ve Phase 154 devir hazırlığı için dengeli yerel araştırma profili.
  - `conservative_portfolio_risk_budgeting_safety`: Düşük kaldıraç (1.0x) ve sıkı risk sınırları (%15 varlık, %30 sektör) odaklı muhafazakâr profil.
  - `institutional_governed_allocation_contracts`: Kurumsal standartlarda yönetişim, korelasyon ve likidite kontrolleri içeren profil.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_PORTFOLIO_CONSTRUCTION_ENABLED=true`: Phase 153 modül etkinliği.
- `PORTFOLIO_CONSTRUCTION_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `PORTFOLIO_CONSTRUCTION_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `PORTFOLIO_CONSTRUCTION_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `PORTFOLIO_CONSTRUCTION_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_BROKER_EXECUTION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_REAL_LOT_SIZING=false`: Gerçek lot/kontrat boyutlandırması engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_REAL_CAPITAL_ALLOCATION=false`: Gerçek sermaye tahsisi engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_REAL_PORTFOLIO_WEIGHTS=false`: Gerçek portföy ağırlığı üretimi engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_REAL_OPTIMIZATION=false`: Sayısal portföy optimizasyonu engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_METRIC_CALCULATION=false`: Portföy metrik hesabı engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_TRAINING=false`: Model eğitimi engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_PREDICTION=false`: Tahmin üretimi engellenmiştir.
- `PORTFOLIO_CONSTRUCTION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `PORTFOLIO_CONSTRUCTION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Portföy İnşa Parametreleri ve Eşikleri
- `PORTFOLIO_CONSTRUCTION_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `PORTFOLIO_CONSTRUCTION_MAX_ASSET_WEIGHT=0.20`: Tek varlık maksimum portföy ağırlığı sınırı (%20).
- `PORTFOLIO_CONSTRUCTION_MAX_SECTOR_WEIGHT=0.40`: Sektör/grup maksimum ağırlığı sınırı (%40).
- `PORTFOLIO_CONSTRUCTION_MAX_LEVERAGE=1.0`: Maksimum brüt kaldıraç sınırı (1.0x).
- `PORTFOLIO_CONSTRUCTION_MAX_DRAWDOWN_BUDGET=0.15`: Maksimum portföy drawdown bütçesi (%15).
- `PORTFOLIO_CONSTRUCTION_TARGET_VOLATILITY=0.12`: Yıllık hedef volatilite bütçesi (%12).
- `PORTFOLIO_CONSTRUCTION_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 154 Handoff
- Phase 153, 12 portföy sözleşmesini, 10 evren varlığını, 9 boyutlandırma şablonunu, 9 risk bütçeleme şablonunu, 10 limit modülünü, 11 muhafızı, 11 devre dışı bırakılmış yürütme raporunu, master bütünlük manifestosunu ve Phase 154 (Portfolio Optimization Contracts) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_154_handoff.py`).

## Phase 154 Portfolio Optimization and Allocation Constraints Configuration

### 1. Portföy Optimizasyonu Profilleri
- `PORTFOLIO_OPTIMIZATION_PROFILE="balanced_local_portfolio_optimization_contracts"`: Varsayılan optimizasyon sözleşme profili (`balanced_local_portfolio_optimization_contracts`, `strict_non_production_portfolio_optimization_safety`, `dry_run_phase_154_optimization_contracts_focus`).
  - `balanced_local_portfolio_optimization_contracts`: 34 etki alanı, 11 optimizasyon sözleşmesi, 11 amaç fonksiyonu şablonu, 22 tahsis kısıtı şablonu ve Phase 155 devir hazırlığı için dengeli yerel araştırma profili.
  - `strict_non_production_portfolio_optimization_safety`: Yüksek hazırlık eşiği (0.65) ve katı non-production güvenlik kontrolleri içeren profil.
  - `dry_run_phase_154_optimization_contracts_focus`: Çözücü yer tutucuları ve kısıt şablonu doğrulama odaklı kuru koşum profili.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_PORTFOLIO_OPTIMIZATION_ENABLED=true`: Phase 154 modül etkinliği.
- `PORTFOLIO_OPTIMIZATION_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `PORTFOLIO_OPTIMIZATION_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `PORTFOLIO_OPTIMIZATION_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `PORTFOLIO_OPTIMIZATION_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_PORTFOLIO_OPTIMIZATION=false`: Sayısal portföy optimizasyonu engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_WEIGHT_GENERATION=false`: Gerçek optimal portföy ağırlığı üretimi engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_CAPITAL_ALLOCATION=false`: Gerçek sermaye tahsisatı üretimi engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_REBALANCE_GENERATION=false`: Yeniden dengeleme emirleri üretimi engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_SOLVER_EXECUTION=false`: Sayısal çözücü kütüphaneleri (CVXPY, SciPy vb.) koşturulamaz.
- `PORTFOLIO_OPTIMIZATION_ALLOW_EFFICIENT_FRONTIER_GENERATION=false`: Gerçek etkin sınır hesaplaması engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_METRIC_CALCULATION=false`: Optimizasyon metrik hesaplaması engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_MODEL_PREDICT=false`: Model tahmini engellenmiştir.
- `PORTFOLIO_OPTIMIZATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `PORTFOLIO_OPTIMIZATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Optimizasyon Parametreleri ve Eşikleri
- `PORTFOLIO_OPTIMIZATION_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `PORTFOLIO_OPTIMIZATION_MAX_ASSET_WEIGHT=0.20`: Tek varlık maksimum portföy ağırlığı sınırı (%20).
- `PORTFOLIO_OPTIMIZATION_MIN_ASSET_WEIGHT=0.00`: Tek varlık minimum portföy ağırlığı sınırı (%0 - long only).
- `PORTFOLIO_OPTIMIZATION_MAX_GROUP_WEIGHT=0.40`: Grup/sektör maksimum ağırlığı sınırı (%40).
- `PORTFOLIO_OPTIMIZATION_MAX_GROSS_EXPOSURE=1.00`: Maksimum brüt maruziyet / kaldıraç sınırı (1.0x).
- `PORTFOLIO_OPTIMIZATION_MAX_TURNOVER=0.30`: Maksimum portföy turnover sınırı (%30).
- `PORTFOLIO_OPTIMIZATION_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 155 Handoff
- Phase 154; 11 optimizasyon sözleşmesini, 11 amaç fonksiyonu şablonunu, 22 tahsis kısıtı şablonunu, 5 çözücü yer tutucusunu, 7 çıktı sözleşmesini, 6 yukarı akış bağımlılığını, 11 güvenlik muhafızını, 52 yasaklı kolon politikasını, 10 devre dışı bırakılmış yürütme raporunu, master optimizasyon manifestosunu ve Phase 155 (Portfolio Risk Attribution and Reporting) için 15 doğrulanmış devir önkoşulunu teslim eder (`phase_155_handoff.py`).

## Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring Configuration

### 1. Risk Raporlama Profilleri
- `RISK_REPORTING_PROFILE="balanced_local_risk_reporting_contracts"`: Varsayılan risk raporlama sözleşme profili (`balanced_local_risk_reporting_contracts`, `conservative_risk_reporting_contracts`, `institutional_risk_reporting_contracts`, `audit_risk_reporting_contracts`).
  - `balanced_local_risk_reporting_contracts`: 28 etki alanı, 15 araştırma kapsamı, 9 risk rapor sözleşmesi, 10 exposure sözleşmesi, 9 limit izleme sözleşmesi ve Phase 156 devir hazırlığı için dengeli yerel araştırma profili.
  - `conservative_risk_reporting_contracts`: Düşük eşikler (0.05 drawdown, 0.08 volatilite) ve sıkı risk sınırları odaklı muhafazakâr profil.
  - `institutional_risk_reporting_contracts`: Kurumsal standartlarda çoklu varlık, rejim ve konsantrasyon sınırları içeren profil.
  - `audit_risk_reporting_contracts`: Bağımsız iç/dış denetim ve model yönetişimi gereksinimlerine uygun doğrulama profili.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_RISK_REPORTING_ENABLED=true`: Phase 155 modül etkinliği.
- `RISK_REPORTING_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `RISK_REPORTING_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `RISK_REPORTING_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `RISK_REPORTING_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `RISK_REPORTING_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `RISK_REPORTING_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `RISK_REPORTING_ALLOW_RISK_REPORT_EXECUTION=false`: Gerçek risk raporu derlemesi engellenmiştir.
- `RISK_REPORTING_ALLOW_EXPOSURE_ATTRIBUTION_EXECUTION=false`: Gerçek maruziyet hesaplaması engellenmiştir.
- `RISK_REPORTING_ALLOW_LIMIT_MONITORING_EXECUTION=false`: Gerçek limit izleme döngüsü engellenmiştir.
- `RISK_REPORTING_ALLOW_METRIC_CALCULATION=false`: Risk metrik hesabı engellenmiştir.
- `RISK_REPORTING_ALLOW_VAR_CALCULATION=false`: VaR hesabı engellenmiştir.
- `RISK_REPORTING_ALLOW_EXPECTED_SHORTFALL_CALCULATION=false`: ES hesabı engellenmiştir.
- `RISK_REPORTING_ALLOW_EXPOSURE_CALCULATION=false`: Exposure hesabı engellenmiştir.
- `RISK_REPORTING_ALLOW_LIMIT_BREACH_GENERATION=false`: Limit ihlali tetiklemesi engellenmiştir.
- `RISK_REPORTING_ALLOW_ALERT_GENERATION=false`: Canlı alarm/uyarı üretimi engellenmiştir.
- `RISK_REPORTING_ALLOW_DASHBOARD_GENERATION=false`: Dashboard üretimi engellenmiştir.
- `RISK_REPORTING_ALLOW_PORTFOLIO_ADJUSTMENT=false`: Otomatik portföy düzeltmesi/rebalance engellenmiştir.
- `RISK_REPORTING_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `RISK_REPORTING_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `RISK_REPORTING_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `RISK_REPORTING_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Risk Raporlama Parametreleri ve Eşikleri
- `RISK_REPORTING_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `RISK_REPORTING_MAX_GROSS_EXPOSURE=1.0`: Maksimum brüt maruziyet sınırı (1.0x).
- `RISK_REPORTING_MAX_NET_EXPOSURE=1.0`: Maksimum net maruziyet sınırı (%100).
- `RISK_REPORTING_MAX_CONCENTRATION_RATIO=0.25`: Tek varlık maksimum konsantrasyon sınırı (%25).
- `RISK_REPORTING_MAX_DRAWDOWN_LIMIT=0.15`: Maksimum portföy drawdown sınırı (%15).
- `RISK_REPORTING_MAX_VOLATILITY_LIMIT=0.20`: Yıllık maksimum volatilite sınırı (%20).
- `RISK_REPORTING_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 156 Handoff
- Phase 155; 9 risk raporu sözleşmesini, 10 exposure sözleşmesini, 13 exposure yer tutucusunu, 10 risk katkı ve izleme yer tutucusunu, 10 limit izleme sözleşmesini, 12 muhafızı, 48 yasaklı kolon politikasını, 12 devre dışı bırakılmış yürütme raporunu, master risk rapor bütünlük manifestosunu ve Phase 156 (Portfolio Scenario Testing and Drawdown Control) için 10 doğrulanmış devir önkoşulunu teslim eder (`phase_156_handoff.py`).

## Phase 156 Portfolio Scenario Testing and Drawdown Control Configuration

### 1. Senaryo Testi ve Drawdown Kontrol Profilleri
- `PORTFOLIO_SCENARIO_CONTROL_PROFILE="balanced_local_portfolio_scenario_control_contracts"`: Varsayılan profil (`balanced_local_portfolio_scenario_control_contracts`, `conservative_portfolio_scenario_control_contracts`, `institutional_portfolio_scenario_control_contracts`, `audit_portfolio_scenario_control_contracts`).
  - `balanced_local_portfolio_scenario_control_contracts`: 30 etki alanı, 18 araştırma kapsamı, 13 senaryo testi sözleşmesi, 7 drawdown kontrol sözleşmesi, 7 portföy kontrol aksiyonu yer tutucusu ve Phase 157 devir hazırlığı için dengeli yerel araştırma profili.
  - `conservative_portfolio_scenario_control_contracts`: Düşük eşikler (0.05 uyarı, 0.10 ihlal) ve sıkı kontrol kuralları odaklı muhafazakâr profil.
  - `institutional_portfolio_scenario_control_contracts`: Kurumsal stres senaryoları, rejim geçişleri ve likidite krizleri odaklı profil.
  - `audit_portfolio_scenario_control_contracts`: Bağımsız denetim ve model yönetişimi gereksinimlerine uygun doğrulama profili.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_PORTFOLIO_SCENARIO_CONTROL_ENABLED=true`: Phase 156 modül etkinliği.
- `PORTFOLIO_SCENARIO_CONTROL_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `PORTFOLIO_SCENARIO_CONTROL_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `PORTFOLIO_SCENARIO_CONTROL_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_SCENARIO_EXECUTION=false`: Gerçek senaryo simülasyonu engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_DRAWDOWN_CONTROL_EXECUTION=false`: Gerçek drawdown kontrol döngüsü engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_PORTFOLIO_ADJUSTMENT=false`: Otomatik portföy müdahalesi engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_HEDGE_EXECUTION=false`: Otomatik hedge açma engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_DERISK_EXECUTION=false`: Otomatik de-risking engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_REBALANCE_EXECUTION=false`: Otomatik rebalance engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_METRIC_CALCULATION=false`: Senaryo/drawdown metrik hesabı engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_ALERT_GENERATION=false`: Canlı alarm/uyarı üretimi engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_DASHBOARD_GENERATION=false`: Dashboard üretimi engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `PORTFOLIO_SCENARIO_CONTROL_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Senaryo ve Kontrol Parametreleri ve Eşikleri
- `PORTFOLIO_SCENARIO_CONTROL_MIN_READINESS_SCORE=0.50`: Minimum kabul edilebilir hazırlık skoru.
- `PORTFOLIO_SCENARIO_CONTROL_DRAWDOWN_WARNING_THRESHOLD=0.08`: Drawdown uyarı eşiği (%8).
- `PORTFOLIO_SCENARIO_CONTROL_DRAWDOWN_BREACH_THRESHOLD=0.15`: Drawdown ihlal eşiği (%15).
- `PORTFOLIO_SCENARIO_CONTROL_MAX_RECOVERY_DAYS=60`: Azami toparlanma süresi hedefi (60 gün).
- `PORTFOLIO_SCENARIO_CONTROL_MIN_RESILIENCE_SCORE=0.60`: Asgari dayanıklılık skoru hedefi (0.60).
- `PORTFOLIO_SCENARIO_CONTROL_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 157 Handoff
- Phase 156; 13 senaryo testi sözleşmesini, 7 drawdown kontrol sözleşmesini, 7 portföy kontrol aksiyonu yer tutucusunu, 8 çıktı sözleşmesini, 10 yukarı akış bağımlılığını, 14 muhafızı, 52 yasaklı kolon politikasını, 14 devre dışı bırakılmış yürütme raporunu, master senaryo kontrol bütünlük manifestosunu ve Phase 157 (Portfolio Acceptance Report) için 10 doğrulanmış devir önkoşulunu teslim eder (`phase_157_handoff.py`).

## Phase 157 Portfolio Acceptance Report and Phase 153-157 Consolidated Acceptance Configuration

### 1. Portföy Kabul Profilleri
- `PORTFOLIO_ACCEPTANCE_PROFILE="balanced_local_portfolio_acceptance_contracts"`: Varsayılan kabul profili (`balanced_local_portfolio_acceptance_contracts`, `conservative_portfolio_acceptance_contracts`, `institutional_portfolio_acceptance_contracts`, `audit_portfolio_acceptance_contracts`).
  - `balanced_local_portfolio_acceptance_contracts`: 32 etki alanı, 20 araştırma kapsamı, 24 bileşen checkpoint sözleşmesi, Phase 153-156 faz kabul sözleşmeleri, go/no-go sınırları ve Phase 158 devir hazırlığı için dengeli yerel araştırma profili.
  - `conservative_portfolio_acceptance_contracts`: Sıkı kabul eşikleri (%90 checkpoint tamlığı, sıfır blocker, sıfır warning) odaklı muhafazakâr profil.
  - `institutional_portfolio_acceptance_contracts`: Kurumsal denetim izleri, bağımsız doğrulama kanıtları ve model yönetişimi odaklı profil.
  - `audit_portfolio_acceptance_contracts`: Tam bağımsız denetim, gap analizi ve regülasyon uyum odaklı profil.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_PORTFOLIO_ACCEPTANCE_ENABLED=true`: Phase 157 modül etkinliği.
- `PORTFOLIO_ACCEPTANCE_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `PORTFOLIO_ACCEPTANCE_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `PORTFOLIO_ACCEPTANCE_RESEARCH_ONLY=true`: Sadece araştırma ve kabul sözleşmesi tasarımı amaçlı çalışma kısıtı.
- `PORTFOLIO_ACCEPTANCE_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_PORTFOLIO_CONSTRUCTION=false`: Gerçek portföy oluşturma engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_POSITION_SIZING=false`: Gerçek pozisyon büyüklüğü hesaplama engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_PORTFOLIO_OPTIMIZATION=false`: Gerçek optimizasyon engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_RISK_REPORTING=false`: Gerçek risk raporlama engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_SCENARIO_EXECUTION=false`: Gerçek senaryo simülasyonu engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_DRAWDOWN_CONTROL=false`: Gerçek drawdown kontrolü engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_PORTFOLIO_ADJUSTMENT=false`: Otomatik portföy müdahalesi engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_REBALANCE_EXECUTION=false`: Otomatik rebalance engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesabı engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_ALERT_GENERATION=false`: Canlı alarm/uyarı üretimi engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_DASHBOARD_GENERATION=false`: Dashboard üretimi engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `PORTFOLIO_ACCEPTANCE_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `PORTFOLIO_ACCEPTANCE_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Kabul Eşikleri ve Parametreleri
- `PORTFOLIO_ACCEPTANCE_MIN_READINESS_SCORE=0.50`: Asgari kabul edilebilir hazırlık skoru.
- `PORTFOLIO_ACCEPTANCE_MIN_CHECKPOINT_COMPLETION=0.80`: Asgari checkpoint tamamlanma oranı (%80).
- `PORTFOLIO_ACCEPTANCE_MAX_BLOCKERS_ALLOWED=0`: İzin verilen azami blocker sayısı (0).
- `PORTFOLIO_ACCEPTANCE_MAX_GAPS_ALLOWED=5`: İzin verilen azami gap sayısı (5).
- `PORTFOLIO_ACCEPTANCE_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 158 Handoff
- Phase 157; 24 bileşen checkpoint sözleşmesini, Phase 153-156 faz kabul sözleşmelerini, 12 bağımlılık sözleşmesini, 12 doğrulama kanıtı sözleşmesini, 32 NO-GO ve 28 SAFE-GO sınırını, 16 devre dışı bırakılmış yürütme raporunu, 56 yasaklı kolon politikasını, master portföy kabul manifestosunu ve Phase 158 için 12 doğrulanmış devir önkoşulunu teslim eder (`phase_158_handoff.py`).

## Phase 158 Full-System Integration and Advanced Acceptance Rehearsal Configuration

### 1. Sistem Entegrasyon Profilleri
- `FULL_SYSTEM_INTEGRATION_PROFILE="balanced_local_full_system_integration_contracts"`: Varsayılan tam sistem entegrasyon profili (`balanced_local_full_system_integration_contracts`, `strict_non_production_system_integration_safety`, `dry_run_acceptance_rehearsal_focus`).
  - `balanced_local_full_system_integration_contracts`: 36 sistem bileşeni, 32 bağımlılık, 13 checkpoint, 11 sözleşme, 13 manifest, 11 kabul provası ve Phase 159 devir hazırlığı için dengeli yerel entegrasyon profili.
  - `strict_non_production_system_integration_safety`: Sıkı kabul eşikleri, sıfır tolerans (%100 checkpoint tamlığı, sıfır blocker, sıfır gap) ve mutlak güvenlik sınırları odaklı profil.
  - `dry_run_acceptance_rehearsal_focus`: Kuru koşum, sentetik senaryo tatbikatları ve kabul provası simülasyonu odaklı profil.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_FULL_SYSTEM_INTEGRATION_ENABLED=true`: Phase 158 modül etkinliği.
- `FULL_SYSTEM_INTEGRATION_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `FULL_SYSTEM_INTEGRATION_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `FULL_SYSTEM_INTEGRATION_RESEARCH_ONLY=true`: Sadece araştırma ve entegrasyon sözleşmesi tasarımı amaçlı çalışma kısıtı.
- `FULL_SYSTEM_INTEGRATION_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_PORTFOLIO_CONSTRUCTION=false`: Gerçek portföy oluşturma engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_POSITION_SIZING=false`: Gerçek pozisyon büyüklüğü hesaplama engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_PORTFOLIO_OPTIMIZATION=false`: Gerçek optimizasyon engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_RISK_REPORTING=false`: Gerçek risk raporlama engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_SCENARIO_EXECUTION=false`: Gerçek senaryo simülasyonu engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_DRAWDOWN_CONTROL=false`: Gerçek drawdown kontrolü engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_PORTFOLIO_ADJUSTMENT=false`: Otomatik portföy müdahalesi engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_REBALANCE_EXECUTION=false`: Otomatik rebalance engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_REHEARSAL_EXECUTION=false`: Gerçek kabul provası/tatbikat yürütmesi engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_METRIC_CALCULATION=false`: Gerçek metrik hesabı engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_ALERT_GENERATION=false`: Canlı alarm/uyarı üretimi engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_DASHBOARD_GENERATION=false`: Dashboard üretimi engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `FULL_SYSTEM_INTEGRATION_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `FULL_SYSTEM_INTEGRATION_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Kabul Provası, Eşik ve Denetim Parametreleri
- `FULL_SYSTEM_INTEGRATION_MIN_READINESS_SCORE=0.50`: Asgari kabul edilebilir hazırlık skoru.
- `FULL_SYSTEM_INTEGRATION_MIN_CHECKPOINT_COMPLETION=0.80`: Asgari checkpoint tamamlanma oranı (%80).
- `FULL_SYSTEM_INTEGRATION_MAX_BLOCKERS_ALLOWED=0`: İzin verilen azami blocker sayısı (0).
- `FULL_SYSTEM_INTEGRATION_MAX_GAPS_ALLOWED=5`: İzin verilen azami gap sayısı (5).
- `FULL_SYSTEM_INTEGRATION_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 159 Handoff
- Phase 158; 36 sistem bileşeni kaydını, 32 sistem bağımlılığı kaydını, 13 checkpoint sözleşmesini, 11 sistemler arası entegrasyon sözleşmesini, 13 alt sistem manifestosunu, 8 doğrulama kanıtı sözleşmesini, 18 NO-GO, 6 non-production, 5 dry-run ve 10 inceleme kapısı sınırını, 11 kabul provası sözleşmesini, 8 prova checkpoint'ini, 11 alt sistem tanımını, 11 özel sınır politikasını, 13 devre dışı bırakılmış yürütme raporunu, master entegrasyon manifestosunu ve Phase 159 (Final Hardening, Operator Runbook and Release Candidate) için 13 doğrulanmış devir önkoşulunu teslim eder (`phase_159_handoff.py`).

## Phase 159 Final Hardening, Operator Runbook and Release Candidate Configuration

### 1. Hardening ve Release Candidate Profilleri
- `FINAL_HARDENING_PROFILE="balanced_local_final_hardening"`: Varsayılan final hardening profili (`balanced_local_final_hardening`, `strict_release_candidate_hardening`, `dry_run_freeze_focus`).
  - `balanced_local_final_hardening`: 10 bileşen, 7 freeze denetimi, 10 envanter, 16 operatör kılavuzu, 8 RC checklist'i ve Phase 160 devir hazırlığı için dengeli yerel hardening profili.
  - `strict_release_candidate_hardening`: Sıkı doğrulama, sıfır tolerans (%100 checklist tamlığı, sıfır blocker, sıfır gap) ve katı freeze kuralları odaklı profil.
  - `dry_run_freeze_focus`: Kuru koşum, sentetik senaryolar ve freeze doğrulama provaları odaklı profil.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_FINAL_HARDENING_ENABLED=true`: Phase 159 modül etkinliği.
- `FINAL_HARDENING_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `FINAL_HARDENING_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici API/ağ çağrısı yapılamaz.
- `FINAL_HARDENING_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `FINAL_HARDENING_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `FINAL_HARDENING_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `FINAL_HARDENING_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `FINAL_HARDENING_ALLOW_SIGNAL_GENERATION=false`: AL/SAT sinyali üretimi engellenmiştir.
- `FINAL_HARDENING_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi üretimi engellenmiştir.
- `FINAL_HARDENING_ALLOW_PRODUCTION_DEPLOYMENT=false`: Üretim ortamına deploy engellenmiştir.
- `FINAL_HARDENING_ALLOW_RELEASE_PUBLISH=false`: Harici release yayını engellenmiştir.
- `FINAL_HARDENING_ALLOW_REAL_INCIDENT_RESPONSE=false`: Gerçek sistem olay müdahalesi engellenmiştir.
- `FINAL_HARDENING_ALLOW_REAL_RECOVERY=false`: Gerçek sistem kurtarma/restart engellenmiştir.
- `FINAL_HARDENING_ALLOW_BACKTEST_EXECUTION=false`: Gerçek backtest motoru engellenmiştir.
- `FINAL_HARDENING_ALLOW_OPTIMIZER_EXECUTION=false`: Gerçek portföy optimizasyonu engellenmiştir.
- `FINAL_HARDENING_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `FINAL_HARDENING_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `FINAL_HARDENING_ALLOW_FULL_ARTICLE_USAGE=false`: Haber tam metni kullanımı yasaktır (`metadata_only: True`).
- `FINAL_HARDENING_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Release Candidate Eşikleri ve Denetim Parametreleri
- `FINAL_HARDENING_MIN_READINESS_SCORE=0.80`: Asgari kabul edilebilir RC hazırlık skoru.
- `FINAL_HARDENING_MIN_CHECKPOINT_COMPLETION=0.85`: Asgari checkpoint tamamlanma oranı (%85).
- `FINAL_HARDENING_MAX_BLOCKERS_ALLOWED=0`: İzin verilen azami blocker sayısı (0).
- `FINAL_HARDENING_MAX_GAPS_ALLOWED=5`: İzin verilen azami gap sayısı (5).
- `FINAL_HARDENING_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. Phase 160 Handoff
- Phase 159; 10 nihai hardening sözleşmesini, 16 operatör prosedürünü (runbook), 8 release candidate kontrol listesini (checklist), 7 dondurma (freeze) denetimini, 10 sistem envanterini, 10 NO-GO ve 8 Safe-Go sınırını, 10 operatör inceleme kapısını, 8 RC kontrol noktasını, RC bulgular manifestosunu ve Phase 160 (Full Advanced Bot Final Delivery) için 14 doğrulanmış devir önkoşulunu teslim eder (`phase_160_handoff.py`).

## Phase 160 Full Advanced Bot Final Delivery Configuration

### 1. Nihai Teslimat Profilleri
- `FINAL_DELIVERY_PROFILE="balanced_local_final_delivery_package"`: Varsayılan teslimat profili (`balanced_local_final_delivery_package`, `strict_non_production_final_delivery_package`, `dry_run_audit_delivery_package`).
  - `balanced_local_final_delivery_package`: 160 fazlık sistemin tüm envanter, kanıt ve sözleşmelerini yerel dengeli teslimat standartlarında sunar.
  - `strict_non_production_final_delivery_package`: Sıkı güvenlik eşikleri, sıfır blocker (0), sıfır gap (0) ve katı No-Go kuralları odaklı teslimat profili.
  - `dry_run_audit_delivery_package`: Denetim ve kanıt doğrulama odaklı teslimat profili.

### 2. Güvenlik, Çalışma Rejimi ve Sınır Parametreleri
- `ADVANCED_FINAL_DELIVERY_ENABLED=true`: Phase 160 modül etkinliği.
- `FINAL_DELIVERY_DRY_RUN_DEFAULT=true`: Varsayılan simülasyon ve dry-run modu.
- `FINAL_DELIVERY_LOCAL_ONLY=true`: Çevrimdışı ve yerel kısıt; harici ağ çağrısı yapılamaz.
- `FINAL_DELIVERY_RESEARCH_ONLY=true`: Sadece araştırma ve sözleşme tasarımı amaçlı çalışma kısıtı.
- `FINAL_DELIVERY_ALLOW_LIVE_TRADING=false`: Canlı borsa bağlantısı kesinlikle engellenmiştir.
- `FINAL_DELIVERY_ALLOW_BROKER_INTEGRATION=false`: Broker API entegrasyonu kesinlikle engellenmiştir.
- `FINAL_DELIVERY_ALLOW_REAL_ORDER=false`: Gerçek emir oluşturma engellenmiştir.
- `FINAL_DELIVERY_ALLOW_SIGNAL_GENERATION=false`: AL/SAT sinyali üretimi engellenmiştir.
- `FINAL_DELIVERY_ALLOW_INVESTMENT_ADVICE=false`: Yatırım tavsiyesi üretimi engellenmiştir.
- `FINAL_DELIVERY_ALLOW_PRODUCTION_DEPLOYMENT=false`: Üretim ortamına deploy engellenmiştir.
- `FINAL_DELIVERY_ALLOW_MODEL_TRAINING=false`: Model eğitimi engellenmiştir.
- `FINAL_DELIVERY_ALLOW_PREDICTION=false`: Model tahmini engellenmiştir.
- `FINAL_DELIVERY_ALLOW_BACKTEST_EXECUTION=false`: Gerçek backtest motoru engellenmiştir.
- `FINAL_DELIVERY_ALLOW_PORTFOLIO_EXECUTION=false`: Gerçek portföy optimizasyonu engellenmiştir.
- `FINAL_DELIVERY_ALLOW_SOURCE_OVERWRITE=false`: Kaynak veri dosyaları ezilemez (`source_preserved: True`).

### 3. Teslimat ve Plan Kapanış Eşikleri
- `FINAL_DELIVERY_MIN_READINESS_SCORE=0.90`: Asgari kabul edilebilir nihai hazırlık skoru.
- `FINAL_DELIVERY_MAX_BLOCKERS_ALLOWED=0`: İzin verilen azami blocker sayısı (0).
- `FINAL_DELIVERY_MAX_GAPS_ALLOWED=0`: İzin verilen azami gap sayısı (0).
- `FINAL_DELIVERY_SAVE_REPORTS=true`: Raporların diske kaydedilmesi ayarı.

### 4. 160 Fazlık Plan Kapanışı
- Mevcut faz: 160
- Hedef final faz: 160
- Sonraki faz: Yok (`None`)
- 160 Fazlık Plan Durumu: `CLOSED` (`final_plan_closed=True`)
