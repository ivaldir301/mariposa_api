from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.routes import jobs

app = FastAPI()

app.include_router(jobs.router, tags=["job"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}