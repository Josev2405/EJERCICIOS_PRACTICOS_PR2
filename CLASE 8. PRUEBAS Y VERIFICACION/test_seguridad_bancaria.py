import unittest
from seguridad_bancaria import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):

    def setUp(self):
        self.cuenta = CuentaBancaria(1000)

    def test_retirar(self):
        """Si el monto excede el saldo de la cuenta, 
        se debe lanzar una excepcion ValueError"""
        with self.assertRaises(ValueError):
            self.cuenta.retirar(1500)

if __name__ == "__main__":
    unittest.main()
