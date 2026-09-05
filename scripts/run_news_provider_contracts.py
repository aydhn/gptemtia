import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from advanced_news_metadata.news_pipeline import NewsMetadataPipeline

def main():
    print("Running news provider contracts script...")
    pipeline = NewsMetadataPipeline(None, None, Path("."))
    req_res_schemas, _ = pipeline.build_news_request_response_schemas(save=False)
    contracts, _ = pipeline.build_news_contracts(save=False)
    
    out_dir = Path("reports/output/advanced_news_metadata")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "csv").mkdir(parents=True, exist_ok=True)
    (out_dir / "markdown").mkdir(parents=True, exist_ok=True)
    (out_dir / "txt").mkdir(parents=True, exist_ok=True)
    
    req_res_schemas["request_schema"].to_csv(out_dir / "csv/news_request_schema.csv", index=False)
    req_res_schemas["response_schema"].to_csv(out_dir / "csv/news_response_schema.csv", index=False)
    req_res_schemas["error_schema"].to_csv(out_dir / "csv/news_error_schema.csv", index=False)
    contracts["interface"].to_csv(out_dir / "csv/news_interface_contract.csv", index=False)
    contracts["adapter"].to_csv(out_dir / "csv/news_adapter_contract.csv", index=False)
    contracts["output_validation"].to_csv(out_dir / "csv/news_output_validation_contract.csv", index=False)
    contracts["safety"].to_csv(out_dir / "csv/news_safety_boundary.csv", index=False)
    
    with open(out_dir / "txt/news_provider_contracts_summary.txt", "w", encoding="utf-8") as f:
        f.write("Phase 111 News Provider Contracts generated successfully.\n")
    with open(out_dir / "markdown/news_provider_contracts_summary.md", "w", encoding="utf-8") as f:
        f.write("# Phase 111 News Provider Contracts\n\nNo scraping; no copyrighted content ingestion.\n")
    print("Done news provider contracts script.")

if __name__ == "__main__":
    main()
