from fastapi import FastAPI
from routes import gestion_activos  # Importamos el módulo

app = FastAPI()

# Incluir los endpoints de gestión de activos
app.include_router(gestion_activos.router)

@app.get("/")
def read_root():
    return {"message": "¡La API está funcionando!"}
