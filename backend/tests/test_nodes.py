from backend.app.nodes import role_matching_node


class FakeResponse:
    def __init__(self, content: str):
        self.content = content


class FakeLLM:
    def __init__(self):
        self.calls = []

    def invoke(self, messages):
        self.calls.append(messages)
        return FakeResponse("Data Scientist")


def test_role_matching_uses_llm_when_available(monkeypatch):
    fake_llm = FakeLLM()
    monkeypatch.setattr("backend.app.nodes.llm", fake_llm, raising=False)

    state = {"target_role": "data science", "current_skills": []}
    result = role_matching_node(state)

    assert result["target_role"] == "Data Scientist"
    assert fake_llm.calls
