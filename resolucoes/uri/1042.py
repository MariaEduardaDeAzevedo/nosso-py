lista = [int(a) for a in input().split()] #Lê as entradas digitadas pelo usuário e adiciona elas já convertidas para inteiro em uma lista

print(*sorted(lista), sep = "\n") #Faz um sort na lista e imprime cada elemento da lista pulando uma linha
print() #Pula uma linha
print(*lista, sep = "\n") #Imprime cada elemento da lista pulando uma linha
