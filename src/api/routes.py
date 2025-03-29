import httpx
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

from services.agent_service import run_router_agent

router = APIRouter()


class RunRequest(BaseModel):
    query: str
    callback_url: str


@router.post("/run-agent")
async def router_endpoint(request: RunRequest):
    try:
        result_data = await run_router_agent(request.query)
        async with httpx.AsyncClient(timeout=10.0) as client:
            await client.post(
                request.callback_url,
                json={"result": result_data},
                headers={"Content-Type": "application/json", "Accept": "application/json"},
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to run agent or notify callback: {e}")
    return {"status": "agent executed and callback sent"}


@router.post("/webhook")
async def webhook_endpoint(request: Request):
    try:
        payload = await request.json()
        print("Received webhook payload:", payload)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid payload")
    return {"status": "success"}
