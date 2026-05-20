import pandas as pd
from research_reports.research_models import SymbolResearchSnapshot
from research_reports.research_config import ResearchReportProfile

def calculate_composite_research_rank(row: pd.Series) -> float:
    # A simple example calculation for rank based on research_score
    return float(row.get('research_score', 0.0))

def build_symbol_ranking_table(snapshots: list[SymbolResearchSnapshot], profile: ResearchReportProfile) -> pd.DataFrame:
    if not snapshots:
        return pd.DataFrame()

    data = []
    for snapshot in snapshots:
        data.append({
            "symbol": snapshot.symbol,
            "asset_class": snapshot.asset_class,
            "research_score": snapshot.research_score,
            "technical_score": 0.0, # stubs, in reality would calculate from snapshot.technical_summary
            "risk_level_score": 0.0,
            "backtest_score": 0.0,
            "performance_score": 0.0,
            "validation_score": 0.0,
            "ml_score": 0.0,
            "paper_score": 0.0,
            "quality_score": 0.0,
            "warning_count": len(snapshot.warnings),
            "missing_sources_count": snapshot.quality_summary.get('missing_sources_count', 0) if snapshot.quality_summary else 0,
            "research_status": snapshot.research_status
        })

    df = pd.DataFrame(data)

    # Calculate composite rank and sort
    df['rank_score'] = df.apply(calculate_composite_research_rank, axis=1)
    df = df.sort_values(by='rank_score', ascending=False).reset_index(drop=True)
    df.insert(0, 'rank', df.index + 1)

    return df

def build_asset_class_ranking_tables(ranking_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    if ranking_df.empty or 'asset_class' not in ranking_df.columns:
        return {}

    tables = {}
    for asset_class, group in ranking_df.groupby('asset_class'):
        if pd.isna(asset_class):
            asset_class = 'unknown'
        tables[str(asset_class)] = group.sort_values(by='rank').reset_index(drop=True)

    return tables

def build_ranking_summary(ranking_df: pd.DataFrame) -> dict:
    return {
        "total_symbols_ranked": len(ranking_df),
        "top_symbol": ranking_df.iloc[0]['symbol'] if not ranking_df.empty else None,
        "warnings": []
    }
