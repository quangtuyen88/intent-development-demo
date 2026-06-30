# Intent Map

- Domain: `adk-demo`
- Target repo: `quangtuyen88/intent-development-demo`
- Initial map: shaped from interview session `adk-demo-s1`

## Canonical domain shape

The `adk-demo` domain delivers a **minimal, runnable Google ADK (Agent
Development Kit) agent**, with `intent-cli` owning the planning trail
(interview → draft → slice → packet → issue).

### Intents

1. **adk-agent-core** — a `root_agent` (`LlmAgent`, `gemini-2.5-flash`) exposing
   two deterministic tools, `get_weather(city)` and `get_current_time(city)`.
   Package follows ADK conventions so `adk run adk_demo` / `adk web` work when a
   Gemini key is present. (slice 1, this draft)
2. **no-key-runtime** — `run_demo.py` runs the agent through an ADK `Runner`
   when a key is set, and falls back to direct tool calls otherwise, so the
   demo runs with no credentials. `test_agent.py` asserts the tool contract.
   (slice 1, this draft)

### Out of scope (for now)

Streaming, multi-agent handoff, persistent sessions, real weather API.

Each child intent links back to this map and the host data under `.intent-cli/`.
