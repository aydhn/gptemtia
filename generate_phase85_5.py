import os
from pathlib import Path

ROOT = Path("commodity_fx_signal_bot")
TARGET_DIR = ROOT / "local_governance_control"

# governance_roles.py
with open(TARGET_DIR / "governance_roles.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_governance_roles(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    roles = [
        "operator",
        "reviewer",
        "technical maintainer",
        "safety reviewer",
        "documentation reviewer",
        "executive observer",
        "risk committee rehearsal observer"
    ]
    data = [{"role": r, "description": f"Role for {r}", "is_rehearsal_only": True} for r in roles]
    return pd.DataFrame(data)

def build_governance_roles_matrix_rehearsal(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_governance_roles(profile)
    return df, summarize_governance_roles(df)

def summarize_governance_roles(role_df: pd.DataFrame) -> dict:
    if role_df is None or role_df.empty:
        return {"total": 0}
    return {"total": len(role_df)}
""")

# decision_authority.py
with open(TARGET_DIR / "decision_authority.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_decision_authority_map(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"decision_type": "Accept Rehearsal", "authorized_role": "reviewer", "notes": "Not a real decision"}
    ]
    return pd.DataFrame(data)

def build_decision_authority_map_rehearsal(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_decision_authority_map(profile)
    return df, summarize_decision_authority_map(df)

def summarize_decision_authority_map(authority_df: pd.DataFrame) -> dict:
    if authority_df is None or authority_df.empty:
        return {"total": 0}
    return {"total": len(authority_df)}
""")

# approval_boundaries.py
with open(TARGET_DIR / "approval_boundaries.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_approval_boundaries(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [{"boundary_name": "Documentation Approval", "is_rehearsal": True}]
    return pd.DataFrame(data)

def build_default_non_approval_boundaries(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    boundaries = [
        "live trading",
        "broker execution",
        "investment advice",
        "production deployment",
        "model deployment",
        "cloud upload",
        "package publish",
        "compliance certification",
        "legal sign-off",
        "official committee approval"
    ]
    data = [{"boundary_name": b, "reason": "Explicitly forbidden in local governance"} for b in boundaries]
    return pd.DataFrame(data)

def build_approval_boundary_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_approval_boundaries(profile)
    return df, {"total": len(df)}

def build_non_approval_boundary_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_non_approval_boundaries(profile)
    return df, {"total": len(df)}

def summarize_approval_boundaries(approval_df: pd.DataFrame, non_approval_df: pd.DataFrame) -> dict:
    return {
        "approval_boundaries": len(approval_df) if approval_df is not None else 0,
        "non_approval_boundaries": len(non_approval_df) if non_approval_df is not None else 0
    }
""")

# governance_no_go_safe_go.py
with open(TARGET_DIR / "governance_no_go_safe_go.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_governance_no_go_conditions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    conditions = [
        "real approval claim",
        "committee approval claim",
        "legal/compliance signoff claim",
        "production approval claim",
        "live/broker/deploy claim",
        "investment advice wording",
        "dashboard/telemetry claim",
        "raw secret output",
        "file deletion/move/overwrite claim",
        "cloud upload/package publish claim"
    ]
    data = [{"condition": c, "type": "NO-GO"} for c in conditions]
    return pd.DataFrame(data)

def build_governance_safe_go_conditions(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    conditions = [
        "governance rehearsal documented",
        "manual approval ledger present",
        "non-approval boundaries documented",
        "no-go/safe-go present",
        "escalation matrix present",
        "executive oversight packet present",
        "operator supervision guide present",
        "manual review required"
    ]
    data = [{"condition": c, "type": "SAFE-GO"} for c in conditions]
    return pd.DataFrame(data)

def build_governance_no_go_safe_go_summary(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    no_go = build_governance_no_go_conditions(profile)
    safe_go = build_governance_safe_go_conditions(profile)
    df = pd.concat([no_go, safe_go], ignore_index=True)
    return df, summarize_governance_no_go_safe_go(df)

def summarize_governance_no_go_safe_go(summary_df: pd.DataFrame) -> dict:
    if summary_df is None or summary_df.empty:
        return {"total": 0}
    return {
        "no_go_count": len(summary_df[summary_df["type"] == "NO-GO"]),
        "safe_go_count": len(summary_df[summary_df["type"] == "SAFE-GO"])
    }
""")

# oversight_evidence.py
with open(TARGET_DIR / "oversight_evidence.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from pathlib import Path
from .governance_control_config import LocalGovernanceControlProfile

def map_oversight_evidence_sources(project_root: Path, profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"evidence_name": "Test Reports", "source_path": "reports/output/tests", "is_audit_proof": False}
    ]
    return pd.DataFrame(data)

def build_oversight_evidence_index(project_root: Path, profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = map_oversight_evidence_sources(project_root, profile)
    return df, summarize_oversight_evidence(df)

def summarize_oversight_evidence(evidence_df: pd.DataFrame) -> dict:
    if evidence_df is None or evidence_df.empty:
        return {"total": 0}
    return {"total": len(evidence_df)}
""")

# oversight_reading_order.py
with open(TARGET_DIR / "oversight_reading_order.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_oversight_reading_order(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"order": 1, "document": "FINAL_LOCAL_GOVERNANCE_CONTROL_ROOM_PACKET.md"},
        {"order": 2, "document": "EXECUTIVE_OVERSIGHT_PACKET.md"}
    ]
    return pd.DataFrame(data)

def build_oversight_report_reading_order(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_oversight_reading_order(profile)
    return df, summarize_oversight_reading_order(df)

def summarize_oversight_reading_order(order_df: pd.DataFrame) -> dict:
    if order_df is None or order_df.empty:
        return {"total": 0}
    return {"total": len(order_df)}
""")

# governance_metrics.py
with open(TARGET_DIR / "governance_metrics.py", "w", encoding="utf-8") as f:
    f.write("""import pandas as pd
from .governance_control_config import LocalGovernanceControlProfile

def build_default_governance_metrics(profile: LocalGovernanceControlProfile) -> pd.DataFrame:
    data = [
        {"metric_id": "M1", "metric_name": "Readiness Score", "is_real_kpi": False}
    ]
    return pd.DataFrame(data)

def build_governance_kpi_rehearsal_registry(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    data = [{"kpi": "Approval Rate Rehearsal", "target": "100%", "is_real_kpi": False}]
    df = pd.DataFrame(data)
    return df, {"total": len(df)}

def build_governance_metric_dictionary(profile: LocalGovernanceControlProfile) -> tuple[pd.DataFrame, dict]:
    df = build_default_governance_metrics(profile)
    return df, {"total": len(df)}

def summarize_governance_metrics(kpi_df: pd.DataFrame, metric_df: pd.DataFrame) -> dict:
    return {
        "kpi_count": len(kpi_df) if kpi_df is not None else 0,
        "metric_count": len(metric_df) if metric_df is not None else 0
    }
""")
print("Done writing boundaries and metrics.")
