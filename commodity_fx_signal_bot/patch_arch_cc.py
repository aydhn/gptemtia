import re

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

cc_arch = """
## Phase 50: Offline Analyst Command Center

The Command Center provides guided orchestration and safe runbooks for offline research capabilities:

All Offline Modules / Scripts / Reports / DataLake / Knowledge Base
-> CommandRegistry
-> CommandSafety
-> WorkflowRegistry
-> RunbookRegistry
-> DryRunPlanner
-> InteractiveQueryFlows
-> ProjectStatus
-> ModuleHealth
-> ScriptDiscovery
-> PhaseCoverage
-> Consolidation
-> Onboarding
-> Troubleshooting
-> CommandQuality
-> Offline Analyst Command Center Reports
"""

content = content + "\n\n" + cc_arch

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
    f.write(content)
