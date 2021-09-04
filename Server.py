from sys import argv, stderr,exit
from socket import getaddrinfo, socket
from socket import AF_INET, SOCK_STREAM, AI_ADDRCONFIG, AI_PASSIVE
from socket import IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR
from posix import abort
from os import fork

def getEnderecoHost(host,porta):
    try:
        enderecoHost = getaddrinfo(
        host,
        porta,
        family=AF_INET,
        type=SOCK_STREAM,
        proto=IPPROTO_TCP,
        flags=AI_ADDRCONFIG | AI_PASSIVE)
    except:
        print("Não obtive informações sobre o servidor (???)", file=stderr)
        abort()
    return enderecoHost

def criaSocket(enderecoServidor):
    fd = socket(enderecoServidor[0][0], enderecoServidor[0][1])
    if not fd:
        print("Não consegui criar o socket", file=stderr)
        abort()
    return fd

def setModo(fd):
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#Liberar o socket mais rapido possivel, coloca ele em reuso
    return
def bindaSocket(fd, host,porta):
    try:
        fd.bind((host, porta))
    except:
        print("Erro ao dar bind no socket do servidor", porta, file=stderr)
        abort()
    print("Serivor rodando ",host, porta)
    return

def escuta(fd):
    try:
        fd.listen(0)#Ele que manda na quantidade de pessoas
    except:
        print("Erro ao começar a escutar a porta", file=stderr)
        abort()
    print("Iniciando o serviço")
    return

'''def conecta(fd):
    (con, cliente) = fd.accept()
    print("Servidor conectado com", cliente)
    return con'''   

#/home/icemakegirl/Documentos/ProgWeb/paginas/teste1.html HTTP/1.1

def fazTudo(fd):
    while True:
        buffer = fd.recv(1024).decode("utf-8")#O servidor fica esperando escutar
        if not buffer:
            break
        print('==>', buffer)
        #aqui comeca a leitura do arquivo para da inicio a escrita da saida
        fd.send(bytearray(buffer, 'utf-8'))#Aqui pegar o arquivo, ler ele e mandar para o cliente
    print("Conexão terminada com", fd)
    fd.close()
    return    
def main():
    '''if len(argv) == 2:
        porta = int(argv[1])
    else:
        porta = 8752'''
    porta=8080
    host='localhost'#Deixar host none
    enderecoHost = getEnderecoHost(host,porta)
    fd = criaSocket(enderecoHost)
    setModo(fd)#O que vai acontecer quando ele for desconectado, como ele vai ser tratado
    bindaSocket(fd, host,porta)
    print("Servidor pronto em", enderecoHost)
    escuta(fd)
    while True:
        '''con = conecta(fd)
        if con == -1:
            continue
        '''
        (con, cliente) = fd.accept()
        pid = fork()
        if pid == 0:
            fd.close()
            print("Servidor connectado com ", cliente)
            while True:
                msg = con.recv(1024).decode("utf-8")
                if not msg: break
                print(cliente, msg)
                #fazTudo(con)
                con.send(bytearray(msg, 'utf-8'))
            print("Conexão terminada com ", cliente)
            
            con.close()
            exit()
        else:
            con.close()
        

    return

if __name__ == '__main__':
    main()