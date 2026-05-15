from notifications.notification_config import NotificationProfile
from notifications.notification_models import NotificationMessage, sanitize_sensitive_text

class MessageFormatter:
    def __init__(self, profile: NotificationProfile):
        self.profile = profile

    def format_message(self, message: NotificationMessage) -> str:
        text = f"{message.title}\n\n{message.body}"
        return self.escape_text(sanitize_sensitive_text(text))

    def split_message(self, text: str) -> list[str]:
        max_chars = self.profile.message_max_chars
        if len(text) <= max_chars:
            return [text]

        parts = []
        current_part = ""
        lines = text.split("\n")

        for line in lines:
            if len(current_part) + len(line) + 1 > max_chars:
                if current_part:
                    parts.append(current_part)
                current_part = line + "\n"
            else:
                current_part += line + "\n"

        if current_part:
            parts.append(current_part)

        # Add part indicators
        total_parts = len(parts)
        for i in range(total_parts):
            parts[i] = f"[Parça {i+1}/{total_parts}]\n" + parts[i]

        return parts

    def escape_text(self, text: str) -> str:
        if self.profile.parse_mode == "HTML":
            # For Telegram HTML, replace <, >, & outside of tags
            # A simple approach for this context since we explicitly build tags
            text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            # Restore our specific valid tags (b, i, code)
            text = text.replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
            text = text.replace("&lt;i&gt;", "<i>").replace("&lt;/i&gt;", "</i>")
            text = text.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")
            return text
        return text

    def truncate_text(self, text: str, max_chars: int | None = None) -> str:
        limit = max_chars if max_chars else self.profile.message_max_chars
        if len(text) > limit:
            return text[:limit - 3] + "..."
        return text
