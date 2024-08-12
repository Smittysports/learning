#pragma once

/** \page Initialization
 * Types of initialization
 * - Copy
 *   - Using an '=' sign with a scalar or aggragate
 *   - Passing an object by value
 *   - Returning an object by value
 *   - Throwing an exception
 *   - Catching an exception by value
 * - Aggregate
 *   - Using an '= {}' sign with braces, works with aggregates only
 *   - An array is an aggregate
 *   - An aggragate is also a class with no user-declared constructor, no private or protected
 *     non-static data members, no base classes, and no virtual functions.
 *   - Even though brace initializing will aggregate initialize an object, it will copy initialize
 *     each of the members
 *   - If a constructor is explicit, then aggregate initialization will fail if the compiler
 *     receives a value that must be converted
 * - Direct
 *   - Using non empty parenthesis ()
 *   - Works with constructors
 *   - Can be used for scalar types as well to treat user-defined types and built-in types uniformly
 *   - Can be used for aggregates since C++20
 *   - Best choice for use in templates, over using an initializer list
 * - Value
 *   - Using empty parenthesis ()
 *   - The initialization depends on the type
 *     - If it is an object with a default constructor, it just calls it
 *     - For non-union classes with no declared constructors, the object is zero-initialized and the default constructor is called
 *     - If is is an array, it will value initialize all elements
 *     - If it is a scalar, it zero initializes it
 *     - Otherwise, the initialization is only valid if it has no user-provided constructors
 * - Default
 *   - Done by simply omittiing the parenthesis when creating a class
 *   - Scalars are left uninitialized
 *   - Calls the default constructor
 *   - Static variables wiith no initializer are default initialized to 0
 * - Initializer List (uniform initialization or brace initialization)
 *   - Using braces {} for all types
 *   - Performs value initialization when instantiating a class
 *   - It will call the default constructor for a class
 *   - For a scalar type, it will be zero initialized
 *   - If there are constructors with Initializer list as well as normal constructors, such as with
 *     many templates, using braces will always choose the initializer list. Make sure to use the
 *     correct initialization method that is needed.
 *   - It is often a good idea to not implement an Initializer list constructor, so that the Initializer
 *     list syntax can be used safely.
 *   - Prefer Initializer list syntax.
 *     - The '=' should be for assignment, not initialization.
 *     - A common initialization scheme is beneficial
 * - In-class member initialization
 *   - Class member variables can be initilaized when they are declared, rather than in the constructor
 *   - This is safer and easier to read
 * 
 * Reason to care:
 * - The conversion permissions are based on the type of initialization
 * - A constructor not declared with 'explicit' is called a converting constructor
 *   - The compiler can perform an implicit conversion of the datatype
 *   - It cannot do this if it is defined with explicit
 * 
 * Issues prior to modern updates:
 * - No uniform syntax
 * - Narrowing conversions
 * - Value-initialization require roundabout syntax
 * - No ability to initialize an STL container like an array
 * 
 * Tricky:
 * - If you try to instantiate a class like this:
 *   Foo myFoo();
 *   - It will not create an object
 *   - It creates a function that takes no parameters and returns Foo
 *   - This is a consequence of C's parsing rules and we have to live with it
 *   - Note: The compiler will always interpret a declaration as a function if it would be valid to do so
 *
 * Note: Initialization occurs only when an object is first created. Otherwise, it uses assignment.
 * - Assignment replaces the values of an existing object, so it may need to clean up the previous state
 * - This is a large reason for needing both construction and assignment.
 * 
 * Scalars:
 * - integers, characters, floating point, enumerations, pointers
 * 
 * Aggregates (pre-C++20):
 * - structures, classes, arrays
 * - No user-declared constructors
 * - no private or protected non-static data members
 * - no base classes
 * - no virtual functions
 * 
 *  Aggregates (since C++20):
 * - structures, classes, arrays
 * - No user-declared or inherited constructors
 * - no private or protected direct non-static data members
 * - no virtual, private, or protected base classes
 * - no virtual functions
 * 
 * Invariant:
 * - A logical assertion that is always held to be true during a certain phase of execution.
 * - ex.. a loop invariant is a condition that is true at the beginning and at the end of every iteration of a loop
 *        - Note: this does not say anything about its truth partway through
 * - ex.. a class invariant
 *        - A character string's stored length should always be one less than the size of the array that is pointed to
 *        - The string 'hello\0' is size 5, even though it has a null terminator
 * - A constructor can be used to impose the invariant, whereas an aggregate initialization would
 *  break the invariant ()
 *   - If a class has any user provided constructors, then the class is not an aggregate and does not
 *     support aggregate intiatlization
 * 
 * Zero initialization:
 * - Zero initialization is the setting of a variable to a zero value implicitly converted to the type:
 *   - Numeric variables are initialized to 0 (or 0.0, or 0.0000000000, etc.).
 *   - Char variables are initialized to '\0'.
 *   - Pointers are initialized to nullptr.
 *   - Arrays, POD (plain old data) classes, structs, and unions have their members initialized to a zero value.
 * - Zero initialization is performed at different times:
 *   - At program startup, for all named variables that have static duration. These variables may later be initialized again.
 *   - During value initialization, for scalar types and POD class types that are initialized by using empty braces.
 *   - For arrays that have only a subset of their members initialized.
 *
 * In C, and available in C++:
 *  Scalars can be initialized with a single value:
 *   int x = 3;
 *   - This is called copy-initialization
 * 
 *  Aggregates can be initialized with a brace-enclosed list:
 *  - This is called aggregate-initialization
 *  - Unions can be initialized this way, but with a single value in the braces
 * 
 * \code
 * struct widget {
 *     int id;
 *     double price;
 * };
 * 
 * widget w1 = {1000, 6.5};
 * int values[3] = {1, 2, 3};
 * \endcode
 * 
 * Uninitialized:
 * - If an object does not have an explicit initializer, then it will either be zeroed or
 *   indeterminate.
 * - It will be zeroed if it is:
 *   - declared static
 *   - declared thread_local
 *   - declared at namespace scope (the class is intantiated directly from a namespace, and
 *     not from within another class or function)
 * - Otherwise, it will be indeterminate
 */

struct widget {
    int id;
    double price;
};

class widgetWithExplicitConstructor {
    public:    
        int id;
        double price;

        //widgetWithExplicitConstructor() = default;
        //explicit widgetWithExplicitConstructor() : id(0), price(0.0f){};
        ~widgetWithExplicitConstructor() = default;
};

/** Direct initialization takes place with parenthesis ().
 * 
 * Direct initialization can also be used with the members initlization list
 * of a class. 
 */
class WidgetWithDirectInitialization {
public:   
    WidgetWithDirectInitialization() : id(5), price(25.5f){};
    ~WidgetWithDirectInitialization() = default;
    /** Copy constructor
     * 
     * The copy constructor can be invoked with direct initialization. It is not invoked with
     * copy initialization since that is reserved for use with scalars and aggregates.
     *
     * Comment this out to test what occurs when it is deleted.
     */
    //WidgetWithDirectInitialization(const WidgetWithDirectInitialization& E) = delete;
    const int getID() {return id;}
    const double getPrice() {return price;}
private:  
    int id;
    double price; 
};

class InitializationTest {
    public:
    InitializationTest() = default;
    ~InitializationTest() = default;

    /** Basic copy initialization
     * 
     */
    void copyInitialization();

    /** Aggregate initialization is used for structures, arrays, etc...
     * 
     * Both aggregate initialization and copy initialization use an =. If an object is
     * already created using aggregate initialization, it can then be copied to another object
     * using copy initialization (note, both use the same syntax)
     * - This works for structures and unions
     * - Copy initialization does not work for an array
     *   int a1[3] = {1, 2, 3}; // aggregate initialization
     *   int as[3] = a1;        // error (not allowed)
     */
    void aggregateInitialization();

    /**
     * Uninitialized:
     * - If an object does not have an explicit initializer, then it will either be zeroed or
     *   indeterminate.
     * - It will be zeroed if it is:
     *   - declared static
     *   - declared thread_local
     *   - declared at namespace scope (the class is intantiated directly from a namespace, and
     *     not from within another class or function)
     * - Otherwise, it will be indeterminate
     */
    void determinateAndIndeterminate();

    /** Uniform initialization juus uses a bracket, with no equal sign.
     * 
     * It works for all types.
     */
    void uniformInitialization();

    void test();
    void print();
};