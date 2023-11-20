#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "Shapes.h"


class Rectangle final : public Shapes {
    double length, width;

public:
    Rectangle(double l, double w);

    [[nodiscard]] double area() const override;

    [[nodiscard]] double perimeter() const override;
};



#endif //RECTANGLE_H
