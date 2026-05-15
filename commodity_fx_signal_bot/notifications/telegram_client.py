import requests
import logging

logger = logging.getLogger(__name__)

class TelegramClient:
    def __init__(
        self,
        bot_token: str | None,
        chat_id: str | None,
        parse_mode: str = "HTML",
        disable_web_page_preview: bool = True,
        timeout_seconds: int = 15,
    ):
        self._bot_token = bot_token
        self._chat_id = chat_id
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview
        self.timeout_seconds = timeout_seconds

    def is_configured(self) -> bool:
        return bool(self._bot_token) and bool(self._chat_id)

    def get_safe_destination_label(self) -> str:
        if not self._chat_id:
            return "not_configured"
        # Mask chat id if it's very long, or just return basic
        # E.g. -100123456789 -> -1001******89
        if len(self._chat_id) > 6:
            return f"{self._chat_id[:4]}...{self._chat_id[-2:]}"
        return "***MASKED_CHAT_ID***"

    def send_message(self, text: str) -> dict:
        if not self.is_configured():
            return {
                "success": False,
                "status": "delivery_not_configured",
                "error_message": "Telegram bot token or chat ID is missing."
            }

        url = f"https://api.telegram.org/bot{self._bot_token}/sendMessage"
        payload = {
            "chat_id": self._chat_id,
            "text": text,
            "parse_mode": self.parse_mode,
            "disable_web_page_preview": self.disable_web_page_preview
        }

        try:
            response = requests.post(url, json=payload, timeout=self.timeout_seconds)
            response_data = response.json()

            if response.status_code == 200 and response_data.get("ok"):
                return {
                    "success": True,
                    "status": "delivery_sent",
                    "response": {"message_id": response_data.get("result", {}).get("message_id")}
                }
            elif response.status_code == 429: # Rate limit
                return {
                    "success": False,
                    "status": "delivery_rate_limited",
                    "error_message": f"Rate limited. Response: {response_data.get('description')}",
                    "response": {"error_code": response.status_code}
                }
            else:
                return {
                    "success": False,
                    "status": "delivery_failed",
                    "error_message": f"Telegram API Error: {response_data.get('description')}",
                    "response": {"error_code": response.status_code}
                }
        except requests.exceptions.RequestException as e:
            logger.error("Telegram API Request Error. Masking details for security.")
            return {
                "success": False,
                "status": "delivery_failed",
                "error_message": f"Request failed: {type(e).__name__}"
            }
