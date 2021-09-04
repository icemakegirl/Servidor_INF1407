from sys import argv, stderr
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, IPPROTO_TCP, AI_ADDRCONFIG
from posix import abort
from time import sleep


def getEnderecoServidor(host, porta):
    enderecoServidor=None#Converte um endereco servidor em um IP
    try:
        enderecoServidor = getaddrinfo(host,
        porta,
        family=AF_INET,
        type=SOCK_STREAM,
        proto=IPPROTO_TCP,
        flags=AI_ADDRCONFIG)
    except:
        print("Não obtive informações sobre servidor", file=stderr)
        abort()
    return enderecoServidor

def criaSocket(enderecoServidor):
    fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
    if not fd:
        print("Não consegui criar o socket")
        abort()
    
    return fd    

def conecta(socketfd, enderecoServidor):
    try:
        socketfd.connect(enderecoServidor[0][4])
    except :
        print("Erro ao tentar conexão com o servidor",
            enderecoServidor[0][4],file=stderr)
        abort()
    return

def fazOResto(fd):
    bufferSaida=-1
    while True:
        bufferSaida-=1
        #bufferSaida = input("Use o Comando GET:\n ")
        #if len(bufferSaida) == 0:
         #   break
        fd.send(bytearray(str(bufferSaida), 'utf-8'))#envia para o servidor
        sleep(10)
        bufferEntrada = fd.recv(1024)#Aguarda resposta do servidor
        print("==>", bufferEntrada)
    return

def main():
    if len(argv) == 3:
        host = argv[1]
        porta = int(argv[2])
    else:
        host = 'localhost'
        porta = 8080
    enderecoServidor = getEnderecoServidor(host, porta)
    socketfd = criaSocket(enderecoServidor)#Cria um arquivo descritivo
    conecta(socketfd, enderecoServidor)
    fazOResto(socketfd)
    socketfd.close()
    return



if __name__ == '__main__':
    main()


