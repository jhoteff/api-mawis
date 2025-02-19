from fastapi import FastAPI
from routes import gestion_activos, gestion_flotas, planificacion_rutas, gestion_tickets, recursos_humanos, facturacion

app = FastAPI()

app.include_router(gestion_activos.router)
app.include_router(gestion_flotas.router)
app.include_router(planificacion_rutas.router)
app.include_router(gestion_tickets.router)
app.include_router(recursos_humanos.router)
app.include_router(facturacion.router)

@app.get("/")
def read_root():
    return {"message": "¡La API está funcionando!"}
