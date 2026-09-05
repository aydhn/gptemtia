import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline
from advanced_news_metadata.news_scoring import build_news_readiness_score_report
from advanced_news_metadata.news_report_builder import build_phase_112_handoff_markdown_report

def main():
    print("Running news provider health check script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    health_df, health_summary = pipeline.build_news_health_check(save=False)
    
    profiles, _ = pipeline.build_news_profiles_and_domains(save=False)
    sources, _ = pipeline.build_news_sources_and_schemas(save=False)
    caps, _ = pipeline.build_news_provider_metadata_and_capabilities(save=False)
    regs, _ = pipeline.build_news_registry_and_resolver(save=False)
    contracts, _ = pipeline.build_news_contracts(save=False)
    
    score_df, score_summary = build_news_readiness_score_report(
        profiles["profiles"], profiles["domains"], sources["sources"],
        sources["metadata_schema"], caps["capabilities"], regs["registry"],
        contracts["safety"], health_df, pipeline.profile
    )
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    health_df.to_csv(out_dir / "csv/news_health_check.csv", index=False)
    score_df.to_csv(out_dir / "csv/news_readiness_score.csv", index=False)
    
    with open(out_dir / "txt/news_health_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Health Check executed successfully.\n")
    with open(out_dir / "markdown/phase_112_handoff.md", "w", encoding="utf-8") as f:
        f.write(build_phase_112_handoff_markdown_report(score_summary))
    print("Done news provider health check script.")

if __name__ == "__main__":
    main()
