from fastapi import FastAPI
from routes import gestion_activos, gestion_flotas

app = FastAPI()

app.include_router(gestion_activos.router)
app.include_router(gestion_flotas.router)

@app.get("/")
def read_root():
    return {"message": "¡La API está funcionando!"}
