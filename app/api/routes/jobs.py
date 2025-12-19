from fastapi import APIRouter, Depends
from app.db.deps import get_current_user
from app.db.models import User

router = APIRouter()

@router.post("/get-jobs")
def get_jobs(
    current_user: User = Depends(get_current_user)
):
    return {
        "user_id": current_user.id,
        "email": current_user.email,
        "jobs": [],
    }
