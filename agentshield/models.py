from dataclasses import dataclass


@dataclass
class ScanResult:
    """Holds the result of a single AgentShield URL scan."""

    url: str
    result: str
    risk_score: int
    summary: str

    def is_safe(self) -> bool:
        return self.result == "SAFE"

    def is_suspicious(self) -> bool:
        return self.result == "SUSPICIOUS"

    def is_malicious(self) -> bool:
        return self.result == "MALICIOUS"

    def __str__(self) -> str:
        bar_len = 20
        filled = round(self.risk_score / 100 * bar_len)
        bar = "█" * filled + "░" * (bar_len - filled)
        return (
            f"AgentShield Scan\n"
            f"  URL        : {self.url}\n"
            f"  Result     : {self.result}\n"
            f"  Risk score : [{bar}] {self.risk_score}/100\n"
            f"  Summary    : {self.summary}"
        )
