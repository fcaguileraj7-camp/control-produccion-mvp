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

@app.put("/piezas/{pieza_id}")
def actualizar_estado(pieza_id: int, estado: str):
    for pieza in piezas:
        if pieza["id"] == pieza_id:
            pieza["estado"] = estado
            return {"mensaje": "estado actualizado", "pieza": pieza}
    
    return {"error": "pieza no encontrada"}

from fastapi.responses import HTMLResponse

@app.get("/vista", response_class=HTMLResponse)
def vista():
    with open("app/templates/index.html", encoding="utf-8") as f:
        return f.read()
    