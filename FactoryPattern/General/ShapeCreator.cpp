#include "ShapeCreator.h"
#include "Triangle.h"
#include "Rectangle.h"
#include "Circle.h"

std::unique_ptr<Shape> ShapeCreator::createShape(const ShapeType type)
{
    std::unique_ptr<Shape> newShape{};

    switch (type)
    {
        case ShapeType::Triangle:
            newShape = std::make_unique<Triangle>(Triangle());
            break;

        case ShapeType::Circle:
            newShape = std::make_unique<Circle>(Circle());
            break;

        case ShapeType::Rectangle:
            newShape = std::make_unique<Rectangle>(Rectangle());
            break;
    }
    return newShape;
}