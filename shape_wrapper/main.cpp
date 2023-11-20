#include <pybind11/pybind11.h>

#include "Triangle.h"
#include "Rectangle.h"
#include "Circle.h"

namespace py = pybind11;

PYBIND11_MODULE(module_shape_wrapper, m) {
    py::class_<Triangle>(m, "Triangle")
        .def(py::init<double, double, double>())
        .def("area", &Triangle::area)
        .def("perimeter", &Triangle::perimeter);

    py::class_<Rectangle>(m, "Rectangle")
        .def(py::init<double, double>())
        .def("area", &Rectangle::area)
        .def("perimeter", &Rectangle::perimeter);

    py::class_<Circle>(m, "Circle")
        .def(py::init<double>())
        .def("area", &Circle::area)
        .def("perimeter", &Circle::perimeter);
}
