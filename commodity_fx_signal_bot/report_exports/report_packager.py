import json
import shutil
from pathlib import Path
from typing import List, Tuple, Dict
import logging
from report_exports.export_models import ReportExportArtifact, sanitize_export_filename

logger = logging.getLogger(__name__)

class ReportPackager:
    def __init__(self, package_root: Path):
        self.package_root = package_root
        self.package_root.mkdir(parents=True, exist_ok=True)

    def build_package_dir(self, report_id: str, report_type: str, symbol: str | None, timeframe: str) -> Path:
        sym_part = sanitize_export_filename(symbol) if symbol else "universe"
        tf_part = sanitize_export_filename(timeframe)
        rid_part = sanitize_export_filename(report_id)
        dir_name = f"pkg_{report_type}_{sym_part}_{tf_part}_{rid_part}"
        package_dir = self.package_root / dir_name
        package_dir.mkdir(parents=True, exist_ok=True)
        return package_dir

    def copy_artifacts_to_package(self, artifacts: List[ReportExportArtifact], package_dir: Path) -> Tuple[List[Path], Dict]:
        copied_paths = []
        errors = []
        for art in artifacts:
            if not art.path:
                continue
            src_path = Path(art.path)
            if not src_path.exists():
                errors.append(f"Artifact source not found: {src_path}")
                continue
            try:
                dest_path = package_dir / src_path.name
                shutil.copy2(src_path, dest_path)
                copied_paths.append(dest_path)
            except Exception as e:
                errors.append(f"Failed to copy {src_path.name}: {str(e)}")
        summary = {"copied_count": len(copied_paths), "errors": errors}
        return copied_paths, summary

    def write_package_readme(self, package_dir: Path, manifest: Dict) -> Path:
        readme_path = package_dir / "README.txt"
        content = [
            "===========================================================",
            f"REPORT PACKAGE: {manifest.get('report_id')}",
            "===========================================================",
            f"Report Type: {manifest.get('report_type')}",
            f"Symbol: {manifest.get('symbol', 'N/A')}",
            f"Timeframe: {manifest.get('timeframe')}",
            f"Created At (UTC): {manifest.get('created_at_utc')}",
            "",
            "WARNING: Bu çıktı offline araştırma raporu dışa aktarım/arşiv raporudur.",
            "Canlı emir, broker talimatı, gerçek pozisyon, canlı sinyal veya yatırım tavsiyesi değildir.",
            "==========================================================="
        ]
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        return readme_path

    def build_package(self, manifest: Dict, artifacts: List[ReportExportArtifact]) -> Tuple[Path, Dict]:
        report_id = manifest.get("report_id", "unknown")
        report_type = manifest.get("report_type", "unknown")
        symbol = manifest.get("symbol")
        timeframe = manifest.get("timeframe", "1d")
        package_dir = self.build_package_dir(report_id, report_type, symbol, timeframe)
        copied_paths, copy_summary = self.copy_artifacts_to_package(artifacts, package_dir)
        manifest_path = package_dir / "manifest.json"
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        readme_path = self.write_package_readme(package_dir, manifest)
        summary = {
            "package_dir": str(package_dir),
            "copied_artifacts": copy_summary["copied_count"],
            "copy_errors": copy_summary["errors"],
            "has_readme": readme_path.exists(),
            "has_manifest": manifest_path.exists()
        }
        return package_dir, summary
