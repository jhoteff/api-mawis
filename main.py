from fastapi import FastAPI

app = FastAPI()

@app.get("/", methods=["GET", "HEAD"])  # Permite GET y HEAD
def hello():
    return {"message": "¡Funciona!"}