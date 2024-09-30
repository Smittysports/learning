/** \page VariadicTemplate Variadic Template
 * 
 * 
 */

#include <type_traits>

/** Variadics work great for logging. A user can pass any nmber of arguments and
 * the logging class will allow them to be printed.
 */
 void Log() {};

/** Log will work with any number of arguments. The compiler will create all of the needed functions
 * Ex... 
 * Log (1, 5.0, 2, true);
 * will create 4 new functions:
 *   Log<int, double, int, bool>(int, double, int, bool)
 *   Log<double, int, bool>(double, int, bool)
 *   Log<int, bool>(int, bool)
 *   Log<bool>(bool)
 *
 * Type traits work great with variadics, since they can be used to perform special behavior
 * at compile time, or runtime if the variable cannot be determined at compile time.
 *
 * The use of constexpr states that 'if everything is provided at compile time, the function can
 * be evaluated at compile time'.
 *
 * Without the 'if constexpr(is_pointer_v<T>)', the Log function would print the address of a
 * pointer instead of the value in the pointer.
 */
template<typename T, typename... Types>
void Log(T firstArg, Types... args)
{
    //std::cout << "sizeof Types = " << sizeof...(Types) << "\n";
    std::cout << "Args left: " << sizeof...(args) << ", ";  
    std::cout << "Type: " << typeid(T).name() << ", ";  
    if constexpr(std::is_pointer_v<T>)
    {    
        if ( std::is_same_v<const char*, T> || std::is_same_v<char*, T> )
            std::cout << std::string(firstArg) << "\n";
        else
            std::cout << *firstArg << "\n";
    }
    else
        std::cout << firstArg << "\n";
    Log(args...);
};

template<typename T,
    typename = std::enable_if_t<(std::is_same_v<int, T> || std::is_same_v<unsigned int, T>)> >
T Factorial(T firstArg)
{
    static_assert(std::is_integral_v<T>);
    if (firstArg > 1)
        return firstArg * Factorial(firstArg - 1);
    else
        return firstArg;
}
