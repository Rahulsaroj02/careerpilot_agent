from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence, Union

import pandas as pd


def load_csv_dataframe(csv_path: Union[str, Path]) -> pd.DataFrame:
    """Load a CSV file into a DataFrame with a clear file error."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    return pd.read_csv(path)


def clean_text(value: Optional[str]) -> str:
    """Normalize whitespace in a text field."""
    if value is None:
        return ""
    if not isinstance(value, str):
        value = str(value)
    return " ".join(value.split()).strip()


def clean_skill_list(skills: Optional[Union[str, Sequence[str], Iterable[str]]]) -> list[str]:
    """Convert skill input into a cleaned list of strings."""
    if skills is None:
        return []

    if isinstance(skills, str):
        items = re.split(r"[;,\n]+", skills)
    else:
        items = list(skills)

    cleaned: list[str] = []
    for item in items:
        cleaned_value = clean_text(item)
        if cleaned_value:
            cleaned.append(cleaned_value)

    return cleaned


def format_skills(skills: Sequence[str], separator: str = ", ") -> str:
    """Format a skill sequence into a readable string."""
    return separator.join(clean_skill_list(skills))


def validate_required_fields(
    data: Mapping[str, Any], required_fields: Sequence[str]
) -> None:
    """Ensure required fields are present and non-empty."""
    missing_fields: list[str] = []
    for field in required_fields:
        value = data.get(field)
        if value is None:
            missing_fields.append(field)
        elif isinstance(value, str) and not clean_text(value):
            missing_fields.append(field)
        elif isinstance(value, (list, tuple, set, dict)) and not value:
            missing_fields.append(field)

    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
