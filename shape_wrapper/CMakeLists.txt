cmake_minimum_required(VERSION 3.27)
project(shape_wrapper)

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)
FetchContent_Declare(
        pybind11
        GIT_REPOSITORY https://github.com/pybind/pybind11
        GIT_TAG v2.11.1
)
FetchContent_GetProperties(pybind11)
if(NOT pybind11_POPULATED)
    FetchContent_Populate(pybind11)
    add_subdirectory(${pybind11_SOURCE_DIR} ${pybind11_BINARY_DIR})
endif()

pybind11_add_module(module_shape_wrapper MODULE main.cpp
        src/shapes/Shapes.h
        src/shapes/Triangle.h
        src/shapes/Triangle.cpp
        src/shapes/Rectangle.h
        src/shapes/Rectangle.cpp
        src/shapes/Circle.h
        src/shapes/Circle.cpp
)


target_include_directories(module_shape_wrapper PUBLIC src/shapes)
