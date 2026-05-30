import pandas as pd
from report_summarization.summary_config import ReportSummaryProfile
from report_summarization.summary_models import BriefCard, build_brief_id

def extract_symbols_from_reports(inventory_df: pd.DataFrame, findings_df: pd.DataFrame) -> list[str]:
    symbols = set()
    if not findings_df.empty and "related_symbols" in findings_df:
        for sym_list in findings_df["related_symbols"]:
            if isinstance(sym_list, list):
                symbols.update(sym_list)
    return list(symbols)

def build_symbol_brief(symbol: str, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, summaries_df: pd.DataFrame) -> BriefCard:
    summary_text = f"Offline arastirma bulgulari ozeti ({symbol}). Bu AL/SAT karari degildir."

    return BriefCard(
        brief_id=build_brief_id("symbol_brief", f"Symbol Brief: {symbol}", symbol=symbol),
        brief_type="symbol_brief",
        title=f"{symbol} Offline Brief",
        module_name=None,
        symbol=symbol,
        summary=summary_text,
        key_points=[],
        follow_ups=[],
        priority="informational_priority",
        source_paths=[],
        warnings=[]
    )

def build_symbol_brief_cards(inventory_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame, summaries_df: pd.DataFrame, profile: ReportSummaryProfile) -> tuple[pd.DataFrame, dict]:
    symbols = extract_symbols_from_reports(inventory_df, findings_df)
    cards = []
    for sym in symbols:
        cards.append(build_symbol_brief(sym, findings_df, warnings_df, summaries_df))

    df = pd.DataFrame([c.__dict__ for c in cards])
    return df, summarize_symbol_briefs(df)

def summarize_symbol_briefs(symbol_briefs_df: pd.DataFrame) -> dict:
    if symbol_briefs_df.empty:
        return {"total_symbol_briefs": 0}
    return {
        "total_symbol_briefs": len(symbol_briefs_df),
        "symbols": symbol_briefs_df["symbol"].unique().tolist() if "symbol" in symbol_briefs_df else []
    }
