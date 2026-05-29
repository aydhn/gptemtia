with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "r") as f:
    content = f.read()

new_section = """
## Analyst UX and Operator Productivity Flow (Phase 58)

Command Center / Documentation / Scenario Regression / Quality Gates / Final Review
-> CommandAliases
-> IntentClassifier
-> SafeCommandMapper
-> PromptPacks
-> WorkflowShortcuts
-> QueryMapping
-> AnalystTaskBoard
-> CheatSheets
-> ProductivityChecklist
-> UXValidation
-> UXQuality
-> Analyst UX Reports
"""

content = content + "\n" + new_section

with open("commodity_fx_signal_bot/docs/ARCHITECTURE.md", "w") as f:
    f.write(content)
