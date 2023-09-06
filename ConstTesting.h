#pragma once

class ConstantClass
{
    public:
        ConstantClass() = default;
        ~ConstantClass() = default;

        constexpr int getMax()
        {
            return m_maxIntVal;
        }

    private:
        constexpr static int m_maxIntVal = 55;
};