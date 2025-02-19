from fastapi import APIRouter
from datetime import datetime
from typing import List

router = APIRouter(prefix="/gestion-activos", tags=["Gestión de Activos"])

# Endpoint 1: GetAperturasCerraduras
@router.get("/aperturas-cerraduras")
def get_aperturas_cerraduras(fechaDesde: str, fechaHasta: str):
    return {
        "fechaDesde": fechaDesde,
        "fechaHasta": fechaHasta,
        "aperturas": [
            {"fechaHora": datetime.now(), "codigoCerradura": "1234", "codigoTarjeta": "5678"},
            {"fechaHora": datetime.now(), "codigoCerradura": "4321", "codigoTarjeta": "8765"},
        ]
    }

# Endpoint 2: GetAtributosDisponibles
@router.get("/atributos-disponibles")
def get_atributos_disponibles(listaEmpresas: List[str] = []):
    return {
        "empresas": listaEmpresas,
        "atributos": [
            {"ATR_CODIGO": "001", "ATR_DESCRIPCION": "Color", "EMP_DESCRIPCION": "Empresa A"},
            {"ATR_CODIGO": "002", "ATR_DESCRIPCION": "Tamaño", "EMP_DESCRIPCION": "Empresa B"},
        ]
    }

# Endpoint 3: GetCategorias
@router.get("/categorias")
def get_categorias():
    return {
        "categorias": [
            {"CAT_CODIGO": "CAT001", "CAT_DESCRIPCION": "Orgánico"},
            {"CAT_CODIGO": "CAT002", "CAT_DESCRIPCION": "Plástico"},
        ]
    }

# ✅ Endpoint 4: GetClientes
@router.get("/clientes")
def get_clientes():
    return {
        "clientes": [
            {"PER_CODIGO": "CLI001", "PER_NOMBRE": "Juan", "PER_APELLIDO1": "Pérez", "PER_NIFCIF": "12345678A"},
            {"PER_CODIGO": "CLI002", "PER_NOMBRE": "María", "PER_APELLIDO1": "Gómez", "PER_NIFCIF": "87654321B"},
        ]
    }

# ✅ Endpoint 5: GetContenedoresNoRecogidos
@router.get("/contenedores-no-recogidos")
def get_contenedores_no_recogidos(fechaDesde: str, fechaHasta: str):
    return {
        "fechaDesde": fechaDesde,
        "fechaHasta": fechaHasta,
        "contenedores": [
            {"idContenedor": "CONT001", "ubicacion": "Calle 123", "estado": "No recogido"},
            {"idContenedor": "CONT002", "ubicacion": "Av. Central", "estado": "No recogido"},
        ]
    }

# ✅ Endpoint 6: GetDistritos
@router.get("/distritos")
def get_distritos():
    return {
        "distritos": [
            {"codigo": "D01", "nombre": "Centro"},
            {"codigo": "D02", "nombre": "Sur"},
        ]
    }

# ✅ Endpoint 7: GetElementos
@router.get("/elementos")
def get_elementos():
    return {
        "elementos": [
            {"ELE_CODIGO": "ELEM001", "DESCRIPCION": "Contenedor amarillo"},
            {"ELE_CODIGO": "ELEM002", "DESCRIPCION": "Contenedor azul"},
        ]
    }

# ✅ Endpoint 8: GetInventarioContenedores
@router.get("/inventario-contenedores")
def get_inventario_contenedores():
    return {
        "contenedores": [
            {"id": "CONT001", "tipo": "Plástico", "ubicacion": "Calle 123"},
            {"id": "CONT002", "tipo": "Papel", "ubicacion": "Av. Central"},
        ]
    }

# ✅ Endpoint 9: GetInventarioUbicaciones
@router.get("/inventario-ubicaciones")
def get_inventario_ubicaciones():
    return {
        "ubicaciones": [
            {"idUbicacion": "UBI001", "tipo": "Punto limpio", "coordenadas": [40.4168, -3.7038]},
            {"idUbicacion": "UBI002", "tipo": "Contenedor callejero", "coordenadas": [41.3879, 2.16992]},
        ]
    }

# ✅ Endpoint 10: GetLecturasSensores
@router.get("/lecturas-sensores")
def get_lecturas_sensores(desde: str, hasta: str):
    return {
        "desde": desde,
        "hasta": hasta,
        "lecturas": [
            {"sensor": "SEN001", "valor": 75.5, "fecha": "2024-02-01"},
            {"sensor": "SEN002", "valor": 62.3, "fecha": "2024-02-02"},
        ]
    }
