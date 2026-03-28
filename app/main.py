from fastapi import FastAPI

app = FastAPI()

# Datos iniciales (MVP)
piezas = [
    {"id": 1, "nombre": "Cerradura imán", "estado": "pendiente"},
    {"id": 2, "nombre": "Acople cerradura imán", "estado": "pendiente"},
    {"id": 3, "nombre": "Posición delantera de puertas", "estado": "pendiente"},
    {"id": 4, "nombre": "Posición trasera de puertas", "estado": "pendiente"},
]

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/piezas")
def obtener_piezas():
    return piezas