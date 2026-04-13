from piezas import (
    crear_tabla,
    insertar_piezas_iniciales,
    obtener_piezas,
    actualizar_estado
)

# Inicializar sistema
crear_tabla()
insertar_piezas_iniciales()

print("ANTES:")
for pieza in obtener_piezas():
    print(pieza)

actualizar_estado(1, "en_proceso")

print("\nDESPUÉS:")
for pieza in obtener_piezas():
    print(pieza)