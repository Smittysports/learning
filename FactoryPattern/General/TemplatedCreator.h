#pragma once

#include "ShapeCreator.h"

template <typename T>
class TemplatedCreator : public ShapeCreator
{
    public:
        virtual std::unique_ptr<Shape> createShape(); 
};

/** A templated createShape method that allows any new shape to be created without
 * having to manually add it. The new Shape product just needs to be created, which
 * it would have to be done no matter what.
 * 
 * For this example, we can use a Polygon, since it is not already included in the base
 * ShapeCreator class and is not in the enumeration.
 */
template <typename T>
std::unique_ptr<Shape> TemplatedCreator<T>::createShape()
{
    return std::make_unique<T>(T());
}