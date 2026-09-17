# GLOBAL PROJECT POLICY (2026-09-17)
> **ÖNEMLİ KURAL GÜNCELLEMESİ**: Ayrıntılar için `GLOBAL_PROJECT_POLICY.md` belgesini inceleyiniz.
> - **Kesin Yasak**: Gerçek borsa/broker bağlantısı, canlı emir gönderimi, gerçek para ile işlem, broker API key/secret, production deployment, yatırım tavsiyesi, kâr garantisi, web scraping, lookahead bias.
> - **İzinli ve Hedeflenen**: Gerçek tarihsel veriyle local backtest, local paper trading motoru (sanal bakiye/pozisyon/emir/fill/PnL), Telegram research/paper-trade sinyalleri (PAPER BUY/SELL/EXIT/WATCH/HOLD), model confidence/risk/regime açıklamaları, walk-forward/OOS/slippage testleri, local ML training/inference, local optimizasyon.
> - **Geçmiş İfadeler**: Önceki fazlardaki "disabled" ifadeleri yalnızca canlı broker/trade/production bağlamında geçerlidir; yerel araştırma, model eğitimi, backtest ve Telegram paper trading'i engellemez.
> - **Git & Branch Kuralı**: Her zaman `master` branch üzerinden ilerlenecektir. Her faz/görev tamamlandığında istisnasız `git add .`, `git commit` ve `git push origin master` yapılacaktır. Repo durumu asla kirli (dirty) bırakılmayacak, `origin/master` ile yerel master daima senkron ve hizalı tutulacaktır.


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

## Phase 133 Regime Validation and No-Lookahead Acceptance Agent Constraints
- **Strict Non-Signal & Validation Acceptance Invariant**: Agent, kabul geçitleri, testler veya skorlama katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya yönlü iddia üretemez (`non_signal: True`, `allow_acceptance_as_signal: False`).
- **Zero-Execution & Model Training Prohibition**: Bu fazda HMM, GMM, KMeans, DBSCAN veya herhangi bir model eğitimi, kümeleme algoritması yürütmesi veya denetimli/denetimsiz makine öğrenmesi inference operasyonu kesinlikle çalıştırılamaz (`allow_model_training: False`, `allow_clustering_execution: False`, `allow_target_label_generation: False`, `allow_prediction_generation: False`).
- **Strict No-Lookahead Boundary**: Zaman damgalı birleştirmelerde `context_ts <= base_ts` kesin temporal kuraldır. Negatif shift (`shift(-1)`), `lead()`, `future_return`, `forward_return` ve geleceğe referans veren etiketler no-lookahead acceptance tarafından tespit edilir ve engellenir (`allow_lookahead: False`).
- **Strictly Metadata-Only News Boundary**: Haber bileşeninde haber tam metni (`full_text`), makale gövdesi (`article_body`), ham içerik (`raw_content`), taranmış HTML (`scraped_html`), NLP duygu modeli çıktıları (`sentiment_score`) veya embeddingler (`embedding`, `vector`) kesinlikle yasaktır ve boundary guard ile reddedilir (`allow_full_article_usage: False`, `allow_web_scraping: False`, `allow_nlp_sentiment_model: False`).
- **Source Preservation & Non-Destructive Invariant**: Girdi DataFrameleri asla yerinde değiştirilemez (`df.copy()` zorunludur). Ham kaynak dosyalar üzerine yazılamaz (`allow_source_overwrite: False`), otomatik veri doldurma (`auto_imputation: False`) ve otomatik özellik silme (`auto_feature_drop: False`) kesinlikle yasaktır (`destructive_action_allowed: False`, `source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_regime_validation_claims`).
- **Phase 134 Handoff Invariant**: Phase 133 çıktıları, 14 devir kalemi ile Phase 134 (Regime FeatureStore Integration) fazına eksiksiz devredilir (`phase_134_handoff.py`).
- **Current Phase: 133, Next Phase: 134 (Regime FeatureStore Integration), Target Final Phase: 160**.

## Phase 134 Regime FeatureStore Integration Agent Constraints
- **Strict Non-Signal & FeatureStore Catalog Invariant**: Agent, FeatureStore sözleşmeleri, katalogları veya metaverileri üzerinde kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, long/short pozisyonlama, hedef değişken (`target`), model tahmini (`prediction`) veya yönlü iddia üretemez (`non_signal: True`, `allow_featurestore_as_signal: False`).
- **Zero-Execution & Model Training Prohibition**: Bu fazda hiçbir makine öğrenmesi modeli eğitilemez (`model_training_executed: False`), model fitting yapılamaz (`model_fit_executed: False`), model tahmini üretilemez (`model_predict_executed: False`), kümeleme algoritması çalıştırılamaz (`clustering_executed: False`), denetimsiz segmentasyon yürütülemez (`unsupervised_execution: False`).
- **Strict Local & Read-Only / Non-Destructive Write Discipline**: Okuma sözleşmeleri kesinlikle yerel dosya sistemiyle sınırlıdır; ağ çağrısı, broker entegrasyonu, canlı emir veya credential kullanımı yasaktır. Yazma sözleşmeleri yalnızca metaveri ekleme (`append`) ve zaman damgalı anlık görüntü (`snapshot`) ile sınırlıdır; kaynak dosyaların üzerine yazılması (`allow_source_overwrite: False`), silinmesi (`allow_file_deletion: False`), tahribatlı temizlik (`allow_destructive_clean: False`), otomatik doldurma (`allow_auto_imputation: False`) ve otomatik özellik silme (`allow_auto_feature_drop: False`) kesinlikle yasaktır (`source_preserved: True`).
- **Strict Query Contract & Forbidden Column Enforcement**: FeatureStore sorguları yalnızca izin verilen 8 metaveri filtresiyle yapılabilir. 12 yasaklı sorgu terimi (`buy`, `sell`, `signal`, `target`, `prediction`, `recommendation` vb.) ve 23 yasaklı kolon adı (`future_return`, `full_text`, `article_body`, `raw_content`, `scraped_html`, `embedding`, `vector`, `sentiment_score` vb.) kesinlikle engellenir.
- **Mandatory Acceptance References**: Her FeatureStore rejim kataloğu kaydı, Phase 133 doğrulama kabul referansını (`validation_acceptance_ref`), no-lookahead kabul referansını (`no_lookahead_acceptance_ref`) ve haber metaveri saflık referansını (`metadata_only_news_acceptance_ref`) taşımak zorundadır.
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_regime_featurestore_claims`).
- **Phase 135 Handoff Invariant**: Phase 134 çıktıları, 14 devir kalemi ile Phase 135 (Regime Classification Acceptance Report) fazına eksiksiz devredilir (`phase_135_handoff.py`).
- **Current Phase: 134, Next Phase: 135 (Regime Classification Acceptance Report), Target Final Phase: 160**.

## Phase 135 Regime Classification Acceptance Report and Block Finalization Agent Constraints
- **Phase 126-135 Final Acceptance & Non-Signal Invariant**: Agent, kabul raporları, geçitler, manifestolar veya skorlama katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_acceptance_as_signal: False`).
- **Zero-Execution & Model Training Prohibition**: Bu fazda hiçbir makine öğrenmesi modeli eğitilemez (`model_training_executed: False`), fit yapılamaz (`model_fit_executed: False`), tahmin yürütülemez (`model_predict_executed: False`), kümeleme algoritması (HMM, GMM, KMeans vb.) çalıştırılamaz (`clustering_executed: False`), denetimsiz segmentasyon yapılamaz (`unsupervised_execution: False`).
- **Strictly Metadata-Only News Boundary**: Haber metaveri katmanında kesinlikle haber tam metni (`full_text`), makale gövdesi (`article_body`), ham içerik (`raw_content`), web kazıma (`scraped_html`), NLP duygu modeli çıktıları (`sentiment_score`) veya embedding/vektör veri tabanı kullanılamaz (`full_text_used: False`, `scraping_executed: False`, `sentiment_model_used: False`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez veya ezilemez (`allow_source_overwrite: False`), otomatik doldurma (`auto_imputation: False`) ve otomatik özellik düşürme (`auto_feature_drop: False`) kesinlikle yasaktır (`destructive_action_allowed: False`, `source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_regime_acceptance_claims`).
- **Phase 136 Handoff Invariant**: Phase 135 çıktıları, 14 devir kalemi ile Phase 136 (GPU Acceleration and Advanced ML Runtime Foundation) fazına eksiksiz devredilir (`phase_136_handoff.py`).
- **Current Phase: 135, Next Phase: 136 (GPU Acceleration and Advanced ML Runtime Foundation), Target Final Phase: 160**.

## Phase 136 GPU Acceleration and Advanced ML Runtime Foundation Agent Constraints
- **Strict Non-Signal & Hardware Foundation Invariant**: Agent, donanım keşfi, hızlandırıcı kaydı, çalışma zamanı anlık görüntüsü veya hazırlık puanlama katmanında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_trading_signals: False`).
- **Zero-Execution, Zero-Training & Zero-Inference Prohibition**: Bu fazda hiçbir makine öğrenmesi modeli eğitilemez (`model_training_executed: False`), fit yapılamaz (`model_fit_executed: False`), tahmin/çıkarım yürütülemez (`model_predict_executed: False`), tensör tahsis edilemez (`tensor_allocated: False`), kümeleme veya denetimsiz segmentasyon yapılamaz (`clustering_executed: False`).
- **Graceful CPU Fallback & Offline Discovery**: GPU veya CUDA bulunamadığında kod asla çökmeyecek, sessizce ve zarifçe CPU fallback moduna geçecektir. Tüm donanım ve kütüphane denetimleri yereldir; ağ çağrısı, web kazıma, model indirme veya API anahtarı kullanımı yasaktır.
- **Enforced Safety Contracts**: 12 güvenlik sözleşmesi ve deney izin politikaları (`allowed_now` vs `blocked_now`) her zaman denetlenir. Model eğitimi ve canlı işlem izinleri kesinlikle kapalıdır (`blocked_now`).
- **Strictly Metadata-Only & Source Preservation Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez veya ezilemez (`allow_source_overwrite: False`), otomatik doldurma (`allow_auto_imputation: False`) ve otomatik özellik silme (`allow_auto_feature_drop: False`) kesinlikle yasaktır (`source_preserved: True`). Haber verilerinde tam metin, makale gövdesi veya duygu skoru kullanılamaz.
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_ml_runtime_claims`).
- **Phase 137 Handoff Invariant**: Phase 136 çıktıları, 14 devir kalemi ile Phase 137 (Advanced ML Dataset Contracts and Experiment Registry) fazına eksiksiz devredilir (`phase_137_handoff.py`).
- **Current Phase: 136, Next Phase: 137 (Advanced ML Dataset Contracts and Experiment Registry), Target Final Phase: 160**.

## Phase 137 Advanced ML Dataset Contracts and Experiment Registry Agent Constraints
- **Strict Non-Signal & Dataset Contract Invariant**: Agent, veri kümesi sözleşmeleri, şema kuralları, sızıntı korumaları veya deney kayıtları üzerinde kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_dataset_as_signal: False`).
- **Zero-Materialization Prohibition**: Bu fazda hiçbir veri kümesi (`dataset_materialized: False`) veya özellik anlık görüntüsü (`feature_snapshot_materialized: False`) fiziksel olarak diske yazılamaz. Tüm yapılar sözleşme ve şema düzeyinde tutulur.
- **Zero-Execution, Zero-Training & Zero-Inference Prohibition**: Model eğitimi (`fit`, `train`), model tahmini/çıkarımı (`predict`, `transform`), tensör tahsisi, kümeleme ve ansambl algoritmaları kesinlikle yasaktır (`training_blocked: True`, `prediction_blocked: True`).
- **Target/Label Generation Prohibition**: Hedef değişken (`target`, `label`), ileriye dönük getiri (`future_return`, `forward_return`, `next_return`) ve negatif indeks kaydırmaları (`shift(-1)`) kesinlikle yasaktır ve sızıntı korumalarıyla engellenir.
- **Strictly Metadata-Only News Boundary**: Haber metaverisinde tam metin, makale gövdesi, kazınmış HTML, duygu analizi veya embeddingler kesinlikle kullanılamaz (`metadata_only: True`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez veya ezilemez (`allow_source_overwrite: False`), otomatik doldurma (`allow_auto_imputation: False`) ve otomatik özellik silme (`allow_auto_feature_drop: False`) kesinlikle yasaktır (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_advanced_ml_dataset_claims`).
- **Phase 138 Handoff Invariant**: Phase 137 çıktıları, 13 devir kalemi ile Phase 138 (Baseline ML Model Contracts and Training Harness Governance) fazına eksiksiz devredilir (`phase_138_handoff.py`).
- **Current Phase: 137, Next Phase: 138 (Baseline ML Model Contracts and Training Harness Governance), Target Final Phase: 160**.

## Phase 138 Baseline ML Model Contracts and Dry-Run Training Harness Agent Constraints
- **Strict Non-Signal & Baseline Model Contract Invariant**: Agent, model sözleşmeleri, dry-run harness şablonları, trainer stub'ları veya hazırlık puanlama çıktılarında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `trade_signal_allowed: False`).
- **Zero-Real-Training & Zero-Model-Fit Prohibition**: Bu fazda hiçbir model eğitilemez (`real_training_executed: False`), hiçbir optimizasyon döngüsü çalıştırılamaz, `.fit()` ve `.train()` metotları kesinlikle kilitlidir (`model_fit_allowed: False`, `real_training_allowed: False`).
- **Zero-Prediction & Zero-Inference Prohibition**: Model çıkarımı (`predict`, `inference`, `transform`, `predict_proba`), sınıflandırma etiketleri veya regresyon tahminleri üretilemez (`model_predict_executed: False`, `model_predict_allowed: False`).
- **Zero-Target/Label-Generation Prohibition**: Hedef değişkenler (`target`, `label`), ileriye dönük getiriler (`future_return`, `forward_return`, `next_return`) ve negatif indeks kaydırmaları (`shift(-1)`) kesinlikle yasaktır (`target_label_generated: False`).
- **Zero-Artifact-Persistence & Zero-Registry-Write Prohibition**: Model ağırlıkları veya nesneleri (`pickle.dump`, `joblib.dump`, `torch.save`) diske kaydedilemez (`artifact_persisted: False`). Harici veya dahili model kayıt defterlerine (`model_registry`, `mlflow`) kayıt yapılamaz (`model_registry_written: False`).
- **Strict Dry-Run Harness & Blocked-By-Policy Discipline**: Tüm eğitim simülasyonları dry-run sözleşme modunda çalışır (`dry_run: True`, `would_run: False`, `blocked_by_policy: True`, `execution_status: "no_real_training_executed"`).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz. Girdi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_baseline_ml_claims`).
- **Phase 139 Handoff Invariant**: Phase 138 çıktıları, 12 devir kalemi ile Phase 139 (GPU-Accelerated Training Harness and Resource Governance) fazına eksiksiz devredilir (`phase_139_handoff.py`).
- **Current Phase: 138, Next Phase: 139 (GPU-Accelerated Training Harness and Resource Governance), Target Final Phase: 160**.

## Phase 139 GPU-Accelerated Training Harness and Resource Governance Agent Constraints
- **Strict Non-Signal & Resource Governance Invariant**: Agent, GPU/CPU kaynak yönetişimi, cihaz seçimi, bellek bütçesi, zaman aşımı ve training harness çıktılarında kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `trade_signal_allowed: False`).
- **Zero-Real-Training & Zero-Model-Fit Prohibition**: Bu fazda hiçbir model eğitilemez (`real_training_executed: False`), hiçbir optimizasyon döngüsü çalıştırılamaz, `.fit()` ve `.train()` metotları kesinlikle kilitlidir (`model_fit_allowed: False`, `real_training_allowed: False`).
- **Zero-Prediction & Zero-Inference Prohibition**: Model çıkarımı (`predict`, `inference`, `transform`, `predict_proba`), sınıflandırma etiketleri veya sayısal getiri tahminleri üretilemez (`model_predict_executed: False`, `model_predict_allowed: False`).
- **Zero-Target/Label-Generation Prohibition**: Hedef değişkenler (`target`, `label`), ileriye dönük getiriler (`future_return`, `forward_return`, `next_return`) ve negatif indeks kaydırmaları (`shift(-1)`) kesinlikle yasaktır (`target_label_generated: False`).
- **Zero-Artifact-Persistence & Zero-Registry-Write Prohibition**: Model ağırlıkları veya nesneleri (`pickle.dump`, `joblib.dump`, `torch.save`) diske kaydedilemez (`artifact_persisted: False`). Harici veya dahili model kayıt defterlerine (`model_registry`, `mlflow`) kayıt yapılamaz (`model_registry_written: False`).
- **Hardware Safety & Resource Limits**: Maksimum GPU bellek fraksiyonu %80 (`max_memory_fraction_limit: 0.80`), maksimum zaman aşımı 3600 saniye (`max_timeout_seconds_limit: 3600`) aşılamaz. Donanım yokluğunda veya CUDA hatasında zarif CPU fallback uygulanmalıdır.
- **Strict Dry-Run Harness & Blocked-By-Policy Discipline**: Tüm eğitim simülasyonları dry-run sözleşme modunda çalışır (`dry_run: True`, `would_run: False`, `blocked_by_policy: True`, `execution_status: "no_real_training_executed"`). 5 devre dışı bırakılmış yürütme raporu eksiksiz üretilmelidir.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Girdi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_gpu_training_claims`).
- **Phase 140 Handoff Invariant**: Phase 139 çıktıları, 12 devir kalemi ile Phase 140 (Ensemble Model Contracts and Candidate Model Registry) fazına eksiksiz devredilir (`phase_140_handoff.py`).
- **Current Phase: 139, Next Phase: 140 (Ensemble Model Contracts and Candidate Model Registry), Target Final Phase: 160**.

## Phase 140 Ensemble Model Contracts and Candidate Model Registry Agent Constraints
- **Strict Non-Signal & Candidate Model Contract Invariant**: Agent, topluluk modelleri, aday model kayıt defteri, uyumluluk matrisi veya ensemble stratejileri üzerinde kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (non_signal: True, allow_ensemble_as_signal: False).
- **Zero-Ensemble-Execution Prohibition**: Hiçbir ensemble stratejisi (Voting, Blending, Stacking, Dynamic Weighting) çalıştırılamaz (ensemble_execution_allowed: False, execution_blocked: True). Aday model tahminleri birleştirilemez, oof/holdout tahminleri hesaplanamaz, meta-model fit edilemez (meta_model_fit_allowed: False).
- **Zero-Candidate-Training & Zero-Prediction Prohibition**: Aday modeller üzerinde hiçbir eğitim (fit, train, backward) veya çıkarım (predict, inference, transform, predict_proba) yapılamaz (candidate_training_allowed: False, candidate_prediction_allowed: False).
- **Zero-Target/Label-Generation Prohibition**: Hedef değişkenler (target, label), ileriye dönük getiriler (future_return, forward_return, next_return) ve negatif indeks kaydırmaları (shift(-1)) kesinlikle yasaktır (target_label_generated: False).
- **Zero-Artifact-Persistence & Zero-Registry-Write Prohibition**: Model ağırlıkları, tensörler veya serileştirilmiş nesneler (pickle.dump, joblib.dump, torch.save) diske kaydedilemez (artifact_persistence_allowed: False). Harici veya dahili model kayıt defterlerine (model_registry, mlflow, wandb) kayıt yapılamaz (model_registry_write_allowed: False).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber verilerinde tam metin, makale gövdesi, HTML, NLP duygu modelleri veya embedding kullanılamaz (metadata_only: True). Zaman serisi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (df.copy() zorunludur). Kaynak tablolar silinemez, ezilemez (allow_source_overwrite: False), otomatik değer doldurma (allow_auto_imputation: False) veya özellik silme (allow_auto_feature_drop: False) yapılamaz (source_preserved: True).
- **Forbidden Claims & Commercial Exclusions**: official_approval, production_ready, broker_ready, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (validate_no_forbidden_ensemble_claims).
- **Phase 141 Handoff Invariant**: Phase 140 çıktıları, 12 devir kalemi ile Phase 141 (Probability Calibration and Uncertainty Estimation) fazına eksiksiz devredilir (phase_141_handoff.py).
- **Current Phase: 140, Next Phase: 141 (Probability Calibration and Uncertainty Estimation), Target Final Phase: 160**.

## Phase 141 Probability Calibration and Uncertainty Estimation Agent Constraints
- **Strict Non-Signal & Calibration Contract Invariant**: Agent, olasılık kalibrasyonu, belirsizlik kestirimi, güven puanları veya aralık çıktılarını kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini olarak üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Calibration-Execution Prohibition**: Hiçbir kalibrasyon yöntemi (Platt scaling, Isotonic regression, Temperature scaling vb.) çalıştırılamaz (`calibration_fit_allowed: False`, `calibration_transform_allowed: False`, `execution_blocked: True`). Olasılık dönüşümleri kilitlidir.
- **Zero-Uncertainty-Estimation Prohibition**: Hiçbir belirsizlik yöntemi (MC Dropout, Ensemble variance, Conformal prediction vb.) çalıştırılamaz (`uncertainty_estimation_allowed: False`, `prediction_interval_allowed: False`). Sayısal belirsizlik değerleri veya tahmin aralıkları üretilemez.
- **Zero-Probability-Prediction Prohibition**: Modelden olasılık tahmini (`predict_proba`, class probabilities, softmax scores) veya güven skoru üretilemez (`probability_prediction_allowed: False`).
- **Zero-Target/Label-Generation Prohibition**: Hedef değişkenler (`target`, `label`), ileriye dönük getiriler (`future_return`, `forward_return`) ve negatif indeks kaydırmaları (`shift(-1)`) kesinlikle yasaktır (`target_label_generated: False`).
- **Zero-Artifact-Persistence & Zero-Registry-Write Prohibition**: Kalibrasyon parametreleri, ölçekleme faktörleri veya serileştirilmiş nesneler diske kaydedilemez (`artifact_persistence_allowed: False`). Harici veya dahili model kayıt defterlerine kayıt yapılamaz (`model_registry_write_allowed: False`).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Girdi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır.
- **Phase 142 Handoff Invariant**: Phase 141 çıktıları, 8 devir kalemi ile Phase 142 (Model Drift Monitoring and Data/Feature Drift Linkage) fazına eksiksiz devredilir (`phase_142_handoff.py`).
- **Current Phase: 141, Next Phase: 142 (Model Drift Monitoring and Data/Feature Drift Linkage), Target Final Phase: 160**.

## Phase 142 Model Drift Monitoring and Data/Feature Drift Linkage Agent Constraints
- **Strict Non-Signal & Drift Contract Invariant**: Agent, drift izleme, veri/öznitelik drift bağlantısı, eşik değerler veya uyarı yer tutucuları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Drift-Calculation Prohibition**: Hiçbir drift metriği (PSI, KS testi, Jensen-Shannon diverjansı, Wasserstein mesafesi, korelasyon drifti) canlı veri üzerinde hesaplanamaz (`drift_calculation_allowed: False`, `all_zero_calculation: True`). Tüm metrikler sözleşme yer tutucusudur.
- **Zero-Live-Monitoring & Zero-Alerting Prohibition**: Canlı izleme servisleri veya daemon döngüleri çalıştırılamaz; drift tespiti durumunda otomatik e-posta, webhook veya konsol uyarısı (alert) tetiklenemez (`alerting_allowed: False`).
- **Zero-Retraining-Trigger Prohibition**: Drift eşik aşımı gerekçesiyle otomatik yeniden eğitim (retraining pipeline) tetiklenemez (`retraining_trigger_allowed: False`).
- **Zero-Model-Action Prohibition**: Drift gerekçesiyle modeller production'dan kaldırılamaz, devre dışı bırakılamaz veya yenisiyle otomatik değiştirilemez (`model_action_allowed: False`).
- **Zero-Materialization & Zero-Registry-Write Prohibition**: Veri kümesi veya öznitelik anlık görüntüsü materialize edilemez; model kayıt defterine yazma yapılamaz (`materialization_allowed: False`, `model_registry_write_allowed: False`).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Girdi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır.
- **Phase 143 Handoff Invariant**: Phase 142 çıktıları, 8 devir kalemi ile Phase 143 (Explainability and Feature Attribution Reports) fazına eksiksiz devredilir (`phase_143_handoff.py`).
- **Current Phase: 142, Next Phase: 143 (Explainability and Feature Attribution Reports), Target Final Phase: 160**.

## Phase 143 Explainability and Feature Attribution Reports Agent Constraints
- **Strict Non-Signal & Explainability Contract Invariant**: Agent, açıklanabilirlik raporları, öznitelik atıf sözleşmeleri, SHAP/LIME yer tutucuları veya neden kodları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-XAI-Calculation Prohibition**: Hiçbir açıklanabilirlik veya atıf metriği (SHAP değerleri, LIME ağırlıkları, permütasyon önem skorları, PDP/ICE eğrileri) canlı veri veya gerçek model üzerinde hesaplanamaz (`explainability_calculation_allowed: False`, `attribution_calculation_allowed: False`, `all_uncalculated: True`). Tüm metrikler sözleşme yer tutucusudur.
- **Zero-SHAP-LIME-Execution Prohibition**: SHAP ve LIME kütüphaneleri çağrılamaz; pertürbasyon veya arka plan örneklemesi yapılamaz (`shap_execution_allowed: False`, `lime_execution_allowed: False`).
- **Zero-Surrogate-Training Prohibition**: Karar ağacı veya kural tabanlı vekil modeller eğitilemez (`surrogate_model_allowed: False`).
- **Zero-Counterfactual-Generation Prohibition**: Karşıgözlemsel optimizasyon veya arama çalıştırılamaz (`counterfactual_generation_allowed: False`).
- **Zero-Model-Action Prohibition**: Açıklama veya atıf gerekçesiyle modeller production'dan kaldırılamaz, devre dışı bırakılamaz, budanamaz veya otomatik yeniden eğitilemez (`model_action_allowed: False`).
- **Zero-Materialization & Zero-Registry-Write Prohibition**: Veri kümesi veya öznitelik anlık görüntüsü materialize edilemez; model kayıt defterine yazma yapılamaz (`materialization_allowed: False`, `model_registry_write_allowed: False`).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Girdi birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır.
- **Phase 144 Handoff Invariant**: Phase 143 çıktıları, 8 devir kalemi ile Phase 144 (Model Governance, Model Cards and Audit Trail) fazına eksiksiz devredilir (`phase_144_handoff.py`).
- **Current Phase: 143, Next Phase: 144 (Model Governance, Model Cards and Audit Trail), Target Final Phase: 160**.

## Phase 144 Model Governance, Model Cards and Audit Trail Agent Constraints
- **Strict Non-Signal & Governance Contract Invariant**: Agent, model yönetişim sözleşmeleri, model kartları, risk kayıtları, kontrol listeleri veya onay sınırları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Model-Registry-Write Prohibition**: Hiçbir model ağırlığı, kontrol noktası veya nesnesi harici/dahili model kayıt defterlerine (MLflow, Weights & Biases vb.) yazılamaz (`allow_model_registry_write: False`).
- **Zero-Artifact-Persistence Prohibition**: Model ağırlıkları (.pkl, .joblib, .pt vb.) diske serileştirilemez veya kalıcı olarak kaydedilemez (`allow_artifact_persistence: False`).
- **Zero-Deployment Prohibition**: Modeller canlı veya hazırlık (staging) servislerine dağıtılamaz (`allow_model_deployment: False`, `allow_production_deployment: False`).
- **Zero-Production-Approval Prohibition**: Resmi üretim onayı, serbest bırakma onayı veya canlıya geçiş onayı verilemez (`allow_production_approval: False`, `allow_release_approval: False`).
- **Zero-Broker-Ready-Claim Prohibition**: Aracı kurum hazır durumu onayı veya broker API bağlantı izni verilemez (`allow_broker_ready_approval: False`, `allow_broker_ready_claim: False`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`) veya model tahmini/çıkarımı (`predict`, `inference`, `predict_proba`) kesinlikle çalıştırılamaz.
- **Zero-Real-Audit-Log Prohibition**: Gerçek regülasyon denetim logu yazılmaz; tüm audit nesneleri dry-run yer tutucudur (`allow_real_audit_log: False`).
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_governance_claims`).
- **Phase 145 Handoff Invariant**: Phase 144 çıktıları, 12 devir kalemi ile Phase 145 (Advanced ML Acceptance Report and Candidate Finalization) fazına eksiksiz devredilir (`phase_145_handoff.py`).
- **Current Phase: 144, Next Phase: 145 (Advanced ML Acceptance Report and Candidate Finalization), Target Final Phase: 160**.

## Phase 145 Advanced ML Acceptance Report and Consolidated Acceptance Layer Agent Constraints
- **Strict Non-Signal & Acceptance Contract Invariant**: Agent, kabul raporları, bileşen kayıt defteri, hazırlık puanları veya devir paketleri üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`, `predict_proba`), olasılık kestirimi, kalibrasyon hesabı, drift tespiti, SHAP/LIME hesabı veya backtest/slippage simülasyonu çalıştırılamaz.
- **Zero-Registry-Write & Zero-Artifact-Persistence Prohibition**: Model kayıt defterlerine yazma yapılamaz; model ağırlıkları ve serileştirilmiş artefaktlar kaydedilemez (`allow_model_registry_write: False`, `allow_artifact_persistence: False`).
- **Zero-Deployment & Zero-Production-Approval Prohibition**: Modeller canlı veya hazırlık (staging) servislerine dağıtılamaz (`allow_model_deployment: False`); üretim onayı veya broker hazır durumu onayı verilemez (`allow_production_approval: False`, `allow_broker_ready_approval: False`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`advanced_ml_contract_acceptance_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve yönetişim kontrol noktası başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü veya kârlılık garantisi olarak sunulamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_advanced_ml_acceptance_claims`).
- **Phase 146 Handoff Invariant**: Phase 145 çıktıları, 13 devir kalemi ile Phase 146 (Realistic Backtest, Transaction Cost and Slippage Modeling) fazına eksiksiz devredilir (`phase_146_handoff.py`).
- **Current Phase: 145, Next Phase: 146 (Realistic Backtest, Transaction Cost and Slippage Modeling), Target Final Phase: 160**.

## Phase 146 Realistic Backtest, Transaction Cost and Slippage Modeling Agent Constraints
- **Strict Non-Signal & Backtest Contract Invariant**: Agent, backtest motor sözleşmeleri, emir simülasyonları, fill kuralları, işlem maliyet modelleri veya muhasebe kayıtları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Backtest-Execution Prohibition**: Canlı veya gerçek backtest motoru koşturulamaz (`allow_backtest_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), walk-forward yürütülmez (`allow_walk_forward_execution: False`), benchmark kıyaslaması koşturulamaz (`allow_benchmark_execution: False`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_backtest_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`READY_FOR_PHASE_147_WALK_FORWARD_HANDOFF`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, strateji başarısı veya kârlılık garantisi olarak sunulamaz.
- **Phase 147 Handoff Invariant**: Phase 146 çıktıları, 14 devir kalemi ile Phase 147 (Walk-Forward Validation and Out-of-Sample Testing) fazına eksiksiz devredilir (`phase_147_handoff.py`).
- **Current Phase: 146, Next Phase: 147 (Walk-Forward Validation and Out-of-Sample Testing), Target Final Phase: 160**.

## Phase 147 Walk-Forward Validation and Out-of-Sample Benchmarking Agent Constraints
- **Strict Non-Signal & Validation Contract Invariant**: Agent, walk-forward bölme sözleşmeleri, OOS benchmark sözleşmeleri, metrik yer tutucuları veya doğrulama manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Validation-Execution Prohibition**: Canlı veya gerçek walk-forward yürütülemez (`allow_walk_forward_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), benchmark yürütülemez (`allow_benchmark_execution: False`), gerçek metrik hesabı koşturulamaz (`allow_metric_calculation: False`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur. Embargo/purge aralıkları sızıntıya karşı korunmalıdır.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_walk_forward_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`READY_FOR_PHASE_148_STRESS_TESTING_HANDOFF`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü veya kârlılık garantisi olarak sunulamaz.
- **Phase 148 Handoff Invariant**: Phase 147 çıktıları, 14 devir kalemi ile Phase 148 (Stress Testing, Scenario Simulation and Robustness) fazına eksiksiz devredilir (`phase_148_handoff.py`).
- **Current Phase: 147, Next Phase: 148 (Stress Testing, Scenario Simulation and Robustness), Target Final Phase: 160**.

## Phase 148 Stress Testing and Scenario Simulation Agent Constraints
- **Strict Non-Signal & Scenario Contract Invariant**: Agent, stres testi profilleri, senaryo sözleşmeleri, şok yer tutucuları veya stres manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Stress-Execution & Simulation Prohibition**: Canlı veya gerçek stres testi yürütülemez (`allow_stress_test_execution: False`), senaryo simülasyonu çalıştırılamaz (`allow_scenario_simulation: False`), Monte Carlo simülasyonu yapılamaz (`allow_monte_carlo_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), gerçek stres metrik hesabı (Stressed PnL, VaR, CVaR, MaxDD) koşturulamaz (`allow_metric_calculation: False`). Tüm yürütmeler güvenli kuru koşum sözleşmeleridir (`execution_blocked=True`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur. Senaryo parametrelerinin eğitim dönemine sızması (scenario leakage) engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_stress_testing_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`READY_FOR_PHASE_149_MONTE_CARLO_ROBUSTNESS_HANDOFF`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, sermaye güvencesi veya kârlılık garantisi olarak sunulamaz.
- **Phase 149 Handoff Invariant**: Phase 148 çıktıları, 14 devir kalemi ile Phase 149 (Monte Carlo Robustness and Parameter Stability) fazına eksiksiz devredilir (`phase_149_handoff.py`).
- **Current Phase: 148, Next Phase: 149 (Monte Carlo Robustness and Parameter Stability), Target Final Phase: 160**.

## Phase 149 Monte Carlo Robustness and Parameter Stability Agent Constraints
- **Strict Non-Signal & Robustness Contract Invariant**: Agent, Monte Carlo simülasyon sözleşmeleri, bootstrap yer tutucuları, yeniden örnekleme sözleşmeleri, parametre duyarlılık sözleşmeleri veya dayanıklılık manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Monte-Carlo-Execution Prohibition**: Canlı veya gerçek Monte Carlo simülasyonu yürütülemez (`allow_monte_carlo_execution: False`), bootstrap örneklemesi çalıştırılamaz (`allow_bootstrap_sampling: False`), parametre optimizasyonu yapılamaz (`allow_parameter_optimization: False`), parametre taraması yürütülemez (`allow_parameter_grid_sweep: False`), gerçek metrik hesabı (Monte Carlo VaR, CVaR, resampled Sharpe, drawdown dağılımları) koşturulamaz (`allow_metric_calculation: False`). Tüm sözleşmeler kuru koşum yer tutucularıdır (`execution_blocked=True`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur. Yeniden örnekleme ve pertürbasyon işlemlerinde geleceğe sızıntı engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_monte_carlo_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`READY_FOR_PHASE_150_BACKTEST_GOVERNANCE_HANDOFF`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, sermaye güvencesi veya kârlılık garantisi olarak sunulamaz.
- **Phase 150 Handoff Invariant**: Phase 149 çıktıları, 10 devir kalemi ile Phase 150 (Backtest Governance, Bias Control and Overfitting Safeguards) fazına eksiksiz devredilir (`phase_150_handoff.py`).
- **Current Phase: 149, Next Phase: 150 (Backtest Governance, Bias Control and Overfitting Safeguards), Target Final Phase: 160**.

## Phase 150 Backtest Governance and Bias Control Agent Constraints
- **Strict Non-Signal & Governance Contract Invariant**: Agent, backtest yönetişim profilleri, yanlılık kontrol sözleşmeleri, sonuç iddia sınırları, gerçekçilik sözleşmeleri veya yönetişim manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Backtest-Execution & Result Claim Prohibition**: Canlı veya gerçek backtest motoru yürütülemez (`allow_backtest_execution: False`), simülasyon çalıştırılamaz (`allow_simulation_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), gerçek metrik hesabı (Sharpe, drawdown, kârlılık, alpha vb.) koşturulamaz (`allow_metric_calculation: False`), sonuç veya performans iddiasında bulunulamaz (`allow_result_claim: False`, `allow_performance_claim: False`). Tüm sözleşmeler kuru koşum yer tutucularıdır (`execution_blocked=True`).
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur. Yanlılık kontrollerinde ve bölmelerde geleceğe sızıntı engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık, üstünlük veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_backtest_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`READY_FOR_PHASE_151_PERFORMANCE_DIAGNOSTICS_HANDOFF`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, sermaye güvencesi veya kârlılık garantisi olarak sunulamaz.
- **Phase 151 Handoff Invariant**: Phase 150 çıktıları, 10 devir kalemi ile Phase 151 (Benchmark Comparison and Strategy Evaluation Reports) fazına eksiksiz devredilir (`phase_151_handoff.py`).
- **Current Phase: 150, Next Phase: 151 (Benchmark Comparison and Strategy Evaluation Reports), Target Final Phase: 160**.

## Phase 151 Benchmark Comparison and Strategy Evaluation Reports Agent Constraints
- **Strict Non-Signal & Evaluation Contract Invariant**: Agent, benchmark karşılaştırma raporu sözleşmeleri, strateji değerlendirme sözleşmeleri, referans evrenler, baseline standartları veya değerlendirme manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`).
- **Zero-Real-Simulation & Result Claim Prohibition**: Canlı veya gerçek benchmark simülasyonu koşturulamaz (`allow_benchmark_execution: False`), strateji backtesti yürütülemez (`allow_backtest_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), gerçek metrik hesabı (Sharpe, win-rate, getiri, alpha vb.) koşturulamaz (`allow_metric_calculation: False`), sonuç veya performans iddiasında bulunulamaz (`allow_result_claim: False`, `allow_performance_claim: False`). Tüm sözleşmeler kuru koşum yer tutucularıdır (`execution_blocked=True`).
- **Zero-Strategy-Approval & Zero-Capital-Allocation Prohibition**: Otomatik strateji resmi onayı verilemez (`allow_strategy_approval: False`), sermaye tahsisi, pozisyon büyüklüğü veya portföy yapısı oluşturulamaz (`allow_capital_allocation: False`). Strateji sonuçları yalnızca ampirik araştırma hipotezi olarak etiketlenmelidir.
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Zaman damgası birleştirmelerinde strictly backward asof (`direction='backward'`) ve kronolojik sıralama zorunludur. Yanlılık kontrollerinde ve bölmelerde geleceğe sızıntı engellenmelidir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez (`df.copy()` zorunludur). Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma (`allow_auto_imputation: False`) veya özellik silme (`allow_auto_feature_drop: False`) yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık, üstünlük veya yatırım tavsiyesi iddiaları kesinlikle yasaktır (`validate_no_forbidden_benchmark_evaluation_claims`).
- **Readiness Score Semantics**: 1.00 hazırlık puanı (`benchmark_evaluation_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, sermaye güvencesi veya kârlılık garantisi olarak sunulamaz.
- **Phase 152 Handoff Invariant**: Phase 151 çıktıları, 10 devir kalemi ile Phase 152 (Backtest Acceptance Report) fazına eksiksiz devredilir (`phase_152_handoff.py`).
- **Current Phase: 151, Next Phase: 152 (Backtest Acceptance Report), Target Final Phase: 160**.

## Phase 152 Backtest Acceptance Report Agent Constraints
- **Strict Non-Signal & Acceptance Contract Invariant**: Agent, backtest kabul profilleri, bileşen kayıtları, kontrol noktaları veya kabul manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı, alfa tetiği veya model tahmini üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Real-Backtest-Execution & Zero-Benchmark-Simulation Prohibition**: Canlı veya gerçek backtest motoru koşturulamaz (`allow_backtest_execution: False`), benchmark simülasyonu çalıştırılamaz (`allow_benchmark_execution: False`), parametre optimizasyonu yapılamaz (`allow_optimizer_execution: False`), metrik hesaplaması yapılamaz (`allow_metric_calculation: False`), sonuç veya performans iddialarında bulunulamaz (`allow_result_claim: False`, `allow_performance_claim: False`).
- **Zero-Strategy-Approval & Zero-Portfolio-Execution Prohibition**: Strateji resmi onayı verilemez (`allow_strategy_approval: False`), sermaye tahsisi yapılamaz (`allow_capital_allocation: False`), gerçek portföy kurulamaz (`allow_portfolio_construction: False`), pozisyon büyüklüğü üretilemez (`allow_position_sizing: False`).
- **Zero-Auto-Action Remediation Invariant**: Bulgularda veya hata durumlarında otomatik aksiyon önerileri (`auto-run backtest`, `auto-run benchmark`, `auto-calculate metrics`, `auto-approve strategy`, `auto-allocate capital`, `auto-position-size`, `auto-construct portfolio`, `auto-optimize strategy`, `auto-train model`, `auto-run prediction`, `auto-send broker order`, `auto-deploy`) kesinlikle üretilemez; `create_backtest_acceptance_finding` bunu programatik olarak engeller.
- **Zero-Real-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, kârlılık veya getiri garantisi iddiaları kesinlikle yasaktır (`validate_no_forbidden_backtest_acceptance_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`backtest_acceptance_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 153 Handoff Invariant**: Phase 152 çıktıları, 13 devir kalemi ile Phase 153 (Portfolio Construction, Position Sizing and Risk Budgeting) fazına eksiksiz devredilir (`phase_153_handoff.py`).
- **Current Phase: 152, Next Phase: 153 (Portfolio Construction, Position Sizing and Risk Budgeting), Target Final Phase: 160**.

## Phase 153 Portfolio Construction, Position Sizing and Risk Budgeting Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, portföy inşa profilleri, evren sözleşmeleri, pozisyon boyutlandırma şablonları, risk bütçeleme kuralları veya master manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`, `allow_real_order: False`).
- **Zero-Real-Optimization & Zero-Weight-Generation Prohibition**: Gerçek portföy optimizasyonu (Mean-Variance, Black-Litterman, HRP vb.) koşturulamaz (`allow_real_optimization: False`), gerçek sermaye ağırlıkları veya portföy dağılımı üretilemez (`allow_real_portfolio_weights: False`, `actual_weight=None`).
- **Zero-Real-Position-Sizing & Zero-Capital-Allocation Prohibition**: Gerçek lot, kontrat veya pozisyon büyüklüğü hesaplanamaz (`allow_real_lot_sizing: False`, `actual_size_calculated=None`, `actual_lot_generated=None`), gerçek sermaye tahsisi yapılamaz (`allow_real_capital_allocation: False`, `actual_budget_calculated=None`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek portföy metrikleri (Sharpe, Sortino, VaR, ES, MaxDD vb.) hesaplanamaz (`allow_metric_calculation: False`, `is_calculated=False`, `actual_value=None`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `optimal_portfolio`, `guaranteed_return` iddiaları kesinlikle yasaktır (`validate_no_forbidden_portfolio_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`portfolio_construction_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 154 Handoff Invariant**: Phase 153 çıktıları, 14 devir kalemi ile Phase 154 (Portfolio Optimization Contracts) fazına eksiksiz devredilir (`phase_154_handoff.py`).
- **Phase 153 Finished**: Phase 153 tamamlanmış ve Phase 154'e devredilmiştir.

## Phase 154 Portfolio Optimization and Allocation Constraints Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, portföy optimizasyon sözleşmeleri, amaç fonksiyonları, tahsis kısıtları veya master manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_execution: False`, `allow_real_order: False`).
- **Zero-Real-Optimization & Zero-Solver-Execution Prohibition**: Sayısal optimizasyon çözücüleri (CVXPY, SciPy minimize vb.) koşturulamaz (`allow_real_optimization: False`, `allows_execution: False`), optimizasyon döngüsü çalıştırılamaz (`is_optimized: False`).
- **Zero-Real-Weight-Generation & Zero-Capital-Allocation Prohibition**: Gerçek optimal portföy ağırlıkları hesaplanamaz (`allow_real_portfolio_weights: False`, `actual_weight=None`), gerçek sermaye tahsisi yapılamaz (`allow_real_capital_allocation: False`, `actual_allocated_capital=None`).
- **Zero-Real-Rebalance Prohibition**: Yeniden dengeleme emirleri üretilemez ve iletilemez (`allow_real_rebalance: False`, `rebalance_order_generated=False`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek portföy optimizasyon metrikleri (Sharpe, Diversification Ratio, Tracking Error vb.) hesaplanamaz (`allow_metric_calculation: False`, `is_calculated=False`, `actual_value=None`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (52 Columns)**: 52 adet sızıntı/tahmin/canlı işlem kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_optimization_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `optimal_portfolio`, `guaranteed_return` iddiaları kesinlikle yasaktır (`validate_no_forbidden_optimization_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`portfolio_optimization_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 155 Handoff Invariant**: Phase 154 çıktıları, 15 devir kalemi ile Phase 155 (Portfolio Risk Attribution and Reporting) fazına eksiksiz devredilir (`phase_155_handoff.py`).
- **Phase 154 Finished**: Phase 154 tamamlanmış ve Phase 155'e devredilmiştir.

## Phase 155 Risk Reporting, Exposure Attribution and Limit Monitoring Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, risk raporları, maruziyet ayrıştırma sözleşmeleri, limit izleme kuralları veya master manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Real-Risk-Reporting-Execution Prohibition**: Gerçek risk raporu derlenemez ve çalıştırılamaz (`allow_risk_report_execution: False`, `risk_report_generated: False`).
- **Zero-Real-Exposure-Attribution Prohibition**: Gerçek portföy maruziyeti hesaplanamaz ve atfedilemez (`allow_exposure_attribution_execution: False`, `actual_exposure_calculated=None`).
- **Zero-Real-Limit-Monitoring Prohibition**: Gerçek limit izleme döngüleri ve canlı alarm tetiklemeleri koşturulamaz (`allow_limit_monitoring_execution: False`, `limit_monitoring_executed: False`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek risk metrikleri (VaR, ES, volatilite, maksimum düşüş, beta vb.) hesaplanamaz (`allow_metric_calculation: False`, `allow_var_calculation: False`, `actual_value=None`).
- **Zero-Real-Alerting & Zero-Dashboard Prohibition**: Dış bildirim, webhook, SMS, e-posta veya interaktif gösterge paneli (dashboard) üretilemez (`alert_routing_disabled: True`, `dashboard_generated: False`).
- **Zero-Real-Portfolio-Adjustment Prohibition**: Limit aşımlarına karşılık otomatik pozisyon kapatma, de-risking veya yeniden dengeleme yapılamaz (`allow_portfolio_adjustment: False`, `portfolio_adjustment_generated: False`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Geleceğe sızıntı yapan zaman damgası veya forward-return kolonları kesinlikle engellenir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (48 Columns)**: 48 adet sızıntı/tahmin/canlı işlem kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_risk_reporting_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `risk_free`, `optimal_risk` iddiaları kesinlikle yasaktır (`validate_no_forbidden_risk_reporting_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`risk_reporting_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 156 Handoff Invariant**: Phase 155 çıktıları, 10 devir kalemi ile Phase 156 (Portfolio Scenario Testing and Drawdown Control) fazına eksiksiz devredilir (`phase_156_handoff.py`).
- **Current Phase: 155, Next Phase: 156 (Portfolio Scenario Testing and Drawdown Control), Target Final Phase: 160**.

## Phase 156 Portfolio Scenario Testing and Drawdown Control Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, senaryo test sözleşmeleri, şok modelleri, drawdown kontrol kuralları, toparlanma planları veya kontrol aksiyonları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Real-Scenario-Execution Prohibition**: Gerçek senaryo simülasyonu koşturulamaz ve senaryo PnL hesabı yapılamaz (`allow_scenario_execution: False`, `scenario_tested: False`).
- **Zero-Real-Drawdown-Control Prohibition**: Gerçek drawdown ölçümü, canlı uyarı/alarm üretimi veya canlı ihlal tetiklemesi yapılamaz (`allow_drawdown_control_execution: False`, `drawdown_controlled: False`).
- **Zero-Real-Portfolio-Adjustment & Zero-Hedge/De-risk Prohibition**: Portföy maruziyeti azaltılamaz, otomatik hedge açılamaz, de-risking emirleri üretilemez, yeniden dengeleme veya dondurma işlemi uygulanamaz (`allow_portfolio_adjustment: False`, `allow_hedge_execution: False`, `allow_derisk_execution: False`, `allow_rebalance_execution: False`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek senaryo veya drawdown metrikleri (Stressed PnL, MaxDD, Recovery Time, Resilience Score) hesaplanamaz (`allow_metric_calculation: False`, `actual_value=None`).
- **Zero-Real-Alerting & Zero-Dashboard Prohibition**: Dış bildirim, webhook, SMS, e-posta veya interaktif gösterge paneli (dashboard) üretilemez (`alert_routing_disabled: True`, `dashboard_generated: False`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Geleceğe sızıntı yapan zaman damgası veya forward-return kolonları kesinlikle engellenir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (52 Columns)**: 52 adet sızıntı/tahmin/canlı işlem/aksiyon kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_portfolio_scenario_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `stress_tested_approved`, `crash_proof` iddiaları kesinlikle yasaktır (`validate_no_forbidden_portfolio_scenario_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`portfolio_scenario_control_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 157 Handoff Invariant**: Phase 156 çıktıları, 10 devir kalemi ile Phase 157 (Portfolio Acceptance Report) fazına eksiksiz devredilir (`phase_157_handoff.py`).
- **Current Phase: 156, Next Phase: 157 (Portfolio Acceptance Report), Target Final Phase: 160**.

## Phase 157 Portfolio Acceptance Report and Phase 153-157 Consolidated Acceptance Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, portföy kabul raporları, checkpoint değerlendirmeleri, go/no-go kararları, blocker/gap tespitleri veya master kabul manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Real-Portfolio-Construction & Zero-Real-Position-Sizing Prohibition**: Gerçek portföy oluşturulamaz, gerçek pozisyon büyüklüğü hesaplanamaz ve tahsis yapılamaz (`allow_portfolio_construction: False`, `allow_position_sizing: False`).
- **Zero-Real-Optimization & Allocation Prohibition**: Gerçek optimizasyon çözücüsü koşturulamaz, gerçek kısıt çözümü veya yeniden dengeleme yapılamaz (`allow_portfolio_optimization: False`, `allow_rebalance_execution: False`).
- **Zero-Real-Risk-Reporting & Scenario Execution Prohibition**: Gerçek risk raporu derlenemez, gerçek maruziyet hesaplanamaz, gerçek senaryo simülasyonu veya drawdown kontrol döngüsü koşturulamaz (`allow_risk_reporting: False`, `allow_scenario_execution: False`, `allow_drawdown_control: False`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek portföy metrikleri, risk ölçümleri veya acceptance performans puanı hesaplanamaz (`allow_metric_calculation: False`, `actual_value=None`).
- **Zero-Real-Alerting & Zero-Dashboard Prohibition**: Dış bildirim, webhook, SMS, e-posta veya interaktif gösterge paneli (dashboard) üretilemez (`alert_routing_disabled: True`, `dashboard_generated: False`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Geleceğe sızıntı yapan zaman damgası veya forward-return kolonları kesinlikle engellenir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (56 Columns)**: 56 adet sızıntı/tahmin/canlı işlem/onay/performans kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_portfolio_acceptance_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `portfolio_approved`, `guaranteed_return` iddiaları kesinlikle yasaktır (`validate_no_forbidden_portfolio_acceptance_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`portfolio_acceptance_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik, checkpoint tamlığı ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 158 Handoff Invariant**: Phase 157 çıktıları, 12 devir kalemi ile Phase 158 fazına eksiksiz devredilir (`phase_158_handoff.py`).
- **Current Phase: 157, Next Phase: 158, Target Final Phase: 160**.

## Phase 158 Full-System Integration and Advanced Acceptance Rehearsal Agent Constraints
- **Strict Non-Signal & Contract Invariant**: Agent, tam sistem entegrasyon sözleşmeleri, kabul provası (acceptance rehearsal) şablonları, checkpoint değerlendirmeleri, go/no-go kararları, blocker/gap tespitleri veya master entegrasyon manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Real-Portfolio-Construction & Zero-Real-Position-Sizing Prohibition**: Gerçek portföy oluşturulamaz, gerçek pozisyon büyüklüğü hesaplanamaz ve sermaye tahsisi yapılamaz (`allow_portfolio_construction: False`, `allow_position_sizing: False`).
- **Zero-Real-Optimization & Rebalance Prohibition**: Gerçek optimizasyon çözücüsü koşturulamaz, gerçek kısıt çözümü veya yeniden dengeleme yapılamaz (`allow_portfolio_optimization: False`, `allow_rebalance_execution: False`).
- **Zero-Real-Risk-Reporting & Scenario Execution Prohibition**: Gerçek risk raporu derlenemez, gerçek maruziyet hesaplanamaz, stres testi simülasyonu koşturulamaz ve gerçek drawdown kontrol döngüsü çalıştırılamaz (`allow_risk_reporting: False`, `allow_scenario_execution: False`, `allow_drawdown_control: False`).
- **Zero-Real-Acceptance-Rehearsal-Execution Prohibition**: Gerçek kabul provası veya canlı sistem tatbikatı koşturulamaz (`allow_rehearsal_execution: False`, `rehearsal_executed: False`).
- **Zero-Real-Metric-Calculation Prohibition**: Gerçek portföy metrikleri, risk ölçümleri veya entegrasyon performans puanı hesaplanamaz (`allow_metric_calculation: False`, `actual_value=None`).
- **Zero-Real-Alerting & Zero-Dashboard Prohibition**: Dış bildirim, webhook, SMS, e-posta veya interaktif gösterge paneli (dashboard) üretilemez (`alert_routing_disabled: True`, `dashboard_generated: False`).
- **Zero-Model-Training & Zero-Prediction Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Strictly Metadata-Only News & No-Lookahead Guards**: Haber akışlarında tam metin, makale gövdesi, HTML, NLP duygu puanı veya embedding kullanılamaz (`metadata_only: True`). Geleceğe sızıntı yapan zaman damgası veya forward-return kolonları kesinlikle engellenir.
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik değer doldurma veya özellik silme yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (52 Columns)**: 52 adet sızıntı/tahmin/canlı işlem/onay/prova kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_full_system_integration_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `system_approved`, `guaranteed_return` iddiaları kesinlikle yasaktır (`validate_no_forbidden_full_system_integration_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`full_system_integration_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik, checkpoint tamlığı ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 159 Handoff Invariant**: Phase 158 çıktıları, 13 devir kalemi ile Phase 159 (Final Hardening, Operator Runbook and Release Candidate) fazına eksiksiz devredilir (`phase_159_handoff.py`).
- **Current Phase: 158, Next Phase: 159 (Final Hardening, Operator Runbook and Release Candidate), Target Final Phase: 160**.

## Phase 159 Final Hardening, Operator Runbook and Release Candidate Agent Constraints
- **Strict Non-Signal & Hardening Contract Invariant**: Agent, final hardening sözleşmeleri, operatör prosedürleri (runbooks), release candidate checklist'leri, freeze denetimleri, sistem envanterleri veya RC manifestoları üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Production-Deployment & Zero-Release-Publish Prohibition**: Gerçek ortama deploy etme, release yayınlama, paket yayınlama veya harici sunucuya aktarma yapılamaz (`allow_production_deployment: False`, `release_published: False`).
- **Zero-Model-Training & Zero-Inference Prohibition**: Gerçek model eğitimi (`fit`, `train`, `backward`), tahmin yürütme (`predict`, `inference`), hedef etiket türetimi veya model ağırlığı kaydı yapılamaz.
- **Zero-Backtest-Optimizer-Execution Prohibition**: Gerçek backtest veya portföy optimizasyonu koşturulamaz (`allow_backtest_execution: False`, `allow_optimizer_execution: False`).
- **Zero-Real-Incident-Response & Zero-Real-Recovery Prohibition**: Canlı sistem üzerinde incident response, recovery veya restart çalıştırılamaz; sadece offline sözleşme ve rehber tanımlanır (`allow_real_incident_response: False`, `allow_real_recovery: False`).
- **Strictly Metadata-Only & Dry-Run Invariant**: Tüm kontroller kuru çalıştırma (dry-run) ve local/offline moddadır (`dry_run: True`, `local_only: True`).
- **Source Preservation & Non-Destructive Invariant**: Girdi veri çerçeveleri in-place değiştirilemez. Kaynak tablolar silinemez, ezilemez (`allow_source_overwrite: False`), otomatik dosya silme veya veri temizliği yapılamaz (`source_preserved: True`).
- **Quarantined Forbidden Columns (50 Columns)**: 50 adet sızıntı/tahmin/canlı işlem/deploy/onay kolonu sistem seviyesinde karantinadadır (`validate_no_forbidden_final_hardening_columns`).
- **Forbidden Claims & Commercial Exclusions**: `official_approval`, `production_ready`, `broker_ready`, `release_approved`, `guaranteed_return` iddiaları kesinlikle yasaktır (`validate_no_forbidden_final_hardening_claims`).
- **Readiness Score Semantics**: 1.0000 hazırlık puanı (`final_hardening_contract_ready_non_production`) yalnızca sözleşmesel eksiksizlik, dondurma bütünlüğü ve güvenlik muhafızı başarısını gösterir. Asla canlı ticarete hazır oluş, model üstünlüğü, strateji onayı veya getiri garantisi olarak sunulamaz.
- **Phase 160 Handoff Invariant**: Phase 159 çıktıları, 14 devir kalemi ile Phase 160 (Full Advanced Bot Final Delivery) fazına eksiksiz devredilir (`phase_160_handoff.py`).
- **Current Phase: 159, Next Phase: 160 (Full Advanced Bot Final Delivery), Target Final Phase: 160**.

## Phase 160 Full Advanced Bot Final Delivery and Plan Closure Agent Constraints
- **Strict Non-Signal & Delivery Package Invariant**: Agent, nihai teslimat sözleşmeleri, envanterler, kanıt kayıtları, blok özetleri veya kapanış manifestosu üzerinden kesinlikle AL/SAT sinyali, alım-satım tavsiyesi, emir, broker talimatı veya getiri beklentisi üretemez (`non_signal: True`, `allow_signal_generation: False`).
- **Zero-Live-Trading & Zero-Broker-Execution Prohibition**: Canlı borsa bağlantısı, broker API entegrasyonu, gerçek emir iletimi veya hesap yetkilendirmesi kesinlikle yapılamaz (`allow_live_trading: False`, `allow_broker_integration: False`, `allow_real_order: False`).
- **Zero-Production-Deployment & Zero-Release-Publish Prohibition**: Gerçek ortama deploy etme, release yayınlama, paket yayınlama veya harici sunucuya aktarma yapılamaz (`allow_production_deployment: False`).
- **Zero-Model-Training & Zero-Inference Prohibition**: Model eğitimi, fitting, tahmin üretimi veya ağırlık kaydı yapılamaz (`allow_model_training: False`, `allow_model_predict: False`).
- **Zero-Execution & Pure-Governance Invariant**: Teslimat ve kapanış safhasında gerçek backtest, portföy optimizasyonu, risk simülasyonu veya senaryo koşturulamaz (`allow_backtest_execution: False`, `allow_portfolio_execution: False`).
- **Source Preservation & Non-Destructive Invariant**: Kaynak kodlar yerinde değiştirilemez, ezilemez (`allow_source_overwrite: False`), hiçbir dosya silinemez.
- **Zero Blocker & Zero Gap Invariant**: Sistemik blocker (0) ve mimari gap (0) durumu korunmalıdır.
- **Readiness Score Semantics**: 100.0/100.0 hazırlık skoru (%100.0 - `FULL_ADVANCED_BOT_FINAL_DELIVERY_READY`), 160 fazlık planın sözleşmesel, mimari ve dokümantasyonel tamlığını gösterir; ticari onay veya yatırım tavsiyesi değildir.
- **Final Plan Closure Declaration**:
  - `current_phase = 160`
  - `target_final_phase = 160`
  - `next_phase = None`
  - `phase_160_completed = True`
  - `final_plan_closed = True`
  - 160 fazlık plan resmi olarak tamamlanmış ve kapanmıştır.
