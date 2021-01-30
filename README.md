## Terminal

É um emulador de linhas de comandos que dispensa o uso de interface gráfica e facilita a automação de processos por meio de comandos, bastante utilizado por profissionais da área de TI, e podendo ser acessado pelo atalho **CTRL + ALT + T**.


#### Comandos básicos


Exibir o path atual

	pwd

Exibir todo o conteúdo de uma pasta

	ls #Para listar os arquivos
	ls -l #Para listar os arquivos com mais detalhamento 
	ls -a #Para listar arquivos ocultos
	ls --help #Para consultar o manual do comando ls
	clear #Limpa a tela.
	
Comandos de navegação:
	
	cd~ #Para ir para o diretório home
	cd/ #Para ir para o diretório raiz.
	cd <nome_da_pasta> # Para entrar em uma pasta
	cd .. #Para sair de uma pasta
 
Manipular pastas e arquivos

	mkdir <nome_da_pasta> #Cria uma pasta.
	rmdir <nome_da_pasta> #Remove a pasta.
	mv <pasta1> <pasta2> #Renomear a pasta1 com o nome da pasta2
	mv <pasta1> </path> #Mover a pasta1 para o path.
	cp <arquivo_ou_pasta> <path_destino> #Copia uma pasta ou arquivo para algum path.

	totch <nome_do_arquivo> #Cria um novo arquivo.
	rm <nome_do_arquivo_ou_pasta> #Remove o arquvio ou pasta.
	rm -r <nome_da_pasta> #Remove a pasta e tudo que há nela.

Ver histórico de comandos digitados

	history



#### Atalhos do teclado no terminal

 - Ctrl+c : Cancela o comando atual em funcionamento (incluindo programas abertos pelo terminal).
 - Ctrl+z : Pausa o comando em execução.
 - Ctrl+d : Sai da sessão atual.
 - Ctrl+w : Apaga uma palavra da linha atual.
 - Ctrl+u : apaga a linha inteira.
 - Ctrl+r : Busca um comando recente.
 - Ctrl+l : Limpa o terminal.



#### Exercício de aprendizado de comandos 

Exercícios Práticos de Revisão

1) Abra o Terminal
2) Crie uma Pasta de nome Ubuntu dentro da Pasta Documentos
3) Mova esta Pasta para o diretório Pessoal
4) Crie um arquivo vazio de nome teste.txt dentro da Pasta Ubuntu
5) Renomeie este Arquivo como linux.txt
6) Crie uma cópia deste arquivo na Pasta Downloads
7) Exiba todos os comandos digitados no Terminal
8) Execute a ajuda do comando ls
9) Execute o manual do comando mv
10) Pare a execução do manual
11) Saia do Terminal utilizando sequência de teclas
12) Exclua a pasta Ubuntu
13) Exclua o arquivo linux.txt 
14) Limpe o terminal
15) Utilize o comando para sair do terminal

### Referências

Digital Inovation One: Linux: Introdução ao sistema operacional


## Editando textos com o nano

O Nano é um editor de texto simples, baseado no terminal Linux, bastante útil principalmente em situações em que não há interface gráfica para editores mais complexos.

	nano <nome_do_arquivo> #Abre um arquivo ou cria caso o arquivo não exista.



