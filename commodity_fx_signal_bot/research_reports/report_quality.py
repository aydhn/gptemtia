import pandas as pd
from research_reports.research_models import SymbolResearchSnapshot, ResearchReport

FORBIDDEN_TRADE_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER"
]

def _check_text_for_forbidden_terms(text: str) -> list[str]:
    if not text:
        return []
    found = []
    text_upper = text.upper()
    for term in FORBIDDEN_TRADE_TERMS:
        # Simple string match. More complex regex word boundaries could be used.
        if f" {term} " in f" {text_upper} ":
            found.append(term)
    return found

def check_research_snapshot_quality(snapshot: SymbolResearchSnapshot) -> dict:
    warnings = []
    if snapshot.research_score < 0.1:
        warnings.append("Very low research score.")
    return {
        "passed": len(warnings) == 0,
        "warnings": warnings
    }

def check_research_report_markdown(text: str) -> dict:
    warnings = []
    if not text:
        warnings.append("Markdown is empty.")
    if "gerçek emir, canlı sinyal veya yatırım tavsiyesi değildir" not in text.lower() and "offline araştırma/simülasyon" not in text.lower():
         warnings.append("Disclaimer is missing or incomplete.")

    forbidden = _check_text_for_forbidden_terms(text)
    if forbidden:
        warnings.append(f"Forbidden trade terms found: {', '.join(forbidden)}")

    return {
        "passed": len(warnings) == 0,
        "markdown_not_empty": bool(text),
        "disclaimer_present": "gerçek emir, canlı sinyal veya yatırım tavsiyesi değildir" in text.lower() or "offline araştırma/simülasyon" in text.lower(),
        "forbidden_trade_terms_found": len(forbidden) > 0,
        "warnings": warnings
    }

def check_ranking_table_quality(ranking_df: pd.DataFrame) -> dict:
    warnings = []
    if ranking_df is None or ranking_df.empty:
        warnings.append("Ranking table is empty.")
    return {
        "passed": len(warnings) == 0,
        "ranking_valid": ranking_df is not None and not ranking_df.empty,
        "warnings": warnings
    }

def check_for_forbidden_trade_terms_in_research(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found = []
    if text:
        found.extend(_check_text_for_forbidden_terms(text))
    # Not deeply inspecting df or summary for now, could be added.
    return {
        "passed": len(found) == 0,
        "forbidden_terms": found
    }

def build_research_quality_report(report: ResearchReport | None, snapshots: list[SymbolResearchSnapshot] | None = None, ranking_df: pd.DataFrame | None = None) -> dict:
    warnings = []
    passed = True

    md_quality = {"passed": True}
    if report:
        md_quality = check_research_report_markdown(report.markdown)
        if not md_quality['passed']:
            warnings.extend(md_quality['warnings'])
            passed = False

    ranking_quality = {"passed": True}
    if ranking_df is not None:
        ranking_quality = check_ranking_table_quality(ranking_df)
        if not ranking_quality['passed']:
            warnings.extend(ranking_quality['warnings'])
            passed = False

    snapshot_count = len(snapshots) if snapshots else 0

    return {
        "markdown_not_empty": md_quality.get('markdown_not_empty', True),
        "disclaimer_present": md_quality.get('disclaimer_present', True),
        "forbidden_trade_terms_found": md_quality.get('forbidden_trade_terms_found', False),
        "ranking_valid": ranking_quality.get('ranking_valid', True),
        "snapshot_count": snapshot_count,
        "warning_count": len(warnings),
        "passed": passed,
        "warnings": warnings
    }
