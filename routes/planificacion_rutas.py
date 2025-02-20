from fastapi import APIRouter
from typing import List

router = APIRouter(prefix="/planificacion-rutas", tags=["Planificación de Rutas"])

# ✅ 1. GetDatosModeloRuta
@router.get("/datos-modelo-ruta")
def get_datos_modelo_ruta(codigoRMO: str, fecha: str):
    return {
        "codigoRMO": codigoRMO,
        "fecha": fecha,
        "elementos": [
            {"ELE_CODIGO": "E001", "ORDEN": 1},
            {"ELE_CODIGO": "E002", "ORDEN": 2}
        ],
        "vehiculos": [
            {"VEH_MATRICULA": "1234-ABC"},
            {"VEH_MATRICULA": "5678-DEF"}
        ]
    }

# ✅ 2. GetDatosRuta
@router.get("/datos-ruta")
def get_datos_ruta(codigoRMO: str, matricula: str, fechaInicio: str):
    return {
        "codigoRMO": codigoRMO,
        "matricula": matricula,
        "fechaInicio": fechaInicio,
        "kms": 120.5,
        "peso_total": 1500,
        "total_servicios": 25
    }

# ✅ 3. GetListaModelosRuta
@router.get("/lista-modelos-ruta")
def get_lista_modelos_ruta():
    return {
        "modelos_ruta": [
            {"RMO_CODIGO": "RUTA001", "RMO_DESCRIPCION": "Ruta Norte"},
            {"RMO_CODIGO": "RUTA002", "RMO_DESCRIPCION": "Ruta Sur"}
        ]
    }

# ✅ 4. GetModelosRuta
@router.get("/modelos-ruta")
def get_modelos_ruta():
    return {
        "modelos": [
            {"RMO_ID": 1, "RMO_CODIGO": "RUTA001", "DESCRIPCION": "Ruta Norte"},
            {"RMO_ID": 2, "RMO_CODIGO": "RUTA002", "DESCRIPCION": "Ruta Sur"}
        ]
    }

# ✅ 5. GetRutas
@router.get("/rutas")
def get_rutas():
    return {
        "rutas": [
            {"RUT_ID": 1, "RMO_CODIGO": "RUTA001", "VEH_MATRICULA": "1234-ABC"},
            {"RUT_ID": 2, "RMO_CODIGO"}]
