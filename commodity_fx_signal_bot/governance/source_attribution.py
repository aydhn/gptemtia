import pandas as pd


def infer_data_source_from_artifact(path: str, metadata: dict | None = None) -> str:
    path_lower = path.lower()
    if "raw" in path_lower:
        if "yahoo" in path_lower or "yfinance" in path_lower: return "yahoo_finance_library"
        if "fred" in path_lower: return "fred_api"
        if "evds" in path_lower: return "evds_api"
        return "external_api"
    if "reports" in path_lower: return "report_generated"
    if "experiments" in path_lower: return "experiment_manifest"
    return "data_lake_derived"

def build_data_source_attribution_table(inventory_df: pd.DataFrame, provenance_df: pd.DataFrame | None = None) -> pd.DataFrame:
    records = []
    if inventory_df.empty:
        return pd.DataFrame()

    for _, row in inventory_df.iterrows():
        art_id = row["artifact_id"]
        path = row["relative_path"]

        # Check provenance first
        source = None
        if provenance_df is not None and not provenance_df.empty:
            prov = provenance_df[provenance_df["artifact_id"] == art_id]
            if not prov.empty:
                source = prov.iloc[0].get("source_system")

        if not source:
            source = infer_data_source_from_artifact(path)

        records.append({
            "artifact_id": art_id,
            "artifact_type": row["artifact_type"],
            "path": path,
            "source": source
        })

    return pd.DataFrame(records)

def summarize_source_attribution(source_df: pd.DataFrame) -> dict:
    if source_df.empty:
        return {"total_attributed": 0}

    return {
        "total_attributed": len(source_df),
        "sources": source_df["source"].value_counts().to_dict()
    }

def check_source_attribution_coverage(source_df: pd.DataFrame) -> dict:
    if source_df.empty:
        return {"coverage_ratio": 0.0, "warnings": ["Empty source table"]}

    total = len(source_df)
    unknown = len(source_df[source_df["source"].isin(["unknown_source", "data_lake_derived"])])

    ratio = (total - unknown) / total if total > 0 else 0.0

    warnings = []
    if ratio < 0.5:
        warnings.append("Low source attribution coverage.")

    return {
        "coverage_ratio": ratio,
        "warnings": warnings
    }
