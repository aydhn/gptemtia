import os
from pathlib import Path

ROOT_DIR = Path("C:/Users/immor/OneDrive/Belgeler/Projelerim/gptemtia/advanced_gap_closure")

def w(name, content):
    with open(ROOT_DIR / name, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# gap_closure_profile_registry.py
w("gap_closure_profile_registry.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import GapClosureProfileItem, build_gap_closure_profile_id, to_dict

def build_default_gap_closure_profile_items(profile: FunctionalGapClosureProfile) -> list[GapClosureProfileItem]:
    return [GapClosureProfileItem(
        profile_id=build_gap_closure_profile_id(profile.name),
        profile_name=profile.name,
        current_phase=105,
        target_final_phase=160,
        next_phase=106,
        local_only=True,
        non_production=True,
        research_only=True,
        status_label="gap_closed",
        warnings=[]
    )]

def build_functional_gap_closure_profile_registry(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_gap_closure_profile_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    summary = summarize_gap_closure_profile_registry(df)
    return df, summary

def summarize_gap_closure_profile_registry(df: pd.DataFrame) -> dict:
    return {"total_profiles": len(df)}
""")

# readiness_reconciliation.py
w("readiness_reconciliation.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import ReadinessReconciliationItem, build_readiness_reconciliation_id, to_dict

def build_default_readiness_reconciliation_items(profile: FunctionalGapClosureProfile) -> list[ReadinessReconciliationItem]:
    areas = ["Phase 101 roadmap readiness", "Phase 102 runtime readiness", "Phase 103 research engine interface readiness", "Phase 104 config profile readiness", "DataLake readiness", "FeatureStore readiness", "report builder readiness", "script command readiness", "safety/no-go readiness", "Phase 106 data foundation readiness"]
    items = []
    for area in areas:
        items.append(ReadinessReconciliationItem(
            reconciliation_id=build_readiness_reconciliation_id(area, "101-104"),
            foundation_area=area,
            source_phase_range="101-104",
            current_state="ready",
            target_state="ready",
            reconciliation_status="gap_closed",
            warnings=[],
            manual_review_required=False
        ))
    return items

def build_advanced_readiness_reconciliation_registry(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_readiness_reconciliation_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    summary = summarize_readiness_reconciliation(df)
    return df, summary

def summarize_readiness_reconciliation(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
""")

# mvp_to_v2_closure_matrix.py
w("mvp_to_v2_closure_matrix.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import ClosureMatrixItem, build_closure_matrix_id, to_dict

def build_default_closure_matrix_items(profile: FunctionalGapClosureProfile) -> list[ClosureMatrixItem]:
    areas = [
        ("MVP governance layer", "advanced safety boundary", 106),
        ("MVP DataLake", "v2 provider/data quality foundation", 106),
        ("MVP FeatureStore", "v2 feature engine", 116),
        ("MVP ML scaffold", "v2 ML/GPU pipeline", 136),
        ("MVP backtest scaffold", "v2 realistic backtest", 146),
        ("MVP portfolio research", "v2 portfolio optimization", 153),
        ("MVP reports", "v2 advanced report profiles", 158),
        ("MVP docs", "v2 analyst/operator handoff", 159),
        ("MVP closure docs", "v2 advanced delivery governance", 160)
    ]
    items = []
    for mvp, adv, phase in areas:
        items.append(ClosureMatrixItem(
            closure_id=build_closure_matrix_id(mvp, adv),
            mvp_area=mvp,
            advanced_target_area=adv,
            current_phase_support="partial",
            required_future_phase=str(phase),
            closure_status="gap_partially_closed",
            gap_note="",
            manual_review_required=False
        ))
    return items

def build_mvp_to_v2_closure_matrix(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = build_default_closure_matrix_items(profile)
    df = pd.DataFrame([to_dict(i) for i in items])
    return df, summarize_mvp_to_v2_closure_matrix(df)

def summarize_mvp_to_v2_closure_matrix(df: pd.DataFrame) -> dict:
    return {"total_items": len(df)}
""")

# foundation_audit.py
w("foundation_audit.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_phase_101_104_foundation_audit(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    areas = ["Phase 101 advanced roadmap registry", "Phase 101 master plan", "Phase 102 runtime profile registry", "Phase 102 contracts", "Phase 103 request/result schema", "Phase 103 interface contracts", "Phase 104 profile registries", "Phase 104 composed profiles", "Phase 104 compatibility matrix", "Phase 104 safety profiles"]
    df = pd.DataFrame([{"area": a, "status": "audited"} for a in areas])
    return df, summarize_phase_101_104_foundation_audit(df)

def summarize_phase_101_104_foundation_audit(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# dependency_closure_map.py
w("dependency_closure_map.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_advanced_foundation_dependency_closure_map(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    deps = [
        {"source": "Phase 101 roadmap", "target": "Phase 102 runtime"},
        {"source": "Phase 102 runtime", "target": "Phase 103 research engine"},
        {"source": "Phase 103 research engine", "target": "Phase 104 config profiles"},
        {"source": "Phase 104 config profiles", "target": "Phase 106 provider abstraction"},
        {"source": "DataLake contract", "target": "provider output persistence"},
        {"source": "FeatureStore contract", "target": "normalized data and feature access"},
        {"source": "Report contract", "target": "provider benchmark reports"},
        {"source": "Safety boundary", "target": "no-scraping provider implementation"}
    ]
    df = pd.DataFrame(deps)
    return df, summarize_dependency_closure_map(df)

def summarize_dependency_closure_map(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# missing_functionality_register.py
w("missing_functionality_register.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile
from .gap_closure_models import MissingFunctionalityItem, build_missing_functionality_id, to_dict

def build_default_missing_functionality_items(profile: FunctionalGapClosureProfile) -> list[MissingFunctionalityItem]:
    areas = ["provider", "feature", "regime", "ML", "backtest", "portfolio"]
    return [MissingFunctionalityItem(
        missing_id=build_missing_functionality_id(area, 106),
        functionality_area=area,
        current_gap="Missing implementation",
        required_for_phase=106,
        priority_label="priority_high",
        risk_label="functional_gap_medium_risk",
        recommendation="Implement in future phase",
        manual_review_required=False
    ) for area in areas]

def build_missing_functionality_register(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    df = pd.DataFrame([to_dict(i) for i in build_default_missing_functionality_items(profile)])
    return df, summarize_missing_functionality_register(df)

def summarize_missing_functionality_register(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

# implementation_backlog.py
w("implementation_backlog.py", """
import pandas as pd
from .gap_closure_config import FunctionalGapClosureProfile

def build_required_implementation_backlog(profile: FunctionalGapClosureProfile) -> tuple[pd.DataFrame, dict]:
    items = [
        {"target_phase": 106, "target_module": "Phase 106 data provider abstraction", "input_contract": "yes", "output_contract": "yes", "test_expectation": "yes", "safety_boundary": "yes", "priority": "high", "manual_review_required": False},
        {"target_phase": 160, "target_module": "Phase 158-160 final integration", "input_contract": "yes", "output_contract": "yes", "test_expectation": "yes", "safety_boundary": "yes", "priority": "high", "manual_review_required": False}
    ]
    df = pd.DataFrame(items)
    return df, summarize_required_implementation_backlog(df)

def summarize_required_implementation_backlog(df: pd.DataFrame) -> dict: return {"total": len(df)}
""")

print("Generated registry and map builders")
