from typing import TypedDict, List


class CareerState(TypedDict):
    # Student Information
    name: str
    education: str
    target_role: str
    current_skills: List[str]

    # Career Knowledge
    required_skills: List[str]
    missing_skills: List[str]

    # AI Reasoning
    reasoning: str

    # AI Actions
    roadmap: str
    recommended_projects: List[str]

    # Final Output
    final_report: str
