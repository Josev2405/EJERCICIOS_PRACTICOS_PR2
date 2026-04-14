#DATACLASSES, EFICIENCIA DE LOS DATOS EN PYTHON

#Clase basica de ingenieria de software, sin dataclass

"""class Componente:

    def __init__(self, nombre, costo, stock)
        self.nombre = nombre
        self.costo = costo
        self.stock = stock
    
    #defino la representacion de la clase para el programador con un metodo especial
    def __repr__(self):
        return f"Componente(nombre:'{self.nombre}', costo: {self.costo}, stock: {self.stock})"
    
    #defino un metodo especial para comparar dos objetos de la clase Componente, para que sean considerados iguales si tienen el mismo nombre
    def __eq__(self, other):
        if not isinstance(other, Componente):
            return False
        return (self.nombre, self.costo) == (other.nombre, other.costo)"""
    

"""SOLUCION CON DATACLASS"""

from dataclasses import dataclass

@dataclass
class Componente:
    nombre: str
    costo: float
    stock: int 

    #USO

if __name__ == "__main__":

    componente1 = Componente("Resistor", 0.10, 100)
    componente2 = Componente("Resistor", 0.10, 100)

    #Aca hacemos uso de los metodos especiales que se 
    #generan automaticamente con el decorador @dataclass, como __repr__ y __eq__

    print(componente1) # Componente(nombre='Resistor', costo=0.1, stock=100)
    print(componente1 == componente2) # True, porque tienen el mismo nombre y costo