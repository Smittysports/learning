#pragma once

#include "Shape.h"

/** 'Sphere' is a 'Concrete Product' used in the Factory design pattern.
 * 
 * The 'Shape' is the 'Product' used in the Factory design pattern. It is the base class of
 * Sphere class and its abstract virtual methods must be overridden.
*/
class Sphere : public Shape
{
    public:
        virtual std::string getName() const override {return "Sphere";}
};