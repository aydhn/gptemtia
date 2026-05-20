def list_dx_status_labels() -> list[str]:
    return ["dx_passed", "dx_warning", "dx_failed", "dx_unknown"]

def list_dx_category_labels() -> list[str]:
    return [
        "package_metadata",
        "cli_help",
        "import_smoke",
        "test_matrix",
        "repo_hygiene",
        "docs_quality",
        "troubleshooting",
        "maintenance",
        "local_runbook",
        "unknown_dx_category",
    ]

def list_cli_command_group_labels() -> list[str]:
    return [
        "data",
        "features",
        "candidates",
        "risk_sizing_level",
        "backtest",
        "performance",
        "validation",
        "ml",
        "paper",
        "notifications",
        "orchestration",
        "observability",
        "security",
        "devtools",
        "unknown_group",
    ]

def validate_dx_status(label: str) -> None:
    if label not in list_dx_status_labels():
        raise ValueError(f"Invalid DX status label: {label}")

def validate_dx_category(label: str) -> None:
    if label not in list_dx_category_labels():
        raise ValueError(f"Invalid DX category label: {label}")

def validate_cli_command_group(label: str) -> None:
    if label not in list_cli_command_group_labels():
        raise ValueError(f"Invalid CLI command group label: {label}")

def is_failed_dx_status(label: str) -> bool:
    return label == "dx_failed"
