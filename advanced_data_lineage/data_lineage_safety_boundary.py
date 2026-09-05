from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


NO_GO_ITEMS = [
    ("nogo_001", "live_trading", "Canlı piyasada gerçek işlem yapılması"),
    ("nogo_002", "broker_integration", "Broker API veya emir iletim köprüsü bağlanması"),
    ("nogo_003", "real_order", "Gerçek pozisyon açılması veya portföy işlemi yapılması"),
    ("nogo_004", "exact_buy_sell_instruction", "Kullanıcıya kesin AL/SAT talimatı verilmesi"),
    ("nogo_005", "investment_advice", "Yatırım tavsiyesi veya sermaye piyasası danışmanlığı verilmesi"),
    ("nogo_006", "lineage_score_as_trading_signal", "Lineage skorunun işlem sinyali olarak sunulması"),
    ("nogo_007", "traceability_score_as_official_approval", "İzlenebilirlik skorunun resmi sağlayıcı onayı gibi sunulması"),
    ("nogo_008", "production_approval_claim", "Sistemin production ready olduğu iddiası"),
    ("nogo_009", "model_deployment", "Makine öğrenmesi veya sinyal modeli deployment"),
    ("nogo_010", "production_deployment", "Canlı ortama sunucu veya servis kurulması"),
    ("nogo_011", "web_server_dashboard", "Web sunucusu, dashboard, GUI veya TUI başlatılması"),
    ("nogo_012", "external_llm_vector_embedding", "Harici LLM, vector database veya embedding API çağrısı"),
    ("nogo_013", "graph_database_creation", "Gerçek graph database veya harici graph motoru kurulması"),
    ("nogo_014", "web_scraping", "Web scraping veya veri çekme"),
    ("nogo_015", "html_scraping", "HTML kaynak kodunun kazınması"),
    ("nogo_016", "news_page_scraping", "Haber sitelerinin taranması"),
    ("nogo_017", "browser_automation_scraping", "Selenium, Playwright veya tarayıcı otomasyonu"),
    ("nogo_018", "hidden_api_reverse_engineering", "Tersine mühendislik ile gizli API bulunması"),
    ("nogo_019", "paywall_bypass", "Ödeme duvarlarının aşılması"),
    ("nogo_020", "rate_limit_abuse", "Sağlayıcı istek limitlerinin kötüye kullanılması"),
    ("nogo_021", "credential_output", "API anahtarları veya parolaların loglanması/çıktılanması"),
    ("nogo_022", "full_article_download", "Haber tam metinlerinin indirilmesi"),
    ("nogo_023", "copyrighted_article_copy", "Telifli haber veya makale metinlerinin kopyalanması"),
    ("nogo_024", "required_paid_api_lockin", "Ücretli API'lere zorunlu bağımlılık yaratılması"),
    ("nogo_025", "source_overwrite", "Kaynak veri dosyalarının üzerine yazılması"),
    ("nogo_026", "destructive_cleaning", "Verilerin otomatik veya geri dönülemez şekilde silinmesi"),
    ("nogo_027", "file_deletion_move_overwrite", "Dosya silme, taşıma veya zorunlu ezme eylemleri"),
    ("nogo_028", "cloud_publish", "Bulut ortamlarına veri yüklenmesi"),
    ("nogo_029", "docker_push", "Konteyner depolarına imaj yüklenmesi"),
    ("nogo_030", "git_tag_release", "Sürüm veya git release tag'i atılması"),
    ("nogo_031", "archive_creation", "Gerçek ZIP, TAR veya 7z arşiv dosyası üretilmesi"),
    ("nogo_032", "official_approval_wording", "Resmi onay veya regulator compliance iddiası"),
]

SAFE_GO_ITEMS = [
    ("safego_001", "local_offline_lineage_registry", "Tamamen yerel ve çevrimdışı soy kütüğü kayıt defteri"),
    ("safego_002", "dry_run_fixture_provenance", "Sentetik ve sözleşme fikstürleri üzerinde izlenebilirlik"),
    ("safego_003", "provider_provenance_registry", "Sağlayıcı lisans ve kimlik soy kütüğü kaydı"),
    ("safego_004", "dataset_provenance_registry", "Veri seti düzeyinde kaynak ve normalizasyon eşlemesi"),
    ("safego_005", "schema_provenance_registry", "Kaynak ve kanonik şema sürümlerinin izlenmesi"),
    ("safego_006", "transformation_provenance_registry", "Dönüşüm kurallarının alan seviyesi kaydı"),
    ("safego_007", "normalization_lineage_registry", "Phase 113 normalizasyon kurallarının izlenebilirliği"),
    ("safego_008", "quality_manual_review_lineage", "Kalite bulguları ve manuel inceleme kuyruğu soy kütüğü"),
    ("safego_009", "normalized_output_lineage", "Orijinal ve normalize görünüm manifest bağlarının tutulması"),
    ("safego_010", "license_copyright_metadata_only", "Telif sınırları ve sıfır tam metin garantisi"),
    ("safego_011", "audit_trail_placeholder", "Değişmez denetim izi olay kayıtları"),
    ("safego_012", "traceability_score_diagnostic", "Yalnızca iç teşhis amaçlı izlenebilirlik skoru"),
    ("safego_013", "cross_domain_provenance_map", "Varlık sınıfları arası çapraz soy kütüğü haritası"),
    ("safego_014", "phase_115_benchmark_handoff", "Phase 115 benchmark karşılaştırmaları için girdi hazırlığı"),
    ("safego_015", "non_destructive_preservation", "Tüm ham verilerin değiştirilmeden korunması (`source_preserved: True`)"),
]


def build_data_lineage_no_go_conditions(profile: DataLineageProfile) -> pd.DataFrame:
    records = []
    for c_id, name, desc in NO_GO_ITEMS:
        records.append({
            "condition_id": c_id,
            "rule_name": name,
            "description": desc,
            "status": "BLOCKED_NO_GO",
            "enforced": True,
        })
    return pd.DataFrame.from_records(records)


def build_data_lineage_safe_go_conditions(profile: DataLineageProfile) -> pd.DataFrame:
    records = []
    for c_id, name, desc in SAFE_GO_ITEMS:
        records.append({
            "condition_id": c_id,
            "rule_name": name,
            "description": desc,
            "status": "ALLOWED_SAFE_GO",
            "enforced": True,
        })
    return pd.DataFrame.from_records(records)


def build_data_lineage_safety_boundary(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    no_go_df = build_data_lineage_no_go_conditions(profile)
    safe_go_df = build_data_lineage_safe_go_conditions(profile)
    df = pd.concat([no_go_df, safe_go_df], ignore_index=True)
    summary = summarize_data_lineage_safety_boundary(df)
    return df, summary


def summarize_data_lineage_safety_boundary(df: pd.DataFrame) -> Dict[str, Any]:
    no_go_count = int((df["status"] == "BLOCKED_NO_GO").sum()) if "status" in df.columns else 0
    safe_go_count = int((df["status"] == "ALLOWED_SAFE_GO").sum()) if "status" in df.columns else 0
    return {
        "total_safety_rules": len(df),
        "total_no_go": no_go_count,
        "total_safe_go": safe_go_count,
        "safety_status": "ACTIVE_ENFORCED",
        "current_phase": 114,
        "target_final_phase": 160,
    }
