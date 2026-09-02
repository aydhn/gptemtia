import os
import pandas as pd
from typing import Tuple, Dict, List
from pathlib import Path

def write_incident_timeline_templates():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_incident_timeline_templates(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"template": "Basic Timeline", "description": "Mock timeline."}]
    return pd.DataFrame(data)

def build_incident_timeline_template_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_incident_timeline_templates(profile)
    summary = summarize_incident_timeline_templates(df)
    return df, summary

def summarize_incident_timeline_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not a real incident timeline."
    }
"""
    with open("local_incident_response/incident_timeline_templates.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_post_incident_review_templates():
    code = """import pandas as pd
from typing import Tuple, Dict, List
from local_incident_response.incident_config import LocalIncidentResponseProfile
from local_incident_response.incident_models import PostIncidentTemplate, build_post_incident_template_id, post_incident_template_to_dict

def build_default_post_incident_review_templates(profile: LocalIncidentResponseProfile) -> List[PostIncidentTemplate]:
    templates = [
        PostIncidentTemplate(
            template_id=build_post_incident_template_id("Standard PIR"),
            template_name="Standard PIR",
            template_area="General",
            sections=["Summary", "Timeline", "Root Cause"],
            disclaimer="Not an official incident report.",
            warnings=["Offline review only."]
        )
    ]
    return templates

def build_post_incident_review_template_library(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    templates = build_default_post_incident_review_templates(profile)
    df = pd.DataFrame([post_incident_template_to_dict(t) for t in templates])
    summary = summarize_post_incident_review_templates(df)
    return df, summary

def summarize_post_incident_review_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df) if df is not None else 0,
        "note": "Not an official incident report."
    }
"""
    with open("local_incident_response/post_incident_review_templates.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_root_cause_categories():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_root_cause_categories(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"category": "Configuration Error", "description": "Mock category."}]
    return pd.DataFrame(data)

def build_root_cause_category_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_root_cause_categories(profile)
    summary = summarize_root_cause_categories(df)
    return df, summary

def summarize_root_cause_categories(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not forensic analysis."
    }
"""
    with open("local_incident_response/root_cause_categories.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_corrective_action_rehearsal():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_corrective_actions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"action": "Update Config", "description": "Mock action."}]
    return pd.DataFrame(data)

def build_corrective_action_rehearsal_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_corrective_actions(profile)
    summary = summarize_corrective_actions(df)
    return df, summary

def summarize_corrective_actions(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an auto-fix."
    }
"""
    with open("local_incident_response/corrective_action_rehearsal.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_communication_templates():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_communication_templates(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"template_name": "Internal Update", "body": "Mock body."}]
    return pd.DataFrame(data)

def build_communication_template_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_communication_templates(profile)
    summary = summarize_communication_templates(df)
    return df, summary

def summarize_communication_templates(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Not an official communication."
    }
"""
    with open("local_incident_response/communication_templates.py", "w", encoding="utf-8") as f:
        f.write(code)

def write_escalation_decisions():
    code = """import pandas as pd
from typing import Tuple, Dict
from local_incident_response.incident_config import LocalIncidentResponseProfile

def build_default_escalation_decisions(profile: LocalIncidentResponseProfile) -> pd.DataFrame:
    data = [{"decision": "Escalate to L2", "criteria": "Mock criteria."}]
    return pd.DataFrame(data)

def build_escalation_decision_registry(profile: LocalIncidentResponseProfile) -> Tuple[pd.DataFrame, Dict]:
    df = build_default_escalation_decisions(profile)
    summary = summarize_escalation_decisions(df)
    return df, summary

def summarize_escalation_decisions(df: pd.DataFrame) -> Dict:
    return {
        "count": len(df),
        "note": "Does not automatically escalate."
    }
"""
    with open("local_incident_response/escalation_decisions.py", "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    write_incident_timeline_templates()
    write_post_incident_review_templates()
    write_root_cause_categories()
    write_corrective_action_rehearsal()
    write_communication_templates()
    write_escalation_decisions()
