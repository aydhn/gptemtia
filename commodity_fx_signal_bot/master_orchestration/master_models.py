"""
Master orchestration data models.
"""

from dataclasses import dataclass, asdict

@dataclass
class OrchestrationLayer:
    layer_id: str
    layer_name: str
    layer_type: str
    description: str
    modules: list[str]
    primary_scripts: list[str]
    output_roots: list[str]
    depends_on_layers: list[str]
    warnings: list[str]

@dataclass
class MasterCommand:
    command_id: str
    command_name: str
    command: str
    module_name: str
    operating_modes: list[str]
    safety_label: str
    dry_run: bool
    expected_outputs: list[str]
    depends_on_commands: list[str]
    warnings: list[str]

@dataclass
class MasterRunPlan:
    plan_id: str
    plan_name: str
    operating_mode: str
    dry_run: bool
    commands: list[str]
    blocked_commands: list[str]
    expected_outputs: list[str]
    run_order_notes: list[str]
    warnings: list[str]

@dataclass
class OperationalPlaybookSection:
    section_id: str
    title: str
    audience: str
    purpose: str
    steps: list[dict]
    related_modes: list[str]
    related_commands: list[str]
    warnings: list[str]

@dataclass
class PhaseConsolidationItem:
    phase_number: int
    phase_title: str
    expected_layer: str
    module_or_output: str
    status: str
    evidence_paths: list[str]
    warnings: list[str]

def build_layer_id(layer_name: str, layer_type: str) -> str:
    clean_name = layer_name.lower().replace(" ", "_")
    return f"layer_{clean_name}_{layer_type}"

def build_master_command_id(command_name: str, module_name: str) -> str:
    clean_name = command_name.lower().replace(" ", "_").replace("-", "_")
    return f"cmd_{module_name}_{clean_name}"

def build_master_run_plan_id(plan_name: str, operating_mode: str) -> str:
    clean_name = plan_name.lower().replace(" ", "_")
    return f"plan_{operating_mode}_{clean_name}"

def build_playbook_section_id(title: str, audience: str) -> str:
    clean_title = title.lower().replace(" ", "_").replace("-", "_")
    return f"sec_{audience}_{clean_title}"

def build_phase_consolidation_id(phase_number: int, phase_title: str) -> str:
    clean_title = phase_title.lower().replace(" ", "_").replace("-", "_")
    return f"phase_{phase_number:02d}_{clean_title}"

def orchestration_layer_to_dict(layer: OrchestrationLayer) -> dict:
    return asdict(layer)

def master_command_to_dict(command: MasterCommand) -> dict:
    return asdict(command)

def master_run_plan_to_dict(plan: MasterRunPlan) -> dict:
    return asdict(plan)

def operational_playbook_section_to_dict(section: OperationalPlaybookSection) -> dict:
    return asdict(section)

def phase_consolidation_item_to_dict(item: PhaseConsolidationItem) -> dict:
    return asdict(item)
