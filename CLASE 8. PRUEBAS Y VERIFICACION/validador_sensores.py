class ValidadorSensores:
    
    def es_temperatura_segura(self, temperatura)-> bool:
        #Aqui se implementaria la logica del codigo para validar si la temperatura es segura o no
        if 18 <= temperatura <=25:
            return True
