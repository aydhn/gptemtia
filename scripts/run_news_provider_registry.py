import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news provider registry script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    meta_and_caps, _ = pipeline.build_news_provider_metadata_and_capabilities(save=False)
    reg_and_res, _ = pipeline.build_news_registry_and_resolver(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    meta_and_caps["metadata"].to_csv(out_dir / "csv/news_provider_metadata.csv", index=False)
    reg_and_res["registry"].to_csv(out_dir / "csv/news_provider_registry.csv", index=False)
    reg_and_res["resolver"].to_csv(out_dir / "csv/news_resolver_map.csv", index=False)
    reg_and_res["preferences"].to_csv(out_dir / "csv/news_preference_resolver.csv", index=False)
    reg_and_res["matcher"].to_csv(out_dir / "csv/news_capability_matcher.csv", index=False)
    
    with open(out_dir / "txt/news_provider_registry_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Provider Registry generated successfully.\n")
    with open(out_dir / "markdown/news_provider_registry_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Provider Registry\n\nRegistered news providers and capability mappings.\n")
    print("Done news provider registry script.")

if __name__ == "__main__":
    main()
