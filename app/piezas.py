from db import obtener_conexion
from datetime import datetime

def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        estado TEXT,
        proceso TEXT,
        fecha_creacion TEXT,
        fecha_actualizacion TEXT
    )
    """)

    conexion.commit()
    conexion.close()


def insertar_piezas_iniciales():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Limpiar tabla (solo para pruebas)
    cursor.execute("DELETE FROM piezas")

    piezas = [
        ("Acrilico Trasero 1", "pendiente", "corte"),
        ("Acrilico Trasero 2", "pendiente", "corte"),
        ("Acrilico Trasero 3", "pendiente", "corte")
    ]

    for nombre, estado, proceso in piezas:
        ahora = datetime.now().isoformat()

        cursor.execute("""
        INSERT INTO piezas (nombre, estado, proceso, fecha_creacion, fecha_actualizacion)
        VALUES (?, ?, ?, ?, ?)
        """, (nombre, estado, proceso, ahora, ahora))

    conexion.commit()
    conexion.close()


def obtener_piezas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM piezas")
    datos = cursor.fetchall()

    conexion.close()
    return datos


def actualizar_estado(id_pieza, nuevo_estado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    ahora = datetime.now().isoformat()

    cursor.execute("""
    UPDATE piezas
    SET estado = ?, fecha_actualizacion = ?
    WHERE id = ?
    """, (nuevo_estado, ahora, id_pieza))

    conexion.commit()
    conexion.close()