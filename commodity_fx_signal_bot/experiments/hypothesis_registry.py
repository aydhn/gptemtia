import json
import logging
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd
from typing import Optional

from experiments.experiment_models import (
    ResearchHypothesis,
    build_hypothesis_id,
    research_hypothesis_to_dict
)
from experiments.experiment_labels import validate_hypothesis_status

logger = logging.getLogger(__name__)

class HypothesisRegistry:
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self.file_path = self.registry_dir / "hypothesis_registry.jsonl"
        self._cache = {}
        self._load()

    def _load(self):
        if not self.file_path.exists():
            return
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    h = ResearchHypothesis(**data)
                    self._cache[h.hypothesis_id] = h
        except Exception as e:
            logger.error(f"Failed to load hypothesis registry: {e}")

    def _save(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                for h in self._cache.values():
                    f.write(json.dumps(research_hypothesis_to_dict(h)) + "\n")
        except Exception as e:
            logger.error(f"Failed to save hypothesis registry: {e}")

    def add_hypothesis(self, hypothesis: ResearchHypothesis) -> Path:
        validate_hypothesis_status(hypothesis.hypothesis_status)
        self._cache[hypothesis.hypothesis_id] = hypothesis
        self._save()
        return self.file_path

    def load_hypotheses(self) -> pd.DataFrame:
        if not self._cache:
            return pd.DataFrame()
        data = [research_hypothesis_to_dict(h) for h in self._cache.values()]
        return pd.DataFrame(data)

    def get_hypothesis(self, hypothesis_id: str) -> Optional[dict]:
        h = self._cache.get(hypothesis_id)
        if h:
            return research_hypothesis_to_dict(h)
        return None

    def update_hypothesis_status(self, hypothesis_id: str, status: str, notes: Optional[str] = None) -> dict:
        validate_hypothesis_status(status)
        if hypothesis_id not in self._cache:
            raise ValueError(f"Hypothesis {hypothesis_id} not found.")

        h = self._cache[hypothesis_id]
        h.hypothesis_status = status
        h.updated_at_utc = datetime.now(timezone.utc).isoformat()
        if notes:
            if h.notes:
                h.notes += f"\nUpdate ({h.updated_at_utc}): {notes}"
            else:
                h.notes = notes

        self._save()
        return research_hypothesis_to_dict(h)

    def list_by_status(self, status: str) -> pd.DataFrame:
        df = self.load_hypotheses()
        if df.empty:
            return df
        return df[df["hypothesis_status"] == status]

    def list_by_module(self, target_module: str) -> pd.DataFrame:
        df = self.load_hypotheses()
        if df.empty:
            return df
        return df[df["target_module"] == target_module]

    def summarize(self) -> dict:
        df = self.load_hypotheses()
        if df.empty:
            return {
                "total_hypotheses": 0,
                "by_status": {},
                "by_module": {}
            }

        return {
            "total_hypotheses": len(df),
            "by_status": df["hypothesis_status"].value_counts().to_dict(),
            "by_module": df["target_module"].value_counts().to_dict()
        }

def build_default_hypotheses() -> list[ResearchHypothesis]:
    now = datetime.now(timezone.utc).isoformat()
    defaults = [
        {
            "title": "Trend and Momentum Consensus",
            "description": "Trend + momentum faktörleri meta consensus kalitesini artırır mı?",
            "target_module": "meta_research",
            "expected_effect": "Increases consensus quality",
            "success_metrics": ["quality_adjusted_score", "consensus_score"]
        },
        {
            "title": "Validation Quality vs Paper Volatility",
            "description": "Validation kalitesi düşük stratejilerde paper sonuçları daha oynak mı?",
            "target_module": "paper",
            "expected_effect": "Negative correlation between validation score and paper volatility",
            "success_metrics": ["validation_score", "paper_virtual_drawdown"]
        },
        {
            "title": "Factor-Neutral Basket Concentration",
            "description": "Factor-neutral basket yüksek concentration riskini azaltıyor mu?",
            "target_module": "factor_research",
            "expected_effect": "Reduces concentration risk",
            "success_metrics": ["factor_stability_score"]
        },
        {
            "title": "Regime-Aware Stress Metrics",
            "description": "Regime-aware stress metrics meta uncertainty skorunu iyileştiriyor mu?",
            "target_module": "portfolio_regime",
            "expected_effect": "Improves meta uncertainty",
            "success_metrics": ["regime_stress_score", "uncertainty_score"]
        },
        {
            "title": "Synthetic Benchmark Relative Strength",
            "description": "Synthetic benchmark relative strength, factor rank stabilitesini açıklıyor mu?",
            "target_module": "synthetic_indices",
            "expected_effect": "Explains factor rank stability",
            "success_metrics": ["factor_stability_score"]
        }
    ]

    hypotheses = []
    for d in defaults:
        h_id = build_hypothesis_id(d["title"], "1d", d["target_module"])
        h = ResearchHypothesis(
            hypothesis_id=h_id,
            title=d["title"],
            description=d["description"],
            hypothesis_status="hypothesis_proposed",
            target_module=d["target_module"],
            target_symbols=["*"],
            timeframe="1d",
            expected_effect=d["expected_effect"],
            success_metrics=d["success_metrics"],
            created_at_utc=now,
            updated_at_utc=None,
            notes="",
            warnings=[]
        )
        hypotheses.append(h)

    return hypotheses
