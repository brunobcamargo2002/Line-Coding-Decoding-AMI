#include "Server.hpp"

Server::Server(){
}

void Server::start()
{
    create();
    assign();
    bind_();
    listen_();
    accept_();
    func(connfd);
}

//Função responsável por criar o socket do servidor
void Server::create()
{
    sockfd = socket(AF_INET, SOCK_STREAM, 0); //Cria um socket e retorna o endereço do file descriptor 
    if(sockfd == -1)
        throw_exception(SOCKET_EXCEPTION);
}

//Define endereço e porta
void Server::assign()
{
    servaddr.sin_family = AF_INET; //endereço do tipo internet
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY); //converte o address do local host para valor significado para reg da cpu
    servaddr.sin_port = htons(PORT); //converte a porta para valor significado para reg da cpu
}

//Vincula o endereço e porta ao socket
void Server::bind_()
{
    if(bind(sockfd,(sockaddr*) &servaddr, sizeof(servaddr)))
        throw_exception(BIND_EXCEPTION);
}

//Começa a escutar a porta de entrada
void Server::listen_(){
    if(listen(sockfd, 5) != 0)
        throw_exception(LISTEN_EXCEPTION);
}

//Aceita a requisição
void Server::accept_()
{
    len = sizeof(cli);
    connfd = accept(sockfd,(sockaddr*) &cli, &len);
    if(connfd<0)
        throw_exception(ACCEPT_EXCEPTION);
}

void Server::func(int connfd_) 
{ 
    char buff[MAX]; 
    int n; 
    // infinite loop for chat 
    for (;;) { 
        bzero(buff, MAX); 
   
        // read the message from client and copy it in buffer 
        read(connfd, buff, sizeof(buff)); 
        // print buffer which contains the client contents 
        printf("From client: %s\t To client : ", buff); 
        bzero(buff, MAX); 
        n = 0; 
        // copy server message in the buffer 
        while ((buff[n++] = getchar()) != '\n') 
            ; 
   
        // and send that buffer to client 
        write(connfd, buff, sizeof(buff)); 
   
        // if msg contains "Exit" then server exit and chat ended. 
        if (strncmp("exit", buff, 4) == 0) { 
            printf("Server Exit...\n"); 
            break; 
        } 
    } 
}
void Server::throw_exception(Exceptions exception)
{
    switch(exception){
        case SOCKET_EXCEPTION: throw std::runtime_error("Failed to create a socket");
        case BIND_EXCEPTION: throw std::runtime_error("Failed to bind the assign to socket");
        case LISTEN_EXCEPTION: throw std::runtime_error("Failed to listen");
        case ACCEPT_EXCEPTION: throw std::runtime_error("Failed to accept the client");
    }
}
