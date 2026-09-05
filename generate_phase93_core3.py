import os
from pathlib import Path

base_dir = Path("commodity_fx_signal_bot/local_project_atlas")

with open(base_dir / "atlas_phase_maps.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas phase maps module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_default_phase_dependencies(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([{"phase": "phase93", "depends_on": "phase92"}])

def build_default_phase_output_items(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([{"phase": "phase93", "outputs": "atlas"}])

def build_atlas_phase_dependency_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_phase_dependencies(profile)
    return df, summarize_atlas_phase_map(df)

def build_atlas_phase_to_output_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_phase_output_items(profile)
    return df, summarize_atlas_phase_map(df)

def build_atlas_output_to_script_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"output": "atlas", "script": "run_final_meta_index"}])
    return df, summarize_atlas_phase_map(df)

def build_atlas_command_to_output_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"command": "python run_final_meta_index", "output": "atlas"}])
    return df, summarize_atlas_phase_map(df)

def summarize_atlas_phase_map(df: pd.DataFrame) -> dict:
    return {"entries": len(df)}
''')

with open(base_dir / "atlas_route_maps.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas route maps module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import NavigationItem, build_navigation_item_id

def build_default_route_items(route_label: str, profile: LocalProjectAtlasProfile) -> list[NavigationItem]:
    return [NavigationItem(
        nav_id=build_navigation_item_id(route_label, "start"),
        route_label=route_label,
        nav_title="start",
        nav_area="root",
        target_ref="README.md",
        reading_priority=1,
        manual_review_required=True,
        warnings=["Not SOP"]
    )]

def _build_route_map(route_label: str, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_route_items(route_label, profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_atlas_route_map(df)

def build_atlas_reading_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_reading", profile)

def build_atlas_operator_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_operator", profile)

def build_atlas_analyst_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_analyst", profile)

def build_atlas_maintainer_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_maintainer", profile)

def build_atlas_codex_agent_route_map(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    return _build_route_map("route_codex_agent", profile)

def summarize_atlas_route_map(df: pd.DataFrame) -> dict:
    return {"steps": len(df)}
''')

with open(base_dir / "atlas_glossary.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas glossary module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_default_atlas_glossary_terms(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"term": "Meta-Index", "definition": "Offline list of files and families. Not an official knowledge index."},
        {"term": "Atlas", "definition": "Project directory map. Not a cloud search tool."}
    ])

def build_atlas_glossary_index(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_atlas_glossary_terms(profile)
    return df, summarize_atlas_glossary(df)

def summarize_atlas_glossary(df: pd.DataFrame) -> dict:
    return {"terms": len(df)}
''')

with open(base_dir / "atlas_crosswalks.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas crosswalks module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile
from .atlas_models import AtlasCrosswalkItem, build_atlas_crosswalk_item_id

def build_default_crosswalk_items(area: str, profile: LocalProjectAtlasProfile) -> list[AtlasCrosswalkItem]:
    return [AtlasCrosswalkItem(
        crosswalk_id=build_atlas_crosswalk_item_id(area, "Offline Concept", "Project Mapping"),
        crosswalk_area=area,
        source_concept="Offline Concept",
        target_concept="Project Mapping",
        interpretation_note="Not legal or compliance evidence",
        warnings=["No investment advice"]
    )]

def _build_crosswalk(area: str, profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_crosswalk_items(area, profile)
    df = pd.DataFrame([i.__dict__ for i in items])
    return df, summarize_atlas_crosswalk(df)

def build_atlas_concept_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("concept", profile)
def build_atlas_no_go_safe_go_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("no_go_safe_go", profile)
def build_atlas_safety_boundary_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("safety_boundary", profile)
def build_atlas_maintenance_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("maintenance", profile)
def build_atlas_continuity_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("continuity", profile)
def build_atlas_preservation_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("preservation", profile)
def build_atlas_project_completion_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("project_completion", profile)
def build_atlas_longterm_operations_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("longterm_operations", profile)
def build_atlas_release_candidate_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("release_candidate", profile)
def build_atlas_incident_response_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("incident_response", profile)
def build_atlas_redteam_governance_crosswalk(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]: return _build_crosswalk("redteam_governance", profile)

def summarize_atlas_crosswalk(df: pd.DataFrame) -> dict:
    return {"mappings": len(df)}
''')

with open(base_dir / "atlas_no_go_safe_go.py", "w", encoding="utf-8") as f:
    f.write('''"""Atlas no-go / safe-go module."""
import pandas as pd
from .atlas_config import LocalProjectAtlasProfile

def build_meta_index_no_go_conditions(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "enterprise search claim", "type": "no-go"},
        {"condition": "cloud index claim", "type": "no-go"},
        {"condition": "vector DB claim", "type": "no-go"},
        {"condition": "investment advice wording", "type": "no-go"}
    ])

def build_meta_index_safe_go_conditions(profile: LocalProjectAtlasProfile) -> pd.DataFrame:
    return pd.DataFrame([
        {"condition": "local meta-index documented", "type": "safe-go"},
        {"condition": "manual review required", "type": "safe-go"}
    ])

def build_meta_index_no_go_safe_go_summary(profile: LocalProjectAtlasProfile) -> tuple[pd.DataFrame, dict]:
    df_no = build_meta_index_no_go_conditions(profile)
    df_safe = build_meta_index_safe_go_conditions(profile)
    df = pd.concat([df_no, df_safe], ignore_index=True)
    return df, summarize_meta_index_no_go_safe_go(df)

def summarize_meta_index_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    return {
        "no_go_count": len(summary_df[summary_df["type"] == "no-go"]),
        "safe_go_count": len(summary_df[summary_df["type"] == "safe-go"])
    }
''')

print("Created core3")
