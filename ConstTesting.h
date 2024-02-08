#pragma once

class ConstantClass
{
    public:
        ConstantClass() = default;
        ~ConstantClass() = default;

        /** A constexpr method can be used to obtain a constexpr variable during compile
         * time. The caller of getMax must be declared as constexpr as well or it will revert
         * to runtime.
         *
         * The 'auto followed by the trailing return syntax is not mandatory but is used a lot
         * more in modern programming since it reads 'left to right' like the rest of the
         * function signature.
         *
         * The use of constexpr can be seen easily by putting a breakpoint on the caller of
         * this method and looking at the assembler. It should just be 1 line of code instead
         * of a jump to a function.
         */
        constexpr auto getMax() -> int
        {
            return m_maxIntVal;
        }

    private:
        constexpr static int m_maxIntVal = 55;
};