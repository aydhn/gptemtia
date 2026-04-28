import pytest
from pathlib import Path
import pandas as pd
from datetime import datetime, timezone
from data.storage.download_journal import DownloadJournal, DownloadJournalEntry


@pytest.fixture
def journal_path(tmp_path):
    return tmp_path / "journal.csv"


@pytest.fixture
def journal(journal_path):
    return DownloadJournal(journal_path)


@pytest.fixture
def sample_entry():
    return DownloadJournalEntry(
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        symbol="GC=F",
        requested_symbol="GC=F",
        resolved_symbol="GC=F",
        asset_class="metals",
        timeframe="1d",
        provider_interval="1d",
        period="2y",
        start=None,
        end=None,
        success=True,
        rows=500,
        used_cache=False,
        used_alias=False,
        saved_path="/fake/path.parquet",
        error="",
    )


def test_journal_append_and_load(journal, sample_entry):
    # Append
    journal.append(sample_entry)

    # Load
    df = journal.load()
    assert not df.empty
    assert len(df) == 1
    assert df.iloc[0]["symbol"] == "GC=F"
    assert df.iloc[0]["success"] == True

    # Append another
    sample_entry.symbol = "BTC-USD"
    sample_entry.success = False
    sample_entry.error = "Connection timeout"
    journal.append(sample_entry)

    df = journal.load()
    assert len(df) == 2
    assert df.iloc[1]["symbol"] == "BTC-USD"
    assert df.iloc[1]["success"] == False


def test_journal_tail(journal, sample_entry):
    for i in range(25):
        sample_entry.symbol = f"SYM{i}"
        journal.append(sample_entry)

    df = journal.tail(10)
    assert len(df) == 10
    assert df.iloc[-1]["symbol"] == "SYM24"


def test_journal_summarize(journal, sample_entry):
    # Empty summary
    summary = journal.summarize()
    assert summary["total_entries"] == 0

    # Add entries
    journal.append(sample_entry)

    failed_entry = DownloadJournalEntry(
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        symbol="BAD_SYM",
        requested_symbol="BAD_SYM",
        resolved_symbol=None,
        asset_class="metals",
        timeframe="1d",
        provider_interval="1d",
        period="2y",
        start=None,
        end=None,
        success=False,
        rows=0,
        used_cache=False,
        used_alias=False,
        saved_path=None,
        error="Not found",
    )
    journal.append(failed_entry)

    summary = journal.summarize()
    assert summary["total_entries"] == 2
    assert summary["success_count"] == 1
    assert summary["failure_count"] == 1
    assert summary["success_rate"] == 0.5
    assert "Not found" in summary["recent_errors"]
