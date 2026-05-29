import os

guides = ["docs/USER_GUIDE.md", "docs/OPERATOR_MANUAL.md", "docs/CODEX_AGENT_GUIDE.md", "docs/SAFE_COMMAND_REFERENCE.md"]

new_section = """
### Local Analyst UX & Operator Productivity (Phase 58)
- **Command Aliases:** How to read aliases (`alias_name` maps to a safe offline `command`).
- **Safe Command Suggestions:** When you ask "how to check status", the system suggests offline commands. These are NEVER executed automatically.
- **Natural Language Mapping:** Queries map to local offline documentation and runbooks. No web search is performed.
- **Prompt Packs:** Pre-packaged safe instructions to give to Codex agents.
- **Task Board:** An offline checklist of pending system validations. NOT a trading or investment task board.
- **Safety:** It is strictly prohibited to execute live trades, broker commands, real portfolio actions, or receive investment advice via these tools.
"""

for guide in guides:
    path = f"commodity_fx_signal_bot/{guide}"
    if os.path.exists(path):
        with open(path, "a") as f:
            f.write("\n" + new_section + "\n")
