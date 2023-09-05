#include <iostream>

class Circulo {
private:
    double radio;

public:

    Circulo(double r) {
        radio = r;
    }

    double calcularArea() {
        return 3.14159 * radio * radio;
    }

    double calcularPerimetro() {
        return 2 * 3.14159 * radio;
    }

    void cambiarRadio(double nuevoRadio) {
        radio = nuevoRadio;
    }
};

int main() {

    Circulo circulo(3.0);

    std::cout << "Area del circulo: " << circulo.calcularArea() << std::endl;

    std::cout << "Perimetro del circulo: " << circulo.calcularPerimetro() << std::endl;

    return 0;
}
