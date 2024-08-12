#pragma once

/** \page Move Semantics
 * The definition of 'semantics' is 'The meaning of'.
 * Ex... For basic addition:
 *     The value of a + b (where a is 5 and b is 3) is 8 because the semantics of the + operator is
 *     to take the numerical sum of its operands.
 * Ex... For strings:
 *     The value of a + b (where a is hello and b is world) is "helloworld" because the semantics
 *     of the + operator is to concatenate its operands.
 * Ex... For Copy and Move:
 *     We have the same operator = which has a different meaning in different situations.
 *
 * Move semantics utilize rvalue reference.
 * - Ordinary references that only use 1 & are called lvalue references
 * 
 * The std::move() utility
 * - Resides in the utility header, #include <utility>
 * - Tells the compiler "I no longer need this value here"
 * - Is a helper function to force move semantics on values
 * - If the caller does not have the ability to utilize move semantics, it will resort to copy semantics.
 * - For generic code, we should always use std::move on values we no longer need so that all uses can be supported
 * - std::move is safe for fundamental data types, like int, but they will just be copied
 * - Objects that are const cannot be moved. If there are appropriate copy semantics, std::move will call it, otherwise
 *   it will be a compile error
 * 
 * Return values
 * - A const return value cannot be moved. Because of this, it is no longer good style to return by value with const.
 * - If const is needed for the address of an object, it is better to return it with getRef() or getPtr() and use
 *   move semantics for the getValue()
 * 
 * Move Constructor
 * - The default move constructor will work for members that benefit from it (such as std::string and std::vector)
 * - Members that do not already have Move constructors will require the Move constructor to be overridden to
 *   support them.
 * - The automatic generation of the Move Constructor and Move Assignemnt Operator is disabled if on of the following is user-declared:
 *   Note: User declared also includes an empty declaration, using '= default', and virtual base class destructors
 *   - Copy constructor
 *   - Copy assignment operator
 *   - Another move operation
 *   - Destructor
 * - Auto generated move constructors may break member that have restrictions on values, reference semantics, and no default constructed state
 */

#include <string>
#include <vector>

/**
 * This class must implement a move or copy operator in order for another class to move or copy it.
 * ie... They cannot be deleted.
 * 
 * Ex... If the MoveSemantics class has a member of this class, it will fail to move or copy itself
 * unless this class also has move semantics.
 * 
 * The move of the containing class will also move this class and its m_strVec. A copy will do the same.
*/
class ClassWithNoMove
{
    public:
        ClassWithNoMove() = default;
        ClassWithNoMove(std::vector<std::string> str){m_strVec = str;}
        ~ClassWithNoMove() = default;
        ClassWithNoMove(ClassWithNoMove&&) = default;
        ClassWithNoMove& operator=(ClassWithNoMove&&) = default;
        ClassWithNoMove(const ClassWithNoMove&) = default;
        ClassWithNoMove& operator=(const ClassWithNoMove&) = default;

        void initStrVec(){m_strVec.assign({"a", "b","c"});}
    private:
        std::vector<std::string> m_strVec{};
};

/** The MoveSemantics class is used to provide a class for testing all the capabilites of Move semantics.
 * 
 */
class MoveSemantics
{
    public:
        /** Default constructor */
        MoveSemantics() = default;

        /** Creates a MoveSemantics object that initializes the m_strVals to strVec */
        MoveSemantics(std::vector<std::string> strVec) : m_strVals{strVec} {};

        /** Destructor */
        ~MoveSemantics() = default;

        /** Move Constructor
         *
         * The default move constructor will move the m_strVals vector
         */
        MoveSemantics(MoveSemantics&& tms) = default;

        /** Move assignment operator
         * 
         * Use this instead of the Copy assignment if the tms is no longer needed.
         *
         * @param tms Takes another MoveSemantics object and moves it to this object.
         * This parameter is not const since it must have its data removed. 
         * 
         * The modified tms must still be valid, but it is now in an unspecified state.
         * - This means that it can be used, as long as the caller does not make any assumptions oabout its value
         * 
         * @return MoveSemantics Returns a reference to this new object
         */
        MoveSemantics& operator=(MoveSemantics&& tms) = default;

        /** Copy Constructor
         * 
         * The default copy constructor will make a complete copy of the m_strVals vector
         */
        MoveSemantics(const MoveSemantics& tms) = default;

        /** Copy assignment operator
         * 
         * Use this instead of the Move assignment if the tms is still needed.
         * 
         * @param tms Takes another MoveSemantics object and copies it to this object.
         * This parameter is const since it is only copied.
         * 
         * @return MoveSemantics Returns a reference to this new object
         */
        MoveSemantics& operator=(const MoveSemantics& tms) = default;

        /** Returning a local copy of a class by value will use Move semantics */
        MoveSemantics createMoveSemantics();

        /** Add a string to the m_strVals vector.
         *
         * @param intVal This method accepts a constant string parameter. Adding this to the m_strVals
         * vector will utilize Copy semantics since Move semantics require non-const parameters.
         */
        void addConstString(const std::string& str);
        
        void addStringByValue(std::string str);

        /** Add a string to the m_strVals vector.
         *
         * @param intVal This method accepts a non-constant string parameter that is an lvalue reference.
         * Adding this to the m_strVals vector will utilize Copy semantics.
         */
        void addString(std::string& str);

        /** Move a string to the m_strVals vector
         *
         * @param intVal This method accepts a non-constant string parameter. Adding this to the m_strVals
         * vector will utilize Move semantics since they require non-const parameters.
         */
        void addString(std::string&& str);

        /** Passing a variable by value, but using std::move on it, will cause it to be moved even though
         * the function accepts it by value.
         * 
         * The variable in the function will be initialized with the value being moved.
         */
        void testMovingWithPassByValue();

        /** Shows all the string in the m_strVals vector */
        const void print();

        ClassWithNoMove& getClassWithNoMove() {return m_classWithNoMove;}

    private:
        bool m_isUnspecified{};
        std::vector<std::string> m_strVals{};
        ClassWithNoMove m_classWithNoMove;
};