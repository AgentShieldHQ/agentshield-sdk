# ActionLedger

**Runtime action trust for AI agents.**

ActionLedger scores, explains, and records whether an AI agent should trust a tool, response, peer, memory, or destination before acting.

Every agent action gets a clear verdict, confidence level, recommended action, and audit-ready proof record.

> **Note:** ActionLedger is the current working name for the project. Earlier builds were developed under the AgentShieldHQ name.

---

## Why This Matters

AI agents are no longer just generating text.

They are starting to:

- call tools and APIs
- fetch URLs
- process files
- inspect responses
- update memory
- delegate work to other agents
- act across external systems

Every one of those actions can introduce risk.

A tool may be malicious.  
A response may contain prompt injection.  
A destination may be unsafe.  
A peer agent may be untrusted.  
A shared memory item may be stale, contradictory, or sensitive.

ActionLedger provides a runtime trust layer that helps agents decide:

> Should this action be allowed, reviewed, or blocked?

---

## Core Idea

**Before the action: score it.**  
**After the action: prove it.**

ActionLedger evaluates agent interactions before and after execution, then returns:

- verdict: `SAFE`, `SUSPICIOUS`, or `MALICIOUS`
- risk score: `0–100`
- verdict confidence
- recommended action: `ALLOW`, `REVIEW`, or `BLOCK`
- plain-English explanation
- risk factors
- optional proof / audit record

---

## What ActionLedger Protects

ActionLedger is designed to evaluate trust across the full agent workflow:

| Area | What it checks |
|---|---|
| Tools & APIs | Risky URLs, suspicious domains, unsafe endpoints |
| Responses | Prompt injection, exploit patterns, leaked secrets, malicious instructions |
| Destinations | Redirects, non-HTTPS targets, suspicious outbound paths |
| Peer agents | Trust level, delegation risk, unknown or blocked peers |
| Memory | Sensitive data, stale state, conflicting information |
| Shared workspaces | Decisions, definitions, tasks, failed attempts, and handoffs |

---

## Scan Modes

ActionLedger supports two scan modes:

### FAST Mode

Designed for real-time agent chains.

- Default mode
- Low-latency decision path
- No blocking network enrichment
- Best for runtime pre-call decisions

### DEEP Mode

Designed for enrichment and deeper inspection.

- Slower than FAST mode
- Adds additional checks where available
- Useful for borderline or high-risk cases

---

## Main API Actions

### 1. Pre-call Scan

Scan a URL, API, or tool before an agent calls it.

```bash
curl -X POST https://python-base-1.replit.app/api/scan_tool \
  -H "Content-Type: application/json" \
  -d '{"url": "https://google.com"}'
