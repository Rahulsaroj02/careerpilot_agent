import pandas as pd
import pytest

from backend.app.utils import (
    clean_skill_list,
    clean_text,
    format_skills,
    load_csv_dataframe,
    validate_required_fields,
)


def test_clean_text_and_skill_list():
    assert clean_text("  Python  ") == "Python"
    assert clean_text(None) == ""
    assert clean_skill_list("Java; SQL, HTML") == ["Java", "SQL", "HTML"]
    assert clean_skill_list([" Python ", "", "SQL"]) == ["Python", "SQL"]


def test_format_skills_and_validation(tmp_path):
    csv_path = tmp_path / "roles.csv"
    pd.DataFrame(
        [{"role": "Data Scientist", "required_skills": "Python; SQL"}]
    ).to_csv(csv_path, index=False)

    df = load_csv_dataframe(csv_path)
    assert list(df.columns) == ["role", "required_skills"]
    assert format_skills(["Python", "SQL"]) == "Python, SQL"

    validate_required_fields({"role": "Data Scientist"}, ["role"])

    with pytest.raises(ValueError):
        validate_required_fields({"role": "   "}, ["role"])
