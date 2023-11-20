#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "Shapes.h"


class Triangle final : public Shapes {
    double side_a, side_b, side_c;

public:
    Triangle(double a, double b, double c);

    [[nodiscard]] double area() const override;

    [[nodiscard]] double perimeter() const override;
};



#endif //TRIANGLE_H
