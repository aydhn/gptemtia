import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def build_evidence_digest(policy_df: pd.DataFrame, control_status_df: pd.DataFrame, gap_df: pd.DataFrame, scoring_summary: dict, profile: EvidenceGovernanceProfile) -> tuple[str, dict]:
    sections = build_evidence_digest_sections(policy_df, control_status_df, gap_df)

    digest_text = "# Evidence Digest\n\n"

    digest_text += f"**Completeness Score:** {scoring_summary.get('completeness_score', 0):.2f}\n"
    digest_text += f"**Freshness Score:** {scoring_summary.get('freshness_score', 0):.2f}\n\n"

    for section in sections:
        digest_text += f"## {section['title']}\n\n"
        digest_text += f"{section['content']}\n\n"

    follow_up_df = build_safe_evidence_follow_ups(gap_df)

    return digest_text, summarize_evidence_digest(digest_text, follow_up_df)

def build_evidence_digest_sections(policy_df: pd.DataFrame, control_status_df: pd.DataFrame, gap_df: pd.DataFrame) -> list[dict]:
    sections = []

    sections.append({
        "title": "Genel Evidence Durumu",
        "content": "Sistem genel evidence toplama aşamalarından geçmiştir."
    })

    sections.append({
        "title": "Eksik veya Zayıf Evidence Alanları",
        "content": gap_df.to_markdown(index=False) if (gap_df is not None and not gap_df.empty) else "No major gaps."
    })

    sections.append({
        "title": "Resmi Compliance Sınırı",
        "content": "UYARI: Bu rapor offline/local governance evidence ve compliance-style binder çıktısıdır; resmi compliance sertifikası, hukuki görüş veya yatırım tavsiyesi değildir."
    })

    return sections

def build_safe_evidence_follow_ups(gap_df: pd.DataFrame) -> pd.DataFrame:
    if gap_df is None or gap_df.empty:
        return pd.DataFrame()

    follow_ups = []
    for _, gap in gap_df.iterrows():
        follow_ups.append({
            "gap_id": gap.get("gap_id"),
            "severity": gap.get("severity"),
            "action": gap.get("recommended_safe_follow_up")
        })

    return pd.DataFrame(follow_ups)

def summarize_evidence_digest(digest_text: str, follow_up_df: pd.DataFrame) -> dict:
    return {
        "digest_length_chars": len(digest_text),
        "total_follow_ups": len(follow_up_df) if follow_up_df is not None else 0
    }
