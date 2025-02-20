from fastapi import APIRouter
from typing import List
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/gestion-tickets", tags=["Gestión de Tickets"])

# ✅ 1. GetEvolucionTickets
@router.get("/evolucion-tickets")
def get_evolucion_tickets(desde: str, hasta: str, vehiculos: List[str] = []):
    return {
        "desde": desde,
        "hasta": hasta,
        "tickets": [
            {
                "TIC_REF_INTERNA": 1001,
                "TIC_EMPRESA": "Empresa A",
                "TIC_DESCRIPCION": "Recogida no realizada",
                "TIC_FECHAHORA": "2024-02-19T08:00:00Z",
                "TIC_CALLE": "Calle Mayor",
                "TIC_MUNICIPIO": "Madrid",
                "TIC_PROVINCIA": "Madrid",
                "TIC_CP": "28001",
            }
        ]
    }

# Modelo de datos para la creación de una incidencia externa
class IncidenciaExterna(BaseModel):
    matricula: str
    codigoIncidencia: str
    fechahora: str
    latitud: float
    longitud: float
    extern1: str = None
    extern2: str = None
    extern3: str = None
    calle: str = None
    numero: str = None

# ✅ 2. InsIncidenciaExternaConCalle
@router.post("/incidencia-externa")
def ins_incidencia_externa(incidencia: IncidenciaExterna):
    return {
        "mensaje": "Incidencia registrada con éxito",
        "idIncidencia": 5001,
        "detalles": incidencia.dict()
    }

# Modelo de datos para la creación de un ticket
class Ticket(BaseModel):
    tipoTicket: str
    origenTicket: str
    referenciaExterna: str
    descripcion: str
    fechaTicket: str
    nombreCalle: str
    numCalle: str
    distrito: str
    municipio: str
    provincia: str
    pais: str
    codigoPostal: str
    infoAdicional: str
    tarea: str
    fechaDeseada: str
    extern1: str
    extern2: str
    extern3: str
    latitud: float
    longitud: float

# ✅ 3. InsTicket
@router.post("/crear-ticket")
def ins_ticket(ticket: Ticket):
    return {
        "mensaje": "Ticket creado con éxito",
        "TIC_REF_INTERNA": 6001,
        "detalles": ticket.dict()
    }
