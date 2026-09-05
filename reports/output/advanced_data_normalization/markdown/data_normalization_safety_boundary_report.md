# Phase 113 — Data Normalization Safety Boundary Report

> [!IMPORTANT]
> **YASAL UYARI VE GÜVENLİK SINIRI**:
> Bu çıktı Phase 113 Data Normalization Layer raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, normalized data’yı trade sinyali olarak kullanma, official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu, source overwrite veya destructive cleaning değildir.


## Güvenlik Sınırı Özeti
- **Toplam No-Go Maddesi**: 31
- **Toplam Safe-Go Maddesi**: 24
- **Kaynak Koruma Garantisi**: True
- **Yıkıcı Temizleme Yasağı**: True

## Güvenlik Kuralları
| condition_type | rule_code | description | is_enforced | current_phase | is_allowed |
| --- | --- | --- | --- | --- | --- |
| NO_GO | no_live_trading | Canlı işlem yapılması veya emir gönderilmesi kesinlikle yasaktır. | True | 113 | nan |
| NO_GO | no_broker_integration | Broker API bağlantısı kurulması yasaktır. | True | 113 | nan |
| NO_GO | no_real_order | Gerçek piyasa emri oluşturulması veya iletilmesi yasaktır. | True | 113 | nan |
| NO_GO | no_exact_buy_sell | Kesin AL/SAT veya pozisyon açma/kapama talimatı verilemez. | True | 113 | nan |
| NO_GO | no_investment_advice | Yatırım tavsiyesi veya finansal danışmanlık üretilemez. | True | 113 | nan |
| NO_GO | no_normalized_data_as_signal | Normalize edilmiş veri veya şemalar ticaret sinyali gibi sunulamaz. | True | 113 | nan |
| NO_GO | no_normalization_official_approval | Normalizasyon skoru resmi onay veya sertifikasyon olarak sunulamaz. | True | 113 | nan |
| NO_GO | no_production_approval_claim | Üretim ortamına hazır olduğuna dair iddia üretilemez. | True | 113 | nan |
| NO_GO | no_model_deployment | Model canlıya alınamaz veya sunucuya deploy edilemez. | True | 113 | nan |
| NO_GO | no_production_deployment | Canlı production deployment yapılamaz. | True | 113 | nan |
| NO_GO | no_web_server | Web sunucusu veya harici dinleyici başlatılamaz. | True | 113 | nan |
| NO_GO | no_dashboard_gui_tui | Dashboard, GUI veya TUI arayüzü kurulamaz. | True | 113 | nan |
| NO_GO | no_external_llm | Harici LLM veya inference API çağrısı yapılamaz. | True | 113 | nan |
| NO_GO | no_vector_db | Vektör veritabanı kurulamaz. | True | 113 | nan |
| NO_GO | no_embedding_api | Embedding API çağrısı yapılamaz. | True | 113 | nan |
| NO_GO | no_web_scraping | Web scraping yapılamaz. | True | 113 | nan |
| NO_GO | no_html_scraping | HTML parsing veya web sayfası indirme yapılamaz. | True | 113 | nan |
| NO_GO | no_news_page_scraping | Haber sitelerinden kazıma yapılamaz. | True | 113 | nan |
| NO_GO | no_browser_automation_scraping | Selenium, Playwright vb. tarayıcı otomasyonu ile kazıma yapılamaz. | True | 113 | nan |
| NO_GO | no_hidden_api_reverse_engineering | Gizli API'lere tersine mühendislik yapılamaz. | True | 113 | nan |
| NO_GO | no_paywall_bypass | Ödeme duvarı (paywall) aşma girişiminde bulunulamaz. | True | 113 | nan |
| NO_GO | no_rate_limit_abuse | Sağlayıcı istek limitleri istismar edilemez. | True | 113 | nan |
| NO_GO | no_credential_output | API anahtarları veya hassas parolalar çıktılara yazılamaz. | True | 113 | nan |
| NO_GO | no_full_article_download | Haber tam metinleri indirilemez veya arşivlenemez. | True | 113 | nan |
| NO_GO | no_copyrighted_article_copy | Telifli haber içerikleri kopyalanamaz veya dağıtılamaz. | True | 113 | nan |
| NO_GO | no_required_paid_api | Ücretli API'lere bağımlılık oluşturulamaz. | True | 113 | nan |
| NO_GO | no_source_overwrite | Kaynak veri dosyaları asla silinemez, taşınamaz veya üzerine yazılamaz. | True | 113 | nan |
| NO_GO | no_destructive_cleaning | Aykırı değer veya mükerrer kayıtlar veri setinden silinemez. | True | 113 | nan |
| NO_GO | no_file_deletion_move | Dosya silme veya taşıma eylemleri yapılamaz. | True | 113 | nan |
| NO_GO | no_cloud_publish | Bulut depolama alanına yükleme yapılamaz. | True | 113 | nan |
| NO_GO | no_docker_push_git_tag | Docker imajı push edilemez ve git tag oluşturulamaz. | True | 113 | nan |
| SAFE_GO | local_offline_rules | Tamamen yerel ve çevrimdışı normalizasyon kural motoru işletimi. | nan | 113 | True |
| SAFE_GO | dry_run_fixtures | Sentetik ve sözleşme dataframe'leri üzerinde test yürütme. | nan | 113 | True |
| SAFE_GO | canonical_schema_registry | Merkezi kanonik veri şeması sözleşmelerinin tanımlanması. | nan | 113 | True |
| SAFE_GO | canonical_field_registry | Alan düzeyi sözleşmelerin ve birim politikalarının tespiti. | nan | 113 | True |
| SAFE_GO | non_destructive_views | Kaynak veriyi koruyarak ayrı kanonik görünüm üretimi. | nan | 113 | True |
| SAFE_GO | fx_symbol_normalization | EURUSD -> EUR/USD şeklinde standart ISO slash dönüşümü. | nan | 113 | True |
| SAFE_GO | commodity_symbol_normalization | GOLD -> XAU/USD ve sürekli vadeli sembol eşlemesi. | nan | 113 | True |
| SAFE_GO | macro_indicator_normalization | Makro göstergelerin merkezi ontolojiye uyarlanması. | nan | 113 | True |
| SAFE_GO | calendar_event_normalization | Takvim olay isimlerinin standartlaştırılması. | nan | 113 | True |
| SAFE_GO | news_topic_tag_normalization | Haber etiketlerinin büyük harf taksonomisine dönüştürülmesi. | nan | 113 | True |
| SAFE_GO | region_currency_normalization | Bölge ve para birimi kodlarının ISO standartlarına çekilmesi. | nan | 113 | True |
| SAFE_GO | timestamp_utc_normalization | Zaman damgalarının ISO8601 UTC formatına çevrilmesi (kaynak korunur). | nan | 113 | True |
| SAFE_GO | session_alignment_requirements | Piyasa seans saatleri gereksinimlerinin kayıt altına alınması. | nan | 113 | True |
| SAFE_GO | frequency_normalization | Veri periyotlarının kanonik '1d', '1w', '1mo' kodlarına çevrilmesi. | nan | 113 | True |
| SAFE_GO | unit_vocabulary_normalization | Birimlerin standart sözlükle eşlenmesi (değer dönüştürülmeden). | nan | 113 | True |
| SAFE_GO | numeric_type_safe_cast | Sayısal alanların güvenli float'a çevrilmesi (orijinal korunur). | nan | 113 | True |
| SAFE_GO | string_slug_normalization | Metinlerin slug veya büyük harf token standardına getirilmesi. | nan | 113 | True |
| SAFE_GO | duplicate_key_generation | Mükerrerlik tespiti için birleşik anahtar üretilmesi (kayıt silinmez). | nan | 113 | True |
| SAFE_GO | normalization_findings | Kural uyumsuzluklarının bulgu kütüğüne kaydedilmesi. | nan | 113 | True |
| SAFE_GO | normalization_decisions | Her bulgu için non-destructive karar kaydı oluşturulması. | nan | 113 | True |
| SAFE_GO | manual_review_queue | Belirsiz veya çözülemeyen durumların inceleme kuyruğuna alınması. | nan | 113 | True |
| SAFE_GO | normalized_output_manifest | Kaynak ve normalize edilmiş görünümlerin açıkça belgelenmesi. | nan | 113 | True |
| SAFE_GO | normalization_scoring | İç teşhis amaçlı 0.0-1.0 normalizasyon skorunun hesaplanması. | nan | 113 | True |
| SAFE_GO | phase_114_handoff | Phase 114 veri soy kütüğü için dönüşüm izlerinin devredilmesi. | nan | 113 | True |
