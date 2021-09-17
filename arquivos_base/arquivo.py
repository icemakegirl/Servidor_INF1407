lista_arquivos=['index.html','colorido.jpg',
'fantasy.png',
'minion.jpg',
'teste1.html','toushirou.gif','bonequinho.js','download.jpeg']
host = 'localhost'
caminho_arq=  './Servidor/paginas/'
porta = 8080

Pagina_Erro = './arquivos_base/erro.html'
#GET ./Servidor/paginas/fantasy.png HTTP/1.1
#GET ./Servidor/paginas/teste1.html HTTP/1.1
#GET ./Servidor/paginas/colorido.jpg HTTP/1.1
#GET ./Servidor/paginas/toushirou.gif HTTP/1.1\r\n\r\n
#'GET ./Servidor/paginas/bonequinho.js HTTP/1.1'