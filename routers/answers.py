from fastapi import APIRouter

router = APIRouter(prefix="/answers", tags=["answers"])

@router.get("/")
def get_answers():
    return {"message": "Módulo de respuestas listo", "answers": []}
