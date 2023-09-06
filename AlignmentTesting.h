#pragma once
#include <iostream>

#pragma pack(1)
#pragma pack(show)
class AlignmentTestNotPadded
{
    public:
        int test;
        char k;
        char str[10];
        int* p;
        short sh;
        float fl;
    
    constexpr unsigned int getSizeOfMembers()
    {
        return sizeof(test) + sizeof(k) + sizeof(str) +
               sizeof(p) + sizeof(sh) + sizeof(float);
    }

    void showMemberAddresses()
    {
        std::cout << "Type     " << "Size "      << "Alignment "                             << "Name " << "Address\n";
        std::cout << "int      " << sizeof(test) << "         " << alignof(decltype(test))   << "    test " << &test << "\n";
        std::cout << "char     " << sizeof(k)    << "         " << alignof(decltype(k))      << "    k    " << (void*)&k << "\n";
        std::cout << "char[10] " << sizeof(str)  << "        " << alignof(decltype(str))     << "    str  " << &str << "\n";
        std::cout << "int*     " << sizeof(p)    << "         " << alignof(decltype(p))      << "    p    " << &p << "\n";
        std::cout << "short    " << sizeof(sh)   << "         " << alignof(decltype(sh))     << "    sh   " << &sh << "\n";
        std::cout << "float    " << sizeof(fl)   << "         " << alignof(decltype(fl))     << "    fl   " << &fl << "\n";
    }
};
constexpr static int sizeOfAlignmentTestNotPadded = sizeof(AlignmentTestNotPadded);

#pragma pack()
#pragma pack(show)
class AlignmentTestPadded
{
    public:
        int test;
        char k;
        char str[10];
        int* p;
        short sh;
        float fl;
    
    constexpr unsigned int getSizeOfMembers()
    {
        return sizeof(test) + sizeof(k) + sizeof(str) +
               sizeof(p) + sizeof(sh) + sizeof(float);
    }

    void showMemberAddresses()
    {
        std::cout << "Type     " << "Size "      << "Alignment "                             << "Name " << "Address\n";
        std::cout << "int      " << sizeof(test) << "         " << alignof(decltype(test))   << "    test " << &test << "\n";
        std::cout << "char     " << sizeof(k)    << "         " << alignof(decltype(k))      << "    k    " << (void*)&k << "\n";
        std::cout << "char[10] " << sizeof(str)  << "        " << alignof(decltype(str))     << "    str  " << &str << "\n";
        std::cout << "int*     " << sizeof(p)    << "         " << alignof(decltype(p))      << "    p    " << &p << "\n";
        std::cout << "short    " << sizeof(sh)   << "         " << alignof(decltype(sh))     << "    sh   " << &sh << "\n";
        std::cout << "float    " << sizeof(fl)   << "         " << alignof(decltype(fl))     << "    fl   " << &fl << "\n";
    }
};
constexpr static int sizeOfAlignmentTestPadded = sizeof(AlignmentTestPadded);

class alignas(64) Alignment64Test
{
    public:
        int test;
        char k;
        char str[10];
        int* p;
        short alignas(16) sh;
        float fl;
    
    constexpr unsigned int getSizeOfMembers()
    {
        return sizeof(test) + sizeof(k) + sizeof(str) +
               sizeof(p) + sizeof(sh) + sizeof(float);
    }

    void showMemberAddresses()
    {
        std::cout << "Type     " << "Size "      << "Alignment "                             << "Name " << "Address\n";
        std::cout << "int      " << sizeof(test) << "         " << alignof(decltype(test))   << "    test " << &test << "\n";
        std::cout << "char     " << sizeof(k)    << "         " << alignof(decltype(k))      << "    k    " << (void*)&k << "\n";
        std::cout << "char[10] " << sizeof(str)  << "        " << alignof(decltype(str))     << "    str  " << &str << "\n";
        std::cout << "int*     " << sizeof(p)    << "         " << alignof(decltype(p))      << "    p    " << &p << "\n";
        std::cout << "short    " << sizeof(sh)   << "         " << alignof(decltype(sh))     << "    sh   " << &sh << "\n";
        std::cout << "float    " << sizeof(fl)   << "         " << alignof(decltype(fl))     << "    fl   " << &fl << "\n";
    }
};
constexpr static int sizeOfAlignment64Test = sizeof(Alignment64Test);

