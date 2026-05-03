class Almacen:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto: str)-> list[str]:
        #Aqui se implementaria la logica del codigo para agregar un producto al almacen
        self.productos.append(producto)
        return self.productos
    