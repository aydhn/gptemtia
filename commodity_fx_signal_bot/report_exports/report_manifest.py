import json
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime, timezone
import pandas as pd
from report_exports.export_models import ReportExportArtifact, report_export_artifact_to_dict

def build_report_export_manifest(
    report_id: str,
    report_type: str,
    symbol: Optional[str],
    timeframe: str,
    profile_name: str,
    artifacts: List[ReportExportArtifact],
    metadata: Optional[Dict] = None,
) -> Dict:
    artifact_dicts = [report_export_artifact_to_dict(a) for a in artifacts]
    warnings = []
    for a in artifacts:
        warnings.extend(a.warnings)
    return {
        "report_id": report_id,
        "report_type": report_type,
        "symbol": symbol,
        "timeframe": timeframe,
        "profile_name": profile_name,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "artifacts": artifact_dicts,
        "metadata": metadata or {},
        "quality": {},
        "warnings": list(set(warnings)),
        "disclaimer_present": True,
        "no_trade_instruction_confirmed": True
    }

def save_report_export_manifest(manifest: Dict, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    return output_path

def load_report_export_manifest(path: Path) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def manifest_to_dataframe(manifest: Dict) -> pd.DataFrame:
    artifacts = manifest.get("artifacts", [])
    if not artifacts:
        return pd.DataFrame()
    df = pd.DataFrame(artifacts)
    df["report_id"] = manifest.get("report_id")
    df["report_type"] = manifest.get("report_type")
    df["symbol"] = manifest.get("symbol")
    return df

def validate_report_export_manifest(manifest: Dict) -> Dict:
    result = {"valid": True, "errors": []}
    if not manifest.get("report_id"):
        result["valid"] = False
        result["errors"].append("Missing report_id")
    if not manifest.get("disclaimer_present"):
        result["valid"] = False
        result["errors"].append("Disclaimer not present in manifest")
    if not manifest.get("no_trade_instruction_confirmed"):
        result["valid"] = False
        result["errors"].append("No_trade instruction not confirmed")
    return result
