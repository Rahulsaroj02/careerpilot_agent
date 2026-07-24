from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from .app.graph import graph
    from .app.schemas import CareerRequest, CareerResponse
    from .app.state import CareerState
except ImportError:  # pragma: no cover - support running module directly
    from app.graph import graph
    from app.schemas import CareerRequest, CareerResponse
    from app.state import CareerState

app = FastAPI(title="CareerPilot Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/career-agent", response_model=CareerResponse)
def run_career_agent(request: CareerRequest) -> CareerResponse:
    initial_state: CareerState = {
        "name": request.name,
        "education": request.education,
        "target_role": request.target_role,
        "current_skills": request.current_skills,
        "required_skills": [],
        "missing_skills": [],
        "reasoning": "",
        "roadmap": "",
        "recommended_projects": [],
        "final_report": "",
    }

    final_state = graph.invoke(initial_state)

    return CareerResponse(
        required_skills=final_state.get("required_skills", []),
        missing_skills=final_state.get("missing_skills", []),
        reasoning=final_state.get("reasoning", ""),
        roadmap=final_state.get("roadmap", ""),
        recommended_projects=final_state.get("recommended_projects", []),
        final_report=final_state.get("final_report", ""),
    )
