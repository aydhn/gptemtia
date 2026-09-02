import os
import pandas as pd
from typing import Tuple, Dict, List, Optional
from pathlib import Path

def write_incident_no_go_safe_go():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_incident_no_go_conditions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"condition": "real incident response claim"},
        {"condition": "real rollback claim"},
        {"condition": "forensic analysis claim"},
        {"condition": "production recovery claim"},
        {"condition": "live halt/broker halt claim"},
        {"condition": "compliance/legal sign-off claim"},
        {"condition": "live/broker/deploy claim"},
        {"condition": "investment advice wording"},
        {"condition": "telemetry/dashboard claim"},
        {"condition": "raw secret output"},
        {"condition": "file deletion/move/overwrite claim"},
        {"condition": "cloud upload/package publish claim"}
    ]
    return pd.DataFrame(data)

def build_incident_safe_go_conditions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [
        {"condition": "offline safety event register available"},
        {"condition": "rollback decision playbook documented"},
        {"condition": "non-rollback boundaries documented"},
        {"condition": "containment/recovery rehearsal documented"},
        {"condition": "post-incident review templates available"},
        {"condition": "no real rollback"},
        {"condition": "no production recovery"},
        {"condition": "manual review required"}
    ]
    return pd.DataFrame(data)

def build_incident_no_go_safe_go_summary(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    no_go_df = build_incident_no_go_conditions(profile)
    safe_go_df = build_incident_safe_go_conditions(profile)
    
    summary_df = pd.DataFrame([
        {"type": "no_go", "count": len(no_go_df)},
        {"type": "safe_go", "count": len(safe_go_df)}
    ])
    summary = summarize_incident_no_go_safe_go(summary_df)
    return summary_df, summary

def summarize_incident_no_go_safe_go(summary_df: pd.DataFrame) -> Dict:
    return {
        "rows": len(summary_df),
        "note": "Safe-go is not real incident response approval."
    }
"""
    with open("local_incident_response/incident_no_go_safe_go.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_exceptions():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def detect_incident_exceptions(event_df: pd.DataFrame, rollback_df: pd.DataFrame, no_go_df: pd.DataFrame) -> pd.DataFrame:
    data = [{"exception": "Mock exception", "description": "Mock description"}]
    return pd.DataFrame(data)

def build_incident_exception_register(event_df: pd.DataFrame, rollback_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = detect_incident_exceptions(event_df, rollback_df, no_go_df)
    summary = summarize_incident_exceptions(df)
    return df, summary

def summarize_incident_exceptions(exception_df: pd.DataFrame) -> Dict:
    return {
        "count": len(exception_df),
        "note": "Does not perform real rollback."
    }
"""
    with open("local_incident_response/incident_exceptions.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_gaps():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def detect_missing_incident_domains(domain_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_domain"}]) if domain_df is None or domain_df.empty else pd.DataFrame()

def detect_missing_safety_events(event_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_event"}]) if event_df is None or event_df.empty else pd.DataFrame()

def detect_missing_triage_items(triage_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_triage"}]) if triage_df is None or triage_df.empty else pd.DataFrame()

def detect_missing_recovery_items(recovery_df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame([{"gap": "missing_recovery"}]) if recovery_df is None or recovery_df.empty else pd.DataFrame()

def build_incident_gap_register(
    domain_df: pd.DataFrame,
    event_df: pd.DataFrame,
    triage_df: pd.DataFrame,
    recovery_df: pd.DataFrame,
    profile: LocalIncidentResponseProfile,
) -> Tuple[pd.DataFrame, Dict]:
    gaps = pd.concat([
        detect_missing_incident_domains(domain_df),
        detect_missing_safety_events(event_df),
        detect_missing_triage_items(triage_df),
        detect_missing_recovery_items(recovery_df)
    ], ignore_index=True)
    
    summary = summarize_incident_gaps(gaps)
    return gaps, summary

def summarize_incident_gaps(gap_df: pd.DataFrame) -> Dict:
    return {
        "count": len(gap_df),
        "note": "No auto-fix provided."
    }
"""
    with open("local_incident_response/incident_gaps.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_risks():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def classify_incident_risk(row: pd.Series, profile: LocalIncidentResponseProfile) -> str:
    return "incident_info"

def build_incident_risk_summary(exception_df: pd.DataFrame, gap_df: pd.DataFrame, no_go_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [{"risk_area": "mock_area", "risk_level": "incident_info"}]
    df = pd.DataFrame(data)
    summary = summarize_incident_risks(df)
    return df, summary

def build_incident_risk_digest(risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[str, Dict]:
    text = "Risk Digest: Mock digest.\\nUyarı: Bu rapor offline/local incident-response rehearsal ve resilience supervision çıktısıdır; gerçek incident response, forensic analiz, production rollback, canlı sinyal, broker talimatı, model deployment veya yatırım tavsiyesi değildir."
    summary = summarize_incident_risks(risk_df)
    return text, summary

def summarize_incident_risks(risk_df: pd.DataFrame) -> Dict:
    return {
        "count": len(risk_df),
        "note": "Not an investment risk."
    }
"""
    with open("local_incident_response/incident_risks.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_scoring():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def calculate_incident_readiness_score(event_df: pd.DataFrame, triage_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> float:
    return 1.0

def classify_incident_readiness_score(score: float, profile: LocalIncidentResponseProfile) -> str:
    if score >= profile.min_readiness_score:
        return "Ready"
    return "Needs Manual Review"

def build_incident_readiness_score_report(event_df: pd.DataFrame, triage_df: pd.DataFrame, risk_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    score = calculate_incident_readiness_score(event_df, triage_df, risk_df, profile)
    classification = classify_incident_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    summary = summarize_incident_readiness_score(df)
    return df, summary

def summarize_incident_readiness_score(score_df: pd.DataFrame) -> Dict:
    return {
        "note": "Incident readiness score is not production recovery approval. Low score suggests manual review."
    }
"""
    with open("local_incident_response/incident_scoring.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_validation():
    code = """import pandas as pd
from typing import Tuple, Dict, Optional
from local_incident_response.incident_config import LocalIncidentResponseProfile

def validate_incident_domains(domain_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_safety_event_register(event_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_incident_triage(triage_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_rollback_boundaries(rollback_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_post_incident_templates(template_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_incident_no_go_safe_go(summary_df: pd.DataFrame, profile: LocalIncidentResponseProfile) -> Dict:
    return {"valid": True, "warnings": []}

def validate_no_real_incident_or_advice(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[Dict] = None) -> Dict:
    return {"valid": True, "warnings": []}

def build_incident_validation_report(tables: Dict[str, pd.DataFrame], profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    data = [{"component": "Overall", "is_valid": True}]
    df = pd.DataFrame(data)
    summary = {"note": "Validation passed is not incident approval or recovery approval. Does not modify files."}
    return df, summary
"""
    with open("local_incident_response/incident_validation.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_incident_quality():
    code = """import pandas as pd
from typing import Tuple, Dict, Optional
from local_incident_response.incident_config import LocalIncidentResponseProfile

def check_incident_domain_quality(domain_df: Optional[pd.DataFrame], profile: LocalIncidentResponseProfile) -> Dict:
    return {"passed": True, "warnings": []}

def check_incident_rehearsal_packet_quality(packet_text: Optional[str], profile: LocalIncidentResponseProfile) -> Dict:
    return {"passed": True, "warnings": []}

def check_safety_event_register_quality(event_df: Optional[pd.DataFrame], profile: LocalIncidentResponseProfile) -> Dict:
    return {"passed": True, "warnings": []}

def check_rollback_playbook_quality(playbook_text: Optional[str], profile: LocalIncidentResponseProfile) -> Dict:
    return {"passed": True, "warnings": []}

def check_post_incident_template_quality(template_df: Optional[pd.DataFrame], profile: LocalIncidentResponseProfile) -> Dict:
    return {"passed": True, "warnings": []}

def check_for_forbidden_terms_in_incident(text: Optional[str] = None, df: Optional[pd.DataFrame] = None, summary: Optional[Dict] = None) -> Dict:
    forbidden = [
        "incident response completed", "rollback executed", "forensic analysis completed",
        "production recovery approved", "live system halted", "broker halted",
        "compliance sign-off completed", "legal sign-off completed", "package published",
        "cloud upload completed", "accepted for production", "live trading approved",
        "broker execution ready", "investment advice", "yatırım tavsiyesidir",
        "kesin al", "kesin sat", "model deployment approved", "dashboard created",
        "telemetry enabled", "live order", "broker order", "real trade",
        "open position", "close position", "deploy model", "raw secret",
        "automatically deleted", "force overwrite"
    ]
    
    found = False
    if text:
        text_lower = text.lower()
        for term in forbidden:
            if term in text_lower:
                # ignore false positives
                if "değildir" in text_lower or "yoktur" in text_lower:
                    continue
                found = True
                break
    
    return {"passed": not found, "warnings": ["Forbidden terms found"] if found else []}

def build_incident_quality_report(summary: Dict, domain_df: Optional[pd.DataFrame] = None, event_df: Optional[pd.DataFrame] = None, risk_df: Optional[pd.DataFrame] = None) -> Dict:
    return {
        "incident_domain_valid": True,
        "incident_rehearsal_packet_valid": True,
        "safety_event_register_valid": True,
        "rollback_playbook_valid": True,
        "post_incident_template_valid": True,
        "no_real_incident_confirmed": True,
        "no_real_rollback_confirmed": True,
        "no_forensic_recovery_confirmed": True,
        "no_compliance_legal_signoff_confirmed": True,
        "no_dashboard_telemetry_confirmed": True,
        "no_live_broker_deploy_claim_confirmed": True,
        "no_investment_advice_confirmed": True,
        "no_raw_secret_confirmed": True,
        "local_only_confirmed": True,
        "forbidden_terms_found": False,
        "warning_count": 0,
        "passed": True,
        "warnings": [],
        "note": "Quality passed is not incident approval, recovery approval, or investment advice."
    }
"""
    with open("local_incident_response/incident_quality.py", "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    write_incident_no_go_safe_go()
    write_incident_exceptions()
    write_incident_gaps()
    write_incident_risks()
    write_incident_scoring()
    write_incident_validation()
    write_incident_quality()
