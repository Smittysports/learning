#pragma once

#include "Shape.h"

/** 'Polygon' is a 'Concrete Product' used in the Factory design pattern.
 * 
 * The 'Shape' is the 'Product' used in the Factory design pattern. It is the base class of
 * Polygon class and its abstract virtual methods must be overridden.
*/
class Polygon : public Shape
{
    public:
        virtual std::string getName() const override {return "Polygon";}
};
