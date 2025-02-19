from fastapi import APIRouter

router = APIRouter(prefix="/facturacion", tags=["Facturación"])

# ✅ 1. GetFacturaciones
@router.get("/facturaciones")
def get_facturaciones(desde: str, hasta: str):
    return {
        "desde": d
