import pandas as pd
from pathlib import Path
from typing import List, Dict, Optional
import datetime
import json

from knowledge_base.kb_models import DecisionJournalEntry, build_decision_journal_entry_id

class DecisionJournal:
    def __init__(self, journal_dir: Path):
        self.journal_dir = journal_dir
        self.journal_path = self.journal_dir / "decision_journal.jsonl"
        self.journal_dir.mkdir(parents=True, exist_ok=True)

    def add_entry(self, entry: DecisionJournalEntry) -> Path:
        with open(self.journal_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(vars(entry)) + "\n")
        return self.journal_path

    def load_entries(self) -> pd.DataFrame:
        if not self.journal_path.exists():
            return pd.DataFrame()

        entries = []
        with open(self.journal_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    entries.append(json.loads(line))
        return pd.DataFrame(entries)

    def get_entry(self, entry_id: str) -> Optional[Dict]:
        df = self.load_entries()
        if df.empty or 'entry_id' not in df.columns:
            return None
        matches = df[df['entry_id'] == entry_id]
        if matches.empty:
            return None
        return matches.iloc[0].to_dict()

    def list_by_symbol(self, symbol: str) -> pd.DataFrame:
        df = self.load_entries()
        if df.empty or 'related_symbols' not in df.columns:
            return pd.DataFrame()
        mask = df['related_symbols'].apply(lambda x: symbol in x if isinstance(x, list) else False)
        return df[mask]

    def list_by_module(self, module_name: str) -> pd.DataFrame:
        df = self.load_entries()
        if df.empty or 'related_modules' not in df.columns:
            return pd.DataFrame()
        mask = df['related_modules'].apply(lambda x: module_name in x if isinstance(x, list) else False)
        return df[mask]

    def list_by_status(self, status: str) -> pd.DataFrame:
        df = self.load_entries()
        if df.empty or 'status' not in df.columns:
            return pd.DataFrame()
        return df[df['status'] == status]

    def summarize(self) -> Dict:
        df = self.load_entries()
        if df.empty:
            return {"total_entries": 0}

        status_counts = df['status'].value_counts().to_dict() if 'status' in df.columns else {}
        return {
            "total_entries": len(df),
            "status_counts": status_counts
        }

def build_default_decision_journal_entries() -> List[DecisionJournalEntry]:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    entries = []

    defaults = [
        ("Canlı Emir Kapsam Dışı", "Canlı emir entegrasyonu bilinçli olarak kapsam dışı bırakıldı."),
        ("Yatırım Tavsiyesi Değil", "Raporlar yatırım tavsiyesi olarak adlandırılmayacak."),
        ("Otomatik Çalıştırma Yok", "Research planning önerileri otomatik çalıştırılmayacak."),
        ("Offline Retrieval", "Semantic retrieval local/offline kalacak; ücretli API kullanılmayacak.")
    ]

    for title, desc in defaults:
        entry_id = build_decision_journal_entry_id(title, now)
        entries.append(DecisionJournalEntry(
            entry_id=entry_id,
            status="decision_note",
            title=title,
            description=desc,
            related_symbols=[],
            related_modules=[],
            evidence_document_ids=[],
            follow_up_tasks=[],
            created_at_utc=now,
            updated_at_utc=None,
            warnings=["This is a system rule, not a trade decision."]
        ))

    return entries

def build_decision_entries_from_planning_backlog(backlog_df: pd.DataFrame) -> List[DecisionJournalEntry]:
    # Placeholder
    return []

def build_decision_entries_from_meta_conflicts(conflict_df: pd.DataFrame) -> List[DecisionJournalEntry]:
    # Placeholder
    return []

def decision_entries_to_dataframe(entries: List[DecisionJournalEntry]) -> pd.DataFrame:
    return pd.DataFrame([vars(e) for e in entries])
