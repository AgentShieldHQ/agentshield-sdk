
## 🧠 Why This Matters

Even trusted APIs can return unsafe or manipulative data.

AgentShield protects AI agents at two critical points:

- **Pre-call**: Scan tools and endpoints for risk
- **Post-call**: Inspect responses for prompt injection and malicious instructions

This ensures agents act only on safe, verified inputs — not manipulated outputs.

## 🚀 Status

AgentShield Prototype + Live Demo + SDK = complete

Live Demo:
https://python-base-1.replit.app/api/demo

## Interactive Demo

Try the live scanner:
[https://c5c30dcf-d653-4a74-b39d-7dd79bc6b0c8-00-3lc86x3cqnvn8.worf.replit.dev/api/demo](https://python-base-1.replit.app/api/demo)

## API Docs

Interactive docs:
https://c5c30dcf-d653-4a74-b39d-7dd79bc6b0c8-00-3lc86x3cqnvn8.worf.replit.dev/api/docs

## Python SDK

AgentShield now includes a Python SDK for developers.

Example usage:

```python
from agentshield import scan

result = scan("https://example.com")
print(result.result)
print(result.risk_score)
print(result.summary)


# agentshield

Python SDK for the [AgentShield](https://github.com/your-org/agentshield) URL security scanning API.

## Install

```bash
pip install agentshield
```

## Quick start

```python
from agentshield import scan

result = scan("https://example.com")
print(result)
```

Output:

```
AgentShield Scan
  URL        : https://example.com
  Result     : SAFE
  Risk score : [████████░░░░░░░░░░░░] 40/100
  Summary    : example.com scored 40/100 and appears safe. ...
```

## Configuration

By default the SDK points to the hosted demo server. Override with an env var or keyword argument:

```bash
export AGENTSHIELD_BASE_URL=https://your-server.com
```

```python
result = scan("https://example.com", base_url="https://your-server.com")
```

## Reusable client

```python
from agentshield import AgentShieldClient

with AgentShieldClient(base_url="https://your-server.com") as client:
    for url in ["https://github.com", "https://paypal-fake-login.tk"]:
        r = client.scan(url)
        print(r.result, r.risk_score, url)
```

## Return value

`scan()` returns a `ScanResult` dataclass:

| Field        | Type  | Description                          |
|--------------|-------|--------------------------------------|
| `url`        | `str` | The URL that was scanned             |
| `result`     | `str` | `"SAFE"`, `"SUSPICIOUS"`, or `"MALICIOUS"` |
| `risk_score` | `int` | 0–100                                |
| `summary`    | `str` | Plain-English explanation            |

Helper methods: `.is_safe()`, `.is_suspicious()`, `.is_malicious()`

## Error handling

```python
from agentshield import scan, ConnectionError, APIError

try:
    result = scan("https://example.com")
except ConnectionError as e:
    print("Server unreachable:", e)
except APIError as e:
    print(f"API error {e.status_code}:", e)
```

## License

MIT
