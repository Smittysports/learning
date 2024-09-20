#pragma once

#include <string>

/**  The 'Shape' is the 'Product' used in the Factory design pattern. It must be subclassed
 * by 'Concrete Product' classes.
 * 
 * This abstract base class is used by the factory pattern for creating shapes. */
class Shape
{
    public:
        virtual ~Shape() = default;
        virtual std::string getName() const = 0;
};