from fastapi import FastAPI
from app.api.rag import router as rag_router

app = FastAPI()
app.include_router(rag_router)
