# -*- coding: utf-8 -*-
"""Phase 159: Final Documentation Inventory.

Inventories core markdown documentation files across the codebase.
"""

from typing import Dict, Tuple
import pandas as pd
from advanced_final_hardening.final_hardening_config import (
    FinalHardeningProfile,
    get_default_final_hardening_profile,
)
from advanced_final_hardening.final_hardening_labels import (
    INVENTORY_DOMAIN,
    FINAL_HARDENING_CONTRACT_READY,
)

DOCS_INVENTORY = [
    ("README.md", "README.md", "Proje genel tanıtımı, felsefesi ve çalıştırma yönergeleri"),
    ("ARCHITECTURE.md", "docs/ARCHITECTURE.md", "Sistem mimarisi ve fazlar arası veri akış mimarisi"),
    ("ROADMAP.md", "docs/ROADMAP.md", "Faz 1-160 geliştirme yol haritası"),
    ("PHASE_LOG.md", "docs/PHASE_LOG.md", "Tamamlanan fazların detaylı uygulama günlüğü"),
    ("OPERATOR_MANUAL.md", "docs/OPERATOR_MANUAL.md", "Operatör kullanım kılavuzu ve güvenli çalışma yönergeleri"),
    ("ANALYST_HANDBOOK.md", "docs/ANALYST_HANDBOOK.md", "Kullanıcı ve analist el kitabı"),
    ("SAFE_USAGE_GUIDE.md", "docs/SAFE_USAGE_GUIDE.md", "Güvenli kullanım kılavuzu ve canlı işlem sınırları"),
    ("CONFIGURATION.md", "docs/CONFIGURATION.md", "Konfigürasyon ayarları kılavuzu"),
    ("RELEASE_CANDIDATE_CHECKLIST.md", "docs/RELEASE_CANDIDATE_CHECKLIST.md", "Release candidate hazır oluş kontrol listesi"),
    ("FINAL_HARDENING_GUIDE.md", "docs/FINAL_HARDENING_GUIDE.md", "Final hardening kılavuzu ve Phase 160 devir yönergeleri"),
]


def build_final_docs_inventory_registry(
    profile: FinalHardeningProfile | None = None,
) -> Tuple[pd.DataFrame, Dict]:
    """Build docs inventory registry DataFrame and summary."""
    active_profile = profile or get_default_final_hardening_profile()

    rows = []
    for doc_name, path, desc in DOCS_INVENTORY:
        rows.append({
            "item_id": f"DOC-{doc_name}",
            "inventory_type": "documentation",
            "item_name": doc_name,
            "item_path_or_identifier": path,
            "description": desc,
            "metadata_only": True,
            "domain": INVENTORY_DOMAIN,
            "non_signal": True,
            "local_only": True,
            "dry_run": True,
            "non_production": True,
            "current_phase": active_profile.current_phase,
            "status": FINAL_HARDENING_CONTRACT_READY,
        })

    df = pd.DataFrame(rows)
    summary = {
        "docs_count": len(rows),
        "all_metadata_only": bool(df["metadata_only"].all()),
        "current_phase": active_profile.current_phase,
        "status": FINAL_HARDENING_CONTRACT_READY,
    }
    return df, summary
