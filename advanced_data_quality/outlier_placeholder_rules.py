from typing import Tuple, Dict, Any, List
import pandas as pd
from advanced_data_quality.data_quality_config import DataQualityProfile
from advanced_data_quality.data_quality_models import QualityFinding, build_quality_finding_id


def build_outlier_detection_placeholder_rule_set(profile: DataQualityProfile) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    rules = [
        {
            "rule_name": "numeric_outlier_placeholder",
            "rule_domain": "outlier_placeholder",
            "severity_label": "quality_medium",
            "description": "Sayısal alanlarda aşırı uç değer placeholder kontrolü (tahribatsız).",
        }
    ]
    df = pd.DataFrame.from_records(rules)
    return df, summarize_outlier_placeholder_rules(df)


def build_outlier_placeholder_findings(
    df: pd.DataFrame,
    numeric_fields: List[str],
    dataset_type: str,
    provider_name: str = ""
) -> List[QualityFinding]:
    findings: List[QualityFinding] = []
    if df is None or len(df) < 5:
        return findings

    for col in numeric_fields:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            series = df[col].dropna()
            if len(series) < 5:
                continue
            q25 = series.quantile(0.25)
            q75 = series.quantile(0.75)
            iqr = q75 - q25
            if iqr > 0:
                lower = q25 - 3.0 * iqr
                upper = q75 + 3.0 * iqr
                outliers = series[(series < lower) | (series > upper)]
                if len(outliers) > 0:
                    findings.append(
                        QualityFinding(
                            finding_id=build_quality_finding_id("rule_outlier_placeholder", dataset_type, col),
                            rule_id="rule_outlier_placeholder_outlier_placeholder_detection",
                            finding_type="finding_outlier_placeholder",
                            dataset_type=dataset_type,
                            provider_name=provider_name or "unknown_provider",
                            field_name=col,
                            severity_label="quality_medium",
                            status_label="quality_pass_with_warnings",
                            message=f"Field '{col}' has {len(outliers)} potential outliers beyond 3x IQR.",
                            recommendation="Review flagged values in Manual Review Queue; handle scaling/filtering in Phase 113.",
                            future_phase_owner="Phase 113",
                            manual_review_required=True,
                        )
                    )
    return findings


def summarize_outlier_placeholder_rules(df: pd.DataFrame) -> Dict[str, Any]:
    return {
        "rule_count": len(df),
        "rules": df["rule_name"].tolist() if "rule_name" in df.columns else [],
        "domain": "outlier_placeholder",
    }
