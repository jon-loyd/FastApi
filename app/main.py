from fastapi import FastAPI
from app.api.routes import auth, jobs
from app.core.config import settings

app = FastAPI(title=settings.app_name)

# Register api routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])

@app.get("/health")
def health():
    return {"status": "ok"}
