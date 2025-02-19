from fastapi import APIRouter
from typing import List
from datetime import datetime

router = APIRouter(prefix="/gestion-flotas", tags=["Gestión de Flotas"])

# ✅ 1. GetAccesoAreasRestringidas
@router.get("/acceso-areas-restringidas")
def get_acceso_areas_restringidas(fechaDesde: str, fechaHasta: str, listaMatriculas: List[str] = []):
    return {
        "fechaDesde": fechaDesde,
        "fechaHasta": fechaHasta,
        "accesos": [
            {"fechaHora": "2024-02-19T08:00:00Z", "zona": "Zona A", "matricula": "1234-ABC", "causa": "entrada"},
            {"fechaHora": "2024-02-19T08:30:00Z", "zona": "Zona A", "matricula": "1234-ABC", "causa": "salida"},
        ]
    }

# ✅ 2. GetActividadVehiculos
@router.get("/actividad-vehiculos")
def get_actividad_vehiculos(fechaDesde: str, fechaHasta: str, listaMatriculas: List[str] = []):
    return {
        "fechaDesde": fechaDesde,
        "fechaHasta": fechaHasta,
        "actividad": [
            {"matricula": "1234-ABC", "KM": 150, "tiempoActividad": "5h"},
            {"matricula": "5678-DEF", "KM": 200, "tiempoActividad": "6h"},
        ]
    }

# ✅ 3. GetEventos
@router.get("/eventos")
def get_eventos():
    return {
        "eventos": [
            {"codigo": "2001", "descripcion": "Alerta de batería baja"},
            {"codigo": "2002", "descripcion": "Exceso de velocidad"},
        ]
    }

# ✅ 4. GetUltimaPosicionGPS
@router.get("/ultima-posicion-gps")
def get_ultima_posicion_gps(matricula: str):
    return {
        "matricula": matricula,
        "ultimaPosicion": {
            "fechaHora": "2024-02-19T09:00:00Z",
            "coordenadaX": 40.4168,
            "coordenadaY": -3.7038
        }
    }
