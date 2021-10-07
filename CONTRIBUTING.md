# Quero contribuir, e agora?
Esse repositório foi feito com o propósito de engajar a galera a contribuir! Abaixo segue tudo que você precisa saber para ajudar o **Nosso Py** a crescer:

ANTES DE TUDO... uns links para aprender a fazer fork, clone, PR...

- [GitHub CLI (uma coisa mágica)](https://cli.github.com/manual/)
- [Como fazer PR?](https://www.digitalocean.com/community/tutorials/como-criar-um-pull-request-no-github-pt)
- [Sobre issues](https://docs.github.com/pt/free-pro-team@latest/github/managing-your-work-on-github/about-issues)


### Sumário

- [Quero adicionar um link na sessão "Para aprender"](#Contribuindo-no-Para-Aprender)
-  [Quero adicionar um link na sessão "O maravilhoso mundo das bibliotecas"](#Contribuindo-no-maravilhoso-mundo-das-bibliotecas)
- [Quero enviar ideias para o "Bora programar"](#Enviando-ideias-de-desafios-e-projetos)
- [Quero enviar meu mini-projeto feito, meu desafio cumprido ou testes para os desafios](#Contribuindo-com-código)
- [Quero é vender meu peixe...](#A-feira)

### Contribuindo no Para Aprender
Se você tiver uma dica para quem tá aprendendo, você pode contribuir da seguinte forma:

1. Clique no ícone de editar no README.md (o lápis do canto superior direito)
2. Adicione na tabela da seção as informações seguindo este modelo:

	Link do material | tipo do material (vídeo no youtube, repositório, livro, post, site, artigo...)| descrição breve do material

3. Após isso,  no fim da página faça um commit das suas alterações e abra sua pull request. Não se esqueça de dar uma olhadinha em [como enviar uma PR perfeita](#A-PR-Perfeita).

E se você for mais hardcore, pode forkar, clonar e fazer sua PR de modo raiz. 

### Contribuindo no maravilhoso mundo das bibliotecas
Se você tiver aquela biblioteca que é o seu xodó, uma muito utilizada ou aquela que todo mundo tem que conhecer, manda aqui!

1. Clique no ícone de editar no README.md (o lápis do canto superior direito)
2. Adicione na tabela da seção as informações seguindo este modelo:
	Nome da biblioteca | descrição breve da finalidade da biblioteca| link pro PyPi (de preferência com o título que a biblioteca tem por lá)| Link da documentação (de preferência com título "Link")

3. Após isso,  no fim da página faça um commit das suas alterações e abra sua pull request. Não se esqueça de dar uma olhadinha em [como enviar uma PR perfeita](#A-PR-Perfeita).

E se você for mais hardcore, pode forkar, clonar e fazer sua PR de modo raiz. 

### Enviando ideias de desafios e projetos
Para enviar sua ideia para cá, segue o fio:

#### Enviando desafios
Para enviar um desafio adicione um diretório dentro da pasta desafios com o nome da questão.
Essa pasta deverá conter:

1. Um README.md seguindo o seguinte [template](./templates/DESAFIO.md)
2. Testes, de preferência, mas deixamos que esses possam ser enviados por outra pessoa.

Além disso, você deverá colocar o link para o seu desafio no README.md da pasta desafios, seguindo o modelo do mesmo.

#### Enviando mini-projetos
Para enviar um mini-projeto adicione um diretório dentro da pasta mini-projetos com o nome da sua ideia.
Essa pasta deverá conter:

1. Um README.md seguindo o seguinte [template](./templates/MINI-PROJETO.md)

Além disso, você deverá colocar o link para o seu desafio no README.md da pasta mini-projetos, seguindo o modelo do mesmo.

### Contribuindo com código
Se você quiser enviar um código, está na seção certa!
Siga os passos:

1. Fork esse repositório
2. Clone o repositório forkado
3. Adicione sua contribuição no repositório clonado da seguinte forma:
	3.1 Para desafios enviar uma questão de desafio
		Adicione seu arquivo na pasta desafios/<nome do desafio>, nomeado da seguinte forma: nomedodesafio.py (exemplo: palindromos.py).
	3.2 Para mini-projetos
		Adicione seu arquivo na pasta mini-projetos/<nome do mini-projeto>, nomeado da seguinte forma:
		titulo_do_mini_projeto.py (exemplo: invertedor_de_palavras.py)
		Caso seja uma pasta, siga o mesmo padrão para o nome da pasta.
	3.3 Para testes
		Na pasta desafio/<nome do desafio> adicione o arquivo testes.py contendo seus testes. 
	3.4 Para implementações
		Na pasta implementacoes, adicione uma pasta com o nome do algoritmo ou da funcionalidade do script, que deve conter a implementação, nomeado com o mesmo nome da pasta e um README.md, que descreve a implementação para fins didáticos. É importante também que você comente seu código. 
	3.5 Para resoluções
		Na pasta resolucoes, crie um diretório utilizando o nome da plataforma que contém a questão, se já existir, apenas adicione nela o arquivo seguindo o padrão:
		numero_da_questao.py (ex: 1234.py).
		É importante que você comente seu código para melhor entendimento e, ao resolver, coloque sua questão como feita no README.md, seguindo o padrão do mesmo.
		Caso você queira enviar apenas uma sugestão de questão para a comunidade resolver, apenas adicione no README.md de resolucoes na parte de "Questões ainda sem resolução (Para você resolver!)", seguindo o padrão. 

### A feira
O lugar de vender teu paixe é aqui! Segue como que faz:

1. Clique no ícone de editar no README.md (o lápis do canto superior direito)

2. Adicione na tabela da seção as informações seguindo este modelo:
	Nome do projeto | descrição breve | link pro repositório, de preferência com o nome dele como título

3. Após isso,  no fim da página faça um commit das suas alterações e abra sua pull request. Não se esqueça de dar uma olhadinha em [como enviar uma PR perfeita](#A-PR-Perfeita).

### A PR perfeita
Sem bronca! A PR perfeita só tem que seguir esse arquivo aqui e ser descritiva. Não esqueça de obedecer também o nosso [código de conduta](./codigo-de-conduta.md) para uma ótima convivência!
