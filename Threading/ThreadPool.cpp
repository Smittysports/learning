#include "ThreadPool.h"
#include <iostream>
#include <random>
#include <any>

static int s_producer_int = 0;
static int s_consumer_int = 0;

ThreadPool::ThreadPool()
    : m_filePath("C:/dev/logs/BrianThreadPool.txt")
    , m_maxNumThreads(std::thread::hardware_concurrency() / 2)
{
    std::string myPath = std::filesystem::absolute(m_filePath).string();
    m_outputFile.open(myPath);
    m_outputFile << "Max number of threads = " << this->getMaxNumThreads() << std::endl;
    createInitialWorkerThreads();
}

ThreadPool::~ThreadPool()
{
    if (m_outputFile.is_open())
    {
        std::scoped_lock lock(m_fileMutex);
        m_outputFile.close();
    }
}

void ThreadPool::createInitialWorkerThreads()
{
    for (unsigned int i = 0; i < m_maxNumThreads; ++i) 
        m_threads.emplace_back(std::thread(&ThreadPool::ThreadLoop, this));    
}

void ThreadPool::addJob(const std::function<void()>& job)
{
    m_jobsToRun.push(job);
}

void ThreadPool::ThreadLoop()
{
    while (true)
    {
        std::function<void()> task;
        // ThreadSafeQueue.pop() will pend waiting for a job to be added
        task = m_jobsToRun.pop();
        task();
    }
}

void ThreadPool::createThreadPoolThread()
{
    auto f = [&]() {
        std::this_thread::sleep_for(std::chrono::milliseconds(2000));
        std::scoped_lock lock(m_fileMutex);
        m_outputFile << "Thread #" << s_producer_int++ << std::endl;
    };

    this->addJob(f);
}

/////// For testing basic threads without a threadpool

void ThreadPool::testThread()
{ 
    auto f = [&]() {
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        this->m_queue.push(s_producer_int++);
    };

    std::thread test_thread_object = std::thread{f};
    m_test_thread_object.detach();
}

unsigned int ThreadPool::getThreadQueueCount()
{
    unsigned int count = m_queue.GetNumQueueEntries();
    std::scoped_lock lock(m_fileMutex);
    m_outputFile << "Number of queue entries = " << count << std::endl;
    return count;
}

std::queue<int> ThreadPool::getAllThreadValues(bool verbose)
{
    std::queue<int> tempQueue;
    m_queue.swap(tempQueue);

    if (verbose)
    {
        std::queue<int> copyQueue = tempQueue;
        while (!copyQueue.empty())
        {
        std::scoped_lock lock(m_fileMutex);
        m_outputFile << "Value = " << copyQueue.front() << std::endl;
        copyQueue.pop();
        }
    }
    return tempQueue;
}

int ThreadPool::getThreadValue()
{
    return m_queue.pop();
}

//////// For testing promise and future

void ThreadPool::createProducerThread()
{
    auto f = [&]() {
        std::this_thread::sleep_for(std::chrono::milliseconds(2000));
        try
        {
            m_promise.set_value(11);
        }
        catch (std::exception& e)
        {
            std::scoped_lock lock(m_fileMutex);
            m_outputFile << "Producer thread, exception setting value: " << e.what()<< std::endl;
            //m_promise.set_exception(std::current_exception());
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(2000));
        std::scoped_lock lock(m_fileMutex);
        m_outputFile << "Producer thread finished waiting" << std::endl;
    };

    m_producer_thread_object = std::thread{f};
}

void ThreadPool::createConsumerThread()
{
    auto f = [&]() {
        std::future<int> futureVal = m_promise.get_future();
        std::scoped_lock lock(m_fileMutex);

        try
        {
            m_outputFile << "Consumer thread, future val = " << futureVal.get() << std::endl;
        }
        catch (std::exception& e)
        {
            m_outputFile << "Consumer thread, exception getting value " << e.what() << std::endl;
        }      
    };

    m_consumer_thread_object = std::thread{f};
}
