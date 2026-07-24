from langgraph.graph import END, StateGraph

try:
    from . import nodes
    from .state import CareerState
except ImportError:  # pragma: no cover - support script-style execution
    from backend.app import nodes
    from backend.app.state import CareerState

builder = StateGraph(CareerState)

builder.add_node("intake", nodes.intake_node)
builder.add_node("role_match", nodes.role_matching_node)
builder.add_node("skill_analysis", nodes.skill_analysis_node)
builder.add_node("roadmap", nodes.roadmap_node)
builder.add_node("projects", nodes.project_recommendation_node)
builder.add_node("report", nodes.final_report_node)

builder.set_entry_point("intake")
builder.add_edge("intake", "role_match")
builder.add_edge("role_match", "skill_analysis")
builder.add_edge("skill_analysis", "roadmap")
builder.add_edge("roadmap", "projects")
builder.add_edge("projects", "report")
builder.add_edge("report", END)

graph = builder.compile()
