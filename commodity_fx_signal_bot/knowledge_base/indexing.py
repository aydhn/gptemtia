import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, List
import json

from knowledge_base.kb_models import KnowledgeDocument, KnowledgeChunk

class KnowledgeIndex:
    def __init__(self, documents_df: pd.DataFrame, chunks_df: pd.DataFrame):
        self.documents_df = documents_df
        self.chunks_df = chunks_df

    def search_documents_by_keyword(self, query: str, top_k: int = 10) -> pd.DataFrame:
        if self.documents_df.empty:
            return pd.DataFrame()

        q = query.lower()
        # Simple search in title or relative_path
        matches = self.documents_df[
            self.documents_df['title'].str.lower().str.contains(q, na=False) |
            self.documents_df['relative_path'].str.lower().str.contains(q, na=False)
        ]
        return matches.head(top_k)

    def filter_by_symbol(self, symbol: str) -> pd.DataFrame:
        if self.chunks_df.empty or 'symbols' not in self.chunks_df.columns:
            return pd.DataFrame()

        # Check if the symbol is in the list of symbols for each chunk
        mask = self.chunks_df['symbols'].apply(lambda x: symbol in x if isinstance(x, list) else False)
        return self.chunks_df[mask]

    def filter_by_module(self, module_name: str) -> pd.DataFrame:
        if self.chunks_df.empty or 'modules' not in self.chunks_df.columns:
            return pd.DataFrame()

        mask = self.chunks_df['modules'].apply(lambda x: module_name in x if isinstance(x, list) else False)
        return self.chunks_df[mask]

    def filter_by_document_type(self, document_type: str) -> pd.DataFrame:
        if self.documents_df.empty or 'document_type' not in self.documents_df.columns:
            return pd.DataFrame()

        return self.documents_df[self.documents_df['document_type'] == document_type]

    def summarize(self) -> Dict:
        return build_index_summary(self.documents_df, self.chunks_df)


def build_knowledge_index(documents: List[KnowledgeDocument], chunks: List[KnowledgeChunk]) -> KnowledgeIndex:
    docs_df = pd.DataFrame([vars(d) for d in documents]) if documents else pd.DataFrame()
    chunks_df = pd.DataFrame([vars(c) for c in chunks]) if chunks else pd.DataFrame()
    return KnowledgeIndex(docs_df, chunks_df)

def save_knowledge_index(documents_df: pd.DataFrame, chunks_df: pd.DataFrame, output_dir: Path) -> Dict:
    output_dir.mkdir(parents=True, exist_ok=True)

    docs_path = output_dir / "documents.parquet"
    chunks_path = output_dir / "chunks.parquet"
    summary_path = output_dir / "summary.json"

    if not documents_df.empty:
        documents_df.to_parquet(docs_path)
    if not chunks_df.empty:
        chunks_df.to_parquet(chunks_path)

    summary = build_index_summary(documents_df, chunks_df)
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    return summary

def load_knowledge_index(input_dir: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    docs_path = input_dir / "documents.parquet"
    chunks_path = input_dir / "chunks.parquet"

    docs_df = pd.read_parquet(docs_path) if docs_path.exists() else pd.DataFrame()
    chunks_df = pd.read_parquet(chunks_path) if chunks_path.exists() else pd.DataFrame()

    return docs_df, chunks_df

def build_index_summary(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> Dict:
    doc_count = len(documents_df) if not documents_df.empty else 0
    chunk_count = len(chunks_df) if not chunks_df.empty else 0

    doc_types = {}
    if not documents_df.empty and 'document_type' in documents_df.columns:
        doc_types = documents_df['document_type'].value_counts().to_dict()

    modules = {}
    if not chunks_df.empty and 'modules' in chunks_df.columns:
        # Explode the list column to count occurrences
        exploded = chunks_df.explode('modules')
        if not exploded.empty and 'modules' in exploded.columns:
            modules = exploded['modules'].value_counts().to_dict()

    symbols = {}
    if not chunks_df.empty and 'symbols' in chunks_df.columns:
        exploded = chunks_df.explode('symbols')
        if not exploded.empty and 'symbols' in exploded.columns:
            symbols = exploded['symbols'].value_counts().to_dict()

    return {
        "document_count": doc_count,
        "chunk_count": chunk_count,
        "document_types": doc_types,
        "modules": modules,
        "symbols": symbols
    }
