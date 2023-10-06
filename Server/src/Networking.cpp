#include "Networking.h"
#include <iostream>
#include <chrono>
#include <thread>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment (lib, "Ws2_32.lib")

void Networking::createConnection()
{
    std::cout << "createConnection()\n";

    std::jthread networkingThread(&Networking::tcpThread, this);

    std::cout << "createConnection finished\n";
}

int Networking::udpThread()
{
    sockaddr_in server, client;

    // initialize winsock
    WSADATA wsa;
    std::cout << "Initializing Winsock\n";
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0)
    {
        std::cout << "Failed. Error Code: " << WSAGetLastError() << "\n";
        return 1;
    }

    // create a socket
    std::cout << "Create a socket.\n";
    SOCKET server_socket;
    if ((server_socket = socket(AF_INET, SOCK_DGRAM, 0)) == INVALID_SOCKET)
    {
        std::cout << "Could not create socket: " << WSAGetLastError() << "\n";
    }

    // prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(m_ipAddress.c_str());
    server.sin_port = htons(DEFAULT_PORT);

    char addressBuf[512];
    inet_ntop( AF_INET, &server.sin_addr, addressBuf, sizeof(addressBuf));
    std::cout << "IP Address: " << addressBuf << ":" << DEFAULT_PORT << "\n";

    // bind
    std::cout << "Binding\n";
    if (bind(server_socket, (sockaddr*)&server, sizeof(server)) == SOCKET_ERROR)
    {
        std::cout << "Bind failed with error code: %d" << WSAGetLastError() << "\n";
        return 1;
    }

    while (true)
    {
        std::cout << "Waiting for data...\n";
        char message[DEFAULT_BUFLEN] = {};

        // try to receive some data, this is a blocking call
        int message_len;
        int slen = sizeof(sockaddr_in);
        if (message_len = recvfrom(server_socket, message, DEFAULT_BUFLEN, 0, (sockaddr*)&client, &slen) == SOCKET_ERROR)
        {
            std::cout << "recvfrom() failed with error code: %d" << WSAGetLastError() << "\n";
            return 1;
        }

        // print details of the client/peer and the data received
        std::cout << "Received packet from " << inet_ntoa(client.sin_addr) << ":" << ntohs(client.sin_port) << "\n";
        std::cout << "Data: " << message << "\n";

        // reply the client with the same data
        if (sendto(server_socket, message, strlen(message), 0, (sockaddr*)&client, sizeof(sockaddr_in)) == SOCKET_ERROR)
        {
            std::cout << "sendto() failed with error code: " << WSAGetLastError() << "\n";
            return 1;
        }
    }

    closesocket(server_socket);
    WSACleanup();
}

int Networking::tcpThread()
{
    WSADATA wsaData;
    int iResult = 0;
    SOCKET ListenSocket = INVALID_SOCKET;
    SOCKET ClientSocket = INVALID_SOCKET;

    struct addrinfo *result = NULL;
    struct addrinfo hints;

    int iSendResult;
    char recvbuf[DEFAULT_BUFLEN];
    int recvbuflen = DEFAULT_BUFLEN;

    std::cout << "Initialize Winsock:\n";
    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0) {
        std::cout << "WSAStartup failed with error: " << iResult << "\n";
        return 1;
    }

    ZeroMemory(&hints, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    hints.ai_flags = AI_PASSIVE;

    // Resolve the server address and port
    std::cout << "Resolve the server address and port:\n";
    iResult = getaddrinfo(NULL, std::to_string(DEFAULT_PORT).c_str(), &hints, &result);
    if ( iResult != 0 ) {
        std::cout << "getaddrinfo failed with error: " << iResult << "\n";
        WSACleanup();
        return 1;
    }

    // Create a SOCKET for the server to listen for client connections.
    std::cout << "Create a SOCKET for the server to listen for client connections:\n";
    ListenSocket = socket(result->ai_family, result->ai_socktype, result->ai_protocol);
    if (ListenSocket == INVALID_SOCKET) {
        std::cout << "socket failed with error: " << WSAGetLastError() << "\n";
        freeaddrinfo(result);
        WSACleanup();
        return 1;
    }
    struct sockaddr_in address;
    address.sin_family = AF_INET; 
    address.sin_addr.s_addr = inet_addr(m_ipAddress.c_str());
    address.sin_port = htons(DEFAULT_PORT); 

    // Setup the TCP listening socket
    std::cout << "Setup the TCP listening socket:\n";
    iResult = bind( ListenSocket, (struct sockaddr*)&address, sizeof(address));
    //iResult = bind( ListenSocket, result->ai_addr, (int)result->ai_addrlen);
    if (iResult == SOCKET_ERROR) {
        std::cout << "bind failed with error: " << WSAGetLastError() << "\n";
        freeaddrinfo(result);
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    freeaddrinfo(result);

    std::cout << "Listen:\n";
    iResult = listen(ListenSocket, SOMAXCONN);
    if (iResult == SOCKET_ERROR) {
        std::cout << "listen failed with error: " << WSAGetLastError() << "\n";
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    // Accept a client socket
    std::cout << "Accept a client socket:\n";
    ClientSocket = accept(ListenSocket, NULL, NULL);
    if (ClientSocket == INVALID_SOCKET) {
        std::cout << "accept failed with error: " << WSAGetLastError() << "\n";
        closesocket(ListenSocket);
        WSACleanup();
        return 1;
    }

    // No longer need server socket
    closesocket(ListenSocket);

    // Receive until the peer shuts down the connection
    do {

        iResult = recv(ClientSocket, recvbuf, recvbuflen, 0);
        if (iResult > 0) {
            std::cout << "Bytes received: " << iResult << "\n";
            std::cout << "Data received: " << recvbuf << "\n";

            char htmlResponse[512] = "HTTP/1.1 200 OK";

            iSendResult = send( ClientSocket, htmlResponse, sizeof(htmlResponse), 0 );
            if (iSendResult == SOCKET_ERROR) {
                std::cout << "send failed with error: " << WSAGetLastError() << "\n";
                closesocket(ClientSocket);
                WSACleanup();
                return 1;
            }
            std::cout << "Bytes sent: " << iSendResult << "\n";
        }
        else if (iResult == 0)
            std::cout << "Connection closing:\n";
        else  {
            std::cout << "recv failed with error: " << WSAGetLastError() << "\n";
            closesocket(ClientSocket);
            WSACleanup();
            return 1;
        }

    } while (iResult > 0);

    // shutdown the connection since we're done
    iResult = shutdown(ClientSocket, SD_SEND);
    if (iResult == SOCKET_ERROR) {
        std::cout << "Shutdown failed with error: " << WSAGetLastError() << "\n";
        closesocket(ClientSocket);
        WSACleanup();
        return 1;
    }

    // cleanup
    closesocket(ClientSocket);
    WSACleanup();
    return 0;
}
