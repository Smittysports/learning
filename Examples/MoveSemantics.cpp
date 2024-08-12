#include "MoveSemantics.h"
#include <iostream>

MoveSemantics MoveSemantics::createMoveSemantics()
{
    MoveSemantics temp {{"one", "two", "three"}};
    return temp;
}

void MoveSemantics::addConstString(const std::string& str)
{
    m_strVals.push_back(str);
}

void MoveSemantics::addStringByValue(std::string str)
{
    m_strVals.push_back(str);
}

void MoveSemantics::addString(std::string& str)
{
    m_strVals.push_back(str);
}

void MoveSemantics::addString(std::string&& str)
{
    m_strVals.push_back(std::move(str));
}

void MoveSemantics::testMovingWithPassByValue()
{
    std::string testStr {"My test string"};
    // The testStr will be ivalidated after this function call
    addStringByValue(std::move(testStr));
    // The testStr is now no longer valid, even though the function accepted it by value
    addConstString("Yo");
}

const void MoveSemantics::print()
{
    for (const auto& str : m_strVals)
        std::cout << str << "\n";
}