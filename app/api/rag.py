from fastapi import APIRouter, HTTPException, Request
from app.acl.check import has_access
from app.embedding.search import hybrid_search
from prometheus_client import Counter, Histogram
import time

router = APIRouter()

REQUEST_COUNT = Counter("chat_requests_total", "Total number of chat requests")
REQUEST_LATENCY = Histogram("chat_request_latency_seconds", "Chat request latency")

@router.post("/chat")
def chat(request: Request, query: str, user_id: str):
    REQUEST_COUNT.inc()
    start_time = time.time()

    if not has_access(user_id, query):
        raise HTTPException(status_code=403, detail="Access Denied")

    results = hybrid_search(query)
    REQUEST_LATENCY.observe(time.time() - start_time)
    return {"results": results}