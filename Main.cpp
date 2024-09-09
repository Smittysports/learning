#include <iostream>
#include <vector>
#include <list>
#include <functional>
#include <bitset>
#include "ConstTesting.h"
#include "AlignmentTesting.h"
#include "ViewTesting.h"
#include "ConceptsAndViews.h"
#include "PerfectForwarding.h"
#include "Threading/ThreadPool.h"
#include "Threading/Subscriber.h"
#include "Threading/SubscriptionManager.h"
#include "Examples/Initialization.h"
#include "Examples/MoveSemantics.h"
#include "Server/include/Networking.h"

enum Test
{
    TestNetworking,
    TestConstExpr,
    TestAlignment,
    TestCTAD,
    TestViews,
    TestThreadPool,
    TestSubscription,
    TestPerfectForwarding,
    TestInitialization,
    TestMoveSemantics,
    NumTests
};
std::bitset<Test::NumTests> testChoice {"0"};

void myTempFunc()
{
    std::cout << "MyTempFunc\n";
}

void configTests()
{
    //testChoice.set(Test::TestNetworking);
    testChoice.set(Test::TestThreadPool);
}

int main(int argc, char **argv)
{
    configTests();

    if (testChoice.test(Test::TestNetworking))
    {
        std::cout << "TestNetworking\n";
        Networking networking;
        networking.createConnection();
        std::cout << "Here\n";
    }

    if (testChoice.test(Test::TestConstExpr))
    {
        ConstantClass constantClass;

        // If a method is declared to return a constexpr, then it can be obtained at compile time like this
        constexpr int consIntVal = constantClass.getMax();

        std::cout << "BrianTest\n";
        std::cout << "Max = " << consIntVal << "\n";
    }

    if (testChoice.test(Test::TestAlignment))
    {
        AlignmentTestNotPadded align1;
        std::cout << "Sizeof AlignmentTestNotPadded = " << sizeOfAlignmentTestNotPadded << "\n";
        std::cout << "Alignof Alignment64Test = " << alignof(AlignmentTestNotPadded) << "\n";
        std::cout << "Sizeof data members = " << align1.getSizeOfMembers() << "\n";
        align1.showMemberAddresses();
        std::cout << "---------------------------------\n";

        AlignmentTestPadded align2;
        std::cout << "Sizeof AlignmentTestPadded = " << sizeOfAlignmentTestPadded << "\n";
        std::cout << "Alignof Alignment64Test = " << alignof(AlignmentTestPadded) << "\n";
        std::cout << "Sizeof data members = " << align2.getSizeOfMembers() << "\n";
        align2.showMemberAddresses();
        std::cout << "---------------------------------\n";

        Alignment64Test align3;
        std::cout << "Sizeof Alignment64Test = " << sizeOfAlignment64Test << "\n";
        std::cout << "Alignof Alignment64Test = " << alignof(Alignment64Test) << "\n";
        std::cout << "Sizeof data members = " << align3.getSizeOfMembers() << "\n";
        align3.showMemberAddresses();
    }

    if (testChoice.test(Test::TestCTAD))
    {
        // Before C++ 20
        //std::vector<int> vec{0, 8, 15,47, 11 ,42};
        //std::list<int> lst {0, 8, 15,47, 11 ,42};

        // After C++ 20, with Class Template Argument Deduction (CTAD)
        std::vector vec{0, 8, 15,47, 11 ,42};
        std::list lst {0, 8, 15,47, 11 ,42};

        // Template
        print(vec);
        // Function auto template
        print2(lst);
    }

    if (testChoice.test(Test::TestViews))
    {
        /*
        std::cout << "---------------------------------\n";
        std::cout << "Values in the vector: \n";
        rangedPrint(std::views::all(vec));    
        // Concept using a view that prints the first three elements
        std::cout << "First 3 values in the vector: \n";
        rangedPrint(std::views::take(vec, 3));
        // Same as above, but using the pipe symbol    
        rangedPrint(vec | std::views::take(3));
        // Same as above but apply a transformation to each element in the container
        std::cout << "First 3 values in the vector transformed: \n";
        rangedPrint(vec | std::views::take(3) |
                    std::views::transform([](auto v){
                        return v + 1;
                    }));
        std::cout << "Skip first 3 values in the vector: \n";
        rangedPrint(vec | std::views::drop(3));
        std::cout << "Skip first 3 values in the list: \n";
        rangedPrint(lst | std::views::drop(3));
        */
    }

    if (testChoice.test(Test::TestThreadPool))
    {
        ThreadPool threadPool;
        /*
        for (int i = 0; i < threadPool.getMaxNumThreads(); ++i)
        {
            threadPool.createThreadPoolThread();
        }
        */

        //threadPool.createConsumerThread();
        //threadPool.createProducerThread();
        
        //threadPool.joinProducerThread();
        //threadPool.joinConsumerThread();
    }

    if (testChoice.test(Test::TestSubscription))
    {
        SubscriptionManager subscriptionManager;
        Subscriber subscriber;
        // Bind will create a function object that can be stored in a std::function since it is callable
        std::function<void()> func = std::bind(&Subscriber::printSomething, subscriber, "Hello");
        subscriptionManager.addSubscription(func);
        func = std::bind(&Subscriber::printSomething, subscriber, "Brian");
        subscriptionManager.addSubscription(func);
        // - With a Lambda
        subscriptionManager.addSubscription([](){
            std::cout << "Lambdas are great!\n";
        });

        // - With a free function associated with a std::function
        std::function tempFunc = myTempFunc;
        subscriptionManager.addSubscription(tempFunc);
        // - With a free function
        subscriptionManager.addSubscription(myTempFunc);
        
        subscriptionManager.runAllSubscriptions();
    }

    if (testChoice.test(Test::TestPerfectForwarding))
    {
        ForwardingClass forwardingClass;
        forwardingClass.addBasicClass(1, true, 0.1f, std::vector<int>{11, 12, 13,14});
    }

    if (testChoice.test(Test::TestInitialization))
    {
        InitializationTest initializationTest;
        initializationTest.test();
    }

    if (testChoice.test(Test::TestMoveSemantics))
    {
        MoveSemantics ms1;
        std::string str {"Brian"};
        std::string str2 {"Smith"};
        ms1.addConstString("Test");
        ms1.addString(str);
        ms1.addString(std::move(str2));
        ms1.testMovingWithPassByValue();
        ms1.getClassWithNoMove().initStrVec();

        std::cout << "===============================\n";
        std::cout << "ms1 vector before move:\n";
        ms1.print();
        std::cout << "-------------------------------\n";

        MoveSemantics ms2{ms1};
        std::cout << "ms1 vector after copy:\n";
        ms1.print();
        std::cout << "-------------------------------\n";
        std::cout << "ms2 vector after copy:\n";
        ms2.print();
        std::cout << "-------------------------------\n";

        MoveSemantics ms3{std::move(ms1)};
        std::cout << "ms1 vector after move:\n";
        ms1.print();
        std::cout << "-------------------------------\n";
        std::cout << "ms3 vector after move:\n";
        ms3.print();
        std::cout << "-------------------------------\n";

        // Create a new object m4 by moving a new object returned by a creation method
        MoveSemantics ms4{ms3.createMoveSemantics()};
        std::cout << "ms4 vector:\n";
        ms4.print();
    }
    return 0;
}