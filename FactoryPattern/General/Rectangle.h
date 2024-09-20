#pragma once

#include "Shape.h"

/** 'Rectangle' is a 'Concrete Product' used in the Factory design pattern.
 * 
 * The 'Shape' is the 'Product' used in the Factory design pattern. It is the base class of
 * Rectangle class and its abstract virtual methods must be overridden.
*/
class Rectangle : public Shape
{
    public:
        virtual std::string getName() const override {return "Rectangle";}
};