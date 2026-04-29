"""
Custom exceptions for the project.
"""


class ProjectError(Exception):
    """Base exception for all custom project errors."""


class ConfigError(ProjectError):
    """Raised when there is a configuration error."""


class DataProviderError(ProjectError):
    """Raised when a data provider fails to fetch or process data."""


class DataQualityError(ProjectError):
    """Raised when data quality checks fail."""


class StrategyError(ProjectError):
    """Raised when a strategy encounters an error."""


class BacktestError(ProjectError):
    """Raised when the backtesting engine encounters an error."""


class PaperTradingError(ProjectError):
    """Raised when paper trading encounters an error."""


class TelegramError(ProjectError):
    """Raised when telegram notification fails."""
