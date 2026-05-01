import pandas as pd
from mtf.mtf_config import MTFProfile
from mtf.timeframe_alignment import merge_aligned_contexts


class MTFFeatureJoiner:
    def __init__(self, profile: MTFProfile):
        self.profile = profile

    def join_feature_sets_for_timeframe(
        self,
        frames_by_feature_set: dict[str, pd.DataFrame],
        timeframe: str,
    ) -> tuple[pd.DataFrame, dict]:
        summary = {"missing": []}
        joined_df = pd.DataFrame()

        for fset_name, df in frames_by_feature_set.items():
            if joined_df.empty:
                joined_df = df.copy()
            else:
                # Merge on index
                cols_to_use = df.columns.difference(joined_df.columns)
                if not cols_to_use.empty:
                    joined_df = joined_df.join(df[cols_to_use], how="outer")

        return joined_df.sort_index(), summary

    def build_mtf_frame(
        self,
        base_df: pd.DataFrame,
        context_feature_frames: dict[str, dict[str, pd.DataFrame]],
    ) -> tuple[pd.DataFrame, dict]:

        summary = {
            "input_timeframes": list(context_feature_frames.keys()),
            "input_feature_sets": self.profile.feature_sets,
            "warnings": [],
        }

        # 1. Join sets per timeframe
        merged_contexts = {}
        for tf, sets in context_feature_frames.items():
            df, join_summ = self.join_feature_sets_for_timeframe(sets, tf)
            if not df.empty:
                merged_contexts[tf] = df

        # 2. Align to base
        mtf_df, align_summ = merge_aligned_contexts(
            base_df,
            merged_contexts,
            self.profile.base_timeframe,
            forward_fill=self.profile.forward_fill_context,
            strict_no_lookahead=self.profile.strict_no_lookahead,
            max_context_age_bars=self.profile.max_context_age_bars,
        )

        summary["output_rows"] = len(mtf_df)
        summary["output_columns"] = len(mtf_df.columns)
        summary["warnings"].extend(align_summ.get("warnings", []))

        return mtf_df, summary

    def validate_joined_frame(self, df: pd.DataFrame) -> dict:
        return {"valid": True}
