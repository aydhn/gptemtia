from local_post_completion_preservation.preservation_config import LocalPostCompletionPreservationProfile

def build_preservation_restore_note_sections(profile: LocalPostCompletionPreservationProfile) -> list[dict]:
    return [{"title": "Note", "content": "Gercek restore/rollback talimati degildir; local/offline okuma notudur."}]

def build_preservation_restore_notes_rehearsal(profile: LocalPostCompletionPreservationProfile) -> tuple[str, dict]:
    return "Gercek restore/rollback talimati degildir; local/offline okuma notudur.", {"len": 1}

def summarize_preservation_restore_notes(text: str) -> dict:
    return {"len": len(text)}
