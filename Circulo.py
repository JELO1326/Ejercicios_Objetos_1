class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return 3.14159 * self.radio ** 2

    def calcularPerimetro(self):
        return 2 * 3.14159 * self.radio

    def cambiarRadio(self, nuevo_radio):
        self.radio = nuevo_radio


circulo = Circulo(3)


print("Área del círculo:", circulo.calcularArea())


print("Perímetro del círculo:", circulo.calcularPerimetro())
