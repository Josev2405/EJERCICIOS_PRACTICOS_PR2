import unittest
from validador_sensores import ValidadorSensores #importo la clase ValidadorSensores del archivo validador_sensores.py para poder probar su función es_temperatura_segura

class TestValidadorSensores(unittest.TestCase):
    #defino un setUp() para inicializar los objetos necesarios
    def setUp(self):
        self.validador = ValidadorSensores()

    def test_temperatura_segura(self):
        """Si la temperatura es de 25 grados Celsius, el resultado debe ser True"""
        resultado = self.validador.es_temperatura_segura(25)
        self.assertTrue(resultado)

    def test_temperatura_no_segura(self):
        """Si la temperatura es de 35 grados Celsius, el resultado debe ser False"""
        resultado = self.validador.es_temperatura_segura(35)
        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()