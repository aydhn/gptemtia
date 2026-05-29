with open("commodity_fx_signal_bot/README.md", "r") as f:
    content = f.read()

new_section = """
## Local Analyst UX and Operator Productivity (Phase 58)

The Analyst UX layer improves the daily operational workflow for offline researchers and Codex agents.

- Analyst UX katmanı canlı trading assistant değildir.
- Natural-language-to-safe-command mapping komut çalıştırmaz, sadece güvenli offline öneri üretir.
- Command alias canlı emir alias'ı değildir.
- Prompt pack'ler Codex ajanına güvenli offline geliştirme yönergesi vermek içindir.
- Task board yatırım veya trading task board değildir.
- Query mapping internet araması yapmaz; local docs/runbook/command reference önerir.
- Çıktılar data/lake/analyst_ux ve reports/output/analyst_ux altında oluşur.

Available Commands:
```bash
python -m scripts.run_ux_alias_report
python -m scripts.run_safe_command_suggestions --query "final review durumunu kontrol et"
python -m scripts.run_prompt_pack_report
python -m scripts.run_productivity_checklist
python -m scripts.run_analyst_task_board
python -m scripts.run_operator_productivity_status
```
"""

content = content + "\n" + new_section

with open("commodity_fx_signal_bot/README.md", "w") as f:
    f.write(content)
