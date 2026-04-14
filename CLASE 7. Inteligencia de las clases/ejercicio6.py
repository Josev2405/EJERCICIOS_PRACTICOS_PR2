#SISTEMA DE TAREAS. INTELIGENCIA DE ORDENMAIENTO DE CLASES
"""Atento aquí: El orden de los atributos importa. Si pones el "Nombre" antes que la "Prioridad", 
Python ordenará alfabéticamente antes que por importancia."""

from dataclasses import dataclass, field
import time 

@dataclass(order=True)
class Tarea:

    #El orden de los atributos es 
    #importante para el ordenamiento automático
    #define el criterio de busqueda y comparación (Priority Queue)

    prioridad: int
    timestamp: float = field(default_factory= time.time)
    #El campo timestamp se inicializa automáticamente con el tiempo actual, lo que permite ordenar por el momento de creación en caso de empate en la prioridad
    #Usamos el default_factory para asegurarnos de que cada instancia tenga su propio timestamp único

    descripcion: str = field(compare=False, default="")
    #El campo descripcion no se utiliza para la comparación, por lo que se marca con compare=False y por defecto es una cadena vacía

if __name__ == "__main__":

    #instanciamos las tareas
    t1 = Tarea(prioridad=2, descripcion="Limpieza de logs")
    #Simulamos el paso del timepo para que los timestamps sean diferentes
    time.sleep(0.1) #Dormimos el programa por 0.1 segundos para asegurar que el timestamp de t2 sea diferente al de t1
    t2 = Tarea(prioridad=1, descripcion="Alerta de intrusos")
    time.sleep(0.1)
    t3 = Tarea(prioridad=2, descripcion="Actualizacion menor")
    time.sleep(0.1)

    lista_tareas = [t1, t2, t3]
    tareas_ordenadas = sorted(lista_tareas)

    for tarea in tareas_ordenadas:
        print(f"Priodidad: {tarea.prioridad} | {tarea.descripcion}")