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



## Phase 105 & 106 Agent Constraints
- Phase 105 raporlamalarında `scraping`, `deployment`, `broker` veya `live_trading` terimlerini pozitif yetenek olarak göstermeyin.
- Phase 106 için agent'a "data provider" görevleri verildiğinde, bunu *sadece* local stub veya resmi API adapter kullanarak çözün, scraping eylemine girişmeyin.
- Yatırım tavsiyesi veremeyeceğinizi daima disclaimer olarak koruyun.

## Phase 111 Agent Constraints
- Agent, haber verisi toplamak için asla web scraping, HTML scraping veya browser automation (Puppeteer/Playwright/Selenium) önermez ve uygulayamaz.
- Agent, haber makalelerinin tam metnini indirmeyi, depolamayı veya telifli içeriği repoya eklemeyi kesinlikle reddeder.
- Sentiment ve impact alanları sorulduğunda, bunların yönlü sinyal veya LLM/NLP modeli olmadığını, yalnızca downstream Phase 112/113 için kategorik sözleşme olduğunu vurgular.
- Agent, API key veya credential gerektiren durumlarda bu değerleri loglarda, konsolda veya kodda açıkça yazamaz.

## Phase 112 Data Quality Agent Constraints
- **Yıkıcı Veri Temizliği Kesinlikle Yasaktır**: Agent, kalite hatalarını düzeltmek bahanesiyle otomatik veri silme, satır çıkarma veya dosya üzerine yazma (auto-overwrite) kodu yazamaz. `destructive_action_allowed` her zaman `False` olmalıdır.
- **Trade Sinyali İddiası Yasaktır**: Agent, kalite skorlarını veya anomali bulgularını hiçbir zaman bir yatırım tavsiyesi, alım/satım sinyali veya kesin piyasa tahmini olarak sunamaz.
- **Scraping / Tam Metin Yasağı**: Agent, eksik haber verilerini tamamlamak için web scraping veya harici LLM / vektör veritabanı API çağrısı yapamaz.
- **Phase 113 Normalizasyon Yönlendirmesi**: Format, sembol veya zaman damgası uyumsuzlukları görüldüğünde yerinde mutasyon yerine Phase 113 normalizasyon katmanına devir kaydı oluşturulmalıdır.

## Phase 113 Data Normalization Agent Constraints
- **In-Place Mutation Yasağı**: Agent, normalizasyon fonksiyonlarında `raw_df`'i doğrudan değiştiremez; her zaman `df.copy()` kullanmalı ve normalize edilmiş değerleri yeni sütunlara (`normalized_<field>`) yazmalıdır.
- **Deduplication / Kayıt Silme Yasağı**: Agent, mükerrer kayıtları silen kod yazamaz. Sadece `canonical_duplicate_key` oluşturmalı ve `destructive_action_allowed: False` politikasını korumalıdır.
- **Ticaret Sinyali İddiası Yasağı**: Agent, normalize edilmiş verileri, kanonik şemaları veya normalizasyon skorlarını al/sat sinyali veya yatırım tavsiyesi olarak sunamaz.
- **Resmi Onay İddiası Yasağı**: Agent, normalizasyon motoru başarıyla çalıştığında resmi onay, broker readiness veya compliance sign-off iddiasında bulunamaz.
- **Scraping / LLM / Vector DB Yasağı**: Agent, sembol veya etiket normalizasyonu için harici LLM inference veya web scraping kodu ekleyemez.
- **Phase 114 Lineage Devri**: Her normalizasyon kuralı ve manuel inceleme gereksinimi için Phase 114 veri soy kütüğü hazırlık kaydı (`phase_114_handoff.py`) üretilmelidir.

## Phase 114 Data Lineage and Provenance Agent Constraints
- **Zero Destructive Actions**: Agent, veri soy kütüğü izlerken veya eksik bağlantı tespit ettiğinde kaynak dosyaları ezemez, silemez veya taşıyamaz (`source_preserved: True`, `destructive_action_allowed: False`).
- **No Lineage Score as Signal**: Agent, soy kütüğü veya izlenebilirlik skorlarını ([0.0, 1.0]) kesinlikle bir ticaret sinyali, alım/satım tavsiyesi veya alfa faktörü olarak yorumlayamaz ve sunamaz.
- **No Official Approval Claims**: Agent, izlenebilirlik kayıtları tam olsa dahi, "resmi sağlayıcı onayı", "regülatör uygunluğu" veya "production readiness" iddiasında bulunamaz.
- **No External Graph or Vector DB**: Agent, veri soy kütüğü grafı için harici Neo4j, RedisGraph, Pinecone, Chroma vb. veritabanı veya embedding modeli kuramaz; yalnızca in-memory pandas/tablo temsili (`lineage_graph_placeholder.py`) kullanılabilir.
- **Strict Anti-Scraping and Zero Full-Text**: Agent, haber soy kütüğünde yalnızca metadata referanslarına izin vermelidir (`metadata_only: True`). Web scraping, HTML kazıma veya haber tam metni indirme kesinlikle yasaktır.
- **No Credential Exposure**: Agent, kaynak referanslarında veya sağlayıcı metadata kayıtlarında API anahtarlarını, şifreleri veya gizli dizgileri asla saklayamaz veya loglayamaz (`contains_credentials: False`).
- **Phase 115 Benchmark Devri**: Agent, sonraki faz olan Phase 115 (Data Provider Benchmark Report) için yalnızca girdi verisi hazırlar; benchmark sonuçlarını veya sıralamalarını Phase 114'te peşinen ilan edemez.

## Phase 115 Data Provider Benchmark Agent Constraints
- **No Benchmark Score as Trading Signal**: Agent, provider benchmark skorlarını ([0.0, 1.0]) kesinlikle al/sat sinyali veya yatırım tavsiyesi olarak sunamaz.
- **No Official Approval / Production / Broker Ready Claims**: Agent, hiçbir sağlayıcıyı "approved", "production ready" veya "broker ready" ilan edemez (`official_approval: False`, `production_ready: False`, `broker_ready: False`).
- **No Live API Calls / Real Data Downloads**: Agent, benchmark çalıştırmak için canlı sağlayıcı API çağrısı veya gerçek veri indirme zorunluluğu getiremez; local/offline profiller ve fikstürler kullanılmalıdır.
- **Zero Scraping & Zero Full-Text**: Web scraping, HTML kazıma, haber tam metni toplama veya telifli içerik kopyalama kesinlikle yasaktır (`metadata_only: True`).
- **Zero Destructive Cleaning / Overwrites**: Agent, kaynak verileri ezemez, silemez veya mutasyona uğratamaz; manuel inceleme kuyrukları `destructive_action_allowed: False` olarak kalmalıdır.
- **No Web Server / UI Dashboard / External LLM / Vector DB**: Flask/FastAPI, web dashboard, vektör veri tabanı veya bulut LLM API'leri eklenemez.
- **Phase 116 Feature Engine Handoff**: Phase 116 için yalnızca veri hazırlık gereksinimleri sunulur; gösterge, özellik (feature) veya sinyal üretilmez.
- **Current Phase: 115, Next Phase: 116 (Advanced Indicator/Feature/Factor Engine), Target Final Phase: 160**.

## Phase 116 Advanced Indicator/Feature/Factor Engine Agent Constraints
- **Strictly Non-Signal**: Agent, hiçbir feature/indicator değerini ticaret sinyali, al/sat kuralı veya yönlü tavsiye olarak kodlayamaz (`non_signal: True`).
- **Forbidden Column Names Enforcement**: Agent, DataFrame çıktılarında `signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation` isimli kolonları kesinlikle üretemez.
- **Non-Destructive Transform Enforcement**: Agent, feature dönüşümlerinde girdi DataFrame'ini asla in-place değiştiremez; daima `df.copy()` döndürmelidir.
- **No Lookahead Bias**: Agent, `shift(-1)` veya geleceğe dönük indeks erişimi yapamaz; rolling pencereleri yalnızca `[t - window + 1 : t]` verisini kullanmalıdır.
- **Pure Pandas/NumPy Transformations**: Dış C kütüphanesi veya ta-lib zorunluluğu getirilmemeli; saf pandas ve numpy dönüşümleri kullanılmalıdır.
- **Zero Full-Text & Zero Scraping**: Haber özellikleri strictly metadata-only kalmalı, web scraping veya HTML kazıma yapılmamalıdır.
- **No Broker / Live Trading / Optimizer**: Broker entegrasyonu, gerçek emir, backtest veya parametre optimizasyonu kesinlikle yasaktır.
- **Current Phase: 116, Next Phase: 117 (Technical Indicator Expansion), Target Final Phase: 160**.

## Phase 117 Technical Indicator Expansion Agent Constraints
- **Strictly Non-Signal**: Agent, teknik indikatör kütüphanesinde hiçbir AL/SAT kuralı, long/short pozisyonu, hedef fiyat veya tavsiye üretemez (`non_signal: True`).
- **Forbidden Column Enforcement**: Çıktı kolon adlarında `signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation`, `future_return`, `forward_return`, `next_return` bulunamaz. MACD'de smoothing çizgisi zorunlu olarak `macd_smooth` olmalıdır.
- **Zero Lookahead Bias**: `shift(-1)` veya geleceğe dönük zaman serisi kaydırmaları kesinlikle yasaktır; tüm hesaplamalar geçmiş ve mevcut barla sınırlıdır.
- **Immutable Input**: Girdi DataFrame'leri kesinlikle yerinde (in-place) değiştirilemez; her hesaplama `out = df.copy()` ile başlamalıdır.
- **No TA-Lib Dependency**: Hesaplamalar saf Python, pandas ve numpy tabanlı olmalı, harici TA-Lib C kütüphanesi zorunluluğu konulmamalıdır.
- **Warmup NaN Policy**: Başlangıç penceresi eksik verileri doldurulmamalı veya satırlar silinmemelidir (`preserve_nan_no_fill_no_delete`).
- **No Broker / Live Trading / Optimizer / Strategy Generation**: Broker bağlantısı, gerçek emir, backtest simülasyonu, strateji üretimi veya optimizer kesinlikle yasaktır.
- **Phase 118 Grid Readiness**: Çoklu pencere üretimi için fonksiyonlar parametrik pencere imzasına sahip olmalı ve Phase 118'e hazır devredilmelidir.
- **Current Phase: 117, Next Phase: 118 (Multi-Window Feature Grid), Target Final Phase: 160**.
## Phase 118 Multi-Window Feature Grid Agent Constraints
- **Strictly Non-Signal**: Agent, multi-window feature grid katmanında hiçbir al/sat sinyali, hedef etiket, pozisyon veya yönlü tahmin üretemez (`non_signal: True`, `allow_feature_grid_as_signal: False`).
- **Forbidden Column Enforcement**: Grid kolon adlarında `signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation`, `future_return`, `forward_return` kelimeleri kesinlikle bulunamaz.
- **Strictly Backward-Looking (No Lookahead Bias)**: Agent, `shift(-1)` veya geleceğe dönük zaman serisi indeks kaydırmalarını kullanamaz. Tüm pencere operasyonları geçmiş verilerle sınırlıdır.
- **Immutable Input**: Girdi DataFrame'leri kesinlikle mutasyona uğratılamaz; tüm hesaplama fonksiyonları `out = df.copy()` ile başlamalıdır.
- **Standard Deterministic Naming**: Kolon adları snake_case standardına uymalı (`sma_w20`, `rsi_w14`, `bb_width_w20_std2`); parametre sırası ve kısaltmalar deterministik olmalıdır.
- **Preserve Warmup NaN Policy**: Büyük pencere ısınma NaN değerleri asla doldurulmamalı (`no_forward_fill`) veya satırlar silinmemelidir (`no_auto_drop`).
- **Duplicate Feature Flagging**: Mükerrer kolonlar veya aynı zaman serisini üreten varyantlar otomatik silinmez; manuel inceleme için bayraklandırılır (`flag_for_manual_review`).
- **No Broker / Live Trading / Optimizer / Strategy Generation / Backtest**: Broker bağlantısı, gerçek emir iletimi, model eğitimi, strateji backtesti veya parametre optimizasyonu kesinlikle yasaktır.
- **Phase 119 Cross-Asset Alignment Readiness**: Grid çıktıları çapraz varlık senkronizasyonu için standartlaştırılmış formatta sunulmalıdır.
- **Current Phase: 118, Next Phase: 119 (Cross-Asset Feature Alignment), Target Final Phase: 160**.

## Phase 119 Cross-Asset Feature Alignment Agent Constraints
- **Strict Non-Signal Cross-Asset Layer**: Agent, çapraz varlık hizalamasını kesinlikle arbitraj sinyali, pairs trading kuralı, korelasyon trade stratejisi veya alım-satım tavsiyesi olarak yapılandıramaz (`non_signal: True`, `arbitrage_signals_allowed: False`).
- **Backward-Only Asof Join Enforcement**: Zaman serisi birleştirmelerinde yalnızca `direction="backward"` kullanılabilir (`safe_asof_join_backward`). İleriye dönük (forward veya nearest forward) birleştirmeler veri sızıntısı oluşturacağı için kesinlikle yasaktır.
- **Zero Target/Prediction/Label Generation**: Manifest ve matrislerde `target`, `label`, `prediction`, `y_val` gibi denetimli makine öğrenmesi hedef kolonları üretilemez (`contains_target_or_prediction: False`).
- **Standardized Feature Namespace**: Tüm kolonlar `<domain>__<family>__<source_symbol>__<feature_name>__<window>` formatına uymalı ve yasaklı kelime filtresinden geçmelidir.
- **Metadata-Only News Integration**: Haber verileriyle hizalama yapılırken kesinlikle web scraping veya tam metin indirme yapılmamalı; yalnızca duygu etiketi, konu ve zaman damgası kullanılmalıdır.
- **Current Phase: 119, Next Phase: 120 (Macro/Calendar/News Feature Fusion & Composite Factor Engineering), Target Final Phase: 160**.

## Phase 120 Macro/Calendar/News Feature Fusion Agent Constraints
- **Strict Non-Signal Fusion Layer**: Agent, makro/takvim/haber fusion katmanında hiçbir al/sat sinyali, alım-satım kuralı, yönlü tahmin veya trade tavsiyesi üretemez (`non_signal: True`, `allow_fusion_as_signal: False`).
- **Forbidden Term Enforcement**: Fusion matrislerinde, sözleşmelerinde veya metadata kayıtlarında `signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation` kelimeleri yer alamaz.
- **Strictly Backward-Only Asof Joins**: Bütün zaman serisi birleştirmeleri geriye dönük (`direction="backward"`) olmalıdır (`safe_fusion_asof_join_backward`). Forward veya nearest birleştirmeler kesinlikle yasaktır.
- **Macro Release Lag Enforcement**: Makro veriler fiyata bağlanırken mutlaka `release_timestamp <= base_timestamp` koşulu aranmalıdır. Referans periyodu geçmiş olsa bile henüz yayınlanmamış makro verinin fiyata bağlanması lookahead bias kabul edilir ve engellenir.
- **Strictly Metadata-Only News Fusion**: Haber tarafında kesinlikle web scraping, HTML indirme veya tam metin analizi yapılmamalıdır (`metadata_only: True`). Yalnızca konu etiketi, varlık etiketi, zaman damgası tazeliği ve olay referansı kullanılabilir.
- **Immutable Input**: Girdi DataFrame'leri kesinlikle mutasyona uğratılamaz; tüm birleştirme ve dönüşüm fonksiyonları `df.copy()` ile başlamalıdır.
- **Zero Model Training / Optimization / Strategy Generation**: Katmanda hiçbir makine öğrenmesi modeli eğitilemez, hiperparametre optimizasyonu veya strateji backtesti koşturulamaz.
- **Phase 121 Readiness**: Çıktılar Phase 121 için eksiksiz manifest, metadata ve bağımlılık kayıtlarıyla hazırlanmalıdır.
- **Current Phase: 120, Next Phase: 121, Target Final Phase: 160**.

## Phase 121 Feature Validation and No-Lookahead Guard Agent Constraints
- **Strict Non-Signal & Non-Destructive Invariant**: Agent, feature doğrulama katmanında hiçbir alım/satım tavsiyesi üretemez ve anomalileri otomatik olarak silemez (`destructive_action_allowed: False`, `non_signal: True`).
- **Forbidden Column Quarantine**: `buy`, `sell`, `signal`, `target`, `label`, `prediction`, `recommendation`, `position` gibi terimler içeren kolonlar tespit edildiğinde silinmez; derhal tespit kaydı (`finding`) açılıp manuel inceleme kuyruğuna alınır.
- **No-Lookahead Invariant**: `shift(-1)`, `lead()`, `future_return` veya `release_timestamp > base_timestamp` gibi sızıntılar tespit edildiğinde hata bayrağı kaldırılır ve downstream tüketim engellenir.
- **Backward-Only Joins**: Bütün asof birleştirmelerinde `direction="backward"` zorunludur.
- **Warmup NaN Preservation**: Başlangıç penceresi NaN değerleri sentetik olarak doldurulamaz ve satırlar otomatik olarak atılamaz.
- **Immutable Provenance**: Bütün matris doğrulamalarında SHA-256 tabanlı kontrol toplamı (`checksum`) içeren Feature Matrix Integrity Manifest üretilmelidir.
- **Phase 122 Handoff**: Doğrulanan feature'lar Phase 122 Faktör Metadata ve Faktör Aileleri için temiz ve hazır olarak devredilmelidir.
- **Current Phase: 121, Next Phase: 122 (Factor Metadata and Factor Families), Target Final Phase: 160**.

## Phase 122 Factor Metadata and Factor Families Agent Constraints
- **Strict Non-Signal & Research Taxonomy Invariant**: Agent, faktör metadata ve taksonomi katmanında kesinlikle AL/SAT sinyali, alım-satım kuralı, long/short pozisyonlama, hedef getiri veya model tahmini üretemez (`non_signal: True`, `contains_prediction_or_target: False`).
- **Canonical Factor Namespace**: Faktör ad alanları `factor__<family>__<asset_class>__<symbol>__<factor_name>__<window>` standart formatına harfiyen uymalıdır.
- **Forbidden Claims Enforcement**: Faktör açıklamalarında veya metadata alanlarında 14 yasaklı regex deseninden herhangi biri (`buy signal`, `sell signal`, `trade recommendation`, `alpha forecast` vb.) yer alamaz.
- **Non-Destructive Governance**: Eksik veya biçimsiz faktör girdileri asla sessizce silinemez veya ezilemez (`destructive_action_allowed: False`, `source_preserved: True`). İncelemeler Manuel İnceleme Kuyruğuna (`manual_review_queue`) yönlendirilir.
- **Metadata-Only News Attention**: Haber dikkat faktörleri yalnızca sayısal metadata (frekans, etiket sayıları, tazelik) düzeyinde kalmalıdır; sıfır tam metin, sıfır web scraping, sıfır NLP duygu modeli veya embedding ilkesine kesin bağlı kalınmalıdır.
- **Factor Contract & Dependency Integrity**: Her faktör ailesi 12 sözleşmeye ve 17 kayıtlı bağımlılığa (Phase 116-121 girdilerine) bağlı kalmalıdır.
- **Current Phase: 122, Next Phase: 123 (Feature Quality and Drift Diagnostics), Target Final Phase: 160**.

## Phase 123 Feature Quality and Drift Diagnostics Agent Constraints
- **Strict Non-Signal & Research Diagnostics Invariant**: Agent, feature kalite ve drift tanı katmanında kesinlikle AL/SAT sinyali, alım-satım kuralı, drift tabanlı trade tetiği veya model tahmini üretemez (`non_signal: True`, `allow_quality_drift_as_signal: False`).
- **Non-Destructive & No-Auto-Drop Invariant**: Kusurlu veya aşırı kayma gösteren feature'lar asla otomatik olarak silinemez (auto-drop), doldurulamaz (auto-impute) veya kaynak dosyalar yerinde ezilemez (`destructive_action_allowed: False`, `auto_drop_allowed: False`, `auto_fix_allowed: False`, `source_preserved: True`). Bütün tespitler Manuel İnceleme Kuyruklarına aktarılmalıdır.
- **Forbidden Claims Enforcement**: Rapor ve manifest üretilirken 11 yasaklı claim terimi (`buy_signal`, `sell_signal`, `target_column`, `future_return`, `article_body_raw`, `web_scraping_enabled`, `auto_drop_executed`, `auto_impute_executed`, `live_trading_approved`, `official_production_approval` vb.) asla kullanılamaz.
- **Strict Metadata-Only Boundary**: Makro, takvim ve haber kontrolleri kesinlikle metadata-only sınırında kalmalıdır; sıfır tam metin, sıfır scraping, sıfır embedding vektörü.
- **Factor Family Coverage**: Phase 122'deki 10 faktör ailesinin tamamı kalite, drift, veri mevcudiyeti ve bağımlılık testlerinden geçirilmelidir.
- **Phase 124 Handoff Requirements**: Kalite ve drift skorları, manifestolar ve engelleyici durumlar Phase 124 Feature Store Entegrasyonu katmanı için eksiksiz devredilmelidir (`phase_124_handoff.py`).
- **Current Phase: 123, Next Phase: 124 (Feature Store Integration and Time-Series Feature Serving Layer), Target Final Phase: 160**.
## Phase 124 Feature Store Integration Agent Constraints
- **Strict Non-Signal & Research Store Invariant**: Agent, feature store katmanında kesinlikle AL/SAT sinyali, alım-satım kuralı, depo verisi üzerinden işlem tetiği, model tahmini veya hedef getiri üretemez (`non_signal: True`, `allow_feature_store_as_signal: False`).
- **Canonical Store Namespace**: Feature anahtarları ve ad alanları `entity__namespace__feature_name` snake_case standardına uymalıdır. İzin verilen entity önekleri: `fx`, `commodity`, `macro`, `calendar`, `news`, `cross_asset`, `factor`, `quality_drift`, `validation`.
- **Forbidden Columns Enforcement**: Depo şemalarında veya kolonlarında 20 yasaklı kolon terimi (`signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation`, `future_return`, `forward_return`, `next_return`, `full_text`, `article_body`, `raw_content`, `scraped_html`, `page_html`, `embedding`, `vector`) asla yer alamaz.
- **Non-Destructive & Source Preservation Invariant**: Ham kaynak girdileri asla silinemez, üzerine yazılamaz, otomatik doldurulamaz veya atılamaz (`source_preserved: True`, `destructive_action_allowed: False`, `auto_drop_allowed: False`, `auto_fix_allowed: False`).
- **Validation-Aware Storage Requirement**: Tüm feature kayıtları doğrulama durumu (`VALIDATION_PASS`, `VALIDATION_WARN`, `VALIDATION_FAIL`), kalite skoru, drift skoru ve blocker bayrakları ile birlikte depolanmalıdır.
- **Strict Metadata-Only Boundary**: Haber metadata depolarında asla haber tam metni, web kazıma içeriği veya embedding vektörleri yer alamaz.
- **Current Phase: 124, Next Phase: 125 (Feature/Factor Engine Acceptance Report and Block Finalization), Target Final Phase: 160**.

## Phase 125 Feature/Factor Engine Acceptance Report Agent Constraints
- **Strict Non-Signal & Structural Acceptance Invariant**: Agent, blok kabul raporu ve manifestosunda kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, hedef değişken veya canlı işlem onayı üretemez (`non_signal: True`, `official_approval: False`, `production_ready: False`, `broker_ready: False`).
- **Readiness Score Boundary**: Kabul skoru yalnızca yapısal sözleşme ve geçit kontrolü metriğidir (0.0-1.0 aralığı); asla resmi ticari onay veya kârlılık güvencesi olarak sunulamaz.
- **Non-Destructive & Source Preservation Invariant**: Blok kabulü sırasında ham kaynak verileri asla silinemez, üzerine yazılamaz, otomatik doldurulamaz veya elenemez (`destructive_action_allowed: False`, `source_preserved: True`, `auto_drop_allowed: False`, `auto_fix_allowed: False`).
- **6-Way Compliance Integrity**: Modüller non-signal, no-lookahead, yasaklı kolon blokajı, haber sadece-metaveri, kaynak koruma ve feature store entegrasyonu açısından eksiksiz denetlenmelidir.
- **Contract & Gates Audit**: 16 kabul geçidi, 9 dokümantasyon sözleşmesi, 20 operasyonel betik sözleşmesi ve 10 test sözleşmesi 100% geçmelidir.
- **Phase 126 Regime Handoff Invariant**: Phase 116-125 bloğu kabul edilmiş sayılır ve 12 devir kalemi ile Phase 126 (Regime Classification and Market Behavior Foundation) fazına devredilir (`phase_126_handoff.py`).
- **Current Phase: 125, Next Phase: 126 (Regime Classification and Market Behavior Foundation), Target Final Phase: 160**.

## Phase 126 Regime Classification and Market Behavior Foundation Agent Constraints
- **Strict Non-Signal & Research Foundation Invariant**: Agent, rejim sınıflandırma ve piyasa davranışı temel katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef getiri, model tahmini veya işlem kararı üretemez (`non_signal: True`, `allow_regime_as_signal: False`).
- **No Model Training & No Clustering Invariant**: Bu fazda HMM, GMM, K-Means, DBSCAN, SVM, Random Forest veya herhangi bir ML modeli eğitilemez, fit/transform veya cluster execution yapılamaz (`allow_model_training: False`, `allow_clustering_execution: False`). Yalnızca kural tabanlı taksonomiler, sözleşmeler ve metadata defterleri oluşturulur.
- **Canonical Regime State Naming**: Tüm rejim durumları zorunlu olarak `regime_state_` öneki ile başlamalıdır (örn. `regime_state_high_volatility`). 20 yasaklı kolon ve terim (`signal`, `buy`, `sell`, `long`, `short`, `position`, `target`, `label`, `prediction`, `recommendation`, `future_return`, `forward_return`, `next_return` vb.) rejim çıktılarında yer alamaz.
- **Strict Metadata-Only Environmental Boundary**: Haber metadata bağlamında asla haber tam metni, web scraping veya telifli içerik bulunamaz (`metadata_only: True`, `allow_web_scraping: False`, `allow_full_article_usage: False`).
- **Non-Destructive & Source Preservation Invariant**: Kaynak veriler ve Phase 116-125 feature tabloları asla silinemez, üzerine yazılamaz veya otomatik temizliğe tabi tutulamaz (`source_preserved: True`, `destructive_action_allowed: False`, `auto_drop_allowed: False`, `auto_fix_allowed: False`).
- **No Official Approval / Production Ready Claims**: Rapor ve çıktılarda `official_approval`, `production_ready`, `broker_ready` veya kârlılık iddiaları kesinlikle bulunamaz (`allow_official_approval_claim: False`).
- **Phase 127 Handoff Invariant**: Phase 126 çıktıları, 12 yapılandırılmış girdi kalemi ile Phase 127 (Regime Feature Matrix and State Dataset Contracts) fazına eksiksiz devredilir (`phase_127_handoff.py`).
- **Current Phase: 126, Next Phase: 127 (Regime Feature Matrix and State Dataset Contracts), Target Final Phase: 160**.

## Phase 127 Regime Feature Matrix and State Dataset Contracts Agent Constraints
- **Strict Non-Signal & Research Dataset Invariant**: Agent, feature matrix veya state dataset çıktılarında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, pozisyon kararı veya getiri tahmini üretemez (`non_signal: True`, `contains_target_or_prediction: False`).
- **No Target/Label/Prediction Generation**: Aday bağlamlar (`candidate_contexts`) yalnızca araştırma bayraklarıdır; kesinlikle hedef etiket (`target_label`), supervised sınıf etiketi veya prediction olarak kullanılamaz (`candidate_contexts_as_targets: False`).
- **Zero Model Training / Clustering Execution**: Bu fazda HMM, GMM, K-Means veya herhangi bir gözetimli/gözetimsiz model çalıştırılamaz (`allow_model_training: False`, `allow_clustering_execution: False`). Yalnızca veri kümesi sözleşmeleri, şemalar ve hizalama kuralları tanımlanır.
- **Strict Backward-Only Timestamp Alignment**: Zaman damgalı birleştirmelerde daima geriye-dönük (`direction='backward'`) asof join kullanılmalıdır. `context_timestamp <= base_timestamp` temporal sırası garanti edilmeli; ileriye dönük sızıntı (`shift(-1)`, `lead()`, `t+1`) kesinlikle engellenmelidir (`allow_lookahead: False`).
- **Source Preservation & Zero Destructive Mutation**: Girdi tabloları her zaman `df.copy()` ile korunmalıdır. Ham kaynaklar üzerine yazılamaz (`allow_source_overwrite: False`), otomatik veri doldurma (`auto_imputation: False`) veya otomatik sütun düşürme (`auto_feature_drop: False`) yapılamaz.
- **Strict News Metadata-Only Boundary**: Haber verileri strictly metadata-only (ilgi skoru, varlık etiketleri, tazelik) kalmalı; web scraping veya haber tam metni kullanımı kesinlikle yasaktır (`allow_web_scraping: False`, `allow_full_article_usage: False`).
- **Phase 128 Handoff Invariant**: Phase 127 çıktıları, 12 devir kalemi ile Phase 128 (Regime Rule-Free Labeling Contracts and Unsupervised Prep) fazına eksiksiz devredilir (`phase_128_handoff.py`).
- **Current Phase: 127, Next Phase: 128 (Regime Rule-Free Labeling Contracts and Unsupervised Prep), Target Final Phase: 160**.

## Phase 128 Regime Rule-Free Labeling Contracts and Unsupervised Prep Agent Constraints
- **Strict Non-Signal & Candidate State Invariant**: Agent, kural-bağımsız etiketleme ve aday durum hazırlık katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya denetimli sınıf etiketi üretemez (`non_signal: True`, `contains_target_or_prediction: False`).
- **Rule-Free Labeling Meaning**: "Rule-free labeling" kavramı kesinlikle supervised target label veya trade label değildir; salt denetimsiz aday durum hazırlık sözleşmesidir (`rule_free_is_supervised_target: False`).
- **Zero-Execution Invariant**: Bu fazda KMeans, DBSCAN, GMM, HDBSCAN, SOM gibi kümeleme algoritmaları; PCA, UMAP, t-SNE, Autoencoder gibi boyut indirgeme modelleri veya herhangi bir ML fit/train/predict/transform operasyonu kesinlikle çalıştırılamaz (`clustering_executed: False`, `model_training_executed: False`, `dimensionality_reduction_executed: False`). Yalnızca sözleşmeler, şemalar ve yer tutucu defterleri oluşturulur.
- **Strict No-Lookahead Boundary**: Zaman damgalı birleştirmelerde `context_ts <= base_ts` temporal sırası garanti edilmeli; ileriye dönük sızıntı (`shift(-1)`, `lead()`, `t+1`, `future_return`) kesinlikle engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi tabloları her zaman `df.copy()` ile korunmalı, ham kaynaklar üzerine asla yazılmamalı, otomatik veri doldurma (`auto_imputation`) veya otomatik feature silme (`auto_drop`) yapılmamalıdır.
- **Strict News Metadata-Only Boundary**: Haber verileri strictly metadata-only kalmalı; web scraping veya haber tam metni kullanımı kesinlikle yasaktır (`allow_web_scraping: False`, `allow_full_article_usage: False`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready` veya kârlılık iddiaları kesinlikle yasaktır.
- **Phase 129 Handoff Invariant**: Phase 128 çıktıları, 12 devir kalemi ile Phase 129 (Market Behavior Diagnostics and Regime Quality) fazına eksiksiz devredilir (`phase_129_handoff.py`).
- **Current Phase: 128, Next Phase: 129 (Market Behavior Diagnostics and Regime Quality), Target Final Phase: 160**.

## Phase 129 Market Behavior Diagnostics and Regime Quality Agent Constraints
- **Strict Non-Signal & Behavior Quality Invariant**: Agent, market behavior diagnostics ve candidate-state quality katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya herhangi bir yönlü iddia üretemez (`non_signal: True`, `allow_quality_as_signal: False`, `allow_behavior_as_signal: False`, `allow_candidate_state_as_signal: False`).
- **Behavior Quality Score Non-Signal Invariant**: Hesaplanan davranış kalite skoru ([0.0, 1.0]) asla "score yüksek → long", "trend quality iyi → alım zamanı" veya benzeri işlem yorumuna dönüştürülemez (`allow_directional_claim: False`, `official_approval: False`, `production_ready: False`).
- **Zero-Execution Invariant**: Bu fazda KMeans, DBSCAN, GMM, HDBSCAN, SOM kümeleme algoritmaları; PCA, UMAP, t-SNE boyut indirgeme yöntemleri; herhangi bir ML model fit/train/predict/transform; backtest; optimizer kesinlikle çalıştırılamaz (`clustering_executed: False`, `model_training_executed: False`, `unsupervised_execution: False`).
- **Strict No-Lookahead Boundary**: Behavior diagnostics raporlarında `shift(-1)`, `lead()`, `future_return`, negatif kaydırma ve geleceğe referans veren kolonlar kesinlikle kullanılamaz.
- **Source Preservation & Zero Auto-Modification**: Diagnostics raporları kaynak verileri değiştirmez, sıfırlamaz veya üzerine yazmaz. Otomatik veri doldurma (`auto_imputation: False`) ve otomatik özellik silme (`auto_drop: False`) kesinlikle yasaktır (`destructive_action_allowed: False`, `source_preserved: True`).
- **Strict News Metadata-Only Boundary**: Haber metadata behavior diagnostics'te kesinlikle haber tam metni, `article_body`, web scraping, NLP duygu modeli veya embedding kullanılamaz (`contains_full_text: False`, `sentiment_model_executed: False`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım getirisi iddiaları kesinlikle yasaktır.
- **Phase 130 Handoff Invariant**: Phase 129 çıktıları, 12 devir kalemi ile Phase 130 (Regime Transition and Stability Analysis) fazına eksiksiz devredilir (`phase_130_handoff.py`).
- **Current Phase: 129, Next Phase: 130 (Regime Transition and Stability Analysis), Target Final Phase: 160**.

## Phase 130 Regime Transition and Stability Analysis Agent Constraints
- **Strict Non-Signal & Transition Diagnostics Invariant**: Agent, rejim geçiş ve kararlılık analizi katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya yönlü iddia üretemez (`non_signal: True`, `allow_transition_as_signal: False`, `allow_stability_as_signal: False`).
- **Zero-Execution Invariant**: Bu fazda Markov zinciri uydurma (`markov_chain_fitted: False`), ileriye dönük durum olasılığı projeksiyonu (`forward_probability_generated: False`), KMeans/DBSCAN/GMM kümeleme veya ML model fitting/inference kesinlikle yürütülemez (`model_training_allowed: False`, `clustering_allowed: False`). Geçiş matrisleri yapısal yer tutucu niteliğindedir.
- **Strict No-Lookahead Boundary**: Zaman damgalı sekans analizlerinde strictly monotonic UTC sıralaması esastır. `context_timestamp <= base_timestamp` temporal sırası garanti edilmeli; `shift(-1)`, `lead()`, `future_return`, negatif shift ve geleceğe referans veren etiketler kesinlikle engellenmelidir.
- **Source Preservation & Zero Auto-Modification**: Geçiş analizleri girdi verilerini in-place değiştirmez (`df.copy()` zorunludur). Otomatik eksik veri doldurma (`auto_imputation: False`) ve otomatik özellik düşürme (`auto_drop: False`) yasaktır (`destructive_action_allowed: False`, `auto_fix_forbidden: True`).
- **Strict News Metadata-Only Boundary**: Haber geçiş bağlamında kesinlikle haber tam metni, `article_body`, web scraping, NLP duygu modeli veya embedding kullanılamaz (`full_text_used: False`, `scraping_executed: False`, `sentiment_model_used: False`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım getirisi iddiaları kesinlikle yasaktır (`validate_no_forbidden_transition_claims`).
- **Phase 131 Handoff Invariant**: Phase 130 çıktıları, 9 devir kalemi ile Phase 131 (Cross-Asset Regime Context and Dynamic Behavior Interplay) fazına eksiksiz devredilir (`phase_131_handoff.py`).
- **Current Phase: 130, Next Phase: 131 (Cross-Asset Regime Context and Dynamic Behavior Interplay), Target Final Phase: 160**.

## Phase 131 Cross-Asset Regime Context Expansion Agent Constraints
- **Strict Non-Signal & Multi-Domain Regime Context Invariant**: Agent, cross-asset rejim bağlamı genişletme katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`), ikili işlem (pairs trading) stratejisi veya yönlü iddia üretemez (`non_signal: True`, `allow_context_as_signal: False`, `allow_pairs_trading_signals: False`).
- **Context, Correlation & Divergence/Convergence Meaning**: Hesaplanan korelasyon, lead-lag ilişkileri, ayrışma (divergence) ve yakınsama (convergence) metrikleri kesinlikle işlem sinyali, arbitraj fırsatı veya getiri beklentisi olarak yorumlanamaz; salt araştırma amaçlı çoklu-etki alanı rejim bağlam tanımlayıcılarıdır (`allow_directional_claim: False`).
- **Zero-Execution & Model Training Prohibition**: Bu fazda kümeleme (KMeans, DBSCAN, GMM, HDBSCAN, SOM), boyut indirgeme (PCA, UMAP, t-SNE), regresyon veya herhangi bir makine öğrenmesi modeli eğitilemez, fit/predict/transform yürütülemez (`clustering_executed: False`, `model_training_executed: False`). Korelasyon ve lead-lag şablonları yapısal yer tutucu niteliğindedir.
- **Strict Backward-Only Timestamp Alignment**: Çoklu-etki alanı (FX, emtia, makro, takvim, haber metadata) zaman damgalı birleştirmelerinde strictly backward-looking (`direction='backward'`) asof join uygulanmalıdır. `context_timestamp <= base_timestamp` temporal sırası garanti edilmeli; ileriye dönük sızıntı (`shift(-1)`, `lead()`, `future_return`, negatif kaydırma) kesinlikle engellenmelidir (`allow_lookahead: False`).
- **Source Preservation & Zero Auto-Destructive Modification**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Ham kaynak dosyalar üzerine yazılamaz (`allow_source_overwrite: False`), otomatik veri doldurma (`auto_imputation: False`) ve otomatik özellik silme (`auto_feature_drop: False`) kesinlikle yasaktır (`destructive_action_allowed: False`, `source_preserved: True`).
- **Strict News Metadata-Only Boundary**: Haber etki alanı bağlamında kesinlikle haber tam metni, `article_body`, web scraping, NLP duygu modeli veya embedding kullanılamaz; salt başlık frekansı, varlık etiketleri ve tazelik gecikmesi ile sınırlıdır (`full_text_used: False`, `scraping_executed: False`, `sentiment_model_used: False`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım getirisi iddiaları kesinlikle yasaktır (`validate_no_forbidden_cross_asset_claims`).
- **Phase 132 Handoff Invariant**: Phase 131 çıktıları, 10 devir kalemi ile Phase 132 (Macro, Event & News Regime Context Expansion) fazına eksiksiz devredilir (`phase_132_handoff.py`).
- **Current Phase: 131, Next Phase: 132 (Macro, Event & News Regime Context Expansion), Target Final Phase: 160**.

## Phase 132 Macro/Event/News Regime Context Expansion Agent Constraints
- **Strict Non-Signal & Environmental Context Invariant**: Agent, makro, takvim ve haber rejim bağlamı katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya yönlü iddia üretemez (`non_signal: True`, `allow_context_as_signal: False`).
- **Strictly Metadata-Only News Boundary**: Haber tarafı kesinlikle ve yalnızca metaveri (konu etiketleri, varlık etiketleri, makro tematik etiketler, olay bağlantıları, zaman damgaları ve kaynak kimlikleri) ile sınırlıdır. Haber tam metni, makale gövdesi (`article_body`), ham içerik (`raw_content`), taranmış HTML (`scraped_html`), duygu analizi model çıktıları (`sentiment_score`), gömmeler (`embedding`) veya vektör veri tabanları (`vector`) kesinlikle yasaktır ve boundary guard ile engellenir.
- **Zero-Execution & Model Training Prohibition**: Bu fazda kümeleme (KMeans, DBSCAN, GMM vb.), denetimsiz algoritma yürütme, model eğitimi (`fit`, `predict`), backtest veya optimizasyon kesinlikle çalıştırılamaz (`model_training_executed: False`, `clustering_executed: False`, `unsupervised_execution: False`).
- **Strict No-Lookahead & Scheduled/Actual Alignment**: Makro veri yayınları ve takvim olaylarında zaman damgaları geriye dönük (`direction='backward'`) asof join ile bağlanmalıdır. Planlanan yayın saati ile fiili yayın saati denetlenmeli; verinin erken sızdırılması (`actual < scheduled`) veya geleceğe kaydırma (`shift(-1)`, `future_return`) kesinlikle engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Ham kaynak dosyalar üzerine yazılamaz, otomatik veri doldurma (`auto_imputation: False`) ve otomatik özellik silme (`auto_drop: False`) kesinlikle yasaktır (`destructive_action_allowed: False`, `source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_macro_event_news_claims`).
- **Phase 133 Handoff Invariant**: Phase 132 çıktıları, 13 devir kalemi ile Phase 133 (Regime Validation and No-Lookahead Acceptance) fazına eksiksiz devredilir (`phase_133_handoff.py`).
- **Current Phase: 132, Next Phase: 133 (Regime Validation and No-Lookahead Acceptance), Target Final Phase: 160**.







