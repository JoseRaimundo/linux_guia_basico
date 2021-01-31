## Terminal

É um emulador de linhas de comandos que dispensa o uso de interface gráfica e facilita a automação de processos por meio de comandos, bastante utilizado por profissionais da área de TI, e podendo ser acessado pelo atalho **CTRL + ALT + T**.


#### Comandos básicos

	pwd #Exibir o path atual.
	ls #Para listar os arquivos
	ls -l #Para listar os arquivos com mais detalhamento 
	ls -a #Para listar arquivos ocultos
	ls --help #Para consultar o manual do comando ls
	clear #Limpa a tela.
	
#### Comandos de navegação:
	
	cd~ #Para ir para o diretório home
	cd/ #Para ir para o diretório raiz.
	cd <nome_da_pasta> # Para entrar em uma pasta
	cd .. #Para sair de uma pasta
 
#### Manipular pastas e arquivos

	mkdir <nome_da_pasta> #Cria uma pasta.
	rmdir <nome_da_pasta> #Remove a pasta.
	mv <pasta1> <pasta2> #Renomear a pasta1 com o nome da pasta2
	mv <pasta1> </path> #Mover a pasta1 para o path.
	cp <arquivo_ou_pasta> <path_destino> #Copia uma pasta ou arquivo para algum path.

	totch <nome_do_arquivo> #Cria um novo arquivo.
	rm <nome_do_arquivo_ou_pasta> #Remove o arquvio ou pasta.
	rm -r <nome_da_pasta> #Remove a pasta e tudo que há nela.
	
#### Fluxo de execução

Utilize o simbolo **&** e **&&** para executar mais de um comando por vez.

	<comando1> & <comando2> #Executa dois comandos com uma quebra de execução.
	<comando1> && <comando2> #Executa dois comandos com uma mesma chamada (sem quebra do texto exibido).

Exemplos:

	pwd & ls
	pwd && ls
	mkdir pasta && cd pasta && pwd

#### Atalhos do teclado no terminal

 - Ctrl+c : Cancela o comando atual em funcionamento (incluindo programas abertos pelo terminal).
 - Ctrl+z : Pausa o comando em execução.
 - Ctrl+d : Sai da sessão atual.
 - Ctrl+w : Apaga uma palavra da linha atual.
 - Ctrl+u : apaga a linha inteira.
 - Ctrl+r : Busca um comando recente.
 - Ctrl+l : Limpa o terminal.




## Manipulando arquivos de texto no Linux

Manipular arquivos de texto no Linux é algo importante, pois este tipo de arquivo apresenta uma estrutura simples que dispensa o uso de interface ou de programas mais avançados para serem editados, além de possibilitar em alguns casos, salvar informações, configurações, ou log de programas, etc.

#### Nano
O Nano é um editor de texto simples, baseado no terminal Linux, bastante útil principalmente em situações em que não há interface gráfica para editores mais complexos.

	nano <nome_do_arquivo> #Abre um arquivo ou cria caso o arquivo não exista.

Na imagem abaixo está a interface do Nano, na parte de baixo há os comandos necessários para manipulação de arquivos (o simbolo **^** Representa a tecla Ctrl). Pressione algum comando e em seguida tecle enter para efetivar.

![nano interface](img/nano.png)

#### Comandos para manipulação de arquivos de texto

Para manipulação de arquivos de texto (txt) direto no terminal.

	cat <arquivo.txt> #Para ver o que está escrito no arquivo.
	tac <arquivo.txt> #Igual o cat, porém com as ordem das linhas invertidas.
	head <arquivo.txt> #Exibe as 10 primeiras linhas do arquivo (estas linhas normalmente são utilizadas para informações de cabeçalhos)
	tail <arquivo.txt> #Exibe as 10 ultimas linhas do arquivo.
	
#### Redirecionamento de saída

Utilizando o simbolo **>**, é possível redirecionar a saída de um comando para um arquivo. Por exemplo:
Utilizando o comando abaixo, a saída do comando **teil** (10 ultimas linha de arquivo.txt) serão gravadas em saida.txt.

	tail arquivo.txt > saida.txt

O mesmo pode ser aplicado para qualquer comando, outro exemplo:

Agora a saída do comando **ls** (que o nome de todos os arquivo da pasta) será gravada no arquivo saida.txt.

	ls > saida.txt

Utilizando o comando **>>** o conteúdo será anexado (concatenado) ao final do arquivo de destino. Se for utilizado apenas **>**, o arquivo será sobrescrito.

#### Busca em arquivos

Utilizando o comando **grep** é possível realizar buscas em arquivos ou saída de comandos. Exemplo: Neste exemplo, o comando grep irá buscar pelas ocorrências da palavra "termo" dentro da saída do comando **tail arquivo.txt**.

	tail arquivo.txt | grep "termo"

Outro exemplo: Agora o comando **grep** irá retornar todas as ocorrências da palavra termo  que possuí na saída do comando **ls**.

	ls | grep "termo"

#### Leitura de arquivos

As vezes nos deparamos com arquivos ou saída de comandos com muito texto, o que dificultam a leitura, uma alternativa é usa o comando **more** ou **less**:
	
	cat arquivo.txt | more #Exibe as linhas do arquivo de forma controlável.
	<comando> | more #Exibe as linhas saída do comando de forma controlável.

	



## Outros comandos

#### Histórico de comandos

	history #mostra histórico de comandos digitados.

#### Datas no terminal

	cal #Exibe o calendário do mês atual.
	cal 2020 #Exibe todos os meses do ano de 2020.
	cal julho 2020 #Exibe o calendário do mês julho de 2020.
	date #Exibe a data atual.
	







### Referências

Digital Inovation One: Linux: Introdução ao sistema operacional
