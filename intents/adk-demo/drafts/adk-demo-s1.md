# Draft intent — adk-demo / session adk-demo-s1

> Compiled from accepted interview answers. Operator must accept this draft before any source-of-truth mutation.

## Accepted baseline

### g1-scope — What is the first publishable slice of the adk-demo agent, and what is out of scope?

First publishable slice: a minimal Google ADK agent for the `adk-demo` domain.

- `root_agent` is an `LlmAgent` (model `gemini-2.5-flash`) with two deterministic tools: `get_weather(city)` and `get_current_time(city)`.
- Package layout follows ADK conventions: `adk_demo/agent.py` exposes `root_agent`; `adk_demo/__init__.py` does `from . import agent`, so `adk run adk_demo` / `adk web` work when a Gemini key is set.
- intent-cli owns the planning trail: this interview shapes the intent tree, which unblocks `intent next-slice` and the first packet/issue.

Out of scope for slice 1: streaming, multi-agent handoff, persistent sessions, real weather API.


### g2-runtime — How should the demo run when no API key is present?

The demo must run with no credentials so it works in CI and on a fresh machine.

`run_demo.py` branches on environment:
- If `GOOGLE_API_KEY` or `GEMINI_API_KEY` is set: run `root_agent` through an ADK `Runner` + `InMemorySessionService` against a sample prompt and print the model's reply.
- Otherwise: call the tool functions directly and print their structured output, with a one-line note telling the user to set a key for the full LLM run.

`test_agent.py` asserts the deterministic tool outputs (no network, no key), so there is one runnable check that fails if the tool logic breaks. This is the offline contract that keeps the demo green without an API key.


## Open questions

- none

## Candidate execution units

- TODO — operator decides whether to promote this draft into a published child issue.
