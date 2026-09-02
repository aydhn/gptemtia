import os
from pathlib import Path

base_dir = Path("c:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/commodity_fx_signal_bot")
ls_dir = base_dir / "local_synthesis"

def write_module(filename, content):
    with open(ls_dir / filename, "w", encoding="utf-8") as f:
        f.write(content)

# cross_phase_final_map.py
write_module("cross_phase_final_map.py", """\
import pandas as pd
from typing import Tuple, Dict, List
from .synthesis_config import LocalSynthesisProfile
from .synthesis_models import FinalMapNode

def build_final_map_nodes(profile: LocalSynthesisProfile) -> List[FinalMapNode]:
    return []

def link_final_map_nodes_to_outputs(node_df: pd.DataFrame, artifact_df: pd.DataFrame, report_df: pd.DataFrame, datalake_df: pd.DataFrame) -> pd.DataFrame:
    return node_df

def build_cross_phase_final_map(family_df: pd.DataFrame, artifact_df: pd.DataFrame, report_df: pd.DataFrame, datalake_df: pd.DataFrame, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["node_id", "node_name", "family_label", "layer_name", "description", "related_outputs", "warnings"])
    return df, summarize_cross_phase_final_map(df)

def summarize_cross_phase_final_map(map_df: pd.DataFrame) -> Dict:
    return {"count": len(map_df)}
""")

# end_state_capability_map.py
write_module("end_state_capability_map.py", """\
import pandas as pd
from typing import Tuple, Dict, Optional
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_capability_summary_rows(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame(columns=["capability", "description", "warnings"])

def map_capabilities_to_phase_families(capability_df: pd.DataFrame, family_df: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    return capability_df

def build_end_state_capability_map(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_capability_summary_rows(profile)
    return df, summarize_end_state_capability_map(df)

def summarize_end_state_capability_map(capability_df: pd.DataFrame) -> Dict:
    return {"count": len(capability_df)}
""")

# end_state_boundary_map.py
write_module("end_state_boundary_map.py", """\
import pandas as pd
from typing import Tuple, Dict
from .synthesis_config import LocalSynthesisProfile

def build_final_boundary_rows(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"boundary": "no live trading"}, {"boundary": "no broker execution"}, {"boundary": "no investment advice"}])

def build_end_state_boundary_map(profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_final_boundary_rows(profile)
    return df, summarize_end_state_boundary_map(df)

def summarize_end_state_boundary_map(boundary_df: pd.DataFrame) -> Dict:
    return {"count": len(boundary_df)}
""")

# module_dependency_map.py
write_module("module_dependency_map.py", """\
import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def infer_module_dependencies_from_imports(project_root: Path, profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame(columns=["module", "dependencies"])

def build_end_state_module_dependency_map(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = infer_module_dependencies_from_imports(project_root, profile)
    return df, summarize_module_dependency_map(df)

def summarize_module_dependency_map(dep_df: pd.DataFrame) -> Dict:
    return {"count": len(dep_df)}
""")

# output_catalog.py
write_module("output_catalog.py", """\
import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def classify_output_catalog_domain(path: Path, project_root: Path) -> str:
    return "unknown"

def build_end_state_output_catalog(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["path", "domain", "warnings"])
    return df, summarize_end_state_output_catalog(df)

def summarize_end_state_output_catalog(catalog_df: pd.DataFrame) -> Dict:
    return {"count": len(catalog_df)}
""")

# completion_dossier.py
write_module("completion_dossier.py", """\
import pandas as pd
from typing import Tuple, Dict, List
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile
from .synthesis_models import FinalBinderSection

def build_completion_dossier_sections(family_df: pd.DataFrame, capability_df: pd.DataFrame, boundary_df: pd.DataFrame, output_df: pd.DataFrame) -> List[FinalBinderSection]:
    return []

def save_project_completion_dossier(text: str, output_path: Path) -> Path:
    output_path.write_text(text, encoding="utf-8")
    return output_path

def build_project_completion_dossier(family_df: pd.DataFrame, capability_df: pd.DataFrame, boundary_df: pd.DataFrame, output_df: pd.DataFrame, profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Project Completion Dossier\\nOffline/local only. No investment advice. No production release."
    return text, summarize_project_completion_dossier(text)

def summarize_project_completion_dossier(text: str) -> Dict:
    return {"length": len(text)}
""")

# non_use_policy_binder.py
write_module("non_use_policy_binder.py", """\
from typing import Tuple, Dict, List
from .synthesis_config import LocalSynthesisProfile

def build_non_use_policy_sections(profile: LocalSynthesisProfile) -> List[Dict]:
    return []

def build_final_non_use_policy_binder(profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Non-Use Policy Binder\\nOffline/local only. No investment advice."
    return text, summarize_non_use_policy_binder(text)

def summarize_non_use_policy_binder(text: str) -> Dict:
    return {"length": len(text)}
""")

# safety_boundary_binder.py
write_module("safety_boundary_binder.py", """\
from typing import Tuple, Dict, List
from .synthesis_config import LocalSynthesisProfile

def build_safety_boundary_sections(profile: LocalSynthesisProfile) -> List[Dict]:
    return []

def build_final_safety_boundary_binder(profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Safety Boundary Binder\\nOffline/local only. No live trading."
    return text, summarize_safety_boundary_binder(text)

def summarize_safety_boundary_binder(text: str) -> Dict:
    return {"length": len(text)}
""")

# local_only_statement.py
write_module("local_only_statement.py", """\
import pandas as pd
from typing import Tuple, Dict
from .synthesis_config import LocalSynthesisProfile

def build_local_only_statement_table(profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = pd.DataFrame(columns=["item", "status"])
    return df, {"count": 0}

def build_final_local_only_statement(profile: LocalSynthesisProfile) -> Tuple[str, Dict]:
    text = "# Local Only Statement\\nNo cloud/external service claim."
    df, summary = build_local_only_statement_table(profile)
    return text, summarize_local_only_statement(text, df)

def summarize_local_only_statement(text: str, statement_df: pd.DataFrame) -> Dict:
    return {"length": len(text)}
""")

# final_limitation_register.py
write_module("final_limitation_register.py", """\
import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_default_final_limitations(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"limitation": "offline/local only"}, {"limitation": "no live trading"}])

def build_final_limitation_register(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_final_limitations(profile)
    return df, summarize_final_limitation_register(df)

def summarize_final_limitation_register(limit_df: pd.DataFrame) -> Dict:
    return {"count": len(limit_df)}
""")

# final_manual_review_register.py
write_module("final_manual_review_register.py", """\
import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def collect_manual_review_items_from_final_layers(project_root: Path, profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame(columns=["item", "reason"])

def build_final_manual_review_register(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    df = collect_manual_review_items_from_final_layers(project_root, profile)
    return df, summarize_final_manual_review_register(df)

def summarize_final_manual_review_register(review_df: pd.DataFrame) -> Dict:
    return {"count": len(review_df)}
""")

# no_go_safe_go_summary.py
write_module("no_go_safe_go_summary.py", """\
import pandas as pd
from typing import Tuple, Dict
from pathlib import Path
from .synthesis_config import LocalSynthesisProfile

def build_final_no_go_conditions(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "raw secret output"}, {"condition": "live/broker/deploy claim"}])

def build_final_safe_go_conditions(profile: LocalSynthesisProfile) -> pd.DataFrame:
    return pd.DataFrame([{"condition": "local-only scope documented"}])

def build_final_no_go_safe_go_summary(project_root: Path, profile: LocalSynthesisProfile) -> Tuple[pd.DataFrame, Dict]:
    nogo = build_final_no_go_conditions(profile)
    safego = build_final_safe_go_conditions(profile)
    df = pd.concat([nogo, safego], ignore_index=True)
    return df, summarize_final_no_go_safe_go(df)

def summarize_final_no_go_safe_go(summary_df: pd.DataFrame) -> Dict:
    return {"count": len(summary_df)}
""")
