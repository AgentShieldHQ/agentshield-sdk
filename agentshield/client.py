"""
AgentShield client — thin wrapper around the /api/scan_tool endpoint.
"""
import os
from typing import Optional

import requests as _requests

from .models import ScanResult
from .exceptions import APIError, ConnectionError

_DEFAULT_BASE_URL = os.environ.get(
    "AGENTSHIELD_BASE_URL",
    "https://c5c30dcf-d653-4a74-b39d-7dd79bc6b0c8-00-3lc86x3cqnvn8.worf.replit.dev",
)

_DEFAULT_TIMEOUT = 30


class AgentShieldClient:
    """
    Reusable client for the AgentShield API.

    Example::

        client = AgentShieldClient(base_url="https://your-server.com")
        result = client.scan("https://example.com")
        print(result)
    """

    def __init__(
        self,
        base_url: str = _DEFAULT_BASE_URL,
        timeout: int = _DEFAULT_TIMEOUT,
        api_path: str = "/api/scan_tool",
        verify: bool = True,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.api_path = api_path
        self._verify = verify
        self._session = _requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

    def scan(self, url: str) -> ScanResult:
        """
        Scan a URL and return a :class:`ScanResult`.

        :param url: The URL to scan (e.g. ``"https://example.com"``).
        :raises ConnectionError: If the server cannot be reached.
        :raises APIError: If the server returns a non-200 response.
        """
        endpoint = self.base_url + self.api_path

        try:
            response = self._session.post(
                endpoint,
                json={"url": url},
                timeout=self.timeout,
                verify=self._verify,
            )
        except _requests.exceptions.ConnectionError as exc:
            raise ConnectionError(
                f"Could not connect to AgentShield at {self.base_url}"
            ) from exc
        except _requests.exceptions.Timeout as exc:
            raise ConnectionError(
                f"Request to AgentShield timed out after {self.timeout}s"
            ) from exc

        if not response.ok:
            raise APIError(response.status_code, response.text[:200])

        data = response.json()

        return ScanResult(
            url=url,
            result=data["result"],
            risk_score=data["risk_score"],
            summary=data["summary"],
        )

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self._session.close()

    def __enter__(self) -> "AgentShieldClient":
        return self

    def __exit__(self, *_) -> None:
        self.close()


# ---------------------------------------------------------------------------
# Module-level convenience function
# ---------------------------------------------------------------------------

_default_client: Optional[AgentShieldClient] = None


def scan(
    url: str,
    *,
    base_url: str = _DEFAULT_BASE_URL,
    timeout: int = _DEFAULT_TIMEOUT,
    verify: bool = True,
) -> ScanResult:
    """
    Scan a single URL using the AgentShield API.

    Uses a shared session for efficiency when called multiple times.

    :param url: The URL to scan.
    :param base_url: Override the server base URL
                     (defaults to ``AGENTSHIELD_BASE_URL`` env var or the
                     hosted demo server).
    :param timeout: Request timeout in seconds (default 30).
    :param verify: Verify TLS certificates (default ``True``).
                   Set to ``False`` when testing against a local dev server
                   without a trusted certificate.

    Example::

        from agentshield import scan

        result = scan("https://example.com")
        print(result)
    """
    global _default_client

    if _default_client is None or _default_client.base_url != base_url.rstrip("/"):
        _default_client = AgentShieldClient(base_url=base_url, timeout=timeout, verify=verify)

    return _default_client.scan(url)
