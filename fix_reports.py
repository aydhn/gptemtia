file_path = "commodity_fx_signal_bot/reports/report_builder.py"
with open(file_path, "r") as f:
    content = f.read()

# Fix broken newlines
content = content.replace('lines.append("\nUyarılar:")', 'lines.append("\\nUyarılar:")')
content = content.replace('lines.append("\nUyarı: Rejimler', 'lines.append("\\nUyarı: Rejimler')
content = content.replace('lines.append("\nSon Satırlar:")', 'lines.append("\\nSon Satırlar:")')
content = content.replace('return "\n".join(lines)', 'return "\\n".join(lines)')
content = content.replace('lines.append(f"\nNot:', 'lines.append(f"\\nNot:')
content = content.replace('lines.append("\nSon Satırlar (Olaylar):")', 'lines.append("\\nSon Satırlar (Olaylar):")')
content = content.replace('lines.append(f"\nRejimi Eksik Olanlar', 'lines.append(f"\\nRejimi Eksik Olanlar')

# To be safe, we'll just rewrite the whole new functions
