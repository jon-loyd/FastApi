from fastapi import FastAPI
from app.api.routes import auth
from app.core.config import settings

app = FastAPI(title=settings.app_name)

# Register api routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/health")
def health():
    return {"status": "ok"}
