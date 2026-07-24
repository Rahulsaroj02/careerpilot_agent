from __future__ import annotations

from langchain_core.messages import HumanMessage, SystemMessage

try:
    from .config import career_df, llm, projects_df
    from .prompts import (
        ROLE_MATCH_SYSTEM_PROMPT,
        ROADMAP_SYSTEM_PROMPT,
        SKILL_ANALYSIS_SYSTEM_PROMPT,
    )
    from .state import CareerState
    from .utils import clean_skill_list, clean_text, format_skills, validate_required_fields
except ImportError:  # pragma: no cover - support script-style execution
    from backend.app.config import career_df, llm, projects_df
    from backend.app.prompts import (
        ROLE_MATCH_SYSTEM_PROMPT,
        ROADMAP_SYSTEM_PROMPT,
        SKILL_ANALYSIS_SYSTEM_PROMPT,
    )
    from backend.app.state import CareerState
    from backend.app.utils import clean_skill_list, clean_text, format_skills, validate_required_fields


def intake_node(state: CareerState) -> CareerState:
    """Normalize intake values before the workflow continues."""
    validate_required_fields(state, ["name", "education", "target_role"])

    current_skills = clean_skill_list(state.get("current_skills", []))

    return {
        **state,
        "name": clean_text(state.get("name", "")),
        "education": clean_text(state.get("education", "")),
        "target_role": clean_text(state.get("target_role", "")),
        "current_skills": current_skills,
    }


def role_matching_node(state: CareerState) -> CareerState:
    # Get all available roles from the CSV
    available_roles = career_df["role"].tolist()

    prompt = f"""
Student Input:
{state['target_role']}

Available Roles:
{chr(10).join(available_roles)}

Select the SINGLE closet  and best matching role.

Follow the exact format specified in the system prompt.
"""

    response = llm.invoke(
        [
            SystemMessage(content=ROLE_MATCH_SYSTEM_PROMPT),
            HumanMessage(content=prompt),
        ]
    )

    matched_role = response.content.strip()

    print(f"Matched Role: {matched_role}")

    return {
        **state,
        "target_role": matched_role,
    }


def skill_analysis_node(state: CareerState) -> CareerState:
    target_role = state["target_role"]

    # Search for the selected role
    role_data = career_df[
        career_df["role"].str.lower() == target_role.lower()
    ]

    # Role not found
    if role_data.empty:
        return {
            **state,
            "reasoning": f"Role '{target_role}' not found in the career knowledge base.",
        }

    # Extract required skills from CSV
    required_skills = [
        skill.strip()
        for skill in role_data.iloc[0]["required_skills"].split(";")
    ]

    # Convert current skills to lowercase for comparison
    current_skills_lower = {
        skill.lower()
        for skill in state["current_skills"]
    }

    # Find missing skills
    missing_skills = [
        skill
        for skill in required_skills
        if skill.lower() not in current_skills_lower
    ]

    # Prompt for LLM
    prompt = f"""
Student Education:
{state['education']}

Target Role:
{target_role}

Current Skills:
{', '.join(state['current_skills'])}

Required Skills:
{', '.join(required_skills)}

Missing Skills:
{', '.join(missing_skills)}

Analyze the student's profile.

Explain:

1. Priority order of the missing skills.
2. Why these skills are important.
3. Career advice.

Follow the exact format specified in the system prompt.
"""

    response = llm.invoke(
        [
            SystemMessage(content=SKILL_ANALYSIS_SYSTEM_PROMPT),
            HumanMessage(content=prompt),
        ]
    )

    return {
        **state,
        "required_skills": required_skills,
        "missing_skills": missing_skills,
        "reasoning": response.content,
    }


def roadmap_node(state: CareerState) -> CareerState:
    prompt = f"""
Student Name:
{state['name']}

Education:
{state['education']}

Target Role:
{state['target_role']}

Current Skills:
{', '.join(state['current_skills'])}

Missing Skills:
{', '.join(state['missing_skills'])}

Create a personalized 8-week learning roadmap.

The roadmap should:

- Follow prerequisite order.
- Start from beginner concepts.
- Include practical tasks every week.
- Help the student become job-ready.

Follow the exact format specified in the system prompt.
"""

    response = llm.invoke(
        [
            SystemMessage(content=ROADMAP_SYSTEM_PROMPT),
            HumanMessage(content=prompt),
        ]
    )

    return {
        **state,
        "roadmap": response.content,
    }


def project_recommendation_node(state: CareerState) -> CareerState:
    """Recommend projects based on the selected target role."""
    role = clean_text(state.get("target_role", "")).lower()
    filtered_projects = projects_df[
        projects_df["target_roles"].astype(str).str.lower().str.contains(role, na=False)
    ]

    recommended_projects = filtered_projects["project_name"].astype(str).tolist()
    return {**state, "recommended_projects": recommended_projects}


def final_report_node(state: CareerState) -> CareerState:
    """Build the final report text from the workflow state."""
    report_lines = [
        f"Name: {clean_text(state.get('name', ''))}",
        f"Education: {clean_text(state.get('education', ''))}",
        f"Target Role: {clean_text(state.get('target_role', ''))}",
        f"Current Skills: {format_skills(state.get('current_skills', []))}",
        f"Required Skills: {format_skills(state.get('required_skills', []))}",
        f"Missing Skills: {format_skills(state.get('missing_skills', []))}",
        f"Reasoning: {clean_text(state.get('reasoning', ''))}",
        f"Roadmap: {clean_text(state.get('roadmap', ''))}",
    ]

    report = "\n".join(report_lines)
    return {**state, "final_report": report}
