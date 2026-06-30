# adk-agent-core Implementation Packet

## Goal

Add an importable `adk_demo` package whose `root_agent` Google ADK can run,
backed by two deterministic tools, plus a `run_demo.py` that works with or
without a Gemini key and a `test_agent.py` that passes offline.

## Why

Slice 1 of `adk-demo`: the smallest runnable proof of the intent-cli -> ADK loop.

## Scope

- `adk_demo/agent.py`: `root_agent = LlmAgent(model="gemini-2.5-flash", tools=[get_weather, get_current_time])`.
- `adk_demo/__init__.py`: `from . import agent`.
- `run_demo.py`: branch on `GOOGLE_API_KEY`/`GEMINI_API_KEY` (Runner vs direct tools).
- `test_agent.py`: assert tool outputs (known city ok, unknown city -> error status).

## Out of scope

- Streaming, multi-agent handoff, persistent sessions, real weather/time APIs.

## Verification

`python test_agent.py` (no key), `python run_demo.py`, `git diff --check`.

## Knowledge Maintenance (G461, optional)

Captured while the design context is fresh. Answer or explicitly decline:

- Intent placement: TODO which intent node this supports / whether a new node is needed.
- ADR candidate: TODO ADR-worthy decision + path, or decline.
- Diagram candidate: TODO concept/workflow/topology/state diagram update, or decline.
- Docs update: TODO user-facing docs to change, or decline.
- Closeout learning: TODO knowledge to write back after landing + whether `write_back_required`.

`improve` (G456 / G460) is the later safety net; packet-time maintenance is the normal path.