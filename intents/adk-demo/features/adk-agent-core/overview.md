# adk-agent-core — overview

> **Ask intent-cli first:** `intent-cli guide intent-work setup --kind tree-layout --domain adk-demo --format markdown`

## Goals

Ship a minimal, runnable Google ADK agent for the `adk-demo` domain that proves
the end-to-end loop: intent-cli planning trail -> ADK agent code -> a check that
runs with no API key.

## Acceptance criteria summary

- A `root_agent` (`LlmAgent`, `gemini-2.5-flash`) exposes two deterministic
  tools and is discoverable by `adk run adk_demo`.
- The demo runs with no credentials via a direct-tool fallback.
- A deterministic test asserts the tool contract.

## Related

- [requirements.md](requirements.md)
- [acceptance.md](acceptance.md)
- [decisions.md](decisions.md)
- [open-questions.md](open-questions.md)
- [packets.md](packets.md)