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
