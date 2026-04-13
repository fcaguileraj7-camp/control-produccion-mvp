import sqlite3

def obtener_conexion():
    conexion = sqlite3.connect("produccion.db")
    return conexion