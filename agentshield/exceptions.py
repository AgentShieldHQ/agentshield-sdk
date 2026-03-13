class AgentShieldError(Exception):
    """Base exception for all AgentShield SDK errors."""


class APIError(AgentShieldError):
    """Raised when the AgentShield API returns an unexpected response."""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        super().__init__(f"API error {status_code}: {message}")


class ConnectionError(AgentShieldError):
    """Raised when the SDK cannot reach the AgentShield server."""
