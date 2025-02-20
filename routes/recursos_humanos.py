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
                "OPE_APELLIDO1": "Pérez",
                "OPE_APELLIDO2": "Gómez",
                "OPE_NIF": "12345678A",
                "OPE_TELEFONO1": "600123456",
                "OPE_TELEFONO2": "911223344",
                "OPE_EMAIL": "juan.perez@example.com",
                "OPE_INFO": "Supervisor de ruta",
                "OPE_CATEGORIA_PROFESIONAL": "Conductor",
                "OPE_FECHA_ALTA": "2023-01-15",
                "OPE_FECHA_BAJA": None,
                "EMP_DESCRIPCION": "Empresa A"
            },
            {
                "OPE_CODIGO": "OPE002",
                "OPE_NOMBRE": "María",
                "OPE_APELLIDO1": "López",
                "OPE_APELLIDO2": "Fernández",
                "OPE_NIF": "87654321B",
                "OPE_TELEFONO1": "601987654",
                "OPE_TELEFONO2": "911998877",
                "OPE_EMAIL": "maria.lopez@example.com",
                "OPE_INFO": "Encargada de mantenimiento",
                "OPE_CATEGORIA_PROFESIONAL": "Técnico",
                "OPE_FECHA_ALTA": "2022-06-20",
                "OPE_FECHA_BAJA": None,
                "EMP_DESCRIPCION": "Empresa B"
            }
        ]
    }
