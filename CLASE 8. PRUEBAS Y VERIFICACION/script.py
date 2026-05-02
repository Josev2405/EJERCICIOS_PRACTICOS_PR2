class Car:
    
    def __init__(self, speed: int = 0):
        self._speed = speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_speed):

        if new_speed < 0:
            raise ValueError("La velocidad debe ser positiva.")
        self._speed = new_speed