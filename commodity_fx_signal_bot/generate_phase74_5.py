import os
from pathlib import Path

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

write_file('local_briefing/executive_glossary.py', '''
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
''')

write_file('local_briefing/safe_communication.py', '''
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_safe_communication_rules(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    rules = [
        ("KULLANILACAK", "offline arastirma platformu"),
        ("KULLANILACAK", "yatirim tavsiyesi degildir"),
        ("KULLANILACAK", "canli emir gondermez"),
        ("KULLANILACAK", "manual review gerekir"),
        ("KULLANILACAK", "production release degildir"),
        ("KULLANILACAK", "resmi compliance degildir"),
        ("KULLANILMAYACAK", "garanti getiri"),
        ("KULLANILMAYACAK", "canli trading hazir"),
        ("KULLANILMAYACAK", "broker execution ready")
    ]
    df = pd.DataFrame(rules, columns=["rule_type", "phrase"])
    return df, {"total_rules": len(df)}

def build_safe_communication_guide(profile: LocalBriefingProfile) -> tuple[str, dict]:
    df, summary = build_safe_communication_rules(profile)
    text = "# Safe Communication Guide\\n\\n"
    for _, row in df.iterrows():
        text += f"- **{row['rule_type']}**: {row['phrase']}\\n"
    return text, summary

def summarize_safe_communication_guide(text: str, rules_df: pd.DataFrame) -> dict:
    if rules_df is None or rules_df.empty:
        return {"total_rules": 0}
    return {"total_rules": len(rules_df)}
''')

write_file('local_briefing/communication_do_dont.py', '''
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_do_dont_examples(profile: LocalBriefingProfile) -> pd.DataFrame:
    examples = [
        ("DO", "offline/local dry-run"),
        ("DO", "karar baglami"),
        ("DO", "manuel review"),
        ("DO", "sinirliliklar"),
        ("DO", "guvenli kullanim sinirlari"),
        ("DONT", "kesin al"),
        ("DONT", "kesin sat"),
        ("DONT", "canli trade hazir"),
        ("DONT", "broker baglandi"),
        ("DONT", "uretime cikti"),
        ("DONT", "resmi onaylandi"),
        ("DONT", "garanti getiri")
    ]
    return pd.DataFrame(examples, columns=["type", "phrase"])

def build_communication_do_dont_registry(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    df = build_do_dont_examples(profile)
    return df, summarize_communication_do_dont(df)

def summarize_communication_do_dont(df: pd.DataFrame) -> dict:
    if df is None or df.empty:
        return {"total_do_dont": 0}
    return {"total_do_dont": len(df)}
''')

write_file('local_briefing/stakeholder_templates.py', '''
import pandas as pd
from .briefing_config import LocalBriefingProfile

def build_template_for_audience(audience_label: str, profile: LocalBriefingProfile) -> dict:
    base_template = "This is an offline project update.\\nNo investment advice. Requires manual review."
    return {
        "audience": audience_label,
        "template": f"{audience_label} Update:\\n{base_template}"
    }

def build_stakeholder_update_templates(profile: LocalBriefingProfile) -> tuple[pd.DataFrame, dict]:
    audiences = [
        "executive", "business stakeholder", "analyst",
        "operator handover", "developer handover", "compliance review", "nontechnical overview"
    ]
    templates = [build_template_for_audience(a, profile) for a in audiences]
    df = pd.DataFrame(templates)
    return df, summarize_stakeholder_templates(df)

def summarize_stakeholder_templates(template_df: pd.DataFrame) -> dict:
    if template_df is None or template_df.empty:
        return {"total_templates": 0}
    return {"total_templates": len(template_df)}
''')
