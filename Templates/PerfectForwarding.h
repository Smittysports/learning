#include <vector>
#include <iostream>

/** \page Perfect Forwarding
 *
 * Perfect forwarding allows construction of an object 'in place', which removes the need
 * for wasteful copying.
 *
 * std::forward has a single use case: to cast a templated function parameter (inside the function)
 * to the value category (lvalue or rvalue) the caller used to pass it. This allows rvalue arguments
 * to be passed on as rvalues, and lvalues to be passed on as lvalues, a scheme called “perfect forwarding.”
 *
 * Note: Even though an std::forward and std::move use the same syntax, which is &&, they can be 
 * differentiated because the std::forward is used in a template.
 * Example...
 * - Pushing a class object to a vector will perform a copy
 * -# This can be very wasteful
 * -# Using the std::move will mitigate that by moving the class object, but it must first
 *    be constructed and then moved
 * - Calling 'emplace' with a vector will utilize (forward reference, aka universal reference)
 * -# This allows us to 'forward' the parameters through instead of creating the object
 * - The 'emplace' will create the object 'in place' instead of creating beforehand and moving it 
 */
class BasicClass
{
public:
    BasicClass(int intVal, bool boolVal, float floatVal) :
        m_int(intVal),
        m_bool(boolVal),
        m_float(floatVal)
    {
        std::cout << "Basic class constructed\n";
        std::cout << "    " << m_int << " " << m_bool << " " << m_float << "\n";
    }

    BasicClass(int intVal, bool boolVal, float floatVal, std::vector<int> vec) :
        m_int(intVal),
        m_bool(boolVal),
        m_float(floatVal),
        m_vec(vec)

    {
        std::cout << "Basic class constructed 2\n";
        std::cout << "    " << m_int << " " << m_bool << " " << m_float << "\n";
    }
    ~BasicClass() = default;

private:
    int m_int;
    bool m_bool;
    float m_float;
    std::vector<int> m_vec;
};

class ForwardingClass
{
public:
    ForwardingClass() = default;

    ~ForwardingClass() = default;

    /** The addBasicClass method uses a variadic template, denoted with ...
     * 
     * This allows a variable number of arguments to be passed to this method of any
     * types.
     * 
     * There are 2 main types of value categories: lvalue and rvalue (prvalue). The lvalue is for
     * 'locatable' and typically appear on the left side of a statement. The prvalue is always on
     * the right side since it has no location in memory and needs to be associated with memory.
     * 
     * The Args&& is called a 'forwarding reference', rather than the typical usage of && which
     * is for rValue types. It is used to tell the compiler to 'forward' the arguments and to keep
     * the value type (rValue or lValue).
     * 
     * Note: When passing rValues from one method to the next, it must utilize the std::move
     * notation again each time or else it loses the rValue type and treats it as an lValue type. This
     * is not the case with 'forwarding', lValues will remain lValues and rValues will remain rValues.
     * 
     * - The std::forward is templated as well and takes the Args type.
     * - The args is the parameter being forwarded
     * - The ... is used to tell it to do it multiple times, once for each argument
     */
    template <typename ... Args>
    void addBasicClass(Args&& ... args)
    {
        m_basicClass.emplace_back(std::forward<Args>(args)...);
    }

private:
    std::vector<BasicClass> m_basicClass;
};