from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/recursos-humanos", tags=["Recursos Humanos"])

# ✅ 1. GetOperarios
@router.get("/operarios")
def get_operarios(fechadesde: str = None, fechahasta: str = None, listaOperarios: List[str] = []):
    return {
        "fechadesde": fechadesde,
        "fechahasta": fechahasta,
        "operarios": [
            {
                "OPE_CODIGO": "OPE001",
                "OPE_NOMBRE": "Juan",
                "OPE_APELLI"
            }
        ]
    }