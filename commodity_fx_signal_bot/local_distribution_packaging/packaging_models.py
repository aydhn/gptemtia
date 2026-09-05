from dataclasses import dataclass, asdict

@dataclass
class PackagingDomain:
    domain_id: str
    domain_label: str
    domain_name: str
    description: str
    required_outputs: list[str]
    warnings: list[str]

@dataclass
class DistributionBundleItem:
    bundle_id: str
    item_name: str
    source_ref: str
    bundle_area: str
    artifact_label: str
    include_rehearsal: bool
    exclusion_reason: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class PortableDocsItem:
    portable_doc_id: str
    doc_title: str
    source_ref: str
    route_label: str
    reading_priority: int
    artifact_label: str
    warnings: list[str]

@dataclass
class ReleaseFolderItem:
    folder_item_id: str
    folder_area: str
    folder_path: str
    intended_contents: list[str]
    artifact_label: str
    manual_review_required: bool
    warnings: list[str]

@dataclass
class ZipMapItem:
    zip_map_id: str
    map_area: str
    folder_ref: str
    file_ref: str
    compression_status: str
    boundary_note: str
    warnings: list[str]

@dataclass
class PackagingFinding:
    finding_id: str
    risk_label: str
    title: str
    description: str
    recommendation: str
    manual_review_required: bool
    warnings: list[str]

def build_packaging_domain_id(domain_label: str) -> str:
    return f"dom_{domain_label}"

def build_distribution_bundle_item_id(item_name: str, source_ref: str) -> str:
    return f"bnd_{hash(item_name + source_ref)}"

def build_portable_docs_item_id(doc_title: str, source_ref: str) -> str:
    return f"pdoc_{hash(doc_title + source_ref)}"

def build_release_folder_item_id(folder_area: str, folder_path: str) -> str:
    return f"rfld_{hash(folder_area + folder_path)}"

def build_zip_map_item_id(folder_ref: str, file_ref: str) -> str:
    return f"zmap_{hash(folder_ref + file_ref)}"

def build_packaging_finding_id(title: str) -> str:
    return f"fnd_{hash(title)}"

def packaging_domain_to_dict(item: PackagingDomain) -> dict:
    return asdict(item)

def distribution_bundle_item_to_dict(item: DistributionBundleItem) -> dict:
    return asdict(item)

def portable_docs_item_to_dict(item: PortableDocsItem) -> dict:
    return asdict(item)

def release_folder_item_to_dict(item: ReleaseFolderItem) -> dict:
    return asdict(item)

def zip_map_item_to_dict(item: ZipMapItem) -> dict:
    return asdict(item)

def packaging_finding_to_dict(item: PackagingFinding) -> dict:
    return asdict(item)
