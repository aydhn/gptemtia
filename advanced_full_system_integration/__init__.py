# -*- coding: utf-8 -*-
"""Phase 158: Full-System Integration and Advanced Acceptance Rehearsal Package.

Provides local/offline system-wide integration registries, acceptance rehearsal checklists,
strict non-production safety boundaries, and Phase 159 handoff structures.
"""

from .full_system_integration_config import (
    FullSystemIntegrationProfile,
    get_full_system_integration_profile,
    get_default_full_system_integration_profile,
    list_full_system_integration_profiles,
    validate_full_system_integration_profiles,
)
from .full_system_integration_pipeline import (
    FullSystemIntegrationPipeline,
)

__all__ = [
    "FullSystemIntegrationProfile",
    "get_full_system_integration_profile",
    "get_default_full_system_integration_profile",
    "list_full_system_integration_profiles",
    "validate_full_system_integration_profiles",
    "FullSystemIntegrationPipeline",
]
