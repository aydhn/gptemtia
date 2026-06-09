import pandas as pd
from evidence_governance.evidence_config import EvidenceGovernanceProfile

def build_audit_evidence_binder(policy_df: pd.DataFrame, control_df: pd.DataFrame, mapping_df: pd.DataFrame, artifact_df: pd.DataFrame, profile: EvidenceGovernanceProfile) -> tuple[str, dict]:
    sections = build_binder_sections(policy_df, control_df, mapping_df, artifact_df)

    binder_text = "# Audit Evidence Binder\n\n"

    for section in sections:
        binder_text += f"## {section['title']}\n\n"
        binder_text += f"{section['content']}\n\n"

    summary = summarize_evidence_binder(binder_text, build_binder_index(artifact_df, mapping_df))
    return binder_text, summary

def build_binder_sections(policy_df: pd.DataFrame, control_df: pd.DataFrame, mapping_df: pd.DataFrame, artifact_df: pd.DataFrame) -> list[dict]:
    sections = []

    sections.append({
        "title": "Amaç ve Kapsam",
        "content": "Bu binder, offline/local evidence governance kapsamında toplanan kanıtların derlemesidir."
    })

    sections.append({
        "title": "Resmi Compliance Sınırı",
        "content": "UYARI: Bu rapor offline/local governance evidence ve compliance-style binder çıktısıdır; resmi compliance sertifikası, hukuki görüş, canlı emir, broker talimatı, model deployment, production scheduler veya yatırım tavsiyesi değildir."
    })

    sections.append({
        "title": "Policy Registry",
        "content": policy_df.to_markdown(index=False) if (policy_df is not None and not policy_df.empty) else "No policies defined."
    })

    sections.append({
        "title": "Control Registry",
        "content": control_df.to_markdown(index=False) if (control_df is not None and not control_df.empty) else "No controls defined."
    })

    sections.append({
        "title": "Evidence Artifact Index",
        "content": build_binder_index(artifact_df, mapping_df).to_markdown(index=False) if artifact_df is not None and not artifact_df.empty else "No artifacts found."
    })

    # Packs placeholders
    pack_types = [
        "Safety Evidence", "Secrets Hygiene Evidence", "Backup/Recovery Evidence",
        "Packaging Evidence", "Quality Evidence", "Scenario Regression Evidence",
        "Final Review Evidence", "Documentation Evidence", "Master Orchestration Evidence"
    ]

    for pt in pack_types:
        sections.append({
            "title": pt,
            "content": f"See corresponding `{pt.lower().replace(' ', '_').replace('/', '_')}_pack.csv` for details."
        })

    sections.append({
        "title": "Evidence Gaps & Safe Follow-up",
        "content": "Gaps and follow-ups are detailed in the `evidence_gap_register.csv` and digest report."
    })

    return sections

def build_binder_index(artifact_df: pd.DataFrame, mapping_df: pd.DataFrame) -> pd.DataFrame:
    if artifact_df is None or artifact_df.empty:
        return pd.DataFrame()

    index_data = []
    for _, art in artifact_df.iterrows():
        art_id = art.get("artifact_id")
        # count controls mapped
        mapped_controls = 0
        if mapping_df is not None and not mapping_df.empty and "artifact_id" in mapping_df.columns:
            mapped_controls = len(mapping_df[mapping_df["artifact_id"] == art_id])

        index_data.append({
            "artifact_id": art_id,
            "relative_path": art.get("relative_path"),
            "artifact_label": art.get("artifact_label"),
            "mapped_controls": mapped_controls,
            "freshness_label": art.get("freshness_label")
        })

    return pd.DataFrame(index_data)

def summarize_evidence_binder(binder_text: str, binder_index_df: pd.DataFrame) -> dict:
    return {
        "binder_length_chars": len(binder_text),
        "total_indexed_artifacts": len(binder_index_df) if binder_index_df is not None else 0
    }
