from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/logos", StaticFiles(directory="logos"), name="logos")

# Datos iniciales (MVP)
piezas = [
    {"id": 1, "nombre": "Cerradura imán", "estado": "pendiente"},
    {"id": 2, "nombre": "Acople cerradura imán", "estado": "pendiente"},
    {"id": 3, "nombre": "Posición delantera de puertas", "estado": "pendiente"},
    {"id": 4, "nombre": "Posición trasera de puertas", "estado": "pendiente"},
]

@app.get("/vista", response_class=HTMLResponse)
def vista():
    with open("app/templates/index.html", encoding="utf-8") as f:
        return f.read()

