"""
AgentShield SDK — usage examples.

When running this script on the same machine as the server use:
    LOCAL_SERVER=1 python example.py

When running from your own machine against the public URL:
    python example.py
"""
import os
from agentshield import scan, AgentShieldClient, ConnectionError, APIError

# When running inside the Replit server environment, call via the internal
# proxy to avoid TLS bootstrapping. External callers use the public HTTPS URL.
_ON_SERVER = os.environ.get("LOCAL_SERVER") == "1"
BASE_URL = "http://localhost:80" if _ON_SERVER else os.environ.get(
    "AGENTSHIELD_BASE_URL",
    "https://c5c30dcf-d653-4a74-b39d-7dd79bc6b0c8-00-3lc86x3cqnvn8.worf.replit.dev",
)

# ── 1. Simple one-liner ─────────────────────────────────────────────────────
print("── Simple scan ─────────────────────────────────")
result = scan("https://google.com", base_url=BASE_URL)
print(result)

# ── 2. Inspect individual fields ────────────────────────────────────────────
print("\n── Field access ────────────────────────────────")
print(f"Result     : {result.result}")
print(f"Risk score : {result.risk_score}/100")
print(f"Summary    : {result.summary}")
print(f"Is safe?   : {result.is_safe()}")

# ── 3. Scan multiple URLs with a reusable client ────────────────────────────
print("\n── Batch scan via client ───────────────────────")
urls = [
    "https://github.com",
    "https://paypal-secure-verify.tk",
    "https://openai.com",
]

with AgentShieldClient(base_url=BASE_URL) as client:
    for url in urls:
        r = client.scan(url)
        print(f"  {r.result:12s} ({r.risk_score:3d}/100)  {url}")

# ── 4. Error handling ────────────────────────────────────────────────────────
print("\n── Error handling ──────────────────────────────")
try:
    scan("https://example.com", base_url="http://localhost:9999")
except ConnectionError as e:
    print(f"Could not reach server: {e}")
except APIError as e:
    print(f"API returned an error (HTTP {e.status_code}): {e}")
