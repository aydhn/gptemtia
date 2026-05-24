
import pandas as pd


def link_experiment_runs_to_artifacts(experiment_runs_df: pd.DataFrame, inventory_df: pd.DataFrame) -> pd.DataFrame:
    links = []
    if experiment_runs_df.empty or inventory_df.empty:
        return pd.DataFrame()

    for _, run in experiment_runs_df.iterrows():
        run_id = run.get("run_id")
        exp_id = run.get("experiment_id")

        # Simple heuristic: if experiment_id or run_id is in the artifact path
        if exp_id or run_id:
            search_term = run_id if run_id else exp_id
            mask = inventory_df["relative_path"].str.contains(str(search_term), case=False, na=False)
            matches = inventory_df[mask]

            for _, match in matches.iterrows():
                links.append({
                    "run_id": run_id,
                    "experiment_id": exp_id,
                    "artifact_id": match["artifact_id"],
                    "artifact_type": match["artifact_type"],
                    "artifact_path": match["relative_path"],
                    "linkage_method": "path_match",
                    "linkage_confidence": 0.8,
                    "warnings": []
                })

    return pd.DataFrame(links)

def link_reproducibility_manifests_to_lineage(repro_manifest_df: pd.DataFrame | None, lineage_nodes_df: pd.DataFrame) -> pd.DataFrame:
    links = []
    if repro_manifest_df is None or repro_manifest_df.empty or lineage_nodes_df.empty:
        return pd.DataFrame()

    # Example: link manifest run_ids to nodes
    for _, man in repro_manifest_df.iterrows():
        run_id = man.get("run_id")
        if run_id:
            mask = lineage_nodes_df["path"].str.contains(str(run_id), case=False, na=False)
            matches = lineage_nodes_df[mask]
            for _, match in matches.iterrows():
                links.append({
                    "run_id": run_id,
                    "experiment_id": man.get("experiment_id"),
                    "artifact_id": match["artifact_id"],
                    "artifact_type": match["artifact_type"],
                    "artifact_path": match["path"],
                    "linkage_method": "manifest_run_id",
                    "linkage_confidence": 0.9,
                    "warnings": []
                })

    return pd.DataFrame(links)

def build_experiment_lineage_table(data_lake, inventory_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    # Placeholder for fetching experiment runs and manifests from DataLake
    # Because we don't directly import DataLake structure here to avoid cycles,
    # we simulate the fetch or expect it to be passed.
    # In a real impl, we might call data_lake.load_experiment_runs()

    # Let's try calling it if available
    exp_runs = pd.DataFrame()
    repro_man = pd.DataFrame()
    warnings = []

    try:
        exp_runs = data_lake.load_experiment_runs()
    except Exception:
        warnings.append("Could not load experiment runs")

    try:
        # Pseudo method
        if hasattr(data_lake, 'load_reproducibility_manifests'):
            repro_man = data_lake.load_reproducibility_manifests()
    except Exception:
        warnings.append("Could not load reproducibility manifests")

    df1 = link_experiment_runs_to_artifacts(exp_runs, inventory_df)

    # We don't have nodes easily available here, just use inventory directly
    # for simplicity in this proxy implementation.

    if df1.empty:
        warnings.append("Experiment lineage bridge could not link artifacts.")

    summary = {
        "links_found": len(df1),
        "warnings": warnings,
        "note": "Experiment lineage is NOT model deployment lineage."
    }

    return df1, summary

def summarize_experiment_lineage(experiment_lineage_df: pd.DataFrame) -> dict:
    if experiment_lineage_df.empty:
        return {"total_links": 0}

    return {
        "total_links": len(experiment_lineage_df),
        "unique_experiments": experiment_lineage_df["experiment_id"].nunique() if "experiment_id" in experiment_lineage_df else 0,
        "unique_runs": experiment_lineage_df["run_id"].nunique() if "run_id" in experiment_lineage_df else 0
    }
