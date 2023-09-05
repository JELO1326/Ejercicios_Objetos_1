#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    // Constructor
    Rectangulo(double l, double a) {
        longitud = l;
        ancho = a;
    }

    double calcularArea() {
        return longitud * ancho;
    }

    double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }

    void cambiarLongitud(double nuevaLongitud) {
        longitud = nuevaLongitud;
    }

    void cambiarAncho(double nuevoAncho) {
        ancho = nuevoAncho;
    }
};

int main() {

    Rectangulo rectangulo(3.0, 8.0);

    std::cout << "Área del rectángulo: " << rectangulo.calcularArea() << std::endl;

    std::cout << "Perímetro del rectángulo: " << rectangulo.calcularPerimetro() << std::endl;

    return 0;
}
