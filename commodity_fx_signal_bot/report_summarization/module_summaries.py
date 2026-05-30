import pandas as pd
from report_summarization.summary_models import BriefCard, build_brief_id

def build_module_summary(module_name: str, summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> BriefCard:
    mod_summaries = summaries_df[summaries_df["module_name"] == module_name] if not summaries_df.empty and "module_name" in summaries_df else pd.DataFrame()
    mod_findings = findings_df[findings_df["module_name"] == module_name] if not findings_df.empty and "module_name" in findings_df else pd.DataFrame()
    mod_warnings = warnings_df[warnings_df["module_name"] == module_name] if not warnings_df.empty and "module_name" in warnings_df else pd.DataFrame()

    key_points = []
    if not mod_findings.empty:
        key_points.extend(mod_findings["text"].head(3).tolist())

    warn_list = []
    if not mod_warnings.empty:
        warn_list.extend(mod_warnings["text"].head(2).tolist())

    summary_text = f"{module_name} modulu icin {len(mod_summaries)} rapor bulundu. {len(mod_findings)} bulgu ve {len(mod_warnings)} uyari cikarildi."

    priority = "low_priority"
    if not mod_warnings.empty and "critical_priority" in mod_warnings["priority"].values:
        priority = "critical_priority"
    elif not mod_findings.empty and "high_priority" in mod_findings["priority"].values:
        priority = "high_priority"

    sources = mod_summaries["source_path"].unique().tolist() if not mod_summaries.empty else []

    return BriefCard(
        brief_id=build_brief_id("module_summary", f"{module_name} Summary", module_name),
        brief_type="module_summary",
        title=f"{module_name} Offline Summary",
        module_name=module_name,
        symbol=None,
        summary=summary_text,
        key_points=key_points,
        follow_ups=[],
        priority=priority,
        source_paths=sources,
        warnings=warn_list
    )

def build_all_module_summaries(summaries_df: pd.DataFrame, findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    modules = set()
    if not summaries_df.empty and "module_name" in summaries_df:
        modules.update(summaries_df["module_name"].unique())
    if not findings_df.empty and "module_name" in findings_df.columns:
        modules.update(findings_df["module_name"].unique())

    cards = []
    for m in modules:
        cards.append(build_module_summary(m, summaries_df, findings_df, warnings_df))

    df = pd.DataFrame([c.__dict__ for c in cards])
    return df, summarize_module_briefs(df)

def rank_modules_by_attention_need(findings_df: pd.DataFrame, warnings_df: pd.DataFrame) -> pd.DataFrame:
    scores = {}
    if not findings_df.empty and "module_name" in findings_df.columns:
        for m, count in findings_df.groupby("module_name").size().items():
            scores[m] = scores.get(m, 0) + count

    if not warnings_df.empty and "module_name" in warnings_df.columns:
        for m, count in warnings_df.groupby("module_name").size().items():
            scores[m] = scores.get(m, 0) + (count * 3)

        if "priority" in warnings_df.columns:
            crit = warnings_df[warnings_df["priority"] == "critical_priority"]
            if not crit.empty:
                for m, count in crit.groupby("module_name").size().items():
                    scores[m] = scores.get(m, 0) + (count * 10)

    df = pd.DataFrame(list(scores.items()), columns=["module_name", "attention_score"])
    df = df.sort_values(by="attention_score", ascending=False).reset_index(drop=True)
    return df


def summarize_module_briefs(module_briefs_df: pd.DataFrame) -> dict:
    if module_briefs_df.empty:
        return {"total_modules": 0}
    return {
        "total_modules": len(module_briefs_df),
        "critical_modules": len(module_briefs_df[module_briefs_df["priority"] == "critical_priority"]) if "priority" in module_briefs_df else 0
    }
