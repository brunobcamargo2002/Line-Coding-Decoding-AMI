#include <netinet/in.h> 
#include <iostream>

#include "Server/Server.hpp"

int main(int argc, char ** argv){
    Server server;

    server.start();
}