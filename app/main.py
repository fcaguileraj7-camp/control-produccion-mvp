from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

from piezas import (
    crear_tabla,
    insertar_piezas_iniciales,
    obtener_piezas,
    actualizar_estado
)

# 1. Crear tabla
crear_tabla()

# 2. Insertar datos
insertar_piezas_iniciales()

# 3. Mostrar antes
print("ANTES:")
for pieza in obtener_piezas():
    print(pieza)

# 4. Actualizar estado
actualizar_estado(1, "en_proceso")

# 5. Mostrar después
print("\nDESPUÉS:")
for pieza in obtener_piezas():
    print(pieza)