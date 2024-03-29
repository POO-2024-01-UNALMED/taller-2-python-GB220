class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        color = color
        if color == "rojo":
            self.color = color
        elif color == "verde":
            self.color = color
        elif color == "amarillo":
            self.color = color
        elif color == "negro":
            self.color = color
        elif color == "blanco":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipo = tipo
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    numeroCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        i = 0
        for j in range(0, len(self.asientos)):
            if type(self.asientos[j]) == Asiento:
                i+=1
        return i
    
    def verificarIntegridad(self):
        integridad = "Auto original"
        for i in range (0, len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                if self.asientos[i].registro != self.registro or self.asientos[i].registro != self.motor.registro:
                    integridad = "Las piezas no son originales"
        return integridad

                    


