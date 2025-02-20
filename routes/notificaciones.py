from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/notificaciones", tags=["Notificaciones"])

# Modelo de datos para la notificación
class Notificacion(BaseModel):
    titulo: str
    texto: str
    importancia: int
    fechaHora: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# ✅ 1. InsNotificacion
@router.post("/crear")
def ins_notificacion(notificacion: Notificacion):
    return {
        "mensaje": "Notificación creada con éxito",
        "detalles": notificacion.dict()
    }
