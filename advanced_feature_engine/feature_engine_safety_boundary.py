from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_feature_engine.feature_engine_config import FeatureEngineProfile

NO_GO_CONDITIONS = [
    ("no_live_trading", "Canlı emir gönderimi ve gerçek işlem yürütme.", True),
    ("no_broker_integration", "Broker API entegrasyonu ve credential kullanımı.", True),
    ("no_real_order", "Gerçek pozisyon açma veya borsa emri iletimi.", True),
    ("no_investment_advice", "Yatırım tavsiyesi veya yönlendirici portföy önerisi.", True),
    ("no_feature_as_signal", "Feature veya gösterge değerini AL/SAT sinyali olarak sunma.", True),
    ("no_indicator_directional_certainty", "RSI düşük -> al veya MACD yukarı -> long gibi kesin kural üretme.", True),
    ("no_strategy_generation", "Otomatik strateji veya sinyal kuralı üretimi.", True),
    ("no_backtest_execution", "Strateji performans simülasyonu veya backtest çalıştırma.", True),
    ("no_optimizer_execution", "Parametre optimizasyonu veya aşırı uyum arama.", True),
    ("no_model_deployment", "Makine öğrenmesi model deployment.", True),
    ("no_production_deployment", "Üretim ortamına canlı kod veya servis dağıtımı.", True),
    ("no_web_server", "Web sunucusu veya harici API servisi başlatma.", True),
    ("no_dashboard", "Web dashboard veya analitik arayüz sunucusu.", True),
    ("no_gui_tui", "Etkileşimli GUI/TUI başlatma.", True),
    ("no_external_llm", "Harici LLM veya inference API çağrısı yapma.", True),
    ("no_vector_db", "Vektör veritabanı veya embedding altyapısı kurma.", True),
    ("no_embedding_api", "Dış embedding üretme API'si bağlama.", True),
    ("no_web_scraping", "Web scraping ve web sitesi veri çekme.", True),
    ("no_html_scraping", "HTML içeriği kazıma ve ayrıştırma.", True),
    ("no_news_page_scraping", "Haber sitelerinden sayfa scraping yapma.", True),
    ("no_browser_automation", "Selenium, Playwright veya Puppeteer otomasyonu.", True),
    ("no_hidden_api_reverse_engineering", "Gizli veya dokümante edilmemiş API tersine mühendisliği.", True),
    ("no_paywall_bypass", "Paywall veya kimlik doğrulama baypas etme.", True),
    ("no_rate_limit_abuse", "Sağlayıcı hız limitlerini aşma veya kötüye kullanma.", True),
    ("no_required_network_call", "Zorunlu ağ çağrısı gerektirme; offline çalışabilirlik esastır.", True),
    ("no_required_paid_api", "Ücretli API anahtarı zorunluluğu koyma.", True),
    ("no_credential_output", "API anahtarı, token veya secret loglama/yazdırma.", True),
    ("no_full_article_download", "Telifli haber tam metnini indirme veya depolama.", True),
    ("no_copyrighted_article_copy", "Telif hakkı korunan içerikleri aynen kopyalama.", True),
    ("no_source_overwrite", "Ham veri kaynaklarını veya lake dosyalarını ezme.", True),
    ("no_destructive_cleaning", "Yıkıcı veri silme veya satır kaybetme.", True),
    ("no_file_deletion", "Proje dosyalarını veya eski faz çıktılarını silme.", True),
    ("no_file_move", "Dosya taşıma veya klasör hiyerarşisini kırma.", True),
    ("no_cloud_publish", "Bulut ortamına arşiv veya paket gönderme.", True),
    ("no_docker_push", "Docker registry'ye container imajı yükleme.", True),
    ("no_git_tag", "Git sürüm etiketi veya release oluşturma.", True),
    ("no_archive_creation", "Gerçek ZIP veya tar arşivi oluşturma.", True),
    ("no_official_approval_claim", "Resmi onay, mevzuat onayı veya sertifikasyon iddiası.", True),
]

SAFE_GO_CONDITIONS = [
    ("local_offline_feature_engine", "Offline ortamda teknik gösterge ve feature tanımları yapma.", True),
    ("canonical_input_contracts", "FX, emtia, makro, takvim ve haber için kanonik girdi kontratı oluşturma.", True),
    ("non_destructive_dataframe_copy", "Her zaman df.copy() ile çalışarak orijinal veriyi koruma.", True),
    ("pure_pandas_numpy_transforms", "Harici bağımlılık olmadan saf pandas/numpy matematiksel hesaplamaları.", True),
    ("technical_indicator_catalogs", "Fiyat, trend, momentum, volatilite ve ortalamaya dönüş katalogları.", True),
    ("quote_feature_catalog", "Spread ve mid-price hesaplama katalogları.", True),
    ("volume_liquidity_placeholders", "Hacim ve likidite vekilleri placeholder tanımları.", True),
    ("macro_feature_catalog", "Makro değer değişimi ve sürpriz özellikleri katalogları.", True),
    ("calendar_event_feature_catalog", "Takvim olay günü ve pencere bayrakları katalogları.", True),
    ("news_metadata_feature_catalog", "Yalnızca konu ve varlık etiketleri kullanan haber metadata kataloğu.", True),
    ("feature_metadata_registry", "Warmup ve lookahead risklerini belgeleyen metadata kayıt defteri.", True),
    ("factor_metadata_registry", "Faktör ailesi hiyerarşisi ve araştırma sahipliği defteri.", True),
    ("rolling_window_contracts", "Pozitif tamsayı pencere ve lookahead koruması standartları.", True),
    ("feature_validation_rules", "Yasaklı sinyal kolonlarını ve lookahead shiftlerini tarayan kurallar.", True),
    ("phase_117_handoff", "Phase 117 teknik gösterge genişlemesine temiz temel devretme.", True),
]


def build_feature_engine_no_go_conditions(
    profile: FeatureEngineProfile,
) -> pd.DataFrame:
    records = []
    for cond_id, desc, enforced in NO_GO_CONDITIONS:
        records.append({
            "condition_id": cond_id,
            "category": "NO_GO",
            "description": desc,
            "enforced": enforced,
            "phase": profile.current_phase,
        })
    return pd.DataFrame.from_records(records)


def build_feature_engine_safe_go_conditions(
    profile: FeatureEngineProfile,
) -> pd.DataFrame:
    records = []
    for cond_id, desc, permitted in SAFE_GO_CONDITIONS:
        records.append({
            "condition_id": cond_id,
            "category": "SAFE_GO",
            "description": desc,
            "permitted": permitted,
            "phase": profile.current_phase,
        })
    return pd.DataFrame.from_records(records)


def build_feature_engine_safety_boundary(
    profile: FeatureEngineProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_go_df = build_feature_engine_no_go_conditions(profile)
    safe_go_df = build_feature_engine_safe_go_conditions(profile)

    combined_df = pd.concat([no_go_df, safe_go_df], ignore_index=True)
    summary = summarize_feature_engine_safety_boundary(combined_df)
    return combined_df, summary


def summarize_feature_engine_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    no_go_count = int((df["category"] == "NO_GO").sum()) if not df.empty and "category" in df.columns else 0
    safe_go_count = int((df["category"] == "SAFE_GO").sum()) if not df.empty and "category" in df.columns else 0
    return {
        "safety_status": "ACTIVE",
        "total_rules": len(df),
        "total_no_go_rules": no_go_count,
        "total_safe_go_rules": safe_go_count,
        "all_no_go_enforced": True,
        "non_signal": True,
        "current_phase": 116,
        "target_final_phase": 160,
    }
