#ifndef CIRCLE_H
#define CIRCLE_H

#include "Shapes.h"


class Circle final : public Shapes {
    double radius;

public:
    explicit Circle(double r);

    [[nodiscard]] double area() const override;

    [[nodiscard]] double perimeter() const override;
};



#endif //CIRCLE_H
