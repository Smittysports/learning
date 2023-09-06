#include <iostream>
#include <vector>
#include <list>
#include <functional>
#include "ConstTesting.h"
#include "AlignmentTesting.h"
#include "ViewTesting.h"
#include "ConceptsAndViews.h"
#include "PerfectForwarding.h"
#include "Threading/ThreadPool.h"
#include "Threading/Subscriber.h"
#include "Threading/SubscriptionManager.h"

void myTempFunc()
{
    std::cout << "MyTempFunc\n";
}

int main(int argc, char **argv)
{
    ConstantClass constantClass;

    std::cout << "BrianTest\n";
    std::cout << "Max = " << constantClass.getMax() << "\n";

    // -------------------------- Alignment

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

    // -------------------------- CTAD

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

    // -------------------------- Views
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

    // -------------------------- Thread Pool
    /*
    ThreadPool threadPool;
    for (int i = 0; i < threadPool.getMaxNumThreads(); ++i)
    {
      threadPool.createThreadPoolThread();
    }

    threadPool.createConsumerThread();
    threadPool.createProducerThread();
    
    threadPool.joinProducerThread();
    threadPool.joinConsumerThread();
    */

    // -------------------------- Subscription
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

    // -------------------------- Perfect Forwarding
    ForwardingClass forwardingClass;
    forwardingClass.addBasicClass(1, true, 0.1f, std::vector<int>{11, 12, 13,14});
    return 0;
}