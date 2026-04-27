"""
Custom exceptions for the project.
"""

class ProjectError(Exception):
    """Base exception for all custom project errors."""
    pass

class ConfigError(ProjectError):
    """Raised when there is a configuration error."""
    pass

class DataProviderError(ProjectError):
    """Raised when a data provider fails to fetch or process data."""
    pass

class DataQualityError(ProjectError):
    """Raised when data quality checks fail."""
    pass

class StrategyError(ProjectError):
    """Raised when a strategy encounters an error."""
    pass

class BacktestError(ProjectError):
    """Raised when the backtesting engine encounters an error."""
    pass

class PaperTradingError(ProjectError):
    """Raised when paper trading encounters an error."""
    pass

class TelegramError(ProjectError):
    """Raised when telegram notification fails."""
    pass
