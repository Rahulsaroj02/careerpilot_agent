from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class CareerRequest(BaseModel):
    """User input for the career planning workflow."""

    name: str = Field(..., description="Student name")
    education: str = Field(..., description="Student education level")
    target_role: str = Field(..., description="Target role the student wants")
    current_skills: List[str] = Field(default_factory=list, description="Skills the student already has")


class CareerResponse(BaseModel):
    """Output returned after the career planning workflow completes."""

    required_skills: List[str] = Field(default_factory=list)
    missing_skills: List[str] = Field(default_factory=list)
    reasoning: str = ""
    roadmap: str = ""
    recommended_projects: List[str] = Field(default_factory=list)
    final_report: str = ""


class CareerInput(CareerRequest):
    """Backward-compatible alias for the request model."""


class CareerOutput(CareerResponse):
    """Backward-compatible alias for the response model."""
