# AgentShield

**Security layer for AI agents — before and after every tool call.**

AgentShield protects AI agents across the full tool lifecycle:

- **Before execution** — scan APIs and tools for risk  
- **After execution** — inspect responses for prompt injection, sensitive data, and unsafe behavior  

---

## 🧠 Why This Matters

AI agents increasingly rely on external tools and APIs.

Even trusted endpoints can return:
- prompt injection attacks  
- unsafe instructions  
- sensitive data leaks  

AgentShield ensures agents act only on **safe, verified inputs and outputs** — not manipulated responses.

---

## ⚙️ How It Works

1. Submit a tool or API endpoint  
2. AgentShield scans for risk before execution  
3. AgentShield inspects the response after execution  
4. Receive a clear verdict: **SAFE**, **SUSPICIOUS**, or **MALICIOUS**

---

## 🔍 Scan Modes

AgentShield provides two layers of protection for AI agents, securing both the tools they call and the data they receive.

### 1. Pre-call Scanning (Tool Evaluation)

Scans a URL or API endpoint before execution:

- Domain age analysis  
- Malicious domain detection  
- Security header inspection  

**Use case:**  
Determine whether a tool is safe for an agent to call.

---

### 2. Post-call Inspection (Response Analysis)

Analyzes returned content from APIs or tools:

- Prompt injection detection  
- Sensitive data exposure (API keys, tokens, credentials)  
- Suspicious behavior (exfiltration, external calls, command execution)  

**Use case:**  
Ensure agents do not act on manipulated or unsafe outputs.

---

### ⚙️ Behavior

- If `response_text` is **not provided**  
  → Only pre-call scanning is performed  

- If `response_text` **is provided**  
  → Full lifecycle protection is applied (pre + post call)  

This mirrors real-world agent workflows, where both the tool and its output must be trusted.

---

## 🚀 Current Status

**Phase 2 Complete**

- ✅ Pre-call endpoint scanning  
- ✅ Post-call response inspection  
- ✅ Unified risk scoring + escalation  
- ✅ Interactive demo  
- ✅ Public API  
- ✅ Python SDK  

---

## 🔍 Live Demo

Try the interactive scanner:

👉 https://python-base-1.replit.app/api/demo

---

## 📘 API Docs

Interactive API documentation:

👉 https://python-base-1.replit.app/api/docs

---

## 🔌 API Usage

### Endpoint

```bash
POST /api/scan_tool
