import pandas as pd
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
import datetime
import hashlib
from pathlib import Path
import json

@dataclass
class AnalystNote:
    note_id: str
    title: str
    body: str
    related_symbols: List[str]
    related_modules: List[str]
    tags: List[str]
    created_at_utc: str
    updated_at_utc: Optional[str]
    warnings: List[str]

def build_analyst_note_id(title: str, created_at_utc: str) -> str:
    raw = f"{title}_{created_at_utc}"
    return f"note_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def analyst_note_to_dict(note: AnalystNote) -> dict:
    return asdict(note)

def build_default_analyst_notes() -> List[AnalystNote]:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return [
        AnalystNote(
            note_id=build_analyst_note_id("Proje Sınırları", now),
            title="Proje Sınırları",
            body="Bu proje canlı emir göndermeyecek. Gerçek emir entegrasyonu yok.",
            related_symbols=[],
            related_modules=[],
            tags=["system", "rules"],
            created_at_utc=now,
            updated_at_utc=None,
            warnings=["Yatırım tavsiyesi içermez."]
        ),
        AnalystNote(
            note_id=build_analyst_note_id("Araştırma Yaklaşımı", now),
            title="Araştırma Yaklaşımı",
            body="Tüm sinyaller sadece offline analiz içindir.",
            related_symbols=[],
            related_modules=[],
            tags=["research"],
            created_at_utc=now,
            updated_at_utc=None,
            warnings=[]
        )
    ]

def save_analyst_notes(notes: List[AnalystNote], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / "analyst_notes.jsonl"

    with open(out_path, 'a', encoding='utf-8') as f:
        for note in notes:
            f.write(json.dumps(analyst_note_to_dict(note)) + "\n")

    return out_path

def load_analyst_notes(input_dir: Path) -> pd.DataFrame:
    in_path = input_dir / "analyst_notes.jsonl"
    if not in_path.exists():
        return pd.DataFrame()

    notes = []
    with open(in_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                notes.append(json.loads(line))

    return pd.DataFrame(notes)

def search_analyst_notes(query: str, notes_df: pd.DataFrame) -> pd.DataFrame:
    if notes_df.empty:
        return pd.DataFrame()

    q = query.lower()
    mask = (notes_df['title'].str.lower().str.contains(q, na=False) |
            notes_df['body'].str.lower().str.contains(q, na=False))

    return notes_df[mask]

def summarize_analyst_notes(notes_df: pd.DataFrame) -> Dict:
    if notes_df.empty:
        return {"total_notes": 0}

    return {
        "total_notes": len(notes_df)
    }
