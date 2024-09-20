#pragma once

#include "Shape.h"

/** 'Triangle' is a 'Concrete Product' used in the Factory design pattern.
 * 
 * The 'Shape' is the 'Product' used in the Factory design pattern. It is the base class of
 * Triangle class and its abstract virtual methods must be overridden.
*/
class Triangle : public Shape
{
    public:
        virtual ~Triangle() = default;
        virtual std::string getName() const override {return "Triangle";}
};