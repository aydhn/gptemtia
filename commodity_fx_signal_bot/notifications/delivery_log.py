import pandas as pd
from notifications.notification_models import NotificationMessage, DeliveryResult, notification_message_to_dict, delivery_result_to_dict

class DeliveryLog:
    def __init__(self):
        self.records = []

    def add_message(self, message: NotificationMessage) -> None:
        # Keeping track of messages if needed for full log
        pass

    def add_delivery_results(self, results: list[DeliveryResult]) -> None:
        for r in results:
            self.records.append(delivery_result_to_dict(r))

    def to_dataframe(self) -> pd.DataFrame:
        if not self.records:
            return pd.DataFrame()
        return pd.DataFrame(self.records)

    def summarize(self) -> dict:
        if not self.records:
            return {}

        df = pd.DataFrame(self.records)
        summary = {
            "total_parts": len(df),
            "dry_run_count": len(df[df["dry_run"] == True]),
            "sent_count": len(df[df["delivery_status"] == "delivery_sent"]),
            "failed_count": len(df[df["delivery_status"] == "delivery_failed"]),
            "skipped_count": len(df[df["delivery_status"] == "delivery_skipped"]),
            "not_configured_count": len(df[df["delivery_status"] == "delivery_not_configured"]),
            "by_status": df["delivery_status"].value_counts().to_dict() if "delivery_status" in df else {}
        }
        return summary

def build_delivery_audit(log_df: pd.DataFrame) -> dict:
    if log_df is None or log_df.empty:
        return {}

    return {
        "total_messages": len(log_df),
        "statuses": log_df["delivery_status"].value_counts().to_dict() if "delivery_status" in log_df else {}
    }
