from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile


USAGE_BOUNDARIES = [
    ("boundary_research_only", "research_only", True, "Veriler yalnızca yerel araştırma, analiz ve simülasyon amacıyla kullanılabilir."),
    ("boundary_local_only", "local_only", True, "Veriler yerel dosya sisteminde tutulur; harici ağ sunucularına iletilmez."),
    ("boundary_non_production", "non_production", True, "Sistem ve veriler üretim ortamında devreye alınamaz."),
    ("boundary_no_trading_signal", "no_trading_signal", True, "Lineage/traceability çıktıları kesin AL/SAT veya yatırım tavsiyesi olarak kullanılamaz."),
    ("boundary_no_broker_order", "no_broker_order", True, "Broker API entegrasyonu, gerçek emir gönderimi veya pozisyon açımı yapılamaz."),
    ("boundary_no_investment_advice", "no_investment_advice", True, "Çıktılar sermaye piyasası mevzuatı kapsamında yatırım danışmanlığı teşkil etmez."),
    ("boundary_no_scraping", "no_scraping", True, "Web scraping, HTML parsing veya tarayıcı otomasyonu kesinlikle yasaktır."),
    ("boundary_no_credential_output", "no_credential_output", True, "Kullanıcı API anahtarları, şifreler veya gizli anahtarlar asla loglanamaz/yazdırılamaz."),
    ("boundary_no_full_article_copy", "no_full_article_copy", True, "Telifli haber tam metinleri indirilemez, kopyalanamaz veya saklanamaz."),
    ("boundary_no_destructive_action", "no_destructive_action", True, "Ham veriyi ezme, silme, taşıma veya tahrip edici otomatik temizlik yapılamaz."),
]


def build_data_usage_boundary_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    records = []
    for b_id, b_type, enforced, desc in USAGE_BOUNDARIES:
        records.append({
            "boundary_id": b_id,
            "boundary_type": b_type,
            "is_enforced": enforced,
            "description": desc,
            "status_label": "lineage_complete",
        })
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_usage_boundary_registry(df)
    return df, summary


def summarize_data_usage_boundary_registry(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_usage_boundaries": len(df),
        "all_enforced": bool(df["is_enforced"].all()) if "is_enforced" in df.columns and len(df) > 0 else True,
        "boundary_types": df["boundary_type"].tolist() if "boundary_type" in df.columns else [],
        "current_phase": 114,
        "target_final_phase": 160,
    }
