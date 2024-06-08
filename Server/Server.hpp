#pragma once

#include <sys/socket.h>
#include <netinet/in.h> 


#include <cstring>
#include <unistd.h>


#include <stdexcept>

#define PORT 8081
#define MAX 80

enum Exceptions{
    SOCKET_EXCEPTION,
    BIND_EXCEPTION,
    LISTEN_EXCEPTION,
    ACCEPT_EXCEPTION
};

class Server{
    int sockfd, connfd;
    socklen_t len;
    struct sockaddr_in servaddr, cli;

    
    void create();
    void assign();
    void bind_();
    void listen_();
    void accept_();


    void func(int connfd);

    void throw_exception(Exceptions exception);

    public:
    Server();
    void start();
};


