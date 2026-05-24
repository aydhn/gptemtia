from pathlib import Path
from typing import Tuple, Optional, Dict
import pandas as pd
import datetime
import hashlib
import os

from knowledge_base.kb_config import KnowledgeBaseProfile
from knowledge_base.kb_models import KnowledgeDocument, build_document_id
from knowledge_base.kb_labels import list_knowledge_document_type_labels
from core.logger import get_logger

logger = get_logger(__name__)

class KnowledgeDocumentDiscovery:
    def __init__(self, project_root: Path):
        self.project_root = project_root

        # Define directories to scan based on project structure
        self.lake_dir = project_root / "data" / "lake"
        self.reports_dir = project_root / "reports" / "output"
        self.docs_dir = project_root / "docs"

    def discover_documents(self, profile: KnowledgeBaseProfile) -> Tuple[pd.DataFrame, Dict]:
        documents = []
        warnings = []
        scanned_count = 0
        skipped_count = 0

        dirs_to_scan = []

        if profile.scan_docs:
            dirs_to_scan.append(self.docs_dir)
            readme_path = self.project_root / "README.md"
            if readme_path.exists():
                doc = self._try_build_doc(readme_path, profile)
                if doc:
                    documents.append(doc)
                else:
                    skipped_count += 1
                scanned_count += 1

        if profile.scan_reports_output:
            dirs_to_scan.append(self.reports_dir)

        if profile.scan_data_lake_reports:
            dirs_to_scan.append(self.lake_dir / "research_reports")
            dirs_to_scan.append(self.lake_dir / "report_exports")

        if profile.scan_experiments:
            dirs_to_scan.append(self.lake_dir / "experiments")

        if profile.scan_governance:
            dirs_to_scan.append(self.lake_dir / "governance")

        if profile.scan_planning:
            dirs_to_scan.append(self.lake_dir / "research_planning")

        if profile.scan_meta_research:
            dirs_to_scan.append(self.lake_dir / "meta_research")
            dirs_to_scan.append(self.lake_dir / "factor_research")
            dirs_to_scan.append(self.lake_dir / "synthetic_indices")
            dirs_to_scan.append(self.lake_dir / "portfolio_research")
            dirs_to_scan.append(self.lake_dir / "portfolio_regime")

        allowed_extensions = {".md", ".txt", ".csv", ".json", ".yaml", ".yml"}

        for directory in dirs_to_scan:
            if not directory.exists() or not directory.is_dir():
                warnings.append(f"Directory not found: {directory}")
                continue

            for root, _, files in os.walk(directory):
                # Avoid recursively scanning knowledge_base to prevent infinite loops
                if "knowledge_base" in root:
                    continue

                for file in files:
                    if len(documents) >= profile.max_documents:
                        break

                    path = Path(root) / file
                    if path.suffix.lower() not in allowed_extensions:
                        continue

                    # Skip sensitive or environment files
                    if any(x in file.lower() for x in [".env", "key", "token", "secret", "password"]):
                        skipped_count += 1
                        continue

                    scanned_count += 1
                    doc = self._try_build_doc(path, profile)
                    if doc:
                        documents.append(doc)
                    else:
                        skipped_count += 1

                if len(documents) >= profile.max_documents:
                    warnings.append(f"Hit max_documents limit ({profile.max_documents}). Stopping discovery.")
                    break

        df = pd.DataFrame([vars(d) for d in documents])
        summary = {
            "scanned_files": scanned_count,
            "discovered_documents": len(documents),
            "skipped_files": skipped_count,
            "warnings_count": len(warnings)
        }

        return df, summary

    def _try_build_doc(self, path: Path, profile: KnowledgeBaseProfile) -> Optional[KnowledgeDocument]:
        try:
            return self.build_knowledge_document(path, profile)
        except Exception as e:
            logger.debug(f"Skipping {path}: {e}")
            return None

    def classify_document_type(self, path: Path) -> str:
        p_str = str(path).lower()
        if "research_reports" in p_str: return "research_report_document"
        if "report_exports" in p_str: return "report_export_document"
        if "experiments" in p_str: return "experiment_document"
        if "governance" in p_str: return "governance_document"
        if "research_planning" in p_str: return "planning_document"
        if "meta_research" in p_str: return "meta_research_document"
        if "factor_research" in p_str: return "factor_document"
        if "portfolio_research" in p_str: return "portfolio_document"
        if "portfolio_regime" in p_str: return "regime_document"
        if "synthetic_indices" in p_str: return "synthetic_index_document"
        if "paper" in p_str: return "paper_document"
        if "validation" in p_str: return "validation_document"
        if "ml" in p_str: return "ml_document"
        if "observability" in p_str: return "observability_document"
        if "security" in p_str: return "security_document"
        if "docs/" in p_str or p_str.endswith("readme.md"): return "documentation_document"
        if "phase_log.md" in p_str: return "phase_log_document"
        return "unknown_document"

    def infer_source_module(self, path: Path) -> Optional[str]:
        p_str = str(path).lower()
        modules = [
            "research_reports", "report_exports", "portfolio_research", "portfolio_regime",
            "synthetic_indices", "factor_research", "meta_research", "experiments",
            "governance", "research_planning", "ml", "paper", "validation", "backtesting",
            "observability", "security"
        ]
        for m in modules:
            if m in p_str:
                return m
        return None

    def build_knowledge_document(self, path: Path, profile: KnowledgeBaseProfile) -> KnowledgeDocument:
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        size = path.stat().st_size
        max_bytes = profile.max_document_mb * 1024 * 1024

        warnings = []
        if size > max_bytes:
            warnings.append(f"File size ({size} bytes) exceeds profile limit ({max_bytes} bytes).")
            raise ValueError(f"File too large: {path}")

        try:
            rel_path = str(path.relative_to(self.project_root))
        except ValueError:
            rel_path = path.name

        mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime, tz=datetime.timezone.utc).isoformat()

        doc_id = build_document_id(rel_path, mtime)
        doc_type = self.classify_document_type(path)
        module = self.infer_source_module(path)

        return KnowledgeDocument(
            document_id=doc_id,
            document_type=doc_type,
            title=path.name,
            path=str(path.absolute()),
            relative_path=rel_path,
            source_module=module,
            created_at_utc=datetime.datetime.fromtimestamp(path.stat().st_ctime, tz=datetime.timezone.utc).isoformat(),
            modified_at_utc=mtime,
            size_bytes=size,
            text_hash=None, # Computed during text extraction
            metadata={"extension": path.suffix.lower()},
            warnings=warnings
        )
