def update_report_builder():
    file_path = "reports/report_builder.py"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    imports_insertion = """
from local_maintenance.maintenance_report_builder import (
    build_maintenance_domain_registry_markdown_report,
    build_periodic_review_calendar_markdown_report,
    build_refresh_cadence_markdown_report,
    build_dependency_aging_markdown_report,
    build_sustainability_markdown_report,
    build_maintenance_quality_markdown_report,
    build_maintenance_status_markdown_report,
    build_maintenance_disclaimer
)
"""
    if "from local_maintenance.maintenance_report_builder" not in content:
        # Find imports and add
        idx = content.find("import pandas")
        if idx != -1:
            content = content[:idx] + imports_insertion + content[idx:]

    new_methods = """
    # --- Local Maintenance Text Reports ---
    def build_maintenance_domain_registry_text_report(self, summary: Dict[str, Any], domain_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["MAINTENANCE DOMAIN REGISTRY"]
        lines.append(build_maintenance_disclaimer())
        lines.append(f"Total Domains: {summary.get('total_domains', 0)}")
        if domain_df is not None and not domain_df.empty:
            lines.append(domain_df.to_string(index=False))
        return "\\n".join(lines)

    def build_periodic_review_calendar_text_report(self, summary: Dict[str, Any], calendar_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["PERIODIC REVIEW CALENDAR"]
        lines.append(build_maintenance_disclaimer())
        lines.append(f"Total Items: {summary.get('total_items', 0)}")
        if calendar_df is not None and not calendar_df.empty:
            lines.append(calendar_df.to_string(index=False))
        return "\\n".join(lines)

    def build_refresh_cadence_text_report(self, summary: Dict[str, Any], cadence_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["REFRESH CADENCE REGISTRY"]
        lines.append(build_maintenance_disclaimer())
        lines.append(f"Total Items: {summary.get('total_cadence_items', 0)}")
        if cadence_df is not None and not cadence_df.empty:
            lines.append(cadence_df.to_string(index=False))
        return "\\n".join(lines)

    def build_dependency_aging_text_report(self, summary: Dict[str, Any], dep_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["DEPENDENCY AGING WATCH"]
        lines.append(build_maintenance_disclaimer())
        lines.append(f"Total Dependencies: {summary.get('total_dependencies', 0)}")
        if dep_df is not None and not dep_df.empty:
            lines.append(dep_df.to_string(index=False))
        return "\\n".join(lines)

    def build_maintenance_sustainability_text_report(self, summary: Dict[str, Any], score_df: Optional[pd.DataFrame] = None, risk_df: Optional[pd.DataFrame] = None) -> str:
        lines = ["PROJECT SUSTAINABILITY REPORT"]
        lines.append(build_maintenance_disclaimer())
        if score_df is not None and not score_df.empty:
            lines.append("Score:")
            lines.append(score_df.to_string(index=False))
        if risk_df is not None and not risk_df.empty:
            lines.append("Risks:")
            lines.append(risk_df.to_string(index=False))
        return "\\n".join(lines)

    def build_maintenance_quality_text_report(self, summary: Dict[str, Any], quality: Optional[Dict[str, Any]] = None) -> str:
        lines = ["MAINTENANCE QUALITY REPORT"]
        lines.append(build_maintenance_disclaimer())
        if quality:
            lines.append(f"Passed: {quality.get('passed', False)}")
            for k, v in quality.get('checks', {}).items():
                lines.append(f" - {k}: {v}")
        return "\\n".join(lines)

    def build_maintenance_status_report(self, status_df: pd.DataFrame, summary: Dict[str, Any]) -> str:
        lines = ["MAINTENANCE STATUS REPORT"]
        lines.append(build_maintenance_disclaimer())
        lines.append(f"Total Files: {summary.get('total_files', 0)}")
        if status_df is not None and not status_df.empty:
            lines.append(status_df.to_string(index=False))
        return "\\n".join(lines)
"""
    if "def build_maintenance_domain_registry_text_report" not in content:
        content = content + "\n" + new_methods + "\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

update_report_builder()
