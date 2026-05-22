import pandas as pd
import logging
from synthetic_indices.index_config import SyntheticIndexProfile
from synthetic_indices.index_models import SyntheticIndexDefinition, SyntheticIndexSeries

logger = logging.getLogger(__name__)

FORBIDDEN_TERMS = [
    "AL", "SAT", "BUY", "SELL", "OPEN_LONG", "OPEN_SHORT",
    "EMİR GÖNDER", "POZİSYON AÇ", "POZİSYON KAPAT", "GERÇEK EMİR",
    "BROKER ORDER", "LIVE ORDER"
]

def check_index_definition_quality(definition: SyntheticIndexDefinition, profile: SyntheticIndexProfile) -> dict:
    warnings = []

    if len(definition.symbols) < profile.min_symbols:
        warnings.append(f"Definition symbols {len(definition.symbols)} < {profile.min_symbols}")

    for sym, weight in definition.weights.items():
        if weight > profile.max_single_weight:
            warnings.append(f"Weight {weight} for {sym} > {profile.max_single_weight}")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_index_series_quality(series: SyntheticIndexSeries, profile: SyntheticIndexProfile) -> dict:
    warnings = []

    if series.observation_count < profile.min_observations:
        warnings.append(f"Series observations {series.observation_count} < {profile.min_observations}")

    if series.level_series.empty:
        warnings.append("Level series is empty")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_relative_strength_quality(rs_df: pd.DataFrame) -> dict:
    warnings = []
    if rs_df.empty:
        warnings.append("Relative strength dataframe is empty")
    elif "relative_strength_label" not in rs_df.columns:
         warnings.append("Missing relative_strength_label")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_rotation_quality(rotation_df: pd.DataFrame) -> dict:
    warnings = []
    if rotation_df.empty:
        warnings.append("Rotation dataframe is empty")
    elif "rotation_label" not in rotation_df.columns:
         warnings.append("Missing rotation_label")

    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_benchmark_comparison_quality(comparison_df: pd.DataFrame) -> dict:
    warnings = []
    if comparison_df.empty:
        warnings.append("Benchmark comparison dataframe is empty")
    return {"passed": len(warnings) == 0, "warnings": warnings}

def check_for_forbidden_trade_terms_in_synthetic_indices(text: str | None = None, df: pd.DataFrame | None = None, summary: dict | None = None) -> dict:
    found = []

    def search_text(s: str):
        s_upper = s.upper()
        for term in FORBIDDEN_TERMS:
            if term in s_upper:
                found.append(term)

    if text:
        search_text(text)

    if summary:
        search_text(str(summary))

    if df is not None and not df.empty:
        # Check string columns
        str_cols = df.select_dtypes(include=['object']).columns
        for col in str_cols:
            for val in df[col].dropna():
                search_text(str(val))

    unique_found = list(set(found))
    return {
        "passed": len(unique_found) == 0,
        "forbidden_trade_terms_found": unique_found
    }

def build_synthetic_index_quality_report(
    summary: dict,
    definitions: list[SyntheticIndexDefinition] | None = None,
    index_series_map: dict[str, SyntheticIndexSeries] | None = None,
    rs_df: pd.DataFrame | None = None,
    rotation_df: pd.DataFrame | None = None,
    profile: SyntheticIndexProfile | None = None
) -> dict:

    quality = {
        "definitions_valid": True,
        "series_valid": True,
        "relative_strength_valid": True,
        "rotation_valid": True,
        "benchmark_comparison_valid": True, # Hardcoded True if not passed, assuming we'd check if provided
        "disclaimer_required": True,
        "forbidden_trade_terms_found": [],
        "warning_count": 0,
        "passed": True,
        "warnings": []
    }

    if profile:
        if definitions:
            for d in definitions:
                res = check_index_definition_quality(d, profile)
                if not res["passed"]:
                    quality["definitions_valid"] = False
                    quality["warnings"].extend(res["warnings"])

        if index_series_map:
            for s in index_series_map.values():
                res = check_index_series_quality(s, profile)
                if not res["passed"]:
                    quality["series_valid"] = False
                    quality["warnings"].extend(res["warnings"])

    if rs_df is not None:
        res = check_relative_strength_quality(rs_df)
        if not res["passed"]:
            quality["relative_strength_valid"] = False
            quality["warnings"].extend(res["warnings"])

    if rotation_df is not None:
        res = check_rotation_quality(rotation_df)
        if not res["passed"]:
            quality["rotation_valid"] = False
            quality["warnings"].extend(res["warnings"])

    term_res = check_for_forbidden_trade_terms_in_synthetic_indices(summary=summary, df=rs_df)
    if not term_res["passed"]:
         quality["forbidden_trade_terms_found"] = term_res["forbidden_trade_terms_found"]
         quality["passed"] = False
         quality["warnings"].append(f"Forbidden terms found: {term_res['forbidden_trade_terms_found']}")

    if rotation_df is not None:
         term_res2 = check_for_forbidden_trade_terms_in_synthetic_indices(df=rotation_df)
         if not term_res2["passed"]:
             quality["forbidden_trade_terms_found"].extend(term_res2["forbidden_trade_terms_found"])
             quality["passed"] = False

    quality["forbidden_trade_terms_found"] = list(set(quality["forbidden_trade_terms_found"]))
    quality["warning_count"] = len(quality["warnings"])

    # If there are any critical quality issues, we might mark overall passed = False
    if not quality["definitions_valid"] or not quality["series_valid"]:
        quality["passed"] = False

    return quality
