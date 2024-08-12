#include "Initialization.h"
#include <iostream>

int zeroInitializedInt; // Zero initialized since it is declared at namespace scope
widget zeroInitializedWidget; // Zero initialized since it is declared at namespace scope
  
void InitializationTest::copyInitialization() {
    int i = 3;
    float fl = 5.34f;

    std::cout << "i = " << i << "\n";
    std::cout << "fl = " << fl << "\n";
}

void InitializationTest::aggregateInitialization() {
    // 1) Use = for aggregate initialization
    widget w1 = {1000, 6.5}; // Aggregate initialization
    int values[3] = {1, 2, 3};
    std::cout << "w1.id = " << w1.id << "\n";
    std::cout << "w1.price = " << w1.price << "\n";
    for (const auto& value : values) {
        std::cout << "value = " << value << "\n";
    }

    // 2) Use = for copy initialization (possible since w1 is already instantiated)
    widget w2 = w1; // Copy initialization
}

void InitializationTest::determinateAndIndeterminate() {
    int indeterminatInt;
    widget indeterminateWidget;
    widgetWithExplicitConstructor explicitWidget{};
    // This is value initialization (as of C++03) with roundabout syntax
    WidgetWithDirectInitialization widgetWithDirectInitialization = WidgetWithDirectInitialization();
    WidgetWithDirectInitialization defaultInitializion;
    // Direct initialization, not copy initialization, even though it is using the copy constructor
    WidgetWithDirectInitialization copyOfDirect(widgetWithDirectInitialization);
    // Copy initialization using the Constructor (not the assignment operator)
    // It uses the Constructor instead of the assignment operator since the object is being constructed
    // If it already existed, it would use the assignment
    WidgetWithDirectInitialization copy2OfDirect = widgetWithDirectInitialization;

    std::cout << "====================================================\n";
    std::cout << "zeroInitializedInt = " << zeroInitializedInt << "\n";
    std::cout << "indeterminatInt = " << indeterminatInt << "\n";

    std::cout << "zeroInitializedWidget id = " << zeroInitializedWidget.id << "\n";
    std::cout << "zeroInitializedWidget price = " << zeroInitializedWidget.price << "\n";

    std::cout << "indeterminateWidget id = " << indeterminateWidget.id << "\n";
    std::cout << "indeterminateWidget price = " << indeterminateWidget.price << "\n";

    std::cout << "explicitWidget id = " << explicitWidget.id << "\n";
    std::cout << "explicitWidget price = " << explicitWidget.price << "\n";

    std::cout << "widgetWithDirectInitialization id = " << widgetWithDirectInitialization.getID() << "\n";
    std::cout << "widgetWithDirectInitialization price = " << widgetWithDirectInitialization.getPrice() << "\n";
    
    std::cout << "defaultInitializion id = " << defaultInitializion.getID() << "\n";
    std::cout << "defaultInitializion price = " << defaultInitializion.getPrice() << "\n";

    std::cout << "copyOfDirect id = " << copyOfDirect.getID() << "\n";
    std::cout << "copyOfDirect price = " << copyOfDirect.getPrice() << "\n";

    std::cout << "copy2OfDirect id = " << copy2OfDirect.getID() << "\n";
    std::cout << "copy2OfDirect price = " << copy2OfDirect.getPrice() << "\n";
}

void InitializationTest::uniformInitialization() {
    int x{3};
    int arr[3] {1, 2, 3};
    WidgetWithDirectInitialization classTest{};

    std::cout << "------------------------- UniformInitialization -------------------------\n";
    std::cout << "x = " << x << "\n";
    for (const auto& value : arr) {
        std::cout << "value = " << value << "\n";
    }
    std::cout << "copy2OfDirect id = " << classTest.getID() << "\n";
    std::cout << "copy2OfDirect price = " << classTest.getPrice() << "\n";
}

void InitializationTest::test() {
    copyInitialization();
    aggregateInitialization();
    determinateAndIndeterminate();
    uniformInitialization();
}
void InitializationTest::print() {

}