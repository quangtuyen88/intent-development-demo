# adk-agent-core: minimal runnable Google ADK agent

## Goal

Add a minimal, runnable Google ADK agent (`root_agent`) for the `adk-demo`
domain, with two deterministic tools and a runtime that works with no API key.

## Why This Slice Exists Now

It is slice 1 of the domain: the smallest thing that proves the full loop
(intent-cli planning -> ADK agent code -> a check that runs without credentials).
Everything else in the domain builds on a working `root_agent`.

## Current Observed State

Empty project. `intent-cli` host state and the `adk-demo` intent tree exist, but
there is no agent package and nothing runnable yet.

## Accepted Baseline You May Assume

- `google-adk` >= 2.3 on Python >= 3.10, installed via `uv`.
- ADK package convention: `adk_demo/__init__.py` does `from . import agent`.
- Secrets only via env / `.env`; nothing committed.

## Target Repo / Path / Part

Repository: `quangtuyen88/intent-test`

Target paths: `adk_demo/agent.py`, `adk_demo/__init__.py`, `run_demo.py`, `test_agent.py`

Target part: Google ADK `root_agent` with two deterministic tools + no-key runtime.

## In Scope

- `root_agent` = `LlmAgent` (`gemini-2.5-flash`) with `get_weather(city)` and
  `get_current_time(city)`.
- `run_demo.py`: ADK `Runner` path when a key is set, direct-tool path otherwise.
- `test_agent.py`: deterministic tool asserts, no network/key.

## Out Of Scope

- Streaming, multi-agent handoff, persistent sessions, real weather/time APIs.

## Standalone Child Issue Contract

Deliver an importable `adk_demo` package whose `root_agent` ADK can run, two
deterministic tools returning `{status, ...}` dicts (error status for unknown
cities, never raising), a `run_demo.py` that runs with or without a Gemini key,
and a `test_agent.py` that passes offline. No other behavior.

## Acceptance Criteria

- `python test_agent.py` passes with no API key set.
- `python run_demo.py` prints tool output with no key; runs the agent via
  `Runner` when `GOOGLE_API_KEY`/`GEMINI_API_KEY` is set.
- `adk run adk_demo` resolves `root_agent` without import errors.
- `get_weather`/`get_current_time` return `status: "error"` for an unknown city.

## Verification

`python test_agent.py` (or `pytest`), `python run_demo.py`, and `git diff --check`.

## Related Links

- `intents/adk-demo/intent-tree/00-map.md`
- `intents/adk-demo/features/adk-agent-core/overview.md`
- `intents/adk-demo/interviews/adk-demo-s1.json`

## Knowledge Maintenance

Optional (G461). Tells the implementer/reviewer whether intent / ADR / diagram / docs
writeback is expected for this slice. Answer or explicitly decline:

- Intent placement: `intents/adk-demo/intent-tree/00-map.md` (existing)
- ADR candidate: none
- Diagram candidate: none
- Docs update: `README.md` (run instructions + intent-cli trail)
- Closeout writeback expected: no

## Base Branch Policy

Policy: `direct-main`
Expected PR base branch: `main`

Open all child PRs against `main` directly.
