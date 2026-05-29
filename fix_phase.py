with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "r") as f:
    content = f.read()

new_section = """
### Phase 58: Local Analyst UX, Command Aliases, and Productivity
- Analyst UX profile sistemi eklendi.
- UX label registry eklendi.
- CommandAlias, AnalystIntent, SafeCommandSuggestion, PromptPack ve AnalystTask modelleri eklendi.
- Command alias registry eklendi.
- Rule-based intent classifier eklendi.
- Natural-language-to-safe-command mapping eklendi.
- Prompt packs eklendi.
- Workflow shortcuts eklendi.
- Query-to-runbook/workflow/docs mapping eklendi.
- Analyst task board eklendi.
- Cheat sheets eklendi.
- Productivity checklist eklendi.
- UX validation ve UX quality report eklendi.
- AnalystUXPipeline eklendi.
- DataLake analyst UX kayıt desteği aldı.
- Analyst UX scriptleri eklendi.
- Testler genişletildi.
"""

content = content + "\n" + new_section

with open("commodity_fx_signal_bot/docs/PHASE_LOG.md", "w") as f:
    f.write(content)
