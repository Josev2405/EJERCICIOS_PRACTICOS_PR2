import unittest
from control_inventario import Almacen

class TestControlInventario(unittest.TestCase):

    def setUp(self):
        self.almacen = Almacen()

    def test_agregar_producto(self):
        """Al agregar un producto al almacen, este debe estar presente en la lista de productos"""
        self.almacen.agregar_producto("Cloro")
        self.assertIn("Cloro", self.almacen.productos)

if __name__ == "__main__":
    unittest.main()