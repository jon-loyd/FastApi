from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.session import Base, engine
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    yield
    # Teardown code

app = FastAPI(title=settings.app_name, lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}