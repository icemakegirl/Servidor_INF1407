from sys import argv, stderr,exit
from socket import *
from socket import AF_INET, SOCK_STREAM, AI_ADDRCONFIG, AI_PASSIVE
from socket import IPPROTO_TCP, SOL_SOCKET, SO_REUSEADDR
from posix import abort
from os import fork
from arquivos_base.arquivo import * 
from arquivos_base.funcoes_usadas import *
#from datetime import datetime

def main():
    #host=None
    host='localhost'#Deixar host 

    enderecoHost = getEnderecoHost(host, porta)
    fd = criaSocket(enderecoHost)
    setModo(fd)#O que vai acontecer quando ele for desconectado, como ele vai ser tratado
    bindaSocket(fd, host,porta)
    print("Servidor pronto em", enderecoHost)
    escuta(fd)
    while True:
        (con, cliente) = fd.accept()
        pid = fork()
        if pid == 0:
            fd.close()
            print("Servidor connectado com ", cliente)
            while True:
                msg = con.recv(102400).decode('utf-8')
                if not msg: break
                mensagem=msg.split('\n')
                pega_URL=mensagem[0].split(' ')#Pega a primeira posicao da requisicao do cliente
                print('URL:',pega_URL[1])#Pega o caminho do arquivo no browser
                nome_arquivo=pega_URL[1].split('/')#Aqui ele vem com o caminho completo ex:/Servidor/paginas/teste1.html
                #print('SERV:',nome_arquivo)
                
                print("Nome Arq:",nome_arquivo[-1])#-1 para sempre pegar a ultima posicao da lista independente do tamanho
                try:
                    if '.'+pega_URL[1]==caminho_arq:#Entra aqui caso o caminho das paginas for digitado sem o arquivo
                        print(lista_arquivos[0])
                        caracteristica= caracteristicas_arquivo(lista_arquivos[0])# 0 :retorna tipo de arq, 1:extensao, e 3:modo de leitura
                        #Lendo o arquivo em binario e enviando linha a linha para o cliente
                        with open(caminho_arq+lista_arquivos[0],str(caracteristica[2])) as file:
                            requisicao=file.read()
                            Envia_pagina(con,requisicao,int(caracteristica[0]),str(caracteristica[1]))
                    elif not(nome_arquivo[-1]) in lista_arquivos:#Entra aqui caso o arquivo digitado nao estiver na lista
                        print("Não tem\n")
                        with open(Pagina_Erro,'r') as file:
                            requisicao=file.read()
                            Envia_pagina(con,requisicao,0,'html')
                    else:
                        caracteristica= caracteristicas_arquivo(nome_arquivo[-1])# 0 :retorna tipo de arq, 1:extensao, e 3:modo de leitura
                        #Lendo o arquivo em binario e enviando linha a linha para o cliente
                        
                        with open(caminho_arq+nome_arquivo[-1],str(caracteristica[2])) as file:
                            requisicao=file.read()
                            print('extensao:',str(caracteristica[1]))
                            Envia_pagina(con,requisicao,caracteristica[0],caracteristica[1])
                      
                except:
                    print("Nao foi Possivel abrir nenhum arquivo")
                    abort()
            print("Conexão terminada com ", cliente)
            
            con.close()
            exit()
        else:
            con.close()
    return

if __name__ == '__main__':
    main()