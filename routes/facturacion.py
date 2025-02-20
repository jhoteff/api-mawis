from fastapi import APIRouter

router = APIRouter(prefix="/facturacion", tags=["Facturación"])

# ✅ 1. GetFacturaciones
@router.get("/facturaciones")
def get_facturaciones(desde: str, hasta: str):
    return {
        "desde": desde,
        "hasta": hasta,
        "facturas": [
            {
                "SITIO": "Centro de reciclaje A",
                "CODIGO_SITIO": "SIT001",
                "DESDE": desde,
                "HASTA": hasta,
                "NUMERO_FACTURA": "FAC-20240201",
                "FECHA_CALCULO": "2024-02-15",
                "VALOR_TOTAL": 1520.50,
                "CONCEPTOS": [
                    {"NOMBRE": "Recogida mensual", "VALOR": 1200.00, "LINEA": 1},
                    {"NOMBRE": "Mantenimiento", "VALOR": 320.50, "LINEA": 2}
                ]
            }
        ]
    }
