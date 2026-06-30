# adk-agent-core — acceptance criteria

> See [overview.md](overview.md) for goals.

## Criteria

- [ ] `python -m pytest` (or `python test_agent.py`) passes with no API key set.
- [ ] `python run_demo.py` prints tool output with no key, and runs the LLM
      agent when `GOOGLE_API_KEY`/`GEMINI_API_KEY` is set.
- [ ] `adk run adk_demo` resolves `root_agent` without import errors.
- [ ] `get_weather`/`get_current_time` return `status: "error"` for an unknown
      city rather than raising.