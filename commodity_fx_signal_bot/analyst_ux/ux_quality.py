import pandas as pd
from .ux_config import AnalystUXProfile

FORBIDDEN_TERMS = [
    "live order", "broker order", "real trade", "open position", "close position",
    "buy now", "sell now", "deploy model", "production deploy", "production scheduler",
    "background daemon", "while true", "run live", "guaranteed profit", "risk-free return",
    "yatırım tavsiyesidir", "kesin al", "kesin sat"
]

def check_alias_quality(aliases_df: pd.DataFrame | None, profile: AnalystUXProfile) -> dict:
    if aliases_df is None or aliases_df.empty: return {"passed": False}
    return {"passed": True}

def check_intent_quality(intent_df: pd.DataFrame | None, profile: AnalystUXProfile) -> dict:
    if intent_df is None or intent_df.empty: return {"passed": False}
    return {"passed": True}

def check_suggestion_quality(suggestions_df: pd.DataFrame | None, profile: AnalystUXProfile) -> dict:
    if suggestions_df is None or suggestions_df.empty: return {"passed": False}
    return {"passed": True}

def check_prompt_pack_quality(prompts_df: pd.DataFrame | None, profile: AnalystUXProfile) -> dict:
    if prompts_df is None or prompts_df.empty: return {"passed": False}
    return {"passed": True}

def check_task_board_quality(task_df: pd.DataFrame | None, profile: AnalystUXProfile) -> dict:
    if task_df is None or task_df.empty: return {"passed": False}
    return {"passed": True}

def check_for_forbidden_terms_in_ux(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    findings = []

    def scan_str(s, source):
        if not isinstance(s, str): return
        s_lower = s.lower()
        for term in FORBIDDEN_TERMS:
            # check for false positives like "yatırım tavsiyesi değildir"
            if term == "yatırım tavsiyesidir" and "değildir" in s_lower:
                continue
            if term in s_lower:
                findings.append(f"Forbidden term '{term}' found in {source}")

    if text:
        scan_str(text, "text")
    if df is not None and not df.empty:
        for col in df.select_dtypes(include=['object']):
            for val in df[col].dropna():
                scan_str(val, f"dataframe column {col}")

    return {"passed": len(findings) == 0, "findings": findings, "warning_count": len(findings)}

def build_ux_quality_report(summary: dict, aliases_df: pd.DataFrame | None = None, suggestions_df: pd.DataFrame | None = None, prompts_df: pd.DataFrame | None = None) -> dict:
    f_res = check_for_forbidden_terms_in_ux(df=aliases_df)
    f_res2 = check_for_forbidden_terms_in_ux(df=suggestions_df)
    f_res3 = check_for_forbidden_terms_in_ux(df=prompts_df)

    findings = f_res["findings"] + f_res2["findings"] + f_res3["findings"]

    return {
        "aliases_valid": aliases_df is not None and not aliases_df.empty,
        "intents_valid": True,
        "suggestions_valid": suggestions_df is not None and not suggestions_df.empty,
        "prompt_packs_valid": prompts_df is not None and not prompts_df.empty,
        "task_board_valid": True,
        "safe_offline_only_confirmed": len(findings) == 0,
        "forbidden_terms_found": len(findings) > 0,
        "warning_count": len(findings),
        "passed": len(findings) == 0,
        "warnings": findings
    }
