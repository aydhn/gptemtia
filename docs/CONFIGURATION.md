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







