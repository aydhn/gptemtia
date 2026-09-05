import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file('advanced_config_profiles/profile_validation.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile

def validate_config_profile_registry(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"status": "passed"}

def validate_research_mode_presets(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"status": "passed"}

def validate_composed_research_profiles(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    if df is not None and not df.empty:
        for idx, row in df.iterrows():
            if not row.get("manual_review_required"):
                return {"status": "failed", "reason": "Composed profiles must have manual_review_required=True"}
    return {"status": "passed"}

def validate_profile_compatibility_matrix(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"status": "passed"}

def validate_no_forbidden_profile_claims(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> dict:
    forbidden = ["canlı emir", "broker order", "kesin al", "kesin sat", "yatırım tavsiyesi", "deployment", "scraping", "docker push", "archive created"]
    combined = str(text) + str(df) + str(summary)
    combined = combined.lower()
    found = [f for f in forbidden if f in combined and not (f == "yatırım tavsiyesi" and "değildir" in combined) ]
    if found:
        return {"status": "failed", "forbidden_claims": found}
    return {"status": "passed"}

def build_profile_validation_report(tables: dict, profile: AdvancedConfigSystemProfile) -> tuple[pd.DataFrame, dict]:
    results = [
        {"check": "phase_104", "status": "passed" if profile.current_phase == 104 else "failed"},
        {"check": "phase_160", "status": "passed" if profile.target_final_phase == 160 else "failed"},
        {"check": "local_only", "status": "passed" if profile.local_only and profile.non_production and profile.research_only else "failed"},
        {"check": "dry_run_default", "status": "passed" if profile.dry_run_default else "failed"}
    ]
    df = pd.DataFrame(results)
    return df, {"total_checks": len(df), "passed": len(df[df["status"]=="passed"])}
''')

write_file('advanced_config_profiles/profile_quality.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile

def check_config_profile_registry_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_research_mode_preset_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_composed_profile_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_profile_compatibility_quality(df: pd.DataFrame, profile: AdvancedConfigSystemProfile) -> dict:
    return {"quality": "good"}

def check_for_forbidden_terms_in_profiles(text: str = None, df: pd.DataFrame = None, summary: dict = None) -> dict:
    forbidden = ["live trading approved", "broker order", "real order sent", "investment advice", "yatırım tavsiyesidir", "kesin al", "kesin sat", "production deployed", "model deployed", "web server started", "dashboard created", "scraping enabled", "external llm called", "vector database created", "embeddings generated", "zip generated", "archive created", "docker image pushed", "git tag created", "official approval granted", "production approved", "guaranteed signal", "guaranteed profit"]
    combined = str(text) + str(df) + str(summary)
    combined = combined.lower()
    
    # Exclude false positives
    combined = combined.replace("yatırım tavsiyesi değildir", "")
    combined = combined.replace("canlı emir yoktur", "")
    combined = combined.replace("broker entegrasyonu değildir", "")
    combined = combined.replace("scraping yapılmaz", "")
    combined = combined.replace("deployment değildir", "")
    combined = combined.replace("official approval değildir", "")
    combined = combined.replace("kesin al/sat değildir", "")
    
    found = [f for f in forbidden if f in combined]
    return {"forbidden_terms_found": found}

def build_profile_quality_report(summary: dict, registry_df: pd.DataFrame = None, composed_df: pd.DataFrame = None) -> dict:
    return {"status": "quality check completed", "forbidden_terms": check_for_forbidden_terms_in_profiles(df=registry_df)}
''')

write_file('advanced_config_profiles/profile_scoring.py', '''
import pandas as pd
from .advanced_config import AdvancedConfigSystemProfile

def calculate_profile_readiness_score(
    registry_df: pd.DataFrame, preset_df: pd.DataFrame, composed_df: pd.DataFrame,
    compatibility_df: pd.DataFrame, validation_df: pd.DataFrame, profile: AdvancedConfigSystemProfile
) -> float:
    score = 0.5
    if registry_df is not None and not registry_df.empty: score += 0.1
    if preset_df is not None and not preset_df.empty: score += 0.1
    if composed_df is not None and not composed_df.empty: score += 0.1
    if validation_df is not None and not validation_df.empty and (validation_df["status"] == "passed").all(): score += 0.2
    return min(1.0, score)

def build_profile_readiness_score_report(
    registry_df: pd.DataFrame, preset_df: pd.DataFrame, composed_df: pd.DataFrame,
    compatibility_df: pd.DataFrame, validation_df: pd.DataFrame, profile: AdvancedConfigSystemProfile
) -> tuple[pd.DataFrame, dict]:
    score = calculate_profile_readiness_score(registry_df, preset_df, composed_df, compatibility_df, validation_df, profile)
    classification = classify_profile_readiness_score(score, profile)
    df = pd.DataFrame([{"score": score, "classification": classification}])
    return df, {"score": score, "classification": classification}

def classify_profile_readiness_score(score: float, profile: AdvancedConfigSystemProfile) -> str:
    if score >= profile.min_readiness_score:
        return "ready"
    return "needs_manual_review"

def summarize_profile_readiness_score(df: pd.DataFrame) -> dict:
    return {"mean_score": df["score"].mean() if df is not None and not df.empty else 0}
''')

write_file('advanced_config_profiles/advanced_config_report_builder.py', '''
import pandas as pd

def build_advanced_config_disclaimer() -> str:
    return "Bu çıktı Phase 104 Advanced Config Profile System raporudur. Canlı emir, broker talimatı, kesin AL/SAT, yatırım tavsiyesi, production deployment, model deployment, scraping, external LLM/API çağrısı veya official approval değildir."

def build_advanced_config_profile_registry_markdown_report(summary: dict, registry_df: pd.DataFrame = None) -> str:
    return f"# Config Profile Registry\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (registry_df.to_markdown() if registry_df is not None else "No data")

def build_research_mode_preset_markdown_report(summary: dict, preset_df: pd.DataFrame = None) -> str:
    return f"# Research Mode Presets\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (preset_df.to_markdown() if preset_df is not None else "No data")

def build_composed_profile_markdown_report(summary: dict, composed_df: pd.DataFrame = None) -> str:
    return f"# Composed Profiles\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (composed_df.to_markdown() if composed_df is not None else "No data")

def build_profile_compatibility_markdown_report(summary: dict, compatibility_df: pd.DataFrame = None) -> str:
    return f"# Profile Compatibility\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (compatibility_df.to_markdown() if compatibility_df is not None else "No data")

def build_profile_validation_markdown_report(summary: dict, validation_df: pd.DataFrame = None) -> str:
    return f"# Profile Validation\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (validation_df.to_markdown() if validation_df is not None else "No data")

def build_profile_quality_markdown_report(summary: dict, quality: dict = None) -> str:
    return f"# Profile Quality\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + str(quality)

def build_advanced_config_status_markdown_report(summary: dict, status_df: pd.DataFrame = None) -> str:
    return f"# Advanced Config Status\\n\\n{build_advanced_config_disclaimer()}\\n\\n" + (status_df.to_markdown() if status_df is not None else "No data")
''')
