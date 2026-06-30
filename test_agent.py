"""Offline contract test for the adk-demo tools. No API key, no network."""

from adk_demo.agent import get_current_time, get_weather, root_agent


def test_weather_known():
    r = get_weather("Tokyo")
    assert r["status"] == "success"
    assert "Tokyo" in r["report"]


def test_weather_unknown():
    assert get_weather("Atlantis")["status"] == "error"


def test_time_known():
    r = get_current_time("Tokyo")
    assert r["status"] == "success"
    assert r["timezone"] == "Asia/Tokyo"


def test_time_unknown():
    assert get_current_time("Atlantis")["status"] == "error"


def test_root_agent_wired():
    assert root_agent.name == "adk_demo_agent"
    names = {getattr(t, "__name__", getattr(t, "name", "")) for t in root_agent.tools}
    assert {"get_weather", "get_current_time"} <= names


if __name__ == "__main__":
    for _name, _fn in sorted(globals().items()):
        if _name.startswith("test_") and callable(_fn):
            _fn()
            print("ok:", _name)
    print("all tests passed")
