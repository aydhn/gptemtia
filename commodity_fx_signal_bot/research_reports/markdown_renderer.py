import pandas as pd
from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile
from research_reports.narrative_builder import build_disclaimer_text

def dataframe_to_markdown_table(df: pd.DataFrame, max_rows: int = 20) -> str:
    if df is None or df.empty:
        return "*Dataframe is empty*"
    display_df = df.head(max_rows)
    return display_df.to_markdown(index=False)

def render_report_header(title: str, profile_name: str, timeframe: str) -> str:
    return f"# {title}\n**Profile:** {profile_name} | **Timeframe:** {timeframe}\n"

def render_report_footer() -> str:
    return f"\n---\n**Uyarı:** {build_disclaimer_text()}\n"

def render_symbol_report_markdown(snapshot: SymbolResearchSnapshot, narrative: str, tables: dict[str, pd.DataFrame] | None = None) -> str:
    md = []
    md.append(render_report_header(f"Research Report: {snapshot.symbol}", "symbol_profile", snapshot.timeframe))
    md.append(f"**Research Status:** {snapshot.research_status}")
    md.append(f"**Research Score:** {snapshot.research_score:.2f}")
    if snapshot.warnings:
         md.append("\n**Warnings:**\n- " + "\n- ".join(snapshot.warnings))

    md.append("\n## Narrative Summary\n")
    md.append(narrative)

    if tables:
        for name, df in tables.items():
            md.append(f"\n### {name}\n")
            md.append(dataframe_to_markdown_table(df))

    md.append(render_report_footer())
    return "\n".join(md)

def render_universe_report_markdown(ranking_df: pd.DataFrame, narrative: str, profile: ResearchReportProfile) -> str:
    md = []
    md.append(render_report_header("Universe Research Report", profile.name, "multi"))
    md.append("\n## Narrative Summary\n")
    md.append(narrative)

    md.append("\n## Universe Ranking\n")
    md.append(dataframe_to_markdown_table(ranking_df, profile.max_rows_per_table))

    md.append(render_report_footer())
    return "\n".join(md)

def render_daily_digest_markdown(snapshots: list[SymbolResearchSnapshot], ranking_df: pd.DataFrame, profile: ResearchReportProfile) -> str:
    md = []
    md.append(render_report_header("Daily Research Digest", profile.name, "multi"))
    md.append(f"\nSummarized {len(snapshots)} symbols.\n")

    md.append("\n## Top Rankings\n")
    md.append(dataframe_to_markdown_table(ranking_df, 10))

    md.append(render_report_footer())
    return "\n".join(md)
