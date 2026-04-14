"""Reto 3: Comparación de Sensores (Lógica Automática)
Crea una dataclass LecturaSensor que incluya timestamp (str) y valor (float).
Activa el parámetro order=True.
Crea una lista con 3 lecturas de diferentes valores.
Usa la función sorted() de Python sobre esa lista y verifica que los ordena de menor a mayor automáticamente gracias al polimorfismo interno.
"""
from dataclasses import dataclass 
from operator import attrgetter

@dataclass(order = True)
class LecturaSensor:
    timestamp: str
    valor: float

if __name__ == "__main__":

    lista_lecturas = [LecturaSensor("2024-06-01 10:10:00", 23.5), 
                      LecturaSensor("2024-06-01 10:05:00", 19.8), 
                      LecturaSensor("2024-06-01 10:02:00", 21.2)]
    
    #Usamos la funcion sorted() para ordenar la lista de lecturas, lo que se hace automáticamente gracias al parámetro order=True en la dataclass
    lecturas_ordenadas = sorted(lista_lecturas) #Ordena de menor a mayor por el valor del sensor

    #Imprimimos las lecturas ordenadas para verificar el resultado
    print ("Ordenamiento segun el Timestamp:")
    for lectura in lecturas_ordenadas:
        print(lectura) 

    #La salida es: 
    #LecturaSensor(timestamp='2024-06-01 10:05:00', valor=19.8)
    #LecturaSensor(timestamp='2024-06-01 10:10:00', valor=21.2)
    #LecturaSensor(timestamp='2024-06-01 10:00:00', valor=23.5)

    print("\nOrdenamiento segun el valor del sensor:")
    #Si queremos ordenar por el valor del sensor, podemos usar attrgetter para especificar el atributo por el que queremos ordenar
    lecturas_ordenadas_por_valor = sorted(lista_lecturas, key=attrgetter('valor'))
    for valor in lecturas_ordenadas_por_valor:
        print(valor)
    
    #La salida es:
    #LecturaSensor(timestamp='2024-06-01 10:05:00', valor=19.8)
    #LecturaSensor(timestamp='2024-06-01 10:10:00', valor=21.2)
    #LecturaSensor(timestamp='2024-06-01 10:00:00', valor=23.5)