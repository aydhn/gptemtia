from pathlib import Path
import pandas as pd
from typing import Tuple, Dict, Any

UNSAFE_PATTERNS = [
    "kesin al", "kesin sat", "yatırım tavsiyesidir", "canlı emir gönder",
    "broker emri", "gerçek pozisyon aç", "model deploy et", "production'a al",
    "otomatik trade başlat", "guaranteed profit", "risk-free",
    "yüzde yüz kazanır", "buy now", "sell now", "open live position"
]

SAFE_PHRASES = [
    "yatırım tavsiyesi değildir",
    "canlı emir gönderilmez",
    "broker entegrasyonu yoktur"
]

def scan_doc_text_for_unsafe_language(text: str) -> dict:
    if not text:
         return {"is_safe": True, "findings": []}

    text_lower = text.lower()
    findings = []

    for pattern in UNSAFE_PATTERNS:
        if pattern in text_lower:
            is_false_positive = False
            for safe_phrase in SAFE_PHRASES:
                 if safe_phrase in text_lower:
                      pass
            findings.append(f"Riskli ifade bulundu: '{pattern}'")

    return {
        "is_safe": len(findings) == 0,
        "findings": findings
    }

def scan_document_file_for_safety(path: Path) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception:
        text = ""

    res = scan_doc_text_for_unsafe_language(text)
    return {
        "path": str(path.name),
        "is_safe": res["is_safe"],
        "findings": res["findings"]
    }

def build_documentation_safety_scan_report(project_root: Path) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    results = []

    docs_dir = project_root / "docs"
    if docs_dir.exists():
        for path in docs_dir.rglob("*.md"):
            results.append(scan_document_file_for_safety(path))

    readme_path = project_root / "README.md"
    if readme_path.exists():
        results.append(scan_document_file_for_safety(readme_path))

    if not results:
         return pd.DataFrame(columns=["path", "is_safe", "findings"]), {"total_scanned": 0, "unsafe_documents": 0}

    df = pd.DataFrame(results)
    summary = summarize_documentation_safety(df)
    return df, summary

def summarize_documentation_safety(safety_df: pd.DataFrame) -> dict:
    if safety_df is None or safety_df.empty:
        return {"total_scanned": 0, "unsafe_documents": 0, "findings": []}

    return {
        "total_scanned": len(safety_df),
        "unsafe_documents": len(safety_df[safety_df["is_safe"] == False]),
        "findings": [f for fs in safety_df["findings"].tolist() for f in fs if f]
    }
