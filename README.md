# adk-demo

A minimal, runnable **Google ADK** (Agent Development Kit) agent whose planning
trail is driven by **`intent-cli`**. It is a demo of two tools working together:

- `intent-cli` shapes the work (interview → draft → slice → packet → issue).
- Google ADK runs the resulting agent.

## What's here

```
adk_demo/agent.py     root_agent (LlmAgent, gemini-2.5-flash) + 2 deterministic tools
adk_demo/__init__.py  `from . import agent` so `adk run adk_demo` works
run_demo.py           runs the agent (LLM path with a key, direct-tool path without)
test_agent.py         offline contract test for the tools (no key, no network)
intents/adk-demo/     intent-cli design trail (intent tree, interview, feature spec)
.intent-cli/          intent-cli host state + the published-ready issue packet
```

## Run the agent

```bash
uv run python test_agent.py     # offline, no key — asserts the tool contract
uv run python run_demo.py        # full LLM agent if a key is set, else direct tools
uv run adk run adk_demo          # ADK interactive REPL
uv run adk web                   # ADK web UI
```

Set a Gemini key to exercise the LLM + tool-calling path (otherwise `run_demo.py`
just calls the tools directly):

```bash
export GOOGLE_API_KEY=...         # from https://aistudio.google.com/apikey
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

## The intent-cli trail (how this was planned)

Reproduces the design half of the demo:

```bash
intent-cli intent init --domain adk-demo --target-repo quangtuyen88/intent-development-demo --write
intent-cli interview record-answer --session adk-demo-s1 --domain adk-demo \
  --question g1-scope --prompt "..." --from-file answer.md --write
intent-cli interview compile --session adk-demo-s1 --domain adk-demo
intent-cli intent draft-from-interview --session adk-demo-s1 --domain adk-demo --write
intent-cli intent add-feature --domain adk-demo --name adk-agent-core --write
intent-cli intent next-slice --domain adk-demo --dry-run          # -> candidate adk-agent-core
intent-cli packet draft --execution-unit adk-agent-core --domain adk-demo \
  --target-repo quangtuyen88/intent-development-demo                          # writes the issue packet
intent-cli issue publish-flow adk-agent-core --repo quangtuyen88/intent-development-demo   # add --write to publish
```

The ready-to-publish issue body is `.intent-cli/issues/adk-agent-core/github-body.md`.
Publishing (`--write`) needs `gh` auth and the target GitHub repo to exist; it is
left as a dry-run here.

## Notes

- The agent uses `gemini-2.5-flash` (`gemini-2.0-flash` is retired — 404).
- The `[EXPERIMENTAL] JSON_SCHEMA_FOR_FUNC_DECL` warning from ADK is benign.
