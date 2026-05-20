import pandas as pd
from pathlib import Path
from research_reports.research_models import SymbolResearchSnapshot

def export_ranking_table(ranking_df: pd.DataFrame, output_path: Path) -> Path:
    if ranking_df is not None and not ranking_df.empty:
        ranking_df.to_csv(output_path, index=False)
    else:
        # Save empty file with headers if possible or just empty
        pd.DataFrame().to_csv(output_path, index=False)
    return output_path

def export_symbol_summary_table(snapshots: list[SymbolResearchSnapshot], output_path: Path) -> Path:
    data = []
    for snapshot in snapshots:
        data.append({
            "symbol": snapshot.symbol,
            "research_score": snapshot.research_score,
            "research_status": snapshot.research_status
        })
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    return output_path

def export_section_table(df: pd.DataFrame, output_path: Path) -> Path:
    if df is not None and not df.empty:
        df.to_csv(output_path, index=False)
    else:
        pd.DataFrame().to_csv(output_path, index=False)
    return output_path

def build_csv_export_manifest(paths: list[Path]) -> dict:
    return {
        "exported_files": [str(p) for p in paths],
        "count": len(paths)
    }
