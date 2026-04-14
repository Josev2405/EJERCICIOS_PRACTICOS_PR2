"""Reto 1: El Inventario del Almacén (Diseño Base)
Diseña una dataclass llamada MaterialConstruccion con los atributos: nombre (str), cantidad (int) y proveedor (str).
Instancia dos materiales: "Cemento" y "Ladrillo".
Imprime el objeto "Cemento" y observa cómo la salida es legible sin haber escrito un __str__."""

from dataclasses import dataclass

@dataclass
class MaterialConstruccion:
    nombre: str
    cantidad: int
    proveedor: str

if __name__ == "__main__":

    cemento = MaterialConstruccion("Cemento", 50, "Proveedor A")
    ladrillo = MaterialConstruccion("Ladrillo", 100, "Proveedor B")

    print(cemento) # MaterialConstruccion(nombre='Cemento', cantidad=50, proveedor='Proveedor A')
