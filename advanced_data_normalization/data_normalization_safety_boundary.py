from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_normalization.data_normalization_config import DataNormalizationProfile

NO_GO_CONDITIONS = [
    ("no_live_trading", "Canlı işlem yapılması veya emir gönderilmesi kesinlikle yasaktır."),
    ("no_broker_integration", "Broker API bağlantısı kurulması yasaktır."),
    ("no_real_order", "Gerçek piyasa emri oluşturulması veya iletilmesi yasaktır."),
    ("no_exact_buy_sell", "Kesin AL/SAT veya pozisyon açma/kapama talimatı verilemez."),
    ("no_investment_advice", "Yatırım tavsiyesi veya finansal danışmanlık üretilemez."),
    ("no_normalized_data_as_signal", "Normalize edilmiş veri veya şemalar ticaret sinyali gibi sunulamaz."),
    ("no_normalization_official_approval", "Normalizasyon skoru resmi onay veya sertifikasyon olarak sunulamaz."),
    ("no_production_approval_claim", "Üretim ortamına hazır olduğuna dair iddia üretilemez."),
    ("no_model_deployment", "Model canlıya alınamaz veya sunucuya deploy edilemez."),
    ("no_production_deployment", "Canlı production deployment yapılamaz."),
    ("no_web_server", "Web sunucusu veya harici dinleyici başlatılamaz."),
    ("no_dashboard_gui_tui", "Dashboard, GUI veya TUI arayüzü kurulamaz."),
    ("no_external_llm", "Harici LLM veya inference API çağrısı yapılamaz."),
    ("no_vector_db", "Vektör veritabanı kurulamaz."),
    ("no_embedding_api", "Embedding API çağrısı yapılamaz."),
    ("no_web_scraping", "Web scraping yapılamaz."),
    ("no_html_scraping", "HTML parsing veya web sayfası indirme yapılamaz."),
    ("no_news_page_scraping", "Haber sitelerinden kazıma yapılamaz."),
    ("no_browser_automation_scraping", "Selenium, Playwright vb. tarayıcı otomasyonu ile kazıma yapılamaz."),
    ("no_hidden_api_reverse_engineering", "Gizli API'lere tersine mühendislik yapılamaz."),
    ("no_paywall_bypass", "Ödeme duvarı (paywall) aşma girişiminde bulunulamaz."),
    ("no_rate_limit_abuse", "Sağlayıcı istek limitleri istismar edilemez."),
    ("no_credential_output", "API anahtarları veya hassas parolalar çıktılara yazılamaz."),
    ("no_full_article_download", "Haber tam metinleri indirilemez veya arşivlenemez."),
    ("no_copyrighted_article_copy", "Telifli haber içerikleri kopyalanamaz veya dağıtılamaz."),
    ("no_required_paid_api", "Ücretli API'lere bağımlılık oluşturulamaz."),
    ("no_source_overwrite", "Kaynak veri dosyaları asla silinemez, taşınamaz veya üzerine yazılamaz."),
    ("no_destructive_cleaning", "Aykırı değer veya mükerrer kayıtlar veri setinden silinemez."),
    ("no_file_deletion_move", "Dosya silme veya taşıma eylemleri yapılamaz."),
    ("no_cloud_publish", "Bulut depolama alanına yükleme yapılamaz."),
    ("no_docker_push_git_tag", "Docker imajı push edilemez ve git tag oluşturulamaz."),
]

SAFE_GO_CONDITIONS = [
    ("local_offline_rules", "Tamamen yerel ve çevrimdışı normalizasyon kural motoru işletimi."),
    ("dry_run_fixtures", "Sentetik ve sözleşme dataframe'leri üzerinde test yürütme."),
    ("canonical_schema_registry", "Merkezi kanonik veri şeması sözleşmelerinin tanımlanması."),
    ("canonical_field_registry", "Alan düzeyi sözleşmelerin ve birim politikalarının tespiti."),
    ("non_destructive_views", "Kaynak veriyi koruyarak ayrı kanonik görünüm üretimi."),
    ("fx_symbol_normalization", "EURUSD -> EUR/USD şeklinde standart ISO slash dönüşümü."),
    ("commodity_symbol_normalization", "GOLD -> XAU/USD ve sürekli vadeli sembol eşlemesi."),
    ("macro_indicator_normalization", "Makro göstergelerin merkezi ontolojiye uyarlanması."),
    ("calendar_event_normalization", "Takvim olay isimlerinin standartlaştırılması."),
    ("news_topic_tag_normalization", "Haber etiketlerinin büyük harf taksonomisine dönüştürülmesi."),
    ("region_currency_normalization", "Bölge ve para birimi kodlarının ISO standartlarına çekilmesi."),
    ("timestamp_utc_normalization", "Zaman damgalarının ISO8601 UTC formatına çevrilmesi (kaynak korunur)."),
    ("session_alignment_requirements", "Piyasa seans saatleri gereksinimlerinin kayıt altına alınması."),
    ("frequency_normalization", "Veri periyotlarının kanonik '1d', '1w', '1mo' kodlarına çevrilmesi."),
    ("unit_vocabulary_normalization", "Birimlerin standart sözlükle eşlenmesi (değer dönüştürülmeden)."),
    ("numeric_type_safe_cast", "Sayısal alanların güvenli float'a çevrilmesi (orijinal korunur)."),
    ("string_slug_normalization", "Metinlerin slug veya büyük harf token standardına getirilmesi."),
    ("duplicate_key_generation", "Mükerrerlik tespiti için birleşik anahtar üretilmesi (kayıt silinmez)."),
    ("normalization_findings", "Kural uyumsuzluklarının bulgu kütüğüne kaydedilmesi."),
    ("normalization_decisions", "Her bulgu için non-destructive karar kaydı oluşturulması."),
    ("manual_review_queue", "Belirsiz veya çözülemeyen durumların inceleme kuyruğuna alınması."),
    ("normalized_output_manifest", "Kaynak ve normalize edilmiş görünümlerin açıkça belgelenmesi."),
    ("normalization_scoring", "İç teşhis amaçlı 0.0-1.0 normalizasyon skorunun hesaplanması."),
    ("phase_114_handoff", "Phase 114 veri soy kütüğü için dönüşüm izlerinin devredilmesi."),
]


def build_data_normalization_no_go_conditions(
    profile: DataNormalizationProfile,
) -> pd.DataFrame:
    records = []
    for code, desc in NO_GO_CONDITIONS:
        records.append({
            "condition_type": "NO_GO",
            "rule_code": code,
            "description": desc,
            "is_enforced": True,
            "current_phase": 113,
        })
    return pd.DataFrame.from_records(records)


def build_data_normalization_safe_go_conditions(
    profile: DataNormalizationProfile,
) -> pd.DataFrame:
    records = []
    for code, desc in SAFE_GO_CONDITIONS:
        records.append({
            "condition_type": "SAFE_GO",
            "rule_code": code,
            "description": desc,
            "is_allowed": True,
            "current_phase": 113,
        })
    return pd.DataFrame.from_records(records)


def build_data_normalization_safety_boundary(
    profile: DataNormalizationProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_go_df = build_data_normalization_no_go_conditions(profile)
    safe_go_df = build_data_normalization_safe_go_conditions(profile)
    combined = pd.concat([no_go_df, safe_go_df], ignore_index=True)
    summary = summarize_data_normalization_safety_boundary(combined)
    return combined, summary


def summarize_data_normalization_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    no_go_cnt = len(df[df["condition_type"] == "NO_GO"]) if "condition_type" in df.columns else len(NO_GO_CONDITIONS)
    safe_go_cnt = len(df[df["condition_type"] == "SAFE_GO"]) if "condition_type" in df.columns else len(SAFE_GO_CONDITIONS)
    return {
        "total_conditions": len(df),
        "total_no_go": no_go_cnt,
        "total_safe_go": safe_go_cnt,
        "source_overwrite_forbidden": True,
        "destructive_cleaning_forbidden": True,
        "current_phase": 113,
        "target_final_phase": 160,
    }
