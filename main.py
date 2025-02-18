from fastapi import FastAPI

app = FastAPI()  # Instancia de FastAPI

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}