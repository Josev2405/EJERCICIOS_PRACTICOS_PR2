class CuentaBancaria:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def retirar(self, monto: float)-> float:
        #Aqui se implementaria la logica del codigo para retirar dinero de la cuenta bancaria
        if monto < 0:
            raise ValueError("El monto a retirar no puede ser un valor negativo.")
        elif monto > self.saldo:
            raise ValueError("El monto a retirar excede el saldo de la cuenta.")
        else:
            self.saldo -= monto
            return monto