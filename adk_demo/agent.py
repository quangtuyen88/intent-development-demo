"""Minimal Google ADK agent for the adk-demo domain.

`root_agent` is discovered by `adk run adk_demo` / `adk web`. The two tools are
deterministic so they can be asserted offline (see test_agent.py).
"""

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import LlmAgent

_WEATHER = {
    "tokyo": "22°C and sunny",
    "london": "14°C and drizzling",
    "new york": "18°C and partly cloudy",
}

_TIMEZONES = {
    "tokyo": "Asia/Tokyo",
    "london": "Europe/London",
    "new york": "America/New_York",
}


def get_weather(city: str) -> dict:
    """Return the current weather for a known city.

    Args:
        city: City name, e.g. "Tokyo".

    Returns:
        dict: {"status": "success", "report": str} for a known city, or
        {"status": "error", "error_message": str} otherwise.
    """
    report = _WEATHER.get(city.strip().lower())
    if report is None:
        return {"status": "error", "error_message": f"No weather data for '{city}'."}
    return {"status": "success", "report": f"It is {report} in {city.strip().title()}."}


def get_current_time(city: str) -> dict:
    """Return the current local time for a known city.

    Args:
        city: City name, e.g. "Tokyo".

    Returns:
        dict: {"status": "success", "timezone": str, "now": str} for a known
        city, or {"status": "error", "error_message": str} otherwise.
    """
    tz_name = _TIMEZONES.get(city.strip().lower())
    if tz_name is None:
        return {"status": "error", "error_message": f"No timezone for '{city}'."}
    now = datetime.datetime.now(ZoneInfo(tz_name))
    return {
        "status": "success",
        "timezone": tz_name,
        "now": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


root_agent = LlmAgent(
    name="adk_demo_agent",
    model="gemini-2.5-flash",
    description="Answers weather and current-time questions for a few known cities.",
    instruction=(
        "You are a concise assistant. Use get_weather for weather questions and "
        "get_current_time for time questions. If a tool returns status 'error', "
        "tell the user you do not have data for that city."
    ),
    tools=[get_weather, get_current_time],
)
