def list_reuse_domain_labels() -> list[str]:
    return ["audit_memory_domain"]


def list_template_labels() -> list[str]:
    return ["reusable_prompt_template"]


def list_reuse_status_labels() -> list[str]:
    return ["reuse_ready_for_rehearsal"]


def list_v1_1_seed_status_labels() -> list[str]:
    return ["v1_1_seed_candidate"]


def list_reuse_risk_labels() -> list[str]:
    return ["reuse_info"]


def validate_reuse_domain_label(label: str) -> None:
    if label not in list_reuse_domain_labels():
        raise ValueError(f"Invalid reuse domain label: {label}")


def validate_template_label(label: str) -> None:
    if label not in list_template_labels():
        raise ValueError(f"Invalid template label: {label}")


def validate_reuse_status(label: str) -> None:
    if label not in list_reuse_status_labels():
        raise ValueError(f"Invalid reuse status label: {label}")


def validate_v1_1_seed_status(label: str) -> None:
    if label not in list_v1_1_seed_status_labels():
        raise ValueError(f"Invalid v1_1 seed status label: {label}")


def validate_reuse_risk(label: str) -> None:
    if label not in list_reuse_risk_labels():
        raise ValueError(f"Invalid reuse risk label: {label}")
