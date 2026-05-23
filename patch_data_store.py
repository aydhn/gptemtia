import re

with open("commodity_fx_signal_bot/data/storage/data_lake.py", "r") as f:
    content = f.read()

meta_research_methods = """
    # --- Phase 45: Meta Research ---

    def save_meta_evidence_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_evidence_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_EVIDENCE_DIR / f"evidence_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_source_reliability(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_source_reliability(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RELIABILITY_DIR / f"reliability_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_consensus_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_consensus_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONSENSUS_DIR / f"consensus_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_conflict_report(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_conflict_report(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_CONFLICTS_DIR / f"conflicts_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_uncertainty_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_uncertainty_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_UNCERTAINTY_DIR / f"uncertainty_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_ensemble_table(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_ensemble_table(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_ENSEMBLE_DIR / f"ensemble_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str, df: pd.DataFrame) -> Path:
        if df.empty: return None
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        df.to_parquet(path, index=False)
        return path

    def load_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str) -> pd.DataFrame:
        path = self.paths.LAKE_META_RESEARCH_RANKINGS_DIR / f"ranking_{timeframe}_{profile_name}.parquet"
        if path.exists():
            return pd.read_parquet(path)
        return pd.DataFrame()

    def save_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str, snapshot: dict) -> Path:
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_symbol_snapshot(self, symbol: str, timeframe: str, profile_name: str) -> dict:
        path = self.paths.LAKE_META_RESEARCH_SNAPSHOTS_DIR / f"snapshot_{symbol}_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def save_meta_quality(self, timeframe: str, profile_name: str, quality: dict) -> Path:
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        with open(path, "w", encoding="utf-8") as f:
            import json
            json.dump(quality, f, indent=2, ensure_ascii=False)
        return path

    def load_meta_quality(self, timeframe: str, profile_name: str) -> dict:
        path = self.paths.LAKE_META_RESEARCH_QUALITY_DIR / f"quality_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def save_meta_research_report(self, timeframe: str, profile_name: str, report: dict, markdown: str | None = None) -> Path:
        json_path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            import json
            json.dump(report, f, indent=2, ensure_ascii=False)

        if markdown:
            md_path = self.paths.REPORTS_META_RESEARCH_MD_DIR / f"meta_research_{timeframe}_{profile_name}.md"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(markdown)

        return json_path

    def load_meta_research_report(self, timeframe: str, profile_name: str) -> dict:
        path = self.paths.LAKE_META_RESEARCH_REPORTS_DIR / f"report_{timeframe}_{profile_name}.json"
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                import json
                return json.load(f)
        return {}

    def list_meta_research_reports(self) -> pd.DataFrame:
        rows = []
        for p in self.paths.LAKE_META_RESEARCH_REPORTS_DIR.glob("report_*.json"):
            parts = p.stem.split("_", 2)
            if len(parts) >= 3:
                timeframe = parts[1]
                profile = parts[2]
                rows.append({
                    "timeframe": timeframe,
                    "profile": profile,
                    "path": str(p),
                    "size": p.stat().st_size
                })
        return pd.DataFrame(rows) if rows else pd.DataFrame(columns=["timeframe", "profile", "path", "size"])
"""
if "save_meta_evidence_table" not in content:
    content = content + meta_research_methods
    with open("commodity_fx_signal_bot/data/storage/data_lake.py", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/ml/feature_store.py", "r") as f:
    content = f.read()

meta_methods = """
    # Phase 45: Meta Research
    def load_meta_evidence_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_evidence_table(timeframe, profile)

    def load_meta_source_reliability(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_source_reliability(timeframe, profile)

    def load_meta_consensus_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_consensus_table(timeframe, profile)

    def load_meta_conflict_report(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_conflict_report(timeframe, profile)

    def load_meta_uncertainty_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_uncertainty_table(timeframe, profile)

    def load_meta_ensemble_table(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_ensemble_table(timeframe, profile)

    def load_meta_quality_adjusted_ranking(self, timeframe: str, profile_name: str | None = None) -> pd.DataFrame:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_quality_adjusted_ranking(timeframe, profile)

    def load_meta_symbol_snapshot(self, spec, timeframe: str, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_symbol_snapshot(spec.symbol, timeframe, profile)

    def load_meta_research_report(self, timeframe: str, profile_name: str | None = None) -> dict:
        profile = profile_name or "balanced_meta_research"
        return self.data_lake.load_meta_research_report(timeframe, profile)

    def list_available_meta_research_reports(self) -> dict:
        df = self.data_lake.list_meta_research_reports()
        if df.empty:
            return {}
        return df.to_dict(orient="records")
"""
if "load_meta_evidence_table" not in content:
    content = content + meta_methods
    with open("commodity_fx_signal_bot/ml/feature_store.py", "w") as f:
        f.write(content)

with open("commodity_fx_signal_bot/reports/report_builder.py", "r") as f:
    content = f.read()

meta_reports = """
# Phase 45: Meta Research

def _meta_disclaimer() -> str:
    return (
        "*** DISCLAIMER ***\\n"
        "Bu cikti offline meta-research/kanit agirliklandirma raporudur. "
        "Canli emir, broker talimati, gercek pozisyon, otomatik trade onayi veya "
        "yatirim tavsiyesi degildir. Yalnizca offline arastirma kanitlarini birlestirir.\\n"
    )

def build_meta_research_text_report(summary: dict, tables: dict[str, pd.DataFrame] | None = None) -> str:
    lines = [
        "META RESEARCH REPORT",
        "=" * 50,
        f"Timeframe: {summary.get('timeframe', 'Unknown')}",
        f"Processed Symbols: {summary.get('processed_symbols', 0)}",
        f"Sources Checked: {summary.get('sources_checked', 0)}",
        f"Quality Check Passed: {summary.get('quality_passed', False)}",
        "-" * 50,
        ""
    ]
    if tables and "consensus" in tables and not tables["consensus"].empty:
        lines.append("TOP CONSENSUS (first 20 rows):")
        lines.append(tables["consensus"].head(20).to_string(index=False))
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)

def build_meta_consensus_text_report(summary: dict, consensus_df: pd.DataFrame | None = None) -> str:
    lines = [
        "META CONSENSUS REPORT",
        "=" * 50,
        f"Timeframe: {summary.get('timeframe', 'Unknown')}",
        "-" * 50,
        ""
    ]
    if consensus_df is not None and not consensus_df.empty:
        lines.append(consensus_df.to_string(index=False))
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)

def build_evidence_conflict_text_report(summary: dict, conflict_df: pd.DataFrame | None = None) -> str:
    lines = [
        "EVIDENCE CONFLICT REPORT",
        "=" * 50,
        f"Total Major Conflicts: {summary.get('total_major_conflicts', 0)}",
        f"Avg Conflict Score: {summary.get('avg_conflict_score', 0.0):.3f}",
        "-" * 50,
        ""
    ]
    if conflict_df is not None and not conflict_df.empty:
        lines.append(conflict_df.to_string(index=False))
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)

def build_quality_adjusted_ranking_text_report(summary: dict, ranking_df: pd.DataFrame | None = None) -> str:
    lines = [
        "QUALITY ADJUSTED RANKING REPORT",
        "=" * 50,
        f"Ranked Symbols: {summary.get('ranked_symbols', 0)}",
        "-" * 50,
        ""
    ]
    if ranking_df is not None and not ranking_df.empty:
        lines.append(ranking_df.to_string(index=False))
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)

def build_meta_symbol_snapshot_text_report(summary: dict, snapshot: dict | None = None) -> str:
    lines = [
        f"META RESEARCH SNAPSHOT: {summary.get('symbol', 'UNKNOWN')}",
        "=" * 50,
    ]
    if snapshot:
        c = snapshot.get("consensus", {})
        lines.append(f"Consensus Score: {c.get('consensus_score')}")
        lines.append(f"Quality Adjusted Score: {snapshot.get('quality_adjusted_score')}")
        lines.append(f"Research Alignment: {snapshot.get('final_research_label')}")
        lines.append("-" * 50)
        lines.append("Evidence List:")
        for ev in snapshot.get("evidence", []):
            lines.append(f"  {ev.get('source_label')}: {ev.get('evidence_direction')} (score: {ev.get('normalized_score')})")
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)

def build_meta_research_status_report(status_df: pd.DataFrame, summary: dict) -> str:
    lines = [
        "META RESEARCH SYSTEM STATUS",
        "=" * 50,
        f"Total Reports: {len(status_df)}",
        "-" * 50,
        ""
    ]
    if not status_df.empty:
        lines.append(status_df.to_string(index=False))
        lines.append("")

    lines.append(_meta_disclaimer())
    return "\\n".join(lines)
"""
if "build_meta_research_text_report" not in content:
    content = content + meta_reports
    with open("commodity_fx_signal_bot/reports/report_builder.py", "w") as f:
        f.write(content)
