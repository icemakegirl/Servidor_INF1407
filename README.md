# Servidor_INF1407
Aluna: Joanne Carneiro - Matrícula: 1820362
#####
Para rodar o arquivo utilize:
####
--python3 Servidor.py
###
--Caso não seja permitido o uso da porta default do servidor a função BindaSocket permite que você de input de outra porta, mas é feito pelo terminal do servidor
###

--Existem 3 arquivos dentro da pasta arquivos_base
###
1ª é o de arquivo de configuracao
###
2ª é o arquivo que contem todas as funcoes usadas no Servidor.py
###
3ª é o arquivo de erro


Resumo da Implementacao
=================
<!--ts-->
*	[Método GET: Parcialmente Implementado, os arquivos tipo textos/html aparecem no browser mas as imagens ao invés de aparecerem é feito o download na máquina. Arquivos Javascript também estão sendo escritos na página do browser ao invés de ser feito o seu download
](#metodo_get)
* [Acesso Simultâneo do Cliente :  Implementado e funcionando nos testes feitos por mim.](#acesso)
* [Mensagem de erro: Implementado Caso o arquivo que o cliente colocou não esteja na lista aparece a página de erro.](#mensagem)
* [Página Default: Implementado, Caso o cliente digite só o caminho dos arquivos a página aberta é a primeira da lista](#default)
* [Emitir mensagem caso tenha inconsistência no arquivo de configuração: Não Implementado, mensagem de erro aparece caso não entre em uma das condições feitas na main mas ele não é feita para cada arquivo que foi aberto](#incon)
<!--te-->
