from research_reports.research_config import ResearchReportProfile

def summarize_walk_forward(inputs: dict) -> dict:
    return {
        "split_count": 0,
        "valid_split_count": 0
    }

def summarize_parameter_sensitivity(inputs: dict) -> dict:
    return {
        "stability_score": 0.0,
        "parameter_fragility_warning_count": 0
    }

def summarize_overfitting_risk(inputs: dict) -> dict:
    return {
        "overfitting_risk_score": 0.0
    }

def summarize_robustness(inputs: dict) -> dict:
    return {
        "robustness_score": 0.0,
        "validation_status": "unknown"
    }

def build_validation_research_summary(inputs: dict, profile: ResearchReportProfile) -> dict:
    wf = summarize_walk_forward(inputs)
    ps = summarize_parameter_sensitivity(inputs)
    orisk = summarize_overfitting_risk(inputs)
    rob = summarize_robustness(inputs)

    return {
        **wf,
        **ps,
        **orisk,
        **rob,
        "warnings": []
    }
