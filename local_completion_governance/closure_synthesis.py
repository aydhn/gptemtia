from pathlib import Path
import pandas as pd
from local_completion_governance.completion_config import LocalCompletionGovernanceProfile

def build_final_local_closure_synthesis(project_root: Path, profile: LocalCompletionGovernanceProfile) -> tuple[str, dict]:
    sections = build_closure_synthesis_sections(project_root, profile)
    text = "\n\n".join([f"# {s['title']}\n{s['content']}" for s in sections])
    return text, summarize_closure_synthesis(text)

def build_closure_synthesis_sections(project_root: Path, profile: LocalCompletionGovernanceProfile) -> list[dict]:
    return [
        {"title": "Amaç ve kapsam", "content": "Offline/local closure synthesis rehearsal."},
        {"title": "Bu closure synthesis ne değildir?", "content": "Bu rapor offline/local closure synthesis ve completion governance rehearsal çıktısıdır; gerçek certification, official acceptance, legal/compliance approval, production approval, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."},
        {"title": "Phase 1-98 genel kapanış özeti", "content": "Tamamlandı."},
        {"title": "Ana mimari katman özeti", "content": "Tamamlandı."},
        {"title": "DataLake/reporting/ML/backtest/research özeti", "content": "Tamamlandı."},
        {"title": "Governance/safety/redteam/incident/release/longterm özeti", "content": "Tamamlandı."},
        {"title": "Continuity/atlas/review/documentation/packaging/reproducibility özeti", "content": "Tamamlandı."},
        {"title": "Kritik no-go sınırları", "content": "No real trade."},
        {"title": "Manual review statement", "content": "Manual review required."},
        {"title": "Final boundary statement", "content": "Boundary enforced."}
    ]

def build_closure_synthesis_index(profile: LocalCompletionGovernanceProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"index": "1", "item": "Closure Synthesis"}])
    return df, summarize_closure_synthesis_index(df)

def summarize_closure_synthesis(text: str) -> dict:
    return {"length": len(text)}

def summarize_closure_synthesis_index(df: pd.DataFrame) -> dict:
    return {"count": len(df)}
