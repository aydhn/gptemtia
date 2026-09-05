import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/advanced_gap_closure")

def w(name, content):
    with open(ROOT_DIR / name, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# phase_106_handoff.py
w("phase_106_handoff.py", """
from .gap_closure_config import FunctionalGapClosureProfile

def build_phase_106_handoff_sections(profile: FunctionalGapClosureProfile) -> list[dict]:
    return [{"title": "Phase 106 amacı", "content": "handoff plan"}]

def build_phase_106_data_foundation_handoff(profile: FunctionalGapClosureProfile) -> tuple[str, dict]:
    text = "Phase 106 Data Foundation Handoff: Scraping is forbidden. Credential output is forbidden. No deployment."
    return text, summarize_phase_106_handoff(text)

def summarize_phase_106_handoff(text: str) -> dict: return {"length": len(text)}
""")

# data_provider_requirements.py
w("data_provider_requirements.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import DataFoundationRequirement, to_dict

def build_default_data_provider_requirements(profile: FunctionalGapClosureProfile) -> list[DataFoundationRequirement]:
    areas = ["OHLCV schema", "macro data schema", "event/calendar schema", "news metadata schema"]
    return [DataFoundationRequirement(
        requirement_id=f"req_{a}", requirement_area=a, required_for_phase=106,
        provider_relevance="high", no_scraping_constraint="yes", expected_contract="yes",
        readiness_label="data_foundation_ready", warnings=[]
    ) for a in areas]

def build_data_provider_requirements_matrix(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([to_dict(i) for i in build_default_data_provider_requirements(profile)])
    return df, summarize_data_provider_requirements(df)

def summarize_data_provider_requirements(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# no_scraping_boundary.py
w("no_scraping_boundary.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_no_scraping_allowed_patterns(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pattern": "official API adapter"}, {"pattern": "user-provided CSV/parquet import"}])

def build_no_scraping_forbidden_patterns(profile: FunctionalGapClosureProfile) -> pd.DataFrame:
    return pd.DataFrame([{"pattern": "HTML scraping"}, {"pattern": "bypassing paywall"}])

def build_no_scraping_data_integration_boundary(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"boundary": "no-scraping"}])
    return df, summarize_no_scraping_boundary(df)

def summarize_no_scraping_boundary(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# provider_interface_readiness.py
w("provider_interface_readiness.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_provider_interface_readiness_map(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    areas = ["Research Engine Data Access Interface", "Advanced Config Provider Preference", "Runtime DataLake Contract"]
    df = pd.DataFrame([{"area": a} for a in areas])
    return df, summarize_provider_interface_readiness(df)

def summarize_provider_interface_readiness(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# data_quality_readiness.py
w("data_quality_readiness.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_data_quality_readiness_map(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    areas = ["missing value detection", "duplicate timestamp detection", "outlier/spike detection", "timezone normalization", "symbol normalization", "frequency validation"]
    df = pd.DataFrame([{"area": a} for a in areas])
    return df, summarize_data_quality_readiness(df)

def summarize_data_quality_readiness(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# profile_data_requirement_map.py
w("profile_data_requirement_map.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_research_profile_to_data_requirement_map(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    reqs = [{"profile": "major_fx_pairs", "req": "FX provider requirement"}, {"profile": "precious_metals", "req": "commodities provider requirement"}]
    df = pd.DataFrame(reqs)
    return df, summarize_profile_data_requirement_map(df)

def summarize_profile_data_requirement_map(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# runtime_provider_handoff.py
w("runtime_provider_handoff.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_runtime_to_provider_contract_handoff(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source_layer": "runtime", "manual_review_required": True}])
    return df, summarize_runtime_provider_handoff(df)

def summarize_runtime_provider_handoff(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# research_engine_provider_handoff.py
w("research_engine_provider_handoff.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_research_engine_to_provider_contract_handoff(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source_layer": "research_engine", "manual_review_required": True}])
    return df, summarize_research_engine_provider_handoff(df)

def summarize_research_engine_provider_handoff(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# config_provider_handoff.py
w("config_provider_handoff.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_config_profile_to_provider_preference_handoff(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([{"source_layer": "config", "manual_review_required": True}])
    return df, summarize_config_provider_handoff(df)

def summarize_config_provider_handoff(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

print("Generated handoff and requirement builders")
