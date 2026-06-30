"""Run the adk-demo agent.

With a Gemini key (GOOGLE_API_KEY or GEMINI_API_KEY) set, runs the LLM agent
through an ADK Runner. Without one, calls the tools directly so the demo still
runs end to end.
"""

import os

from adk_demo.agent import get_current_time, get_weather, root_agent

APP_NAME = "adk_demo"
USER_ID = "demo-user"
SESSION_ID = "demo-session"
SAMPLE_PROMPT = "What's the weather and the current time in Tokyo?"


def _has_key() -> bool:
    return bool(os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"))


def run_offline() -> None:
    print("[no API key] calling tools directly:\n")
    print("get_weather('Tokyo')       ->", get_weather("Tokyo"))
    print("get_current_time('Tokyo')  ->", get_current_time("Tokyo"))
    print("get_weather('Atlantis')    ->", get_weather("Atlantis"))
    print("\nSet GOOGLE_API_KEY (or GEMINI_API_KEY) to run the full LLM agent.")


def run_with_llm(prompt: str) -> None:
    import asyncio

    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    session_service = InMemorySessionService()
    asyncio.run(
        session_service.create_session(
            app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
        )
    )
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    message = types.Content(role="user", parts=[types.Part(text=prompt)])

    print(f"[LLM] prompt: {prompt}\n")
    for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response() and event.content and event.content.parts:
            print("agent:", event.content.parts[0].text)


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError:
        pass

    if _has_key():
        run_with_llm(SAMPLE_PROMPT)
    else:
        run_offline()
