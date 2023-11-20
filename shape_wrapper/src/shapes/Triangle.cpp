#include "Triangle.h"

Triangle::Triangle(double a, double b, double c) : side_a(a), side_b(b), side_c(c) {}

double Triangle::area() const {
    double s = (side_a + side_b + side_c) / 2.0;
    return sqrt(s * (s - side_a) * (s - side_b) * (s - side_c));
}

double Triangle::perimeter() const {
    return side_a + side_b + side_c;
}