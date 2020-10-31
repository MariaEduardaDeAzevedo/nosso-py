# Lê o tamanho da lista
tamanho_da_lista = int(input("Digite o tamanho da lista: "))
# Lê a quantidade máxima de páginas
qntd_max = int(input("Digite a quantidade máxima de páginas: "))
# Lê a página atual
pag_atual = int(input("Digite a página atual: "))

# popula a lista de páginas 
lista = []
for i in range(1, tamanho_da_lista + 1):
  lista.append(i)

# calcula a quantidade de páginas a serem exibidas
qntd_pag = min(qntd_max, 5)
# calcula o salto que terá entre a pagina atual e a ultima pagina a ser exibida
step = qntd_pag // 2

# calcula o numero da ultima pagina da lista de paginas a serem exibidas
ultima = pag_atual + step
# calcula o numero da primeira pagina da lista de paginas a serem exibidas
primeira = ultima - qntd_pag + 1
# inicializa a lista de paginas a serem exibidas
paginas = []

# trata os casos em que as páginas estão nos extremos da lista de paginas totais
if primeira < 1:
  primeira = 1
  ultima = qntd_pag
if ultima > len(lista):
  ultima = len(lista)
  primeira = ultima - qntd_pag + 1

# popula a lista de paginas exibidas
for i in range(primeira, ultima + 1):
  paginas.append(i)

print(paginas)