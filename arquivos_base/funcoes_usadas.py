from time import sleep
from sys import argv, stderr,exit
from socket import *
from datetime import datetime
from posix import abort
from os import fork
from arquivos_base.arquivo import *


#Funcoes feitas para o trabalho
#Enviar os Headers para os clientes
def Envia_pagina(con,requisicao,tipo,extensao):
    con.send('HTTP/1.1 200 OK\r\n'.encode())
    if(tipo==1):
        con.send('Content-Type: image/{}\r\n'.format(extensao).encode())
        con.send('Accept-Ranges: bytes\r\n\r\n'.encode())
        con.send(requisicao)
    else:
                 
        con.send('Content-Type: text/{}\r\n ; charset=utf-8'.format(extensao).encode('utf-8'))
        now = datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
        con.send('Content-Length: 300\r\n'.encode('utf-8'))
        con.send('Date: {}\r\n\r\n'.format(now).encode('utf-8'))
        con.send(requisicao.encode('utf-8'))    
    con.shutdown(SHUT_RDWR)
    return
#Ela envia o modo de leitura e se o arquivo e tipo texto ou imagem   
def caracteristicas_arquivo(arquivo):
    separa=arquivo.split('.')

    if(separa[1] in ['png','gif','jpg','jpeg']):
        
        ext=separa[1].encode()
        modo_leitura='rb'
        simg=1
    else:
        
        modo_leitura='r'
        ext=separa[1]
        simg=0

    return [simg,ext,modo_leitura]
    
#Funcoes dos Slides-A BindaSocket tem um input caso não consiga entrar com a porta default do servidor
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

def setModo(fd):
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)#Liberar o socket mais rapido possivel, coloca ele em reuso
    return

def escuta(fd):
    try:
        fd.listen(0)#Ele que manda na quantidade de pessoas
    except:
        print("Erro ao começar a escutar a porta", file=stderr)
        abort()
    print("Iniciando o serviço")
    return

def bindaSocket(fd, host,porta):
    try:
        fd.bind((host, porta))
    except:
        print("Erro ao dar bind no socket do servidor digite outra porta", porta, file=stderr)
        NewPorta=int(input('digite outra Porta'))
        fd.bind((host, NewPorta))
        print("Serivor rodando ",host, NewPorta)
    return


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
