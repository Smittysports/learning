#include "Networking.h"
#include <iostream>
#include <chrono>
#include <thread>

void Networking::createConnection()
{
    std::cout << "createConnection()\n";

    auto lambda=[]()
    {
        int i = 0;
        while (i++ < 10)
        {
            std::cout << "Waiting\n";
            std::this_thread::sleep_for(std::chrono::seconds(3));
        }
    };

    std::jthread networkingThread(lambda);

    std::cout << "createConnection finished\n";
}

void Networking::AcceptThread()
{

}
