import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_default_executive_glossary(profile: LocalBriefingProfile) -> pd.DataFrame:
    terms = [
        ("offline/local", "Projenin kendi cihazinda distan izole calismasi"),
        ("dry-run", "Gercek bir sonuc uretmeden test simulasyonu yapma"),
        ("DataLake", "Tum verilerin toplandigi lokal depolama alani"),
        ("backtest", "Gecmis veriler uzerinde model test etme (tavsiye degildir)"),
        ("paper trading", "Gercek para kullanmadan sanal ortamda islem izleme"),
        ("evidence", "Karar destek surecleri icin kanit verisi"),
        ("metadata card", "Uretilen verilerin teknik kisisel kiti"),
        ("knowledge graph", "Bilgi agi gorsellestirmesi (offline)"),
        ("timeline", "Olaylarin tarihsel siralanmasi"),
        ("consistency", "Verilerin kendi icindeki uyumlulugu"),
        ("readiness", "Offline sistemin hazir olusluk durumu"),
        ("maintenance", "Sistemin lokal bakim prosedurleri"),
        ("archive", "Eski verilerin paketlenmesi"),
        ("disaster recovery tabletop", "Sistem cokusune karsi kurtarma testi"),
        ("training pack", "Ekibe katilim icin offline egitim"),
        ("briefing deck source", "Sunum materyalleri (markdown/json)"),
        ("no-go/safe-go", "Guvenlik risk durumlarina gore operasyon onayi/reddi"),
        ("manual review", "Hicbir islemin insan onayi olmadan dikkate alinmamasi kurali")
    ]
    return pd.DataFrame(terms, columns=["term", "definition"])

def build_executive_glossary_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_executive_glossary(profile)
    return df, summarize_executive_glossary(df)

def summarize_executive_glossary(glossary_df: pd.DataFrame) -> dict:
    if glossary_df is None or glossary_df.empty:
        return {"total_terms": 0}
    return {"total_terms": len(glossary_df)}
