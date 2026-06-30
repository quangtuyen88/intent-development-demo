# adk-agent-core — requirements

> See [overview.md](overview.md) for goals.

## Functional requirements

- `adk_demo/agent.py` defines `root_agent: LlmAgent` with `name`, `model`,
  `instruction`, and `tools=[get_weather, get_current_time]`.
- `get_weather(city)` and `get_current_time(city)` return structured dicts
  (`status` + payload), deterministic for a known city set.
- `adk_demo/__init__.py` runs `from . import agent` so `adk run adk_demo` and
  `adk web` resolve `root_agent`.
- `run_demo.py` runs the agent via an ADK `Runner` when `GOOGLE_API_KEY` or
  `GEMINI_API_KEY` is set, else prints direct tool output.

## Non-functional requirements

- No network or credentials required for the test path.
- Python >= 3.10; dependency pinned via `uv` (`google-adk`).
- Secrets only via env / `.env`; never committed (`.env.example` documents keys).