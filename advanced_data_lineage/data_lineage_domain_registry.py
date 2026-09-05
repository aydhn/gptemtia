from typing import Tuple, Dict, Any, List
import pandas as pd

from advanced_data_lineage.data_lineage_config import DataLineageProfile
from advanced_data_lineage.data_lineage_models import (
    DataLineageDomain,
    build_data_lineage_domain_id,
)


DOMAIN_SPECS = [
    ("data_lineage_profile_domain", "Profile Registry", "Yönetilen lineage profillerinin kayıt defteri", ["data_lineage_profile_registry.csv"]),
    ("data_lineage_domain", "Domain Registry", "Lineage etki alanları ve gereksinimleri", ["data_lineage_domain_registry.csv"]),
    ("provenance_source_domain", "Provenance Sources", "Orijinal veri sağlayıcı kaynak ve depo kayıtları", ["provenance_source_registry.csv"]),
    ("source_reference_domain", "Source References", "Kaynak veri referansları ve URI/tanımlayıcılar", ["source_reference_registry.csv"]),
    ("provider_provenance_domain", "Provider Provenance", "Veri sağlayıcı soy kütüğü ve yetenek bağları", ["provider_provenance_registry.csv"]),
    ("dataset_provenance_domain", "Dataset Provenance", "Veri seti düzeyinde kaynak ve normalizasyon bağları", ["dataset_provenance_registry.csv"]),
    ("schema_provenance_domain", "Schema Provenance", "Kanonik ve kaynak şema soy kütüğü izleri", ["schema_provenance_registry.csv"]),
    ("transformation_provenance_domain", "Transformation Provenance", "Dönüşüm kuralları ve alan seviyesi haritalar", ["transformation_provenance_registry.csv"]),
    ("normalization_lineage_domain", "Normalization Lineage", "Phase 113 normalizasyon kurallarının izlenebilirliği", ["normalization_lineage_registry.csv"]),
    ("quality_finding_lineage_domain", "Quality Finding Lineage", "Phase 112 veri kalitesi bulgularının soy kütüğü", ["quality_finding_lineage_registry.csv"]),
    ("manual_review_lineage_domain", "Manual Review Lineage", "Manuel inceleme kuyruğunun non-destructive izi", ["manual_review_lineage_registry.csv"]),
    ("normalized_output_lineage_domain", "Normalized Output Lineage", "Orijinal ve normalize görünüm manifest eşleşmesi", ["normalized_output_lineage_registry.csv"]),
    ("fx_lineage_domain", "FX Lineage", "Döviz çifti, kotasyon ve OHLCV soy kütüğü", ["fx_lineage_registry.csv"]),
    ("commodity_lineage_domain", "Commodity Lineage", "Emtia spot, vadeli ve roll gereksinimleri soy kütüğü", ["commodity_lineage_registry.csv"]),
    ("macro_lineage_domain", "Macro Lineage", "Makro gösterge, frekans ve revizyon soy kütüğü", ["macro_lineage_registry.csv"]),
    ("calendar_lineage_domain", "Calendar Lineage", "Ekonomik takvim olayları ve planlanan/gerçekleşen zaman izi", ["calendar_lineage_registry.csv"]),
    ("news_metadata_lineage_domain", "News Metadata Lineage", "Haber metadata referansları ve konu etiketleri izi", ["news_metadata_lineage_registry.csv"]),
    ("license_provenance_domain", "License Provenance", "Sağlayıcı lisans notları ve yeniden dağıtım sınırları", ["license_provenance_registry.csv"]),
    ("copyright_boundary_domain", "Copyright Boundary", "Telif hakkı ve sıfır tam metin doğrulama izi", ["copyright_boundary_provenance.csv"]),
    ("metadata_only_provenance_domain", "Metadata-Only Provenance", "Yalnızca metadata kullanım politikası soy kütüğü", ["metadata_only_provenance.csv"]),
    ("data_usage_boundary_domain", "Usage Boundary", "Yerel araştırma kullanım sınırları ve no-go kuralları", ["data_usage_boundary_registry.csv"]),
    ("audit_trail_domain", "Audit Trail Events", "Değişmez denetim izi olay kayıtları", ["audit_trail_event_registry.csv"]),
    ("transformation_audit_domain", "Transformation Audit Trail", "Veri dönüşüm denetim izi kayıtları", ["transformation_audit_trail.csv"]),
    ("lineage_finding_domain", "Lineage Findings", "Soy kütüğü tespitleri ve teşhis kayıtları", ["lineage_finding_registry.csv"]),
    ("provenance_scoring_domain", "Provenance Scoring", "Sağlayıcı ve kaynak güven skoru raporu", ["provenance_confidence_score_report.csv"]),
    ("traceability_scoring_domain", "Traceability Scoring", "Veri seti ve sağlayıcı izlenebilirlik skoru raporu", ["traceability_score_report.csv"]),
    ("lineage_graph_domain", "Lineage Graph Placeholder", "Düğüm-kenar soy kütüğü grafiği yer tutucusu", ["lineage_graph_nodes.csv", "lineage_graph_edges.csv"]),
    ("cross_domain_provenance_domain", "Cross-Domain Provenance Map", "Varlık sınıfları arası çapraz soy kütüğü haritası", ["cross_domain_provenance_map.csv"]),
    ("data_lineage_health_domain", "Data Lineage Health", "Soy kütüğü altyapısı sağlık denetim raporu", ["data_lineage_health_check.csv"]),
    ("data_lineage_validation_domain", "Data Lineage Validation", "Bütünlük ve yasaklı iddia denetim raporu", ["data_lineage_validation_report.csv"]),
    ("data_lineage_safety_domain", "Data Lineage Safety", "No-go ve safe-go güvenlik sınırları", ["data_lineage_safety_boundary.csv"]),
    ("phase_115_handoff_domain", "Phase 115 Handoff", "Data Provider Benchmark Report için girdi devir raporu", ["phase_115_handoff_report.csv"]),
]


def build_default_data_lineage_domains(
    profile: DataLineageProfile,
) -> List[DataLineageDomain]:
    domains: List[DataLineageDomain] = []
    for label, name, desc, req_outputs in DOMAIN_SPECS:
        d_id = build_data_lineage_domain_id(label)
        domains.append(
            DataLineageDomain(
                domain_id=d_id,
                domain_label=label,
                domain_name=name,
                description=desc,
                required_outputs=req_outputs,
                warnings=[],
            )
        )
    return domains


def build_data_lineage_domain_registry(
    profile: DataLineageProfile,
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    domains = build_default_data_lineage_domains(profile)
    records = [d.to_dict() for d in domains]
    df = pd.DataFrame.from_records(records)
    summary = summarize_data_lineage_domains(df)
    return df, summary


def summarize_data_lineage_domains(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "total_domains": len(df),
        "domain_labels": df["domain_label"].tolist() if "domain_label" in df.columns else [],
        "required_output_count": sum(len(outputs) for outputs in df["required_outputs"]) if "required_outputs" in df.columns else 0,
        "current_phase": 114,
        "target_final_phase": 160,
    }
