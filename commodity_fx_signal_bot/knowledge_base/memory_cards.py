import pandas as pd
from typing import List, Dict, Optional
import datetime

from knowledge_base.kb_models import ResearchMemoryCard, build_memory_card_id

def build_symbol_memory_card(symbol: str, documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> ResearchMemoryCard:
    if chunks_df.empty:
        return _empty_card("symbol_memory_card", f"Memory for {symbol}", symbol)

    mask = chunks_df['symbols'].apply(lambda x: symbol in x if isinstance(x, list) else False)
    sym_chunks = chunks_df[mask]

    if sym_chunks.empty:
        return _empty_card("symbol_memory_card", f"Memory for {symbol}", symbol)

    doc_ids = sym_chunks['document_id'].unique().tolist()

    # Very basic extraction of findings/warnings based on keywords in chunks
    findings = []
    warnings = []

    for text in sym_chunks['text'].tolist():
        if isinstance(text, str):
            t_lower = text.lower()
            if any(w in t_lower for w in ['found', 'significant', 'observed', 'indicates']):
                if len(findings) < 5:
                    # Snip
                    findings.append(text[:150] + "...")
            if any(w in t_lower for w in ['warning', 'failed', 'missing', 'conflict', 'uncertain']):
                if len(warnings) < 5:
                    warnings.append(text[:150] + "...")

    card_id = build_memory_card_id("symbol_memory_card", f"Memory for {symbol}", symbol)

    return ResearchMemoryCard(
        card_id=card_id,
        card_type="symbol_memory_card",
        title=f"Memory for {symbol}",
        symbol=symbol,
        module_name=None,
        summary=f"Found {len(sym_chunks)} chunks mentioning {symbol} across {len(doc_ids)} documents.",
        key_findings=list(set(findings)),
        warnings=list(set(warnings)),
        source_document_ids=doc_ids,
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        updated_at_utc=None
    )

def build_hypothesis_memory_cards(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> List[ResearchMemoryCard]:
    # Placeholder for actual hypothesis extraction
    return []

def build_governance_memory_card(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> ResearchMemoryCard:
    card_id = build_memory_card_id("governance_memory_card", "Governance Overview")
    return ResearchMemoryCard(
        card_id=card_id,
        card_type="governance_memory_card",
        title="Governance Overview",
        symbol=None,
        module_name="governance",
        summary="Governance rules and provenance tracking active.",
        key_findings=["All artifacts must have fingerprints."],
        warnings=[],
        source_document_ids=[],
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        updated_at_utc=None
    )

def build_planning_memory_card(documents_df: pd.DataFrame, chunks_df: pd.DataFrame) -> ResearchMemoryCard:
    card_id = build_memory_card_id("planning_memory_card", "Planning Overview")
    return ResearchMemoryCard(
        card_id=card_id,
        card_type="planning_memory_card",
        title="Planning Overview",
        symbol=None,
        module_name="research_planning",
        summary="Research planning backlog tracks next best experiments.",
        key_findings=[],
        warnings=[],
        source_document_ids=[],
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        updated_at_utc=None
    )

def build_warning_memory_cards(chunks_df: pd.DataFrame, max_cards: int = 50) -> List[ResearchMemoryCard]:
    if chunks_df.empty:
        return []

    mask = chunks_df['text'].str.lower().str.contains('warning', na=False)
    warn_chunks = chunks_df[mask].head(max_cards)

    cards = []
    for _, row in warn_chunks.iterrows():
        doc_id = row.get('document_id', 'unknown')
        chunk_id = row.get('chunk_id', 'unknown')
        text = row.get('text', '')

        card_id = build_memory_card_id("warning_memory_card", f"Warning {chunk_id}")
        card = ResearchMemoryCard(
            card_id=card_id,
            card_type="warning_memory_card",
            title=f"Warning from {doc_id}",
            symbol=None,
            module_name=None,
            summary=text[:100] + "...",
            key_findings=[],
            warnings=[text],
            source_document_ids=[doc_id],
            created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            updated_at_utc=None
        )
        cards.append(card)

    return cards

def memory_cards_to_dataframe(cards: List[ResearchMemoryCard]) -> pd.DataFrame:
    return pd.DataFrame([vars(c) for c in cards])

def summarize_memory_cards(cards: List[ResearchMemoryCard]) -> Dict:
    if not cards:
        return {"total_cards": 0}

    types = {}
    for c in cards:
        types[c.card_type] = types.get(c.card_type, 0) + 1

    return {
        "total_cards": len(cards),
        "types": types
    }

def _empty_card(c_type: str, title: str, symbol: Optional[str] = None) -> ResearchMemoryCard:
    card_id = build_memory_card_id(c_type, title, symbol)
    return ResearchMemoryCard(
        card_id=card_id,
        card_type=c_type,
        title=title,
        symbol=symbol,
        module_name=None,
        summary="No data found.",
        key_findings=[],
        warnings=[],
        source_document_ids=[],
        created_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        updated_at_utc=None
    )
