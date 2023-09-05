class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcularArea(self):
        return self.longitud * self.ancho

    def calcularPerimetro(self):
        return 2 * (self.longitud + self.ancho)

    def cambiarLongitud(self, nueva_longitud):
        self.longitud = nueva_longitud

    def cambiarAncho(self, nuevo_ancho):
        self.ancho = nuevo_ancho


rectangulo = Rectangulo(3, 8)


print("Área del rectángulo:", rectangulo.calcularArea())


print("Perímetro del rectángulo:", rectangulo.calcularPerimetro())

