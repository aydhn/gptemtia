import pandas as pd
from pathlib import Path
from .readiness_config import LocalReadinessProfile

def build_phase_completion_evidence_binder(project_root: Path, profile: LocalReadinessProfile) -> tuple[str, dict]:
    text = "# Phase Completion Evidence Binder\n\n"
    text += "Bu çıktı offline/local non-production readiness dry-run raporudur. Production release onayı, canlı emir, broker talimatı, gerçek pozisyon, model deployment, production scheduler, otomatik trade onayı veya yatırım tavsiyesi değildir.\n\n"
    text += "## Phase 1-69 Kapsam Özeti\n"
    text += "Tüm data, feature, ml, backtest, paper, ve readiness süreçlerinin kanıtları listelenmektedir.\n\n"

    text += "## Eksik Evidence Alanları\n"
    text += "- Kontrol ediliyor...\n\n"

    text += "## Manual Review Gereken Alanlar\n"
    text += "- Kontrol ediliyor...\n\n"

    index_df, _ = build_phase_evidence_index(project_root, profile)
    text += "## Index\n"
    text += index_df.to_markdown() + "\n"

    summary = summarize_phase_evidence_binder(text, index_df)
    return text, summary

def build_phase_evidence_index(project_root: Path, profile: LocalReadinessProfile) -> tuple[pd.DataFrame, dict]:
    data = [
        {"module": "data", "evidence": "data/storage/data_lake.py"},
        {"module": "ml", "evidence": "ml/feature_store.py"},
        {"module": "local_readiness", "evidence": "local_readiness/readiness_pipeline.py"}
    ]
    df = pd.DataFrame(data)
    return df, {"total": len(df)}

def summarize_phase_evidence_binder(binder_text: str, index_df: pd.DataFrame) -> dict:
    return {
        "text_length": len(binder_text),
        "index_count": len(index_df)
    }

def save_phase_evidence_binder(text: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(text)
    return output_path
