def cifra_de_cesar(palavra, n):
  cript = []

  for i in palavra:
    letra_ord = ord(i) -  n # a função ord () retorna o unicode da letra 

    # as letras maiusculas de A-Z na tabela ASCII ficam no intervalo de 65 a 90. Então criei essa IA (É brincadeira hahaha) caso saia desse intervalo
    if letra_ord < 65:
      passou = 65 - letra_ord
      letra_ord = 91 - passou 

    letra = chr(letra_ord) # a função chr() o unicode no caractere desse ponto da tabela ASCII
    cript.append(letra)

  answer = "".join(cript) # convertendo a lista cript para uma string
  return answer

def main():
  n = int(input()) # n recebe a quantidade dos casos de teste

  for i in range(0, n):
    palavra = input()
    deslocamento = int(input())
    palavra_cifra = cifra_de_cesar(palavra, deslocamento)
    print(palavra_cifra)

if __name__ == '__main__':
  main()