# Data Quality Safety Boundary Report

> Bu çıktı Phase 112 Data Quality Engine raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, quality score’u trade sinyali olarak kullanma, provider official approval, production deployment, model deployment, scraping, haber tam metni toplama, telifli içerik kopyalama, external LLM/API çağrısı, gerçek provider API çağrısı zorunluluğu veya destructive auto-cleaning değildir.

## Summary
- Total Conditions: 0
- No-Go Conditions: 31
- Safe-Go Conditions: 24

## Safety Boundary Rules
| boundary_type | rule | description |
| --- | --- | --- |
| NO_GO | live_trading | Canlı trading / emir iletimi kesinlikle yasaktır. |
| NO_GO | broker_integration | Broker API bağlantısı veya credential kullanımı yasaktır. |
| NO_GO | real_order | Gerçek pozisyon veya emir oluşturma yasaktır. |
| NO_GO | investment_advice | Yatırım tavsiyesi veya yönlü AL/SAT sinyali üretmek yasaktır. |
| NO_GO | quality_score_as_signal | Quality score'u al/sat veya trade sinyali gibi sunmak yasaktır. |
| NO_GO | provider_official_approval | Provider score'u resmi onay veya akreditasyon gibi sunmak yasaktır. |
| NO_GO | production_approval_claim | Production readiness veya release approval iddiası yasaktır. |
| NO_GO | model_deployment | Model deployment veya model servisi başlatmak yasaktır. |
| NO_GO | production_deployment | Production deployment veya cloud push yasaktır. |
| NO_GO | web_server | Web server, REST API veya websocket sunucusu başlatmak yasaktır. |
| NO_GO | dashboard_gui_tui | Dashboard, GUI veya TUI ekranları oluşturmak yasaktır. |
| NO_GO | external_llm | Harici LLM veya API çağrısı yapmak yasaktır. |
| NO_GO | vector_db_embedding | Vector database kurmak veya embedding API'leri çağırmak yasaktır. |
| NO_GO | web_scraping | Web scraping yapmak yasaktır. |
| NO_GO | html_scraping | HTML parsing veya sayfa kazıma yasaktır. |
| NO_GO | news_page_scraping | Haber siteleri kazıma veya tam metin indirme yasaktır. |
| NO_GO | browser_automation | Browser automation veya selenium/playwright çalıştırmak yasaktır. |
| NO_GO | hidden_api_reverse_engineering | Gizli API reverse engineering yapmak yasaktır. |
| NO_GO | paywall_bypass | Paywall bypass girişimleri kesinlikle yasaktır. |
| NO_GO | rate_limit_abuse | Rate limit aşımı veya agresif sorgulama yasaktır. |
| NO_GO | credential_output | Sağlayıcı şifreleri, API anahtarları veya token yazdırmak/saklamak yasaktır. |
| NO_GO | full_article_download | Haber tam metni indirme veya arşivleme yasaktır. |
| NO_GO | copyrighted_article_copy | Telifli haber içeriğini kopyalamak yasaktır. |
| NO_GO | required_network_call | Gerçek API çağrısını zorunlu kılmak yasaktır; offline çalışabilmelidir. |
| NO_GO | required_paid_api | Ücretli API aboneliğini zorunlu kılmak yasaktır. |
| NO_GO | auto_overwrite_cleaning | Veri temizleme adı altında otomatik overwrite yapmak yasaktır. |
| NO_GO | file_deletion_move | Kaynak dosyaları silmek, taşımak veya içeriğini tahrip etmek yasaktır. |
| NO_GO | cloud_publish | Cloud ortama veri/kod yüklemek yasaktır. |
| NO_GO | docker_push | Docker image build/push yasaktır. |
| NO_GO | git_tag | Git tag oluşturmak yasaktır. |
| NO_GO | archive_creation | Gerçek ZIP, TAR, 7z arşivi oluşturmak yasaktır. |
| SAFE_GO | local_offline_engine | Tüm kalite kontrolleri yerel ve offline olarak çalışır. |
| SAFE_GO | dry_run_mode | Varsayılan olarak kuru çalıştırma (dry-run) modunda güvenli çalışır. |
| SAFE_GO | fixture_dataframes | Gerçek veri olmadan sentetik/örnek kontrat dataframe'leri üzerinde test edilir. |
| SAFE_GO | schema_compliance_check | Zorunlu alan varlığı ve tip uyumu raporlanır. |
| SAFE_GO | missing_data_check | Null/NaN oranları ve eksik alanlar tespit edilir. |
| SAFE_GO | stale_data_check | Zaman damgası tazelik analizi yapılır. |
| SAFE_GO | duplicate_data_check | Birincil anahtarlar üzerinden mükerrer kayıtlar tespit edilir. |
| SAFE_GO | outlier_placeholder_check | Sayısal uç değerler istatistiksel placeholder olarak işaretlenir (tahribatsız). |
| SAFE_GO | timestamp_integrity_check | Tarih formatı geçerliliği ve monoton sıralama doğrulanır. |
| SAFE_GO | frequency_unit_consistency | Kanonik frekans ve birim tanımları denetlenir. |
| SAFE_GO | fx_quality_rules | Döviz bid<=ask, spread ve ohlc tutarlılığı denetlenir. |
| SAFE_GO | commodity_quality_rules | Emtia spot, vadeli işlem metadata ve bar geometrisi doğrulanır. |
| SAFE_GO | macro_quality_rules | Makro gösterge, frekans ve revizyon metadata uyumu denetlenir. |
| SAFE_GO | calendar_quality_rules | Ekonomik takvim olay zamanı ve değer alanları doğrulanır. |
| SAFE_GO | news_metadata_quality_rules | Haberlerde yalnızca metadata ve başlık referansına izin verilir. |
| SAFE_GO | provider_metadata_rules | Sağlayıcı lisans notu, no-scraping kuralı ve credential sızıntısızlığı denetlenir. |
| SAFE_GO | ohlc_consistency_contract | High>=Low, High>=Open/Close, Low<=Open/Close matematiksel kuralları doğrulanır. |
| SAFE_GO | quote_consistency_contract | Bid<=Ask, spread>=0 ve mid spread içinde mi kontrol edilir. |
| SAFE_GO | news_copyright_boundary | Tam metin ve ham HTML tespit edildiğinde CRITICAL finding üretilir. |
| SAFE_GO | quality_finding_registry | Tüm tespitler merkezi kayıt altına alınır. |
| SAFE_GO | manual_review_queue | Tahribatsız (non-destructive) manuel inceleme kuyruğu oluşturulur. |
| SAFE_GO | provider_quality_score | İç diagnostic amaçlı 0-1 aralığında sağlayıcı kalite skoru üretilir. |
| SAFE_GO | dataset_quality_score | İç diagnostic amaçlı 0-1 aralığında veri seti kalite skoru üretilir. |
| SAFE_GO | phase_113_handoff | Phase 113 Normalization Layer için düzeltilmesi gereken alanlar listelenir. |
