import re
from typing import List
import pandas as pd

from knowledge_base.kb_config import KnowledgeBaseProfile
from knowledge_base.kb_models import KnowledgeDocument, KnowledgeChunk, build_chunk_id
from knowledge_base.text_extraction import estimate_token_count

KNOWN_SYMBOLS = [
    "GC=F", "SI=F", "HG=F", "PA=F", "PL=F", "CL=F", "BZ=F", "NG=F",
    "ZW=F", "ZC=F", "ZS=F", "KC=F", "CC=F", "SB=F", "CT=F",
    "USDTRY=X", "EURTRY=X", "GBPTRY=X", "JPYTRY=X", "CNHTRY=X"
]

KNOWN_MODULES = [
    "research_reports", "report_exports", "portfolio_research", "portfolio_regime",
    "synthetic_indices", "factor_research", "meta_research", "experiments",
    "governance", "research_planning", "ml", "paper", "validation", "backtesting",
    "observability", "security"
]

def split_text_into_chunks(text: str, chunk_size: int = 1200, overlap: int = 150) -> List[str]:
    if not text:
        return []

    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size

        # Try to break at a newline or space if we're not at the end
        if end < len(text):
            # Look back for a newline
            newline_pos = text.rfind('\n', start + chunk_size - overlap, end)
            if newline_pos != -1:
                end = newline_pos + 1
            else:
                # Look back for a space
                space_pos = text.rfind(' ', start + chunk_size - overlap, end)
                if space_pos != -1:
                    end = space_pos + 1

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        start = end - overlap
        if start < 0:
            start = 0

    return chunks

def extract_symbols_from_text(text: str) -> List[str]:
    found = []
    for sym in KNOWN_SYMBOLS:
        if sym in text:
            found.append(sym)
    return found

def extract_modules_from_text(text: str) -> List[str]:
    found = []
    for mod in KNOWN_MODULES:
        if mod in text.lower():
            found.append(mod)
    return found

def extract_keywords_from_text(text: str, max_keywords: int = 20) -> List[str]:
    # Very basic keyword extraction based on frequency of words > 4 chars
    words = re.findall(r'\b[a-zA-Z]{5,}\b', text.lower())
    freq: dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # Sort by frequency
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w, _ in sorted_words[:max_keywords]]

def build_chunks_for_document(document: KnowledgeDocument, text: str, profile: KnowledgeBaseProfile) -> List[KnowledgeChunk]:
    text_chunks = split_text_into_chunks(text, profile.chunk_size_chars, profile.chunk_overlap_chars)

    chunks = []
    for i, text_chunk in enumerate(text_chunks):
        chunk_id = build_chunk_id(document.document_id, i)

        chunk = KnowledgeChunk(
            chunk_id=chunk_id,
            document_id=document.document_id,
            chunk_index=i,
            text=text_chunk,
            token_estimate=estimate_token_count(text_chunk),
            symbols=extract_symbols_from_text(text_chunk),
            modules=extract_modules_from_text(text_chunk),
            keywords=extract_keywords_from_text(text_chunk),
            metadata={},
            warnings=[]
        )
        chunks.append(chunk)

    return chunks

def chunks_to_dataframe(chunks: List[KnowledgeChunk]) -> pd.DataFrame:
    return pd.DataFrame([vars(c) for c in chunks])
