#Ler a entrada. 
#São três números inteiros separados por espaços, portanto utilizamos a função split().
#Split sem nenhum parâmetro tem como padrão separar por espaços em branco.
listaDosNumerosEmString = input().split()

#Isto é uma lista de strings. Convertendo para inteiros:
listaDosNumeros = list(map(int,listaDosNumerosEmString))

#Criar a função sugerida no enunciado.
#Essa função calcula o maior número entre dois.
def maiorNumero(a,b):
	soma = a + b + abs(a-b)
	return soma // 2 #O operador "//" faz uma divisão inteira, assim não precisa converter para inteiro depois.

#Calcula o maior número dentre os dois primeiros, usando a função criada acima:
maiorEntreOsPrimeiros = maiorNumero(listaDosNumeros[0], listaDosNumeros[1])

#Calcula o maior número dentre todos, agora entre o terceiro e o maior dentre os dois primeiros:
maior = maiorNumero(maiorEntreOsPrimeiros, listaDosNumeros[2])

#Imprime a resposta:
print(maior, "eh o maior")

#Como uma curiosidade, Python já possui a função embutida max() que já calcula o maior valor de um iterador.
#Ou seja, podemos fazer essa questão de maneira mais simples da seguinte forma:

maior = max(listaDosNumeros)
