from pathlib import Path
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_risk_limitation_table(project_root: Path, profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    risks = [
        ("offline/local scope", "Data disari acilamaz, guncellemeler manueldir"),
        ("data freshness limitations", "Veriler gercek zamanli degildir"),
        ("backtest limitations", "Gecmis performans gelecegi garanti etmez"),
        ("synthetic/demo/test limitations", "Sentetik veriler gercek piyasa krizlerini yansitmayabilir"),
        ("manual review requirement", "Otomasyon olmadan karar alinmamalidir"),
        ("dependency aging", "Lokal paketler eskiyebilir"),
        ("stale reports", "Raporlar olusturuldugu anin bilgisini icerir"),
        ("archive/DR simulation limits", "Sadece belirli senaryolar test edilmistir"),
        ("no live trading", "Canli islem kapabilitesi yoktur"),
        ("no official compliance", "Resmi uyum sertifikasi yoktur"),
        ("no investment advice", "Ciktilar tavsiye niteligi tasimaz")
    ]
    df = pd.DataFrame(risks, columns=["risk_limitation", "description"])
    return df, {"total_risks": len(df)}

def build_risk_limitation_narrative(project_root: Path, profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_risk_limitation_table(project_root, profile)
    text = "# Risk and Limitation Narrative\n\n"
    text += "> **UYARI:** Bu rapor offline/local stakeholder communication ve executive briefing ciktisidir; yatirim tavsiyesi, canli sinyal, broker talimati, model deployment, production release, resmi yonetim kurulu karari veya yatirim komitesi onayi degildir.\n\n"
    for _, row in df.iterrows():
        text += f"- **{row['risk_limitation']}**: {row['description']}\n"
    return text, summary

def summarize_risk_limitation_narrative(text: str, risk_df: pd.DataFrame) -> dict:
    if risk_df is None or risk_df.empty:
        return {"total_risks": 0}
    return {"total_risks": len(risk_df)}
