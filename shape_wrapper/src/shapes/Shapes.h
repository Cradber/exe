#ifndef SHAPES_H
#define SHAPES_H

#include <cmath>

class Shapes {
public:
    virtual ~Shapes() = default;

    [[nodiscard]] virtual double area() const = 0;
    [[nodiscard]] virtual double perimeter() const = 0;
};



#endif //SHAPES_H
