#USAREMOS EL ENFOQUE TDD (TEST DRIVEN DEVELOPMENT) PARA RESOLVER EL EJERCICIO 1 DE LA CLASE 8
#En este caso usaremos el framwork de pruebas unitarias de Python llamado unittest

import unittest
from nomina import Nomina #importo la clase Nomina del archivo nomina.py para poder probar su función calcular_bono
#No importo el metodo calcular_bono directamente porque quiero probar la función a través de la clase Nomina, para asegurarme de que la integración entre la clase y su método funcione correctamente.

class TestNomina(unittest.TestCase):

    def test_calcular_bono(self):
        
        #Aqui puedo agregar casos de prueba para verificar el correcto funcionamiento de la función calcular_bono
        """Si el empleado gana 1000, el bono del 10% debe ser: 100"""
        nomina = Nomina()
        resultado = nomina.calcular_bono(1000)
        self.assertEqual(resultado, 100.00)

if __name__ == "__main__":
    unittest.main()

