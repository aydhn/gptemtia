import hashlib
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict
import re

@dataclass
class KnowledgeDocument:
    document_id: str
    document_type: str
    title: str
    path: str
    relative_path: str
    source_module: Optional[str]
    created_at_utc: Optional[str]
    modified_at_utc: Optional[str]
    size_bytes: Optional[int]
    text_hash: Optional[str]
    metadata: dict
    warnings: List[str]

@dataclass
class KnowledgeChunk:
    chunk_id: str
    document_id: str
    chunk_index: int
    text: str
    token_estimate: int
    symbols: List[str]
    modules: List[str]
    keywords: List[str]
    metadata: dict
    warnings: List[str]

@dataclass
class RetrievalResult:
    result_id: str
    query: str
    document_id: str
    chunk_id: Optional[str]
    method: str
    score: float
    title: str
    path: str
    snippet: str
    metadata: dict
    warnings: List[str]

@dataclass
class ResearchMemoryCard:
    card_id: str
    card_type: str
    title: str
    symbol: Optional[str]
    module_name: Optional[str]
    summary: str
    key_findings: List[str]
    warnings: List[str]
    source_document_ids: List[str]
    created_at_utc: str
    updated_at_utc: Optional[str]

@dataclass
class DecisionJournalEntry:
    entry_id: str
    status: str
    title: str
    description: str
    related_symbols: List[str]
    related_modules: List[str]
    evidence_document_ids: List[str]
    follow_up_tasks: List[str]
    created_at_utc: str
    updated_at_utc: Optional[str]
    warnings: List[str]

def build_document_id(relative_path: str, modified_at_utc: Optional[str] = None) -> str:
    raw = f"{relative_path}_{modified_at_utc or 'unknown'}"
    return f"doc_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def build_chunk_id(document_id: str, chunk_index: int) -> str:
    return f"chk_{document_id}_{chunk_index:04d}"

def build_retrieval_result_id(query: str, document_id: str, chunk_id: Optional[str], method: str) -> str:
    raw = f"{query}_{document_id}_{chunk_id or 'nochunk'}_{method}"
    return f"ret_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def build_memory_card_id(card_type: str, title: str, symbol: Optional[str] = None) -> str:
    raw = f"{card_type}_{title}_{symbol or 'nosymbol'}"
    return f"mem_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def build_decision_journal_entry_id(title: str, created_at_utc: str) -> str:
    raw = f"{title}_{created_at_utc}"
    return f"dec_{hashlib.md5(raw.encode('utf-8')).hexdigest()[:12]}"

def knowledge_document_to_dict(document: KnowledgeDocument) -> dict:
    return asdict(document)

def knowledge_chunk_to_dict(chunk: KnowledgeChunk) -> dict:
    return asdict(chunk)

def retrieval_result_to_dict(result: RetrievalResult) -> dict:
    return asdict(result)

def research_memory_card_to_dict(card: ResearchMemoryCard) -> dict:
    return asdict(card)

def decision_journal_entry_to_dict(entry: DecisionJournalEntry) -> dict:
    return asdict(entry)

def sanitize_query_text(value: str) -> str:
    # Remove potentially dangerous characters but keep it simple
    sanitized = re.sub(r'[^\w\s\-\.\=\:]', ' ', value)
    return " ".join(sanitized.split()).strip()
