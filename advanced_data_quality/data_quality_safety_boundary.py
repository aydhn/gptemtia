from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile

NO_GO_RULES = [
    ("live_trading", "Canlı trading / emir iletimi kesinlikle yasaktır."),
    ("broker_integration", "Broker API bağlantısı veya credential kullanımı yasaktır."),
    ("real_order", "Gerçek pozisyon veya emir oluşturma yasaktır."),
    ("investment_advice", "Yatırım tavsiyesi veya yönlü AL/SAT sinyali üretmek yasaktır."),
    ("quality_score_as_signal", "Quality score'u al/sat veya trade sinyali gibi sunmak yasaktır."),
    ("provider_official_approval", "Provider score'u resmi onay veya akreditasyon gibi sunmak yasaktır."),
    ("production_approval_claim", "Production readiness veya release approval iddiası yasaktır."),
    ("model_deployment", "Model deployment veya model servisi başlatmak yasaktır."),
    ("production_deployment", "Production deployment veya cloud push yasaktır."),
    ("web_server", "Web server, REST API veya websocket sunucusu başlatmak yasaktır."),
    ("dashboard_gui_tui", "Dashboard, GUI veya TUI ekranları oluşturmak yasaktır."),
    ("external_llm", "Harici LLM veya API çağrısı yapmak yasaktır."),
    ("vector_db_embedding", "Vector database kurmak veya embedding API'leri çağırmak yasaktır."),
    ("web_scraping", "Web scraping yapmak yasaktır."),
    ("html_scraping", "HTML parsing veya sayfa kazıma yasaktır."),
    ("news_page_scraping", "Haber siteleri kazıma veya tam metin indirme yasaktır."),
    ("browser_automation", "Browser automation veya selenium/playwright çalıştırmak yasaktır."),
    ("hidden_api_reverse_engineering", "Gizli API reverse engineering yapmak yasaktır."),
    ("paywall_bypass", "Paywall bypass girişimleri kesinlikle yasaktır."),
    ("rate_limit_abuse", "Rate limit aşımı veya agresif sorgulama yasaktır."),
    ("credential_output", "Sağlayıcı şifreleri, API anahtarları veya token yazdırmak/saklamak yasaktır."),
    ("full_article_download", "Haber tam metni indirme veya arşivleme yasaktır."),
    ("copyrighted_article_copy", "Telifli haber içeriğini kopyalamak yasaktır."),
    ("required_network_call", "Gerçek API çağrısını zorunlu kılmak yasaktır; offline çalışabilmelidir."),
    ("required_paid_api", "Ücretli API aboneliğini zorunlu kılmak yasaktır."),
    ("auto_overwrite_cleaning", "Veri temizleme adı altında otomatik overwrite yapmak yasaktır."),
    ("file_deletion_move", "Kaynak dosyaları silmek, taşımak veya içeriğini tahrip etmek yasaktır."),
    ("cloud_publish", "Cloud ortama veri/kod yüklemek yasaktır."),
    ("docker_push", "Docker image build/push yasaktır."),
    ("git_tag", "Git tag oluşturmak yasaktır."),
    ("archive_creation", "Gerçek ZIP, TAR, 7z arşivi oluşturmak yasaktır."),
]

SAFE_GO_RULES = [
    ("local_offline_engine", "Tüm kalite kontrolleri yerel ve offline olarak çalışır."),
    ("dry_run_mode", "Varsayılan olarak kuru çalıştırma (dry-run) modunda güvenli çalışır."),
    ("fixture_dataframes", "Gerçek veri olmadan sentetik/örnek kontrat dataframe'leri üzerinde test edilir."),
    ("schema_compliance_check", "Zorunlu alan varlığı ve tip uyumu raporlanır."),
    ("missing_data_check", "Null/NaN oranları ve eksik alanlar tespit edilir."),
    ("stale_data_check", "Zaman damgası tazelik analizi yapılır."),
    ("duplicate_data_check", "Birincil anahtarlar üzerinden mükerrer kayıtlar tespit edilir."),
    ("outlier_placeholder_check", "Sayısal uç değerler istatistiksel placeholder olarak işaretlenir (tahribatsız)."),
    ("timestamp_integrity_check", "Tarih formatı geçerliliği ve monoton sıralama doğrulanır."),
    ("frequency_unit_consistency", "Kanonik frekans ve birim tanımları denetlenir."),
    ("fx_quality_rules", "Döviz bid<=ask, spread ve ohlc tutarlılığı denetlenir."),
    ("commodity_quality_rules", "Emtia spot, vadeli işlem metadata ve bar geometrisi doğrulanır."),
    ("macro_quality_rules", "Makro gösterge, frekans ve revizyon metadata uyumu denetlenir."),
    ("calendar_quality_rules", "Ekonomik takvim olay zamanı ve değer alanları doğrulanır."),
    ("news_metadata_quality_rules", "Haberlerde yalnızca metadata ve başlık referansına izin verilir."),
    ("provider_metadata_rules", "Sağlayıcı lisans notu, no-scraping kuralı ve credential sızıntısızlığı denetlenir."),
    ("ohlc_consistency_contract", "High>=Low, High>=Open/Close, Low<=Open/Close matematiksel kuralları doğrulanır."),
    ("quote_consistency_contract", "Bid<=Ask, spread>=0 ve mid spread içinde mi kontrol edilir."),
    ("news_copyright_boundary", "Tam metin ve ham HTML tespit edildiğinde CRITICAL finding üretilir."),
    ("quality_finding_registry", "Tüm tespitler merkezi kayıt altına alınır."),
    ("manual_review_queue", "Tahribatsız (non-destructive) manuel inceleme kuyruğu oluşturulur."),
    ("provider_quality_score", "İç diagnostic amaçlı 0-1 aralığında sağlayıcı kalite skoru üretilir."),
    ("dataset_quality_score", "İç diagnostic amaçlı 0-1 aralığında veri seti kalite skoru üretilir."),
    ("phase_113_handoff", "Phase 113 Normalization Layer için düzeltilmesi gereken alanlar listelenir."),
]


def build_data_quality_no_go_conditions(profile: DataQualityProfile) -> pd.DataFrame:
    records = [{"boundary_type": "NO_GO", "rule": r[0], "description": r[1]} for r in NO_GO_RULES]
    return pd.DataFrame.from_records(records)


def build_data_quality_safe_go_conditions(profile: DataQualityProfile) -> pd.DataFrame:
    records = [{"boundary_type": "SAFE_GO", "rule": r[0], "description": r[1]} for r in SAFE_GO_RULES]
    return pd.DataFrame.from_records(records)


def build_data_quality_safety_boundary(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_gos = build_data_quality_no_go_conditions(profile)
    safe_gos = build_data_quality_safe_go_conditions(profile)
    combined = pd.concat([no_gos, safe_gos], ignore_index=True)
    summary = summarize_data_quality_safety_boundary(combined)
    return combined, summary


def summarize_data_quality_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    no_go_count = int((df["boundary_type"] == "NO_GO").sum()) if "boundary_type" in df.columns else len(NO_GO_RULES)
    safe_go_count = int((df["boundary_type"] == "SAFE_GO").sum()) if "boundary_type" in df.columns else len(SAFE_GO_RULES)
    return {
        "total_rules": len(df),
        "no_go_count": no_go_count,
        "safe_go_count": safe_go_count,
        "current_phase": 112,
        "target_final_phase": 160,
    }
