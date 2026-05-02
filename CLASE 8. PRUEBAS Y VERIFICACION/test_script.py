#CON PYTEST SE PUEDEN ESCRIBIR PRUEBAS DE MANERA SENCILLA Y EFICIENTE
import pytest 

from script import Car

#usamos fixtures para crear objetos de prueba reutilizables
@pytest.fixture
def car():
    return Car() #Creamos un objeto del tipo Car()

def test_speed_at_star(car):

    assert car.speed == 0

def test_new_speed(car):
    
    car.speed = 100
    assert car.speed == 100

def test_cannot_set_negative_speed(car):

    with pytest.raises(ValueError, match = "La velocidad debe ser positiva."):
        #Realizamos una validacion para la validacion del valor esperado y, en caso negativo, 
        #una comparacion con el string del mensaje de error esperado.
        car.speed = -10