'''Caso queira testar a página de erro você pode usar:
-localhost:porta
--localhost:porta/Servidor/paginas/arquivo_fora_do_servidor
--localhost:porta/arquivo_fora_do_servidor

Página Default Aparece com:
--localhost:porta/Servidor/paginas/

Páginas aparece no Servidor com:
	--localhost:porta/Servidor/paginas/arquivo_dentro_do_servidor
	--localhost:porta/arquivo_dentro_do_servidor
'''



lista_arquivos=['index.html','colorido.jpg',
'fantasy.png',
'minion.jpg',
'teste1.html','toushirou.gif','bonequinho.js','download.jpeg']
caminho_arq=  './Servidor/paginas/'
porta = 8080

Pagina_Erro = './arquivos_base/erro.html'
