"""
AgentShield Python SDK
======================

Minimal SDK for the AgentShield URL security scanning API.

Quick start::

    from agentshield import scan

    result = scan("https://example.com")
    print(result)

To point at your own server::

    result = scan("https://example.com", base_url="https://your-server.com")

Or configure the default via environment variable::

    AGENTSHIELD_BASE_URL=https://your-server.com python your_script.py
"""

from .client import scan, AgentShieldClient
from .models import ScanResult
from .exceptions import AgentShieldError, APIError, ConnectionError

__version__ = "0.1.0"
__all__ = [
    "scan",
    "AgentShieldClient",
    "ScanResult",
    "AgentShieldError",
    "APIError",
    "ConnectionError",
]
