/** \page FactoryDesignPattern Factory Design Pattern
 * \section Overview
 *
 * \image html FactoryDesignPattern.png
 * 
 * The factory design patern is a creational pattern that creates objects without having to specify the exact class of the object to create.
 * This is done by creating objects by calling a factory method, which is specified in an interface and implemented by child classes.
 * 
 */
#pragma once

#include "Shape.h"
#include <memory>

/** The factory must know the type of objects it can create.
 * This is done using an enumeration.
 */
enum class ShapeType {Triangle, Circle, Rectangle};

/** The ShapeCreator, the Creator in a Factory Design Pattern declares the 'factory method'.
 * For this example, the createShape() method is the 'factory method'.
 * 
 * The 'factory method' will return a 'Concrete Product', in this case, it returns
 * a derived 'Shape', which can be a Triangle, Circle, or Rectangle.
 * 
 * The ShapeCreator is responsible for creating and returning shape objects on demand
 * 
 * The ShapeCreator has a default implementation. It is designed so that it can be subclassed.
 * This is very important to allow for subclasses to change which objects they are
 * allowed to create. */
class ShapeCreator
{
    public:
        virtual ~ShapeCreator() = default;

        virtual std::unique_ptr<Shape> createShape(const ShapeType type);
};