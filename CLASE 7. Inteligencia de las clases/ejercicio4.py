"""Reto 2: El Registro Inmutable (Seguridad)
Crea una dataclass CoordenadaGPS con latitud y longitud (floats).
Configura la clase para que sea frozen.
Intenta cambiar la latitud después de crear el objeto. ¿Qué error arroja Python? (Debería ser un FrozenInstanceError).
"""

from dataclasses import dataclass

@dataclass(frozen = True)
class CoordenadasGPS:
    latitud: float
    longitud: float

if __name__ == "__main__":

    ubicacion = CoordenadasGPS(40.7128, -74.0060) # Coordenadas de Nueva York
    print(ubicacion) # CoordenadasGPS(latitud=40.7128, longitud=-74.006)

    #Intentamos cambiar la latitud, lo que debería arrojar un error
    try:
        ubicacion.latitud = 34.0522 # Coordenadas de Los Angeles
    except Exception as e:
        print(f"Error al intentar modificar la latitud: {type(e).__name__}") # Error al intentar modificar la latitud: FrozenInstanceError