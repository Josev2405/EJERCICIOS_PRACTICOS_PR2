"""Ejercicio basico para entender la diferencia de las Dataclasses con datos mutables y no mutables"""

from dataclasses import dataclass, field 
#la funcion field se utiliza para especificar opciones adicionales para los campos de una dataclass, 
#como valores predeterminados o funciones de fábrica.

@dataclass
class RobotBueno:
    nombre: str
    historial: list = field(default_factory=list) #Usamos default_factory para crear una nueva lista vacia para cada instancia

if __name__ == "__main__":

    robot1 = RobotBueno("R2D2")
    robot2 = RobotBueno("C3PO")

    robot1.historial.append("Saludó a Luke")
    robot2.historial.append("Saludó a Leia")

    print(robot1) # RobotBueno(nombre='R2D2', historial=['Saludó a Luke'])
    print(robot2) # RobotBueno(nombre='C3PO', historial=['Saludó a Leia'])
