from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class State(str, Enum):
    init_startup = "init_startup"
    in_startup_processing = "in_startup_processing"
    init_shutdown = "init_shutdown"
    in_shutdown_processing = "in_shutdown_processing"
    active = "active"
    inactive = "inactive"

class Scenario(BaseModel):
    id: int
    state: State
    parameters: dict

scenarios = {}

@app.get("/scenario/{id}")
async def get_scenario(id: int):
    scenario = scenarios.get(id)
    if scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario

@app.post("/scenario/{id}/state")
async def post_scenario_state(id: int, state: State):
    scenario = scenarios.get(id)
    if scenario is None:
        raise HTTPException(status_code=404, detail="Scenario not found")
    scenario['state'] = state
    return {"message": "State updated", "state": state}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
