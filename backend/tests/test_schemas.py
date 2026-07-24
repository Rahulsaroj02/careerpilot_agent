from backend.app.schemas import CareerRequest, CareerResponse


def test_schema_models():
    request = CareerRequest(
        name="Ada",
        education="Bachelor",
        target_role="Data Scientist",
        current_skills=["Python", "SQL"],
    )
    response = CareerResponse(required_skills=["Python"])

    assert request.name == "Ada"
    assert request.current_skills == ["Python", "SQL"]
    assert response.required_skills == ["Python"]
